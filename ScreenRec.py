# AdamRekorder lololololololol

# Important deps lol i think BUT STILL DONT TOUCH
import cv2
import numpy as np
import pyautogui
import time


SCREEN_SIZE = (1920,1080) # You can change the screen recording size to your liking but i recommend keeping it this way
fourcc = cv2.VideoWriter_fourcc(*"XVID") # dont touch this i beg u 
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE)) # again dont touch this (u can chnage the name)
fps = 60 # you can change the fps to your liking as well but i like it at 60 fps
prev = 0 # dont touch this


# ok here DO NOT TOUCH ANYTHING HERE YOU WILL BREAK THE REKORDER IF U DO
while True:
    time_elapsed = time.time() - prev

    img = pyautogui.screenshot() # taking the screenshots

    if time_elapsed > 1.0/fps:
        prev = time.time()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # Switching from vga colors to rgb
        out.write(frame) # writing the video
    cv2.waitKey(90)

cv2.destroyAllWindows()
out.release()

# more info on the readme.md      
