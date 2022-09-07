
import cv2
import PoseModule as pm
import numpy as np

detector=pm.poseDetector()


cap=cv2.VideoCapture(r"C:\Users\MUHAMMED SALIH K\DATASCIENCE NOTES\DATA SCIENCE\Open CV\Gym_Trainer\squats.mp4")


direction=0
count=0


while True:
    sucess,img=cap.read()
    img=cv2.resize(img,(1280,720))

    img=detector.findPose(img,False)
    lmlist=detector.findPosition(img,False)
    # print(lmlist)

    if len(lmlist)!=0:
        #tracking right leg and find angle
        detector.findAngle(img,24,26,28)
        
        #tracking left leg and find angle
        angle =detector.findAngle(img,23,25,27)
        # print(angle)
        
        #setup range for squat
        low=200
        high=300

    
        percentage=np.interp(angle,(low,high),(0,100))
        # print(percentage)
        # print(angle, "---->>>",percentage)

        #calculating count
        if percentage==100:
            if direction==0:
                count+=0.5
                direction=1
        if percentage==0:
            if direction==1:
                count+=0.5
                direction=0

        # print(count)

        #display counts
        cv2.putText(img,str(int(count)),(100,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)


        bar=np.interp(angle,(low,high),(650,100))
        # print(bar)

        #display bar
        cv2.rectangle(img,(1100,int(bar)),(1200,650),(0,255,0),cv2.FILLED)
        cv2.rectangle(img,(1100,100),(1200,650),(0,255,0),3)

        #display percentage
        cv2.putText(img,str(int(percentage)),(1100,75),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)

    cv2.imshow("sqaut video",img)
    if cv2.waitKey(1) & 0xFF ==27:
        break
