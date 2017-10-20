#!/usr/bin/python
import sys, os, time

class Setup:
    def __init__(self):
        if len(sys.argv) != 2:
            print "Usage: ./setup.py install"
            return
        if sys.argv[1] == "install":
            print "Welcome to Mohib's Tkinter Dash! Installling..."
            time.sleep(.5)
            self.packages()
            print "Download completed!"

    def packages(self):
        os.system("sudo chmod a+x Scripts/*.py")
        os.system("sudo apt-get update")
        os.system("sudo apt-get install python-imaging-tk")
        os.system("sudo apt-get install imagemagick")

Setup()
