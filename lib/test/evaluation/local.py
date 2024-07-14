from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()
    settings.davis_dir = ''
    settings.got10k_path = ''
    settings.lasot_extension_subset_path = ''
    settings.lasot_path = ''
    settings.nfs_path = ''
    settings.otb_path = ''
    settings.prj_dir = '/home/user-njf87/zjk/FERMT'
    settings.results_path = '/data/data-user-njf87/zjk/result/FERMT/track_results'    # Where to store tracking results
    settings.save_dir = '/data/data-user-njf87/zjk/result/FERMT'
    settings.tnl2k_path = ''
    settings.trackingnet_path = ''
    settings.uav_path = ''
    settings.vot18_path = ''


    return settings

