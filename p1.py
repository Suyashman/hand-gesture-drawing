import math
import cv2
import mediapipe as mp
import numpy as np
import time
import pyautogui

#########################################   RESOLUTION
wc, hc = 1280, 720

cap = cv2.VideoCapture(0)
cap.set(3, wc)
cap.set(4, hc)

imgCanvas = np.zeros((720,1280,3),np.uint8)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

######################################### FPS VARIABLES
'''pTime = 0
cTime = 0
dist812 = 0
cTime = time.time()
fps = 1 / (cTime - pTime)
pTime = cTime
cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)  #displays the fps'''
######################################### DRAWING COLOR VARIABLES
b,g,r = 0,0,255
c1,c2,c3 = 0,0,0
color = (0,0,0)

######################################### DRAWING ERAZING VARIABLES
size = 1
drawsize = 1
erazersize = 1
listcords = []
x1,y1 = 0,0

def draw(color,x2,y2):
    #DRAWING
    if(c1 == 1): #DRAWING
        '''print("enterted drawing mode")
        print(color)'''
        if (dist812 <70):
            if(listcords[8][1]+(size//2) <1100 and listcords[8][2]+(size//2)>40):
                if(x2==0 and y2 == 0):
                    x2 = listcords[8][1]
                    y2 = listcords[8][2]
                cv2.line(img,(x2,y2),(listcords[8][1],listcords[8][2]),color,drawsize)
                cv2.line(imgCanvas,(x2,y2),(listcords[8][1],listcords[8][2]),color,drawsize)


    elif(c2 == 1): #ERAZING
        #cv2.rectangle(img, (listcords[8][1], listcords[8][2] - 25), (listcords[12][1], listcords[12][2] + 25),(0, 0, 0), cv2.FILLED)
        if(dist812<70):
            if (x2 == 0 and y2 == 0):
                x2 = listcords[8][1]
                y2 = listcords[8][2]
            cv2.line(img, (x2,y2),(listcords[8][1],listcords[8][2]), (0, 0, 0), erazersize)
            cv2.line(imgCanvas, (x2,y2),(listcords[8][1],listcords[8][2]),(0, 0, 0), erazersize)



def grid(b,g,r):

    #VIBGYOR
    cv2.rectangle(img,(0,0),(157,40),(255,0,143),cv2.FILLED) #VIOLET
    cv2.rectangle(img,(157,0),(314,40),(130,0,75),cv2.FILLED) #INDIGO
    cv2.rectangle(img,(314,0),(471,40),(255,0,0),cv2.FILLED) #BLUE
    cv2.rectangle(img,(471,0),(628,40),(0,255,0),cv2.FILLED) #GREEN
    cv2.rectangle(img,(628,0),(785,40),(0,255,255),cv2.FILLED) #YELLOW
    cv2.rectangle(img,(785,0),(942,40),(0,165,255),cv2.FILLED) #ORANGE
    cv2.rectangle(img,(942,0),(1100,40),(0,0,255),cv2.FILLED) #RED


    if(c1 == 1):  #DRAWING
        b,g,r = 0,255,0
    cv2.line(img, (1100, 0), (1100, 240), (b,g,r), 5)  # c1
    cv2.line(img, (1100, 0), (1280, 0), (b,g,r),5)  # r1
    cv2.line(img, (1100, 238), (1280, 238), (b,g,r), 8)  # r2
    cv2.putText(img, str("DRAWING"), (1120, 40), cv2.FONT_HERSHEY_PLAIN, 2, (b,g,r), 2)
    b,g,r = 0,0,255

    if(c2 == 1):  #ERAZING
        b,g,r = 0,255,0
    cv2.line(img, (1100, 240), (1100, 480), (b,g,r), 5) #c2
    cv2.line(img, (1100, 242), (1280, 242), (b,g,r), 8) #r2
    cv2.line(img, (1100, 478), (1280, 478), (b,g,r), 8) #r3
    cv2.putText(img, str("ERAZER"), (1120, 270), cv2.FONT_HERSHEY_PLAIN, 2, (b,g,r), 2)#TEXT OF ERAZER
    b,g,r = 0,0,255

    if(c3 == 1): #HANDSFREEMODE
        b,g,r = 0, 255, 0
    cv2.line(img, (1100, 480), (1100, 720), (b,g,r), 5) #c3
    cv2.line(img, (1100, 482), (1280, 482), (b,g,r), 8) #r3
    cv2.line(img, (1100, 720), (1280, 720), (b,g,r), 8) #r4
    if(c1 ==1):
        cv2.putText(img, str("BRUSH"), (1120, 510), cv2.FONT_HERSHEY_PLAIN, 2, (b, g, r), 2)  # TEXT OF BRUSH
        cv2.putText(img, str("SIZE"), (1120, 550), cv2.FONT_HERSHEY_PLAIN, 2, (b, g, r), 2)  # TEXT OF SIZE
        cv2.putText(img, str(int(drawsize)), (1160, 600), cv2.FONT_HERSHEY_PLAIN, 2, (b, g, r), 2)  # INT SIZE

    elif(c2==1):
        cv2.putText(img, str("ERAZER"), (1120, 510), cv2.FONT_HERSHEY_PLAIN, 2, (b, g, r), 2)  # TEXT OF ERAZER
        cv2.putText(img, str("SIZE"), (1120, 550), cv2.FONT_HERSHEY_PLAIN, 2, (b, g, r), 2)  # TEXT OF SIZE
        cv2.putText(img, str(int(erazersize)), (1160, 600), cv2.FONT_HERSHEY_PLAIN, 2, (b, g, r), 2)  # INT SIZE
    else:
        cv2.putText(img, str("RESIZE"), (1120, 510), cv2.FONT_HERSHEY_PLAIN, 2, (b, g, r), 2)  # TEXT OF SIZE


    b,g,r = 0,0,255

while True:
    success, img = cap.read()
    # Force webcam frame to match your UI resolution
    img = cv2.resize(img, (1280, 720))
    img = cv2.flip(img,1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                listcords.append([id, cx, cy])


            #print(listcords)
            # DISTANCE BETWEEN INDEX AND MIDDLE FINGER
            dist812 = math.sqrt(((listcords[8][1] - listcords[12][1]) ** 2) + ((listcords[8][2] - listcords[12][2]) ** 2))
            #dist812 = math.sqrt(((listcords[4][1] - listcords[20][1]) ** 2) + ((listcords[4][2] - listcords[20][2]) ** 2))

            #print(dist812)


            if(listcords[8][1] and listcords[12][1] >= 1100):
                if(listcords[8][2] and listcords[12][2] <= 240): #DRAWING
                    #print("DRAW")
                    c1 = 1
                    c2,c3 = 0,0

                elif(listcords[8][2] and listcords[12][2] <= 480): #ERAZER
                    #print("ERAZE")
                    c2 = 1
                    c1,c3 = 0,0

                elif (listcords[8][2] and listcords[12][2] <= 720): #RESIZE
                    #print("IDK")
                    c3 = 1
                    if (drawsize >= 151):
                        drawsize = 1
                    if(erazersize>=151):
                        erazersize = 1
                    if(c1 == 1):
                        drawsize = drawsize+1
                    elif(c2==1):
                        erazersize = erazersize+1



            elif(listcords[8][2]<40 and listcords[8][1]<1100): #ANNOTATING COLOR
                if(listcords[8][1]<157):     #VIOLET
                    color = (255,0,143)
                    cv2.line(img, (0, 45), (157, 45), color, 5)
                elif(listcords[8][1] < 314): #INDIGO
                    color = (130,0,75)
                    cv2.line(img, (157, 45), (314, 45), color, 5)
                elif (listcords[8][1] < 471): #BLUE
                    color = (255,0,0)
                    cv2.line(img, (314, 45), (471, 45), color, 5)
                elif (listcords[8][1] < 628): #GREEN
                    color = (0,255,0)
                    cv2.line(img, (471, 45), (628, 45), color, 5)
                elif (listcords[8][1] < 785): #YELLOW
                    color = (0, 255, 255)
                    cv2.line(img, (628, 45), (785, 45), color, 5)
                elif (listcords[8][1] < 942): #ORANGE
                    color = (0, 165, 255)
                    cv2.line(img, (785, 45), (942, 45), color, 5)
                elif (listcords[8][1] < 1100): #RED
                    color = (0, 0, 255)
                    cv2.line(img, (942, 45), (1100, 45), color, 5)

                #print(color)




            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


        draw(color,x1,y1)
        x1 = listcords[8][1]  #STORES PREVIOUS CORDS FOR DRAWING A LINE FROM PREVIOUS TO CURRENT CORDS
        y1 = listcords[8][2]
        listcords.clear()
    grid(b,g,r)

    img = cv2.addWeighted(img,0.5,imgCanvas,0.5,0)
    cv2.imshow("Camera Vision", img)  # displays the video feed
    cv2.imshow("Canvas", imgCanvas)  # displays the video feed
    cv2.waitKey(1)