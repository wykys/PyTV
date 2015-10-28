#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# created by wykys 2015
#
# This program runs the VLC player with the parameters necessary for playing
# the network stream. It is designed for use in networks KolejNet.
#

import os, psutil
import Tkinter as tk
from platform import system

class PyTV:
    "PyTV initialization"    
    def __init__(self):
        self.win = tk.Tk()        
        self.win.title("PyTV ɔ CC - created by wykys 2015")
        self.win.configure(bg='#222222')
        self.StationInLine = 6
        self.row = 0
        self.column = 0
        self.stations = {}
        self.RouteToVLC = '"C:\Program Files (x86)\VideoLAN\VLC\\vlc.exe"'      #if you are using Windows please insert a valid route to vlc
        # start application                                                     #if you are using Windows rename filename extension of this script to *.pyw to hide Python console
        self.addStations()
        self.runGUI()
    "Play selected station in vlc"
    def play(self, addr):
        if system() == 'Windows':
            for proc in psutil.process_iter():
                if proc.name == 'vlc.exe':
                    proc.kill()
            os.system('start "" /b {0} {1}'.format(self.RouteToVLC, addr))
        elif system() == 'Linux':
            os.system("killall vlc")
            os.system("cvlc {0} &".format(addr))
        else:
            print "I have no idea what operating system are you using :( !"
    "Add station"
    def addStations(self, name=False, addr=False):        
        tmp = False
        fr = open("stations.csv", "r")
        tmp = fr.readlines()    
        fr.close()
        tmp.pop(0) # delete head table

        if tmp != False:
            textcolor = '#FF0066'
            for l in tmp:
                if l == '#FIT VUTBR\n':
                    self.row += 1
                    self.column = 0
                    textcolor = '#00FFFF'
                    continue
                if l == '#CZ RADIO\n':
                    self.row += 1
                    self.column = 0
                    textcolor = '#FF9933'
                    continue
                if l == '#SK RADIO\n':
                    self.row += 1
                    self.column = 0
                    textcolor = '#66FF33'
                    continue
                l = l.split(',')
                name = l[0].strip()
                addr = l[1].strip() 

                if type(name) == str and type(addr) == str:
                    self.column += 1
                    if self.column > self.StationInLine:
                        self.row += 1
                        self.column = 1
                    tk.Button(self.win, text=name, font="Courier 15 bold", command=lambda a=addr: self.play(a), bg='#333333', fg=textcolor).grid(row=self.row, column=self.column, padx=2, pady=2, sticky=tk.W+tk.E)
                    self.stations[name] = addr
    "Run PyTV GUI"
    def runGUI(self):
        self.win.mainloop()    
    "When program window is destroyed"
    def __del__(self):
        if system() == 'Windows':                       #nefunguje
            for proc in psutil.process_iter():
                if proc.name == 'vlc.exe':
                    proc.kill()
        elif system() == 'Linux':
            os.system("killall vlc")


app = PyTV()
