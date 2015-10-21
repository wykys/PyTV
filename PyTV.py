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
        self.StationInLine = 6
        self.row = 0
        self.column = 0
    "Play select station in vlc"
    def play(self, addr):
        os.system("killall vlc")
        os.system("cvlc {0} &".format(addr))
    "Add station"
    def addStation(self, name=False, addr=False):
        if type(name) == str and type(addr) == str:
            self.column += 1
            if self.column > self.StationInLine:
                self.row += 1
                self.column = 1
            tk.Button(self.win, text=name, font="Courier 15 bold", command=lambda a=addr: self.play(a)).grid(row=self.row, column=self.column, padx=2, pady=2, sticky=tk.W+tk.E)
    "Run PyTV GUI"
    def runGUI(self):
        self.win.mainloop()    
    "When is destroy windows"
    def __del__(self):
        os.system("killall vlc")

app = PyTV()
app.addStation("ČT1 HD",            "udp://@239.255.15.1:1234")
app.addStation("ČT2 HD",            "udp://@239.255.15.3:1234")
app.addStation("ČT24",              "udp://@239.255.11.3:1234")
app.addStation("ČT SPORT HD",       "udp://@239.255.15.2:1234")
app.addStation("NOVA",              "udp://@239.255.12.1:1234")
app.addStation("NOVA CINEMA",       "udp://@239.255.12.2:1234")
app.addStation("PRIMA",             "udp://@239.255.12.3:1234")
app.addStation("PRIMA COOL",        "udp://@239.255.12.4:1234")
app.addStation("PRIMA ZOOM",        "udp://@239.255.13.3:1234")
app.addStation("ČT1",               "udp://@239.255.11.1:1234")
app.addStation("ČT2",               "udp://@239.255.11.2:1234")
app.addStation("FANDA",             "udp://@239.255.14.4:1234")
app.addStation("ČT Sport",          "udp://@239.255.11.4:1234")
app.addStation("TV BARRANDOV",      "udp://@239.255.12.5:1234")
app.addStation("PRIMA LOVE",        "udp://@239.255.13.1:1234")
app.addStation("ÓČKO",              "udp://@239.255.13.2:1234")
app.addStation("ÓČKO GOLD",         "udp://@239.255.13.6:1234")
app.addStation("ACTIVE",            "udp://@239.255.13.7:1234")
app.addStation("ČT D / ČT ART",     "udp://@239.255.13.8:1234")
app.addStation("KINO BARRANDOV",    "udp://@239.255.13.9:1234")
app.addStation("RELAX POHODA",      "udp://@239.255.14.3:1234")
app.addStation("SMÍCHOV",           "udp://@239.255.14.5:1234")
app.addStation("TELKA",             "udp://@239.255.14.6:1234")
app.addStation("REBEL",             "udp://@239.255.14.7:1234")
app.addStation("BTV",               "udp://@239.255.14.9:1234")
app.addStation("RETRO MUSIC",       "udp://@239.255.15.5:1234")
app.addStation("KINOSVET",          "udp://@239.255.15.6:1234")
app.addStation("JOJ",               "udp://@239.255.16.1:1234")
app.addStation("JOJ PLUS",          "udp://@239.255.16.2:1234")
app.addStation("MARKÍZA",           "udp://@239.255.16.3:1234")
app.addStation("DOMA",              "udp://@239.255.16.4:1234")
app.addStation("TA3",               "udp://@239.255.16.5:1234")
app.addStation("JOJ WAU",           "udp://@239.255.17.1:1234")
app.addStation("8SEM",              "udp://@239.255.17.3:1234")
app.addStation("JOJ SENZI",         "udp://@239.255.17.4:1234")
app.addStation("STV: 1",            "udp://@239.255.20.1:1234")
app.addStation("STV: 2",            "udp://@239.255.20.2:1234")
app.addStation("STV: 1 HD",         "udp://@239.255.20.3:1234")
app.runGUI()
