import os
import sys
import pdb
import cv2
import argparse
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize

parser = argparse.ArgumentParser()
parser.add_argument("--video")
parser.add_argument("--width", type=int)
parser.add_argument("--height", type=int)
args = parser.parse_args()

video = cv2.VideoCapture(args.video)
fps = video.get(cv2.CAP_PROP_FPS)
outname = args.video.replace(".mp4", 
            f"_{args.width}_{args.height}.avi")

ret, frame = video.read()
all_frames = []


while(1):
    ret, frame = video.read()
    if cv2.waitKey(1) & 0xFF == ord('q') or ret==False :
        video.release()
        cv2.destroyAllWindows()
        break
    # pdb.set_trace()
    resized = cv2.resize(frame, (args.height, args.width)) 
    rotated = cv2.rotate(resized,cv2.ROTATE_90_CLOCKWISE) 
    all_frames.append(rotated)
    # pdb.set_trace()

format = "XVID"
fourcc = VideoWriter_fourcc(*format)
vid = VideoWriter(outname, fourcc, float(fps), (args.width, args.height), True)
for image in all_frames:
    vid.write(image)
vid.release

print(video, fps)