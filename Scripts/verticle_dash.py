#!/usr/bin/python

from Tkinter import *
from xml.dom import minidom
from PIL import ImageTk, Image

file = open("orientation.txt", "r")
orientation = file.readline()
print orientation

"""" GUI Created Based on a 16:9 ratio, most calculations taking into account 9 large sections going vertically. """

class HHDashboard:
    def __init__(self, master):
        self.master = master

        #Will movie the entirety of the screen cpadx pixels in, cpady pixels out.
        self.cpadx = 6
        self.cpady = 25

        #Background Color
        self.bg = '#E20029'
        #Custom Information
        window_title = "HackHarvard 2017"

        #Grabs Width and Height of the Screen.
        self.screen_width, self.screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
        self.screen_width, self.screen_height = 360, 640

        #Forces Full Screen Mode with Title
        master.overrideredirect(1)
        master.geometry("%dx%d+0+0" % (self.screen_width,self.screen_height))
        master.title(window_title)
        master.config(background = self.bg)

        #Right Clicking GUI Will Quit.
        master.bind("<Button-2>", self.quitout)
        master.bind("<Button-1>", self.quitout)
        master.bind("<Button-3>", self.quitout)

        #Initiates Creation of Canvas Function.
        self.create_canvas(master)

    #Initializes all Widgets.
    def create_canvas(self, master):
        #Creates Canvas, w, of size of the screen. with appropriate coloring.
        self.w = Canvas(self.master, width=self.screen_width, height=self.screen_height, )
        self.w.config(bd= 0, highlightbackground = self.bg, highlightcolor = self.bg, background = self.bg)
        self.w.pack()

        self.logos(master)
        self.HH_main_image(master)
        self.schedule(master)
        self.alert_dash(master)


    #HackHarvard Logos display on top left, top right.
    def logos(self, master):
        #Gets the images.
        image = Image.open("../Resources/HH_Logo.png")

        #Converts original size of image to floats.
        o_w, o_h = image.size
        o_w = float(o_w)
        o_h = float(o_h)

        #Resizes original image to 2/9 of height of image.
        scalar = (2.0/16.0) * float(self.screen_height) * (1.0/float(o_h))
        new_w  = scalar * o_w
        new_h = scalar * o_h
        resized = image.resize((int(new_w),int(new_h)),Image.ANTIALIAS)
        final_photo = ImageTk.PhotoImage(resized)

        #Creates the Photo
        self.left_logo = self.w.create_image(self.cpadx + new_w/2, self.cpady + new_h/2, image = final_photo)
        self.right_logo = self.w.create_image((-1 * self.cpadx) + self.screen_width - new_w/2, self.cpady + new_h/2, image = final_photo)

        #Maintains reference
        self.w.image = final_photo

        #For use in HH_title
        self.logo_w = float(new_w)
        self.logo_h = float(new_h)

    #Main image of HackHarvard in between two logos.
    def HH_main_image(self, master):
        #Gets the image.
        image = Image.open("../Resources/HH_Main_Photo.jpg")

        #Converts original size of image to floats.
        o_w, o_h = image.size
        o_w = float(o_w)
        o_h = float(o_h)

        #How much space is remaining between logos.
        remaining = int( float(self.screen_width) - 2.0*(float(self.logo_w)) )

        #Goes based on 2/9 of height
        new_h = (2.0/9.0)*self.screen_height
        new_w = (new_h/o_h)* o_w

        resized = image.resize((int(new_w),int(new_h)),Image.ANTIALIAS)
        final_photo = ImageTk.PhotoImage(resized)

        #Creates the Photo
        self.main_photo = self.w.create_image(self.cpadx + self.logo_w + remaining/2, 1.5*self.cpady + new_h/2, image = final_photo)

        #Maintains reference
        self.w.image0 = final_photo

    #Creates schedule under the logo.
    def schedule(self, master):
        self.schedule_refresh_counter = 0
        self.r_schedule(master)

    def r_schedule(self, master):
        #Gets the images.
        image = Image.open("../Resources/schedule.jpg")

        #Converts original size of image to floats.
        o_w, o_h = image.size
        o_w = float(o_w)
        o_h = float(o_h)

        #Goes based on 3.25/9 of height
        new_h = (3.75/9.0)*self.screen_height
        new_w = (new_h/o_h)* o_w

        resized = image.resize((int(new_w),int(new_h)),Image.ANTIALIAS)
        final_photo = ImageTk.PhotoImage(resized)

        x_coord = self.cpadx + self.screen_width/2
        y_coord = 0*self.cpady + (4.50 * self.screen_height)/9

        print self.schedule_refresh_counter


        #Creates the Initial Photo
        if self.schedule_refresh_counter == 0:
            self.main_photo = self.w.create_image(x_coord, y_coord, image = final_photo)
            #Maintains reference
            self.w.image1 = final_photo

        #Re-uploads new image of same name, adjusting image + placement.
        if self.schedule_refresh_counter != 0:
            self.w.itemconfig(self.main_photo, image = final_photo)
            self.w.coords(self.main_photo, (x_coord, y_coord))
            #Maintains reference
            self.w.image1 = final_photo

        self.schedule_refresh_counter += 1

        self.w.after(10000, lambda: self.r_schedule(master))

        #Creates the Photo
        self.main_photo = self.w.create_image(self.cpadx + self.screen_width/2, 0*self.cpady + (4.25 * self.screen_height)/9, image = final_photo)
        self.w.image1 = final_photo #Maintains reference

    #Creates schedule under the logo.
    def alert_dash(self, master):
        self.alert_refresh_counter = 0
        self.r_alert_dash(master)

    def r_alert_dash(self, master):

        #Gets the images.
        image = Image.open("../Resources/alert-d.jpg")

        #Converts original size of image to floats.
        o_w, o_h = image.size
        o_w = float(o_w)
        o_h = float(o_h)

        #Goes based on 2/9 of height
        new_h = (2.0/9.0)*self.screen_height
        new_w = (new_h/o_h)* o_w


        x_coord = self.cpadx + self.screen_width/2
        y_coord = 0*self.cpady + (7.75 * self.screen_height)/9

        resized = image.resize((int(new_w),int(new_h)),Image.ANTIALIAS)
        final_photo = ImageTk.PhotoImage(resized)

        #Creates the Photo
        if self.alert_refresh_counter == 0:
            self.main_photo = self.w.create_image(x_coord, y_coord, image = final_photo)
            self.w.image2 = final_photo #Maintains reference

        #Re-uploads new image of same name, adjusting image + placement.
        if self.alert_refresh_counter != 0:
            self.w.itemconfig(self.main_photo, image = final_photo)
            self.w.coords(self.main_photo, (x_coord, y_coord))
            self.w.image2 = final_photo #Maintains reference

        self.alert_refresh_counter += 1

        self.w.after(10000, lambda: self.r_alert_dash(master))

    def quitout(self,Event=None):
		root.quit()

root = Tk()
my_gui = HHDashboard(root)
root.mainloop()
