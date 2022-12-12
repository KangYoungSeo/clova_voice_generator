
import os
import numpy as np
import argparse
import cv2
from datetime import date
import json

videoErrorCnt = 0

# video dir_path 
save_dir_path = './221211_rgb/'

# dirname
#today = str(date.today()).replace("-","")[2:] + "_skeletons"
today = "221211"


#bvh list있는 경로
#tmp=today+"_skeleton/bvh_list_1.txt"
#debug
tmp=today + "_rgb/debug.txt"


# 저장 폴더경로 # skeleton 파일 저장 경로
out_path='./'+today+'_rgb/debug' 
if not os.path.isdir(out_path):
    os.mkdir(out_path)


if __name__ == '__main__':
    
    # debug
    with open(tmp,'r',encoding='utf8') as bvh_list:

        for file in bvh_list:
            #txt 데이터의 이름을 불러와 bvh가 아닌 mp4 파일을 로드
            file = file.replace('\n',"") #필수
            video_file = file.replace('.bvh','_F.mp4')

            #구간 태깅 데이터 확인
            json_file = file.replace('1.원천데이터','2.라벨링데이터')
            json_file = json_file[:-4]+'.json'

            try:
                if os.path.isfile(json_file):
                    with open(json_file,'r',encoding='utf8') as j:
                        try:
                            json_data=json.load(j)
                            j.close()
                            
                        except:
                            #with open("errorlist_3.txt", "a") as error_file:
                            #    data = file + ": " + "json컬럼에러" + "\n"
                            #    error_file.write(data)
                            videoErrorCnt + 1

                    json_data_anno=json_data['annotation']['actionAnnotationList']

                    # 구간태깅
                    start_frame = json_data_anno[1]['start_frame']
                    last_frame = json_data_anno[1]['end_frame']
                    print(start_frame)
                    print(last_frame)
                else:
                    videoErrorCnt + 1
            except:
                #with open("errorlist_3.txt", "a") as error_file:
                #    data = file + ": " + "json에러" + "\n"
                #    error_file.write(data)
                videoErrorCnt + 1
            # csv read
            print(video_file)

            if os.path.isfile(video_file) == False:
                videoErrorCnt + 1

            #video 파일 열기
            # get file path for desired video and where to save frames locally
            
            # print(video_file)
            cap = cv2.VideoCapture(video_file)

            if (cap.isOpened() == False):
                videoErrorCnt = videoErrorCnt + 1
        

            #path_to_save = os.path.abspath(save_dir_path)  #  + '/'+ json_file[:-4] + '/'
            path_to_save = os.path.abspath(save_dir_path  + '/'+ json_file[-31:-5] + '/')

            current_frame = 1

            # cap opened successfully
            while (cap.isOpened()):

                # capture each frame
                ret, frame = cap.read()

                if (ret == True):
                    # keep track of how many images you end up with
                    current_frame += 1

                    if(current_frame < start_frame):
                        continue
                    elif(current_frame > last_frame):
                        break

                    # Save frame as a jpg file
                    elif (current_frame % 100 == 0):
                        name = json_file[:-4] +'_' + str(current_frame) + '.jpg'
                        print(f'Creating: {name}')
                        print(cv2.imwrite(os.path.join(path_to_save, name), frame))
                else:
                    break

            # release capture
            cap.release()
            print(videoErrorCnt)
            print('done')
