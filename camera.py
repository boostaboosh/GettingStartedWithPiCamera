from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()
camera.rotation = -90 #rotates camera preview

camera.start_preview(alpha = 200) #alpha level 200 makes the cam preview slightly see through

#take 5 pictures
#for i in range(5):
    #sleep(5)
    #camera.capture('/home/lampone/Desktop/image%s.jpg' % i)

#take a 5 second recording
#camera.start_recording('/home/lampone/Desktop/video.h264')
#sleep(5)
#camera.stop_recording()

#camera.resolution = (2592, 1944)
#camera.framerate = 15
#camera.start_preview()
#sleep(5)
#camera.capture('/home/lampone/Desktop/max.jpg')

#camera.annotate_background = Color('blue')
#camera.annotate_foreground = Color('yellow')
#camera.annotate_text_size = 160
#camera.annotate_text = " Hello World "
#sleep(5)
#camera.capture('/home/lampone/Desktop/text.jpg')

#for i in range(100):
    #camera.annotate_text = "Brightness: %s" % i
    #camera.brightness = i
    
    #camera.annotate_text = "Contrast: %s" % i
    #camera.contrast = i
    
    #sleep(0.1)

#camera.image_effect = 'colorswap'
#sleep(5)
#camera.capture('/home/lampone/Desktop/colorswap.jpg')

#for effect in camera.IMAGE_EFFECTS:
    #camera.image_effect = effect
    #camera.annotate_text = "Effect: %s" % effect
    #sleep(5)

#camera.exposure_mode = 'beach'
#sleep(5)
#camera.capture('/home/lampone/Desktop/beach.jpg')

#for exposure in camera.EXPOSURE_MODES:
    #camera.exposure_mode = exposure
    #camera.annotate_text = "Exposure mode: %s" % exposure
    #sleep(5)

#camera.awb_mode = 'sunlight'
#sleep(5)
#camera.capture('/home/lampone/Desktop/sunlight.jpg')

for autoWhiteBalanceMode in camera.AWB_MODES:
    camera.awb_mode = autoWhiteBalanceMode
    camera.annotate_text = "Auto White Balance Mode: %s" % autoWhiteBalanceMode
    sleep(5)

camera.stop_preview()