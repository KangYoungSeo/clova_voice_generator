import os
import glob
from datetime import date
from pathlib import Path
import numpy as np
import pickle

result= dict()
cnt = 0
data = []
    
def generate_coordinate(skel):
    
    #txt 파일에서 ' '데이터를 기반으로 쪼개기
    file_path = skel +'.txt'
    skel = skel + ''

    pre = dict()
    #먼저 txt 파일을 열어본다.
    with open(file_path, "r", encoding="utf8") as skeleton_list:

        #한줄씩 읽어옴
        cnt = 0
        for skel in skeleton_list: 
            # 그 안에서 공간 별로 쪼갠다
            frame_data = skel.split()
            pre[cnt] = frame_data
            cnt = cnt + 1


    #pre dict에서 탐색해서 필요한 자료만 array형으로 변환 후 삽입

    idx = 0

    #초기화
    #차원 설명 두번째 frame개수, 세번째 joint 개수, 네번째 좌표 개수 (우리는 xy니까 2로 고정) 
    frame_xy = np.zeros((1,len(pre),17,2)).astype(np.float16) ## 5-> int(pre[0][0]) 변환!! 필수!!

    #인덱스 별로 탐색 진행
    #위치가 0~24 사이면 xy 좌표 추출임
    #25~27이면 필요 없기 때문에 pass
    #프레임 별로 로드 하는거 필요

    #프레임 별 오픈
    frame_idx = -1
    for xy in range(4, len(pre)) : 
    
        order = xy % 28
        #print(order)
        #print([pre[xy][0:2]])
    
        #17 이후는 스킵 (22) 
        if (order < 4):
            continue
        elif (order > 20) :
            continue
        
        else :
            if(order == 4) :
                frame_idx = frame_idx + 1
        
            frame_xy[0][frame_idx][order - 4][0] = pre[xy][0]
            frame_xy[0][frame_idx][order - 4][1] = pre[xy][1]


    anno = dict()
        # 17개임
        # 해당 배열에 x,y keypoint 저장
        # 4차원 배열 numpy 자료구조로 구성되어 있음. frame 내 joint별로 넣어짐
    anno['frame_dir'] = file_path
    anno['label'] = int(file_path[9:11])
    anno['img_shape'] = (1080, 1920)
    anno['original_shape'] = (1080, 1920)
    anno['total_frames'] = int(pre[0][0])
    anno['keypoint'] = frame_xy
    anno['keypoint_score'] = np.ones((1,5,17)).astype(np.float16)

    #마지막은 pkl에 저장하기
    #print(anno)
    data.append(anno)

    
    



if __name__ == '__main__':
    final_dic = ''
    #tmp = "/home/irteam/dcloud-global-dir/mocap1/skeleton_list.txt"
    tmp = "./skeleton_list.txt"
    all_dir = glob.glob('/home/irteam/dcloud-global-dir/mocap1/', recursive = True)

    

    #json 파일들의 list를 불러와서 하나씩 json->skeleton으로 변환시키는 부분
    with open(tmp, "r", encoding="utf8") as skeleton_list:
    
            #한줄 씩 입력받게 된다. ex) skeleton_content = EL_OE11_A64_013_L20M02_05_F.json
        for skel in skeleton_list:    
            skel = skel.replace('\n',"")
                
            generate_coordinate(skel)


    print(data)
    with open('test7.pkl','wb') as fw : 
        pickle.dump(data[0],fw)
    