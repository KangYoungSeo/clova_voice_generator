import os
import glob
from datetime import date
from pathlib import Path


all_dir = glob.glob('/home/irteam/dcloud-global-dir/mocap1/221124_skeletons/EL_HE06_A23_FMH01_P109_001.txt', recursive = True)
f = open(to "/E.txt", 'w')


anno = dict()
    # 17개임
    # 해당 배열에 x,y keypoint 저장...
    anno['keypoint'] = pose_results[..., :2]
    anno['keypoint_score'] = pose_results[..., 2]
    anno['frame_dir'] = osp.splitext(osp.basename(vid))[0]
    anno['img_shape'] = (1080, 1920)
    anno['original_shape'] = (1080, 1920)
    anno['total_frames'] = pose_results.shape[1]
    anno['label'] = int(osp.basename(vid).split('A')[1][:3]) - 1
    shutil.rmtree(osp.dirname(frame_paths[0]))
