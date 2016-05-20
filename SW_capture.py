import RPi.GPIO as GPIO
import cv
import datetime
import time

# ---------------------------
# Setup the webcam and font
# ---------------------------
 
# define image size
imageWidth = 320
imageHeight = 240
 
# create a window object
cv.NamedWindow("window1", cv.CV_WINDOW_AUTOSIZE)
camera_index = 0
 
# create a camera object
capture = cv.CaptureFromCAM(camera_index)
 
# set capture width and height
cv.SetCaptureProperty( capture, cv.CV_CAP_PROP_FRAME_WIDTH, imageWidth );
cv.SetCaptureProperty( capture, cv.CV_CAP_PROP_FRAME_HEIGHT, imageHeight );
 
# create a font
font = cv.InitFont(cv.CV_FONT_HERSHEY_COMPLEX_SMALL , 0.5, 0.5, 0, 1, cv.CV_AA)


GPIO.setmode(GPIO.BOARD)

sw = 16 # Set GPIO for get value from switch

GPIO.setup(16, GPIO.IN)
print ("Program working press switch for capture.")

while(True):
    # get image from webcam
    frame = cv.QueryFrame(capture)
 
    # -------------------------------------------
    # Draw the time stamp on a white background
    # -------------------------------------------  
    cv.Rectangle(frame, (0,0), (imageWidth, 15), (255,255,255),cv.CV_FILLED,8,0)
    # get the current date and time
    timeStampString = datetime.datetime.now().strftime("%A %Y-%m-%d %I:%M:%S %p")
    # insert the date time in the image
    cv.PutText(frame, timeStampString, (10,10), font, (0,0,0))
 
    # -----------------------------
    # show the image on the screen
    # -----------------------------
    cv.ShowImage("window1", frame)
    cv.WaitKey(10)

    
    if(GPIO.input(sw) == 0):  # Save image by Switch
        while(GPIO.input(sw) == 0):
            print ("capturing....")
            cv.SaveImage(timeStampString +".jpg",frame)
            print ("Save image success.")
            print ("File name \"" + timeStampString + ".jpg\"")
            time.sleep(0.3)


        
