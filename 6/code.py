
import cv2

import dropbox
import time
import random

from numpy import number
startTime=time.time()
def take_snapshot():
    number=random.randint(0,100)
    vcobject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=vcobject.read()
        imgName="img"+str(number)+".jpg"
        cv2.imwrite(imgName,frame)
        startTime=time.time
        result=False
    return imgName
    print("snapshot taken")
    vcobject.release()
    cv2.destroyAllWindows()

def upload_file(imgName):
    access_Token="sl.BBJGNGdjFEhBz4XLncU4-GhetOMxDYvvp04dj3ceEAb8zrDllzVybHEm8p_wl7V0CCCe3a2v7XvBc01ipNar0cozAkzcWmK514tLG7DYQXSVZH3hHplwphwa3csRsDlk4cPiHl0"
    file_from=imgName
    file_to="/python/"+(imgName)
    dbx=dropbox.Dropbox(access_Token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while (True):
        if((time.time()-startTime)>=300):
            name=take_snapshot()
            upload_file(name)

main()