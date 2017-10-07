#!/usr/bin/python

from Tkinter import *
from xml.dom import minidom
from PIL import ImageTk, Image

"""" GUI Created Based on a 16:9 ratio, most calculations taking into account 9 large sections going vertically. """
    #Adjust line 59 to optimize the right ratio.

class MyFirstGUI:
    def __init__(self, master):
        self.master = master

        #Hardcoded. Will movie the entirety of the screen cpadx pixels in, cpady pixels out.
        self.cpadx = 5
        self.cpady = 25
        self.bg = '#EC1C24'

        #Grabs Width and Height of the Screen.
        self.screen_width, self.screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
        #self.screen_width, self.screen_height = 380, 200
        master.overrideredirect(1)
        master.geometry("%dx%d+0+0" % (self.screen_width,self.screen_height))
        master.title("HackHarvard 2017")
        master.config(background = self.bg)
        master.bind("<Button-2>", self.quitout) #Ends GUI.

        self.create_canvas(master)

    #Initializes all Widgets.
    def create_canvas(self, master):
        self.w = Canvas(self.master, width=self.screen_width, height=self.screen_height, )
        self.w.config(bd= 0, highlightbackground = self.bg, highlightcolor = self.bg, background = self.bg)
        self.w.pack()

        self.logos(master)
        #self.HH_title(master)
        #self.HH_slogan(master)
        self.HH_main_image(master)

    def quitout(self,Event=None):
		root.quit()

    #HackHarvard Logos display on top left, top right.
    def logos(self, master):
        #Gets the images.
        image = Image.open("./Resources/HH_Logo.jpg")

        #Converts original size of image to floats.
        o_w, o_h = image.size
        o_w = float(o_w)
        o_h = float(o_h)

        #Resizes original image to 2/9 of height of image.
        scalar = (2.0/9.0) * float(self.screen_height) * (1.0/float(o_h))
        new_w  = scalar * o_w
        new_h = scalar * o_h
        resized = image.resize((int(new_w),int(new_h)),Image.NEAREST)
        final_photo = ImageTk.PhotoImage(resized)

        #Creates the Photo
        self.left_logo = self.w.create_image(self.cpadx + new_w/2, self.cpady + new_h/2, image = final_photo)
        self.right_logo = self.w.create_image((-1 * self.cpadx) + self.screen_width - new_w/2, self.cpady + new_h/2, image = final_photo)

        self.w.image = final_photo #Maintains reference

        #For use in HH_title
        self.logo_w = float(new_w)
        self.logo_h = float(new_h)

    #Main image of HackHarvard in between two logos.
    def HH_main_image(self, master):
        #Gets the images.
        image = Image.open("./Resources/HH_Main_Photo.jpg")

        #Converts original size of image to floats.
        o_w, o_h = image.size
        o_w = float(o_w)
        o_h = float(o_h)



        #Resizes original image to 3/9 of height of image.
        #OLD SCALAR< REMOVE scalar = (3.0/9.0) * float(self.screen_height) * (1.0/float(o_h))
        remaining = int( float(self.screen_width) - 2.0*(float(self.logo_w)) )
        scalar = remaining / o_w
        new_w  = scalar * o_w
        new_h = scalar * o_h
        resized = image.resize((int(new_w),int(new_h)),Image.NEAREST)
        final_photo = ImageTk.PhotoImage(resized)

        #Creates the Photo
        self.main_photo = self.w.create_image(self.cpadx + self.logo_w + new_w/2, self.cpady + new_h/2, image = final_photo)
        self.w.image0 = final_photo #Maintains reference
        #self.w.lower(main)

        #1. Open Image

        #2. Resize image so that the width = space between two logos.

        #3. Paste in image.

    #Will create title in between the two logos.
    def HH_title(self,master):
        remaining = int( float(self.screen_width) - 2.0*(float(self.new_w)) )

        #self.text = self.w.create_text(self.screen_width/2,self.screen_height/2,text="HackHarvard 2017",font=("avantgarde", 12))
        Title_x = float(self.new_w) + float(remaining)/2.0
        Title_y = float(self.new_h)/2
        self.Title = self.w.create_text(Title_x, Title_y + self.cpady, text="HackHarvard 2017",font=("courier", 12), fill = "white")
        Title_bound =  self.w.bbox(self.Title)

        #Increases font to fit desired size.
        n = 0
        while Title_bound[2] - Title_bound[0] < remaining:
            self.w.itemconfig(self.Title, font=("avantgarde", 12 + n))
            n = n + 1
            print n
            Title_bound =  self.w.bbox(self.Title)

    #Will create title in between the two logos.
    def HH_slogan(self,master):

        #Will take up half of the space horizontally between the logos.
        remaining = int( (float(self.screen_width) - 2.0*(float(self.new_w)))/2 )

        #self.text = self.w.create_text(self.screen_width/2,self.screen_height/2,text="HackHarvard 2017",font=("avantgarde", 12))
        text_x = float(self.new_w) + float(remaining)/2.0
        text_y = self.w.bbox(self.Title)[3]/2
        self.text = self.w.create_text(remaining/2 + text_x, 2 * text_y, text="Breaking New Ground.",font=("courier", 12), anchor = CENTER, fill = "white")
        text_bound =  self.w.bbox(self.text)

        #Increases font to fit desired size.
        n = 0
        while text_bound[2] - text_bound[0] < remaining:
            self.w.itemconfig(self.text, font=("avantgarde", 12 + n))
            n = n + 1
            print n
            text_bound =  self.w.bbox(self.text)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
