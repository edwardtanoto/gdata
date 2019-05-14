import cv2
import os

SAVE_DIR = "word_images_1yrwin_1dslide"

fourcc = cv2.VideoWriter_fourcc('M','J','P','G')

out = cv2.VideoWriter(f'{SAVE_DIR}/video.avi',fourcc, 60.0, (1200,700))

for i in range(1471):
    img_path = f"{SAVE_DIR}/{i}.png"
    print(img_path)
    frame = cv2.imread(img_path)
    out.write(frame)

out.release()