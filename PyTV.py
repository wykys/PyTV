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

import os, platform, psutil
import Tkinter as tk

class PyTV:
    "PyTV initialization"    
    def __init__(self):
        self.win = tk.Tk()        
        self.win.title("PyTV ɔ CC - created by wykys 2015")
        self.StationInLine = 6
        self.row = 0
        self.column = 0
        self.stations = {}
        self.RouteToVLC = '"C:\Program Files (x86)\VideoLAN\VLC\\vlc.exe"'    #if you are a windows user please insert a valid route to vlc
        # start application
        self.addStations()
        self.runGUI()
    "Play selected station in vlc"
    def play(self, addr):
        if platform.system() == 'Windows':
            try:
                for proc in psutil.process_iter():
                    if proc.name == 'vlc.exe':
                        proc.kill()
            except:
                pass
            os.system('start "" /b {0} {1}'.format(self.RouteToVLC, addr))
            return
        else:
            os.system("killall vlc")
            os.system("cvlc {0} &".format(addr))
    "Add station"
    def addStations(self, name=False, addr=False):        
        tmp = False
        fr = open("stations.csv", "r")
        tmp = fr.readlines()    
        fr.close()
        tmp.pop(0) # delete head table

        if tmp != False:
            for i in tmp:
                i = i.split(',')
                name = i[0].strip()
                addr = i[1].strip()                

                if type(name) == str and type(addr) == str:
                    self.column += 1
                    if self.column > self.StationInLine:
                        self.row += 1
                        self.column = 1
                    tk.Button(self.win, text=name, font="Courier 15 bold", command=lambda a=addr: self.play(a)).grid(row=self.row, column=self.column, padx=2, pady=2, sticky=tk.W+tk.E)
                    self.stations[name] = addr
    "Run PyTV GUI"
    def runGUI(self):
        self.win.mainloop()    
    "When program window is destroyed"
    def __del__(self):
        os.system("killall vlc")

app = PyTV()
