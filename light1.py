#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse
from gpiozero import Button
#import keyboard

button_0 = Button(5)
button_1 = Button(6)
button_2 = Button(13)
button_3 = Button(19)
button_4 = Button(26)

button_5 = Button(12)
button_6 = Button(16)
button_7 = Button(20)
button_8 = Button(21)

# LED strip configuration:
LED_COUNT      = 331      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

LED_AMPDRAW    = 0.10 #led amp draw
PS_AMPS        = 3 #amps supplied by power supply
PWR_MULT       = PS_AMPS/(LED_AMPDRAW*LED_COUNT)


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

l_s_b = list(range(0,21))#left stomach bottom
l_s_m = list(range(83,64,-1))#left stomach middle
l_s_t = list(range(84,102))#left stomach top
l_c_b = list(range(187,181,-1))
l_c_m = list(range(175,182))
l_c_t = list(range(174,162,-1))
l_b = list(range(145,154))#left back

l_a_t = list(range(205,187,-1))
l_a_b = list(range(206,224))
l_l_i = list(range(312,294,-1))
l_l_o = list(range(313,331))

r_s_b = list(range(41,20,-1))
r_s_m = list(range(42,65))
r_s_t = list(range(119,101,-1))
r_c_b = list(range(120,126))#left chest bottom
r_c_m = list(range(132,125,-1))#left chest middle
r_c_t = list(range(133,145))#left chest top
r_b = list(range(162,153,-1))

r_a_t = list(range(241,223,-1))#left arm top
r_a_b = list(range(242,259))#left arm bottom
r_l_i = list(range(276,258,-1))#left leg inside
r_l_o = list(range(277,295))#left leg outside


#------------------------
def debugColors():
    #first strip RIGHT
    strip.setPixelColor(0, Color(int(255*PWR_MULT),int(255*PWR_MULT),int(255*PWR_MULT)) )
    strip.setPixelColor(20, Color(int(255*PWR_MULT),int(255*PWR_MULT),int(255*PWR_MULT)) )
    strip.setPixelColor(41, Color(int(255*PWR_MULT),int(255*PWR_MULT),int(255*PWR_MULT)) )

    #second strip LEFT
    strip.setPixelColor(42, Color(0,int(255*PWR_MULT),int(255*PWR_MULT)) )
    strip.setPixelColor(64, Color(0,int(255*PWR_MULT),int(255*PWR_MULT)) )
    strip.setPixelColor(83, Color(0,int(255*PWR_MULT),int(255*PWR_MULT)) )
    
    #third strip RIGHT
    strip.setPixelColor(84, Color(int(255*PWR_MULT),0,int(255*PWR_MULT)) )
    strip.setPixelColor(101, Color(int(255*PWR_MULT),0,int(255*PWR_MULT)) )
    strip.setPixelColor(119, Color(int(255*PWR_MULT),0,int(255*PWR_MULT)) )

    #lowest right chest LEFT
    strip.setPixelColor(120, Color(int(255*PWR_MULT),int(255*PWR_MULT),0) )
    strip.setPixelColor(125, Color(int(255*PWR_MULT),int(255*PWR_MULT),0) )
    
    #middle right chest RIGHT
    strip.setPixelColor(126, Color(int(255*PWR_MULT),0,0) )
    strip.setPixelColor(132, Color(int(255*PWR_MULT),0,0) )

    #top right chest UP
    strip.setPixelColor(133, Color(0,int(255*PWR_MULT),0) )
    strip.setPixelColor(144, Color(0,int(255*PWR_MULT),0) )

    #back RIGHT
    strip.setPixelColor(145, Color(0,int(255*PWR_MULT),0) )
    strip.setPixelColor(162, Color(0,int(255*PWR_MULT),0) )

    #top left chest DOWN
    strip.setPixelColor(163, Color(0,0,int(255*PWR_MULT)) )
    strip.setPixelColor(174, Color(0,0,int(255*PWR_MULT)) )

    #middle left chest RIGHT
    strip.setPixelColor(175, Color(int(255*PWR_MULT),int(255*PWR_MULT),int(255*PWR_MULT)) )
    strip.setPixelColor(181, Color(int(255*PWR_MULT),int(255*PWR_MULT),int(255*PWR_MULT)) )

    #lowest left chest LEFT
    strip.setPixelColor(182, Color(0,int(255*PWR_MULT),int(255*PWR_MULT)) )
    strip.setPixelColor(187, Color(0,int(255*PWR_MULT),int(255*PWR_MULT)) )

    #Right Arm
    #top stripe DOWN
    strip.setPixelColor(188, Color(int(255*PWR_MULT),0,int(255*PWR_MULT)) )
    strip.setPixelColor(205, Color(int(255*PWR_MULT),0,int(255*PWR_MULT)) )
    #bottom stripe UP
    strip.setPixelColor(206, Color(int(255*PWR_MULT),int(255*PWR_MULT),0) )
    strip.setPixelColor(223, Color(int(255*PWR_MULT),int(255*PWR_MULT),0) )

    #left Arm
    #top stripe DOWN
    strip.setPixelColor(224, Color(int(255*PWR_MULT),0,0) )
    strip.setPixelColor(241, Color(int(255*PWR_MULT),0,0) )
    #bottom stripe UP
    strip.setPixelColor(242, Color(int(255*PWR_MULT),int(255*PWR_MULT),0) )
    strip.setPixelColor(258, Color(int(255*PWR_MULT),int(255*PWR_MULT),0) )

    #left leg
    #inside stripe DOWN
    strip.setPixelColor(259, Color(0,int(255*PWR_MULT),0) )
    strip.setPixelColor(276, Color(0,int(255*PWR_MULT),0) )
    #outside stripe UP
    strip.setPixelColor(277, Color(int(255*PWR_MULT),int(255*PWR_MULT),0) )
    strip.setPixelColor(294, Color(int(255*PWR_MULT),int(255*PWR_MULT),0) )

    #right leg
    #inside stripe DOWN
    strip.setPixelColor(295, Color(0,int(255*PWR_MULT),0) )
    strip.setPixelColor(312, Color(0,int(255*PWR_MULT),0) )
    #outside stripe UP
    strip.setPixelColor(313, Color(int(255*PWR_MULT),int(255*PWR_MULT),0) )
    strip.setPixelColor(330, Color(int(255*PWR_MULT),int(255*PWR_MULT),0) )
    
    strip.show()
    time.sleep(50/1000.0)

def bottomUp(style=0,offset=0,wait_ms=12,reverse=False,color=Color(int(255*PWR_MULT),int(255*PWR_MULT),int(255*PWR_MULT))):
    path1 = []
    path2 = []
    path3 = []
    path4 = []
    #create 2 arrays to drive on
    path1.extend(l_l_i)
    path1.extend(l_a_b)
    path1.extend(l_s_b)
    path1.extend(l_s_m)
    path1.extend(l_s_t)
    path1.extend(l_c_b)
    path1.extend(l_c_m)
    path1.extend(l_c_t)
    path1.extend(l_b)

    path2.extend(r_l_i)#left leg outside
    path2.extend(r_a_b)
    path2.extend(r_s_b)
    path2.extend(r_s_m)
    path2.extend(r_s_t)
    path2.extend(r_c_b)
    path2.extend(r_c_m)
    path2.extend(r_c_t)
    path2.extend(r_b)

    path3.extend(l_l_o)#right leg inside
    path3.extend(l_a_t)#right arm bottom

    path4.extend(r_l_o)#right leg outside
    path4.extend(r_a_t)#right arm top

    if reverse:
        path1.reverse()
        path2.reverse()
        path3.reverse()
        path4.reverse()

    #print(max(max(max(len(path1),len(path2)),len(path3)),len(path4)))
    for i in range( max(max(max(len(path1),len(path2)),len(path3)),len(path4)) ):
        if(i<len(path1)):
            if(style>0):
                strip.setPixelColor( path1[i], wheel( (i*(256/len(path1))+offset)&255 ) )
            else:
                strip.setPixelColor(path1[i], color )
        if(i<len(path2)):
            if(style>0):
                strip.setPixelColor(path2[i], wheel( (i*(256/len(path2))+offset)&255 ) )
            else:
                strip.setPixelColor(path2[i], color )
        if(i<len(path3)):
            if(style>0):
                strip.setPixelColor(path3[i], wheel( (i*(256/len(path3))+offset)&255 ) )
            else:
                strip.setPixelColor(path3[i], color )
        if(i<len(path4)):
            if(style>0):
                strip.setPixelColor(path4[i], wheel( (i*(256/len(path4))+offset)&255 ) )
            else:
                strip.setPixelColor(path4[i], color )

        strip.show()
        time.sleep(wait_ms/1000.0)

def insideOut(style=0,offset=0,wait_ms=12, reverse=False, color=Color(int(255*PWR_MULT),int(255*PWR_MULT),int(255*PWR_MULT))):
    path1 = []
    path2 = []
    path3 = []
    path4 = []
    path5 = []
    path6 = []
    path7 = []
    path8 = []
    path9 = []
    path10 = []
    
    path11 = []
    path12 = []
    path13 = []
    path14 = []
    path15 = []
    path16 = []
    path17 = []
    path18 = []
    path19 = []
    path20 = []
    
    path1.extend(l_s_b);
    path2.extend(l_s_m);
    path3.extend(l_s_t);
    path4.extend(l_c_b);
    path5.extend(l_c_m);
    path6.extend(l_c_t);
    path6.extend(l_b);
    path7.extend(l_a_b);
    path8.extend(l_a_t);
    path9.extend(l_l_i);
    path10.extend(l_l_o);

    path11.extend(r_s_b);
    path12.extend(r_s_m);
    path13.extend(r_s_t);
    path14.extend(r_c_b);
    path15.extend(r_c_m);
    path16.extend(r_c_t);
    path16.extend(r_b);
    path17.extend(r_a_b);
    path18.extend(r_a_t);
    path19.extend(r_l_i);
    path20.extend(r_l_o);

    if reverse:
        path1.reverse()
        path2.reverse()
        path3.reverse()
        path4.reverse()
        path5.reverse()
        path6.reverse()
        path7.reverse()
        path8.reverse()
        path9.reverse()
        path10.reverse()
        path11.reverse()
        path12.reverse()
        path13.reverse()
        path14.reverse()
        path15.reverse()
        path16.reverse()
        path17.reverse()
        path18.reverse()
        path19.reverse()
        path20.reverse()

    count = [len(path1),len(path2),len(path3),len(path4),len(path5),len(path6),len(path7),len(path8),len(path9),len(path10),len(path11),len(path12),len(path13),len(path14),len(path15),len(path16),len(path17),len(path18),len(path19),len(path20)]
    for i in range( max(count) ):
        if(i<len(path1)):
            if(style>0):
                strip.setPixelColor( path1[i], wheel( (i*(256/len(path1))+offset)&255 ) )
            else:
                strip.setPixelColor(path1[i], color )
            #strip.setPixelColor(path1[i], color )
        if(i<len(path2)):
            if(style>0):
                strip.setPixelColor( path2[i], wheel( (i*(256/len(path2))+offset)&255 ) )
            else:
                strip.setPixelColor(path2[i], color )
            #strip.setPixelColor(path2[i], color )
        if(i<len(path3)):
            if(style>0):
                strip.setPixelColor( path3[i], wheel( (i*(256/len(path3))+offset)&255 ) )
            else:
                strip.setPixelColor(path3[i], color )
            #strip.setPixelColor(path3[i], color )
        if(i<len(path4)):
            if(style>0):
                strip.setPixelColor( path4[i], wheel( (i*(256/len(path4))+offset)&255 ) )
            else:
                strip.setPixelColor(path4[i], color )
            #strip.setPixelColor(path4[i], color )
        if(i<len(path5)):
            if(style>0):
                strip.setPixelColor( path5[i], wheel( (i*(256/len(path5))+offset)&255 ) )
            else:
                strip.setPixelColor(path5[i], color )
            #strip.setPixelColor(path5[i], color )
        if(i<len(path6)):
            if(style>0):
                strip.setPixelColor( path6[i], wheel( (i*(256/len(path6))+offset)&255 ) )
            else:
                strip.setPixelColor(path6[i], color )
            #strip.setPixelColor(path6[i], color )
        if(i<len(path7)):
            if(style>0):
                strip.setPixelColor( path7[i], wheel( (i*(256/len(path7))+offset)&255 ) )
            else:
                strip.setPixelColor(path7[i], color )
            #strip.setPixelColor(path7[i], color )
        if(i<len(path8)):
            if(style>0):
                strip.setPixelColor( path8[i], wheel( (i*(256/len(path8))+offset)&255 ) )
            else:
                strip.setPixelColor(path8[i], color )
            #strip.setPixelColor(path8[i], color )
        if(i<len(path9)):
            if(style>0):
                strip.setPixelColor( path9[i], wheel( (i*(256/len(path9))+offset)&255 ) )
            else:
                strip.setPixelColor(path9[i], color )
            #strip.setPixelColor(path9[i], color )
        if(i<len(path10)):
            if(style>0):
                strip.setPixelColor( path10[i], wheel( (i*(256/len(path10))+offset)&255 ) )
            else:
                strip.setPixelColor(path10[i], color )
            #strip.setPixelColor(path10[i], color )

        if(i<len(path11)):
            if(style>0):
                strip.setPixelColor( path11[i], wheel( (i*(256/len(path11))+offset)&255 ) )
            else:
                strip.setPixelColor(path11[i], color )
            #strip.setPixelColor(path11[i], color )
        if(i<len(path12)):
            if(style>0):
                strip.setPixelColor( path12[i], wheel( (i*(256/len(path12))+offset)&255 ) )
            else:
                strip.setPixelColor(path12[i], color )
            #strip.setPixelColor(path12[i], color )
        if(i<len(path13)):
            if(style>0):
                strip.setPixelColor( path13[i], wheel( (i*(256/len(path13))+offset)&255 ) )
            else:
                strip.setPixelColor(path13[i], color )
            #strip.setPixelColor(path13[i], color )
        if(i<len(path14)):
            if(style>0):
                strip.setPixelColor( path14[i], wheel( (i*(256/len(path14))+offset)&255 ) )
            else:
                strip.setPixelColor(path14[i], color )
            #strip.setPixelColor(path14[i], color )
        if(i<len(path15)):
            if(style>0):
                strip.setPixelColor( path15[i], wheel( (i*(256/len(path15))+offset)&255 ) )
            else:
                strip.setPixelColor(path15[i], color )
            #strip.setPixelColor(path15[i], color )
        if(i<len(path16)):
            if(style>0):
                strip.setPixelColor( path16[i], wheel( (i*(256/len(path16))+offset)&255 ) )
            else:
                strip.setPixelColor(path16[i], color )
            #strip.setPixelColor(path16[i], color )
        if(i<len(path17)):
            if(style>0):
                strip.setPixelColor( path17[i], wheel( (i*(256/len(path17))+offset)&255 ) )
            else:
                strip.setPixelColor(path17[i], color )
            #strip.setPixelColor(path17[i], color )
        if(i<len(path18)):
            if(style>0):
                strip.setPixelColor( path18[i], wheel( (i*(256/len(path18))+offset)&255 ) )
            else:
                strip.setPixelColor(path18[i], color )
            #strip.setPixelColor(path18[i], color )
        if(i<len(path19)):
            if(style>0):
                strip.setPixelColor( path19[i], wheel( (i*(256/len(path19))+offset)&255 ) )
            else:
                strip.setPixelColor(path19[i], color )
            #strip.setPixelColor(path19[i], color )
        if(i<len(path20)):
            if(style>0):
                strip.setPixelColor( path20[i], wheel( (i*(256/len(path20))+offset)&255 ) )
            else:
                strip.setPixelColor(path20[i], color )
            #strip.setPixelColor(path20[i], color )

        strip.show()
        time.sleep(wait_ms/1000.0)


#------------------
'''keyboard.add_hotkey("p", lambda: temp())

def temp():
    print("PRESSED")'''
# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            '''if keyboard.is_pressed('p'):
                print("yes")'''

            '''if button_2.is_pressed or button_3.is_pressed or button_4.is_pressed:
                colorWipe(strip, Color(90, 0, 0))  # Red wipe'''

            '''print ('Color wipe animations.')
            colorWipe(strip, Color(int(255*PWR_MULT), 0, 0),2)  # Red wipe
            colorWipe(strip, Color(0, int(255*PWR_MULT), 0),10)  # Blue wipe
            colorWipe(strip, Color(0, 0, int(255*PWR_MULT)))  # Green wipe
            print ('Theater chase animations.')
            theaterChase(strip, Color(int(127*PWR_MULT), int(127*PWR_MULT), int(127*PWR_MULT)))  # White theater chase
            theaterChase(strip, Color(int(127*PWR_MULT),   0,   0))  # Red theater chase
            theaterChase(strip, Color(  0,   0, int(127*PWR_MULT)))  # Blue theater chase
            #print ('Rainbow animations.')
            #rainbow(strip)
            #rainbowCycle(strip)
            #theaterChaseRainbow(strip)
            '''

            #debugColors()
 
            bottomUp(style=1,wait_ms=20)
            #time.sleep(5)
            bottomUp(style=1,offset=64,wait_ms=10,reverse=True)
            bottomUp(style=1,offset=128,wait_ms=5)
            bottomUp(style=1,offset=192,wait_ms=2,reverse=True)
            bottomUp(style=1,wait_ms=1)

            colorWipe(strip, Color(int(220*PWR_MULT), int(240*PWR_MULT), int(255*PWR_MULT)),1)  # Red wipe
            #rainbow(strip)
            #rainbowCycle(strip)
            #insideOut(Color(0,0,0),12,True)
            #insideOut(Color(int(255*PWR_MULT),int(255*PWR_MULT),int(255*PWR_MULT)),50)
            #theaterChaseRainbow(strip)
            insideOut(wait_ms = 8,color = Color(0,0,0))
            insideOut(wait_ms = 6,reverse = True, color = Color(int(255*PWR_MULT), int(255*PWR_MULT), int(255*PWR_MULT)))
            insideOut(wait_ms = 4,reverse = True, color = Color(0,0,0))
            insideOut(wait_ms = 2,reverse = True,color = Color(int(255*PWR_MULT), int(255*PWR_MULT), int(255*PWR_MULT)))
            insideOut(wait_ms = 1,reverse = True, color = Color(0,0,0))
            insideOut(wait_ms = 1,reverse = True, color = Color(int(255*PWR_MULT), int(255*PWR_MULT), int(255*PWR_MULT)))
            insideOut(wait_ms = 1,reverse = True, color = Color(0,0,0))
            insideOut(wait_ms = 1,reverse = True, color = Color(int(255*PWR_MULT), int(255*PWR_MULT), int(255*PWR_MULT)))


            insideOut(style = 1,wait_ms = 1)
            insideOut(wait_ms = 1,color = Color(0,0,0))
            insideOut(style = 1, offset = 32, wait_ms = 1)
            insideOut(wait_ms = 1, color = Color(0,0,0))
            insideOut(style = 1, offset = 64, wait_ms = 1)
            insideOut(wait_ms = 1,color = Color(0,0,0))
            insideOut(style = 1,offset = 96,wait_ms = 1)

            bottomUp(wait_ms = 20, color = Color(int(255*PWR_MULT), int(255*PWR_MULT), int(255*PWR_MULT)))
            theaterChase(strip, Color(int(255*PWR_MULT), int(255*PWR_MULT), int(255*PWR_MULT)))  # White theater chase

            #theaterChaseRainbow(strip)
            #theaterChase(strip, Color(int(127*PWR_MULT), int(127*PWR_MULT), int(127*PWR_MULT)))  # White theater chase
            
            bottomUp(wait_ms = 20,reverse=True, color = Color(int(255*PWR_MULT), 0, 0))
            theaterChase(strip, Color(int(255*PWR_MULT), 0, 0))  # White theater chase

            bottomUp(wait_ms = 20,reverse=True, color = Color(0,int(255*PWR_MULT), 0))
            theaterChase(strip, Color(0,int(255*PWR_MULT), 0))  # White theater chase

            bottomUp(wait_ms = 20,reverse=True, color = Color(0,0,int(255*PWR_MULT)))
            theaterChase(strip, Color(0,0,int(255*PWR_MULT)))  # White theater chase

            bottomUp(wait_ms = 20,reverse=True, color = Color(int(255*PWR_MULT),int(255*PWR_MULT),0))
            theaterChase(strip, Color(int(255*PWR_MULT),int(255*PWR_MULT),0))  # White theater chase
            
            bottomUp(wait_ms = 20,reverse=True, color = Color(int(255*PWR_MULT),0,int(255*PWR_MULT)))
            theaterChase(strip, Color(int(255*PWR_MULT),0,int(255*PWR_MULT)))  # White theater chase
            
            bottomUp(wait_ms = 20,reverse=True, color = Color(0,int(255*PWR_MULT),int(255*PWR_MULT)))
            theaterChase(strip, Color(0,int(255*PWR_MULT),int(255*PWR_MULT)))  # White theater chase
            
            bottomUp(wait_ms = 20,reverse=True, color = Color(int(255*PWR_MULT),int(255*PWR_MULT),int(255*PWR_MULT)))
            theaterChase(strip, Color(int(255*PWR_MULT),int(255*PWR_MULT),int(255*PWR_MULT)))  # White theater chase
            
            insideOut(wait_ms = 10,color = Color(0,0,0))

    except KeyboardInterrupt:
        if args.clear:
            #colorWipe(strip, Color(0,0,0), 10)
            insideOut(color = Color(0,0,0),wait_ms = 12,reverse = True)
