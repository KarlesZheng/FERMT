class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/user-njf87/zjk/FERMT'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = self.workspace_dir + '/tensorboard/'    # Directory for tensorboard files.
        self.pretrained_networks = self.workspace_dir + '/pretrained_networks/'
        self.lasot_dir = '/data/data-user-njf87/ytbb/LaSOTBenchmark'
        self.got10k_dir = '/data/data-user-njf87/ytbb/GOT-10K/train'
        self.got10k_val_dir = '/data/data-user-njf87/ytbb/GOT-10K/val'
        self.trackingnet_dir = '/data/data-user-njf87/ytbb/TrackingNet/TRAIN'
        self.coco_dir = '/data/data-user-njf87/COCO'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = '/home/hipeson/data/track/ILSVRC'
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
