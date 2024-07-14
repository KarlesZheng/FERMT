import os
import sys
import argparse
import cv2

prj_path = os.path.join(os.path.dirname(__file__), '..')
if prj_path not in sys.path:
    sys.path.append(prj_path)

from lib.test.evaluation import get_dataset
from lib.test.evaluation.running import run_dataset
from lib.test.evaluation.tracker import Tracker
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
import numpy as np



def main():
    # parser = argparse.ArgumentParser(description='Run tracker on sequence or dataset.')
    # parser.add_argument('tracker_name', type=str, help='Name of tracking method.')
    # parser.add_argument('tracker_param', type=str, help='Name of config file.')
    # parser.add_argument('--runid', type=int, default=None, help='The run id.')
    # parser.add_argument('--dataset_name', type=str, default='otb', help='Name of dataset (otb, nfs, uav, tpl, vot, tn, gott, gotv, lasot).')
    # parser.add_argument('--sequence', type=str, default=None, help='Sequence number or name.')
    # parser.add_argument('--debug', type=int, default=0, help='Debug level.')
    # parser.add_argument('--threads', type=int, default=0, help='Number of threads.')
    # parser.add_argument('--num_gpus', type=int, default=8)

    # args = parser.parse_args()

    # try:
    #     seq_name = int(args.sequence)
    # except:
    #     seq_name = args.sequence

    # run_tracker(args.tracker_name, args.tracker_param, args.runid, args.dataset_name, seq_name, args.debug,
    #             args.threads, num_gpus=args.num_gpus)

    dataset = get_dataset('lasot')
    sam_checkpoint = "/home/hipeson/wsl/segment-anything-main/checkpoint/sam_vit_b_01ec64.pth"
    model_type = "vit_b"

    device = "cuda"

    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
    sam.to(device=device)

    predictor = SamPredictor(sam)

    mask_generator = SamAutomaticMaskGenerator(sam)
    for seq in dataset:
        
        file_path = os.path.join('/home/hipeson/wsl/result/ostrack_lasot/lasot',seq.name+'.txt')
        frame_box = np.loadtxt(file_path,delimiter='\t')
        # print(frame_box.shape)
        # print(len(seq.frames))
        # if(len(seq.frames) != frame_box.shape[0]):
        #     print(seq.name)
        for frame_num, frame_path in enumerate(seq.frames[1:], start=1):
            print(frame_path)
            image = cv2.imread(frame_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            break
        break


if __name__ == '__main__':
    main()
