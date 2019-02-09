import os
imgType = (int(input("What image do you want? Smiley face is 1, Frowny Face is 2, and Neutral Face is 3. Put your answer here: ")))
if imgType == 1:
    os.system("open smileyFace.jpg")
if imgType == 2:
    os.system("open frownyFace.jpg")
if imgType == 3:
    os.system("open neutralface.png")
 
