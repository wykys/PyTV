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

import os
import Tkinter as tk

class PyTV:
    "PyTV initialization"    
    def __init__(self):
        self.win = tk.Tk()        
        self.win.title("PyTV ɔ CC - created by wykys 2015")        
    "Play select station in vlc"
    def play(self, addr):
        os.system("killall vlc")
        os.system("cvlc " + addr + " &")
    "Add station"
    def addStaion(self, name=False, addr=False):
        if type(name) == str and type(addr) == str:
            tk.Button(self.win, text=name, font="Courier 15 bold", command=lambda a=addr: self.play(a)).pack(side=tk.LEFT, padx=2)
    "Run PyTV GUI"
    def runGUI(self):
        self.win.mainloop()    
    "When is destroy windows"
    def __del__(self):
        os.system("killall vlc")

app = PyTV()
app.addStaion("ČT1",    "udp://@239.255.11.1:1234")
app.addStaion("ČT2",    "udp://@239.255.11.2:1234")
app.addStaion("ČT24",   "udp://@239.255.11.3:1234")
app.addStaion("ZOOM",   "udp://@239.255.13.3:1234")
app.addStaion("COOL",   "udp://@239.255.12.4:1234")
app.addStaion("NOVA",   "udp://@239.255.12.1:1234")
app.addStaion("FANDA",  "udp://@239.255.14.4:1234")
app.addStaion("CINEMA", "udp://@239.255.12.2:1234")
app.runGUI()

