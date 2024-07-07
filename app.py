import cv2
import mediapipe as mp
import pyautogui as pag
cap=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width,screen_height=pag.size()
index_y=thumb_y=raise_y=0
while 1:
    t,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame_height,frame_width,_=frame.shape
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id,landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                # print(x,y)
                if id==8:
                    index_x=screen_width/frame_width*x
                    index_y=screen_height/frame_height*y
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    pag.moveTo(index_x,index_y)
                print(abs(index_y-thumb_y))    
                if id==4:
                    thumb_x=screen_width/frame_width*x
                    thumb_y=screen_height/frame_height*y
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))  
                    if abs(index_y-thumb_y)<40:
                        pag.click()  
                        pag.sleep(1)
                if id==12:
                    raise_x=screen_width/frame_width*x
                    raise_y=screen_height/frame_height*y
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))  
                    if abs(raise_y-thumb_y)<40:
                        pag.rightClick()
                        pag.sleep(1)
                    
                    
                    
                




    cv2.imshow('AI MOUSE',frame)
    cv2.waitKey(1)