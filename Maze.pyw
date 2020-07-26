#imports:
try:
    from tkinter import *
    from tkinter import messagebox
except ImportError:
    from Tkinter import *
    from Tkinter import messagebox

try:
    import pygame

except ImportError:
    os.system('py -m pip install pygame')

import math, time, os, webbrowser

root = Tk()

#variables:
global sound

try:
    s = open("settings/sound.txt","r")
    a = s.read()
    sound = int(a)
except:
    s = open("settings/sound.txt","w")
    s.write("1")
    sound = 1

global pcol
try:
    s = open("settings/color.txt","r")
    plcol = s.read()
except:
    s = open("settings/color.txt","w")
    s.write("white")
    plcol = 'white'

#color test
try:
    color = Button(bg = plcol)
except:
    messagebox.showwarning("Player Color Error", "Invalid Color in Player Color Settings, go to the settings to change it")

if plcol == 'orange' or plcol == 'red' or plcol == 'black' or plcol == 'yellow' or plcol == 'gold' or plcol == 'light blue':
    messagebox.showwarning("Bad Color Selection for player", "Your selected color for your player will make the player extremely hard to see, but you can still play")

global menu
menu = 1
global bs
bs = 1
global mbs
mbs = 1
global sbs
sbs = 1
global mmbs
mmbs = 2
global loop
loop = 1
global time
time = 0
global warp
warp = 0
global mfs
mfs = 1

global ms
global cell_size


soundg = StringVar()

#levels

def levelonel():
    global ms, cell_size, bs, sound, ffs, map, row, col, warp, timel, leveln, time, loop
    leveln = "Bloom"
    loop = 1
    if sound == 1:
        select.play()
    root.unbind("<Return>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    root.bind("<a>", movepa)
    root.bind("<KeyPress-Left>", movepa)
    root.bind("<KeyPress-Right>", movepd)
    root.bind("<w>", movepw)
    root.bind("<KeyPress-Up>", movepw)
    root.bind("<s>", moveps)
    root.bind("<KeyPress-Down>", moveps)
    root.bind("<d>", movepd)
    timel = Label(root, font = ("arial", 15), text = "Loading...", bg = "black", fg = "orange")
    timel.place(x = 20,y = 20)
    dev.pack_forget()
    logo.pack_forget()
    levelone.pack_forget()
    leveltwo.pack_forget()
    levelthree.pack_forget()
    back.pack_forget()
    ls.config(text = "Bloom")
    if sound == 1:
        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load('./Music/Bloom.ogg')
            pygame.mixer.music.play(-1)
        except:
            messagebox.showwarning("Music File Not Found Error", "Can not find the file Bloom.ogg, make sure it is in the right directorie")
    ms = 10
    cell_size = 50

    map = [['w' for _ in range(ms)] for _ in range(ms)]

    l = open("./bloom/y2.txt","r")
    r = l.read()
    row = 1
    col = 0
    for x in r:
        map[1][col] = x
        col = col + 1
    l = open("./bloom/y3.txt","r")
    r = l.read()
    row = 2
    col = 0
    for x in r:
        map[2][col] = x
        col = col + 1
    l = open("./bloom/y4.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[3][col] = x
        col = col + 1
    l = open("./bloom/y5.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[4][col] = x
        col = col + 1
    l = open("./bloom/y6.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[5][col] = x
        col = col + 1
    l = open("./bloom/y7.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[6][col] = x
        col = col + 1
    l = open("./bloom/y8.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[7][col] = x
        col = col + 1
    l = open("./bloom/y9.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[8][col] = x
        col = col + 1
    l = open("./bloom/warp.txt","r")
    warp = l.read()
    canvas_side = ms*cell_size
    ffs = Canvas(root, width = canvas_side, height = canvas_side, bg = 'grey')
    ffs.pack()
    timer()
    create()

def create():
    "Create a rectangle with draw function (below) with random color"
    global map
    for row in range(ms):
        for col in range(ms):
            if map[row][col] == 'g':
                color = 'black'
            elif map[row][col] == 'w':
                color = 'orange'
            elif map[row][col] == 'p':
                color = plcol
            elif map[row][col] == 'f':
                color = 'red'
            elif map[row][col] == 'n':
                color = 'light blue'
            elif map[row][col] == 'r':
                color = 'yellow'
            draw(row, col, color)

def timer():
    global time, loop
    if loop == 1:
        time = time + 1
        timel.config(text = "{} sec".format(time))
        root.after(1000, timer)

def draw(row, col, color):
    global y1, y2, x1, x2, px1, px2, py1, py2, prow, pcol, map
    if map[row][col] == 'p':
        px1 = col * cell_size
        py1 = row * cell_size
        px2 = px1 + cell_size
        py2 = py1 + cell_size
        prow = row
        pcol = col
        map[row][col] = 'g'
    x1 = col * cell_size
    y1 = row * cell_size
    x2 = x1 + cell_size
    y2 = y1 + cell_size
    print("block complete")
    ffs.create_rectangle(x1, y1, x2, y2, fill=color)

def draw_rect(px1, py1, cell_size):
    print("making rect")
    ffs.create_rectangle((px1, py1, px1 + cell_size, py1 + cell_size), fill=plcol)

def del_rect():
    global movec
    movec = 0
    print("deleting rect in {} {}".format(prow, pcol))
    ffs.create_rectangle((px1, py1, px1 + cell_size, py1 + cell_size), fill="black")


def movepa(event):
    global px1, py1, cell_size , prow, pcol, sound, ms, movec
    print("B: {} {}".format(prow, pcol))
    del_rect()
    if map[prow][pcol - 1] == "f":
        if sound == 1:
            move.play()
        movec = 1
        px1 = px1 - cell_size
        pcol = pcol - 1
        finish()
    if movec == 0:
        if map[prow][pcol - 1] == "g":
            if sound == 1:
                move.play()
            movec = 1
            px1 = px1 - cell_size
            pcol = pcol - 1
    if movec == 0:
        if map[prow][pcol - 1] == "r":
            if sound == 1:
                move.play()
            movec = 1
            px1 = px1 - cell_size
            pcol = pcol - 1
            map[prow][pcol] = 'g'
            root.bind("<a>", movepd)
            root.bind("<KeyPress-Left>", movepd)
            root.bind("<KeyPress-Right>", movepa)
            root.bind("<w>", moveps)
            root.bind("<KeyPress-Up>", moveps)
            root.bind("<s>", movepw)
            root.bind("<KeyPress-Down>", movepw)
            root.bind("<d>", movepa)
    if movec == 0:
        if map[prow][pcol - 1] == "n":
            if sound == 1:
                move.play()
            movec = 1
            px1 = px1 - cell_size
            pcol = pcol - 1
            map[prow][pcol] = 'g'
            root.bind("<a>", movepa)
            root.bind("<KeyPress-Left>", movepa)
            root.bind("<KeyPress-Right>", movepd)
            root.bind("<w>", movepw)
            root.bind("<KeyPress-Up>", movepw)
            root.bind("<s>", moveps)
            root.bind("<KeyPress-Down>", moveps)
            root.bind("<d>", movepd)
    if pcol == -1:
        if sound == 1:
            move.play()
        pcol = pcol + ms
        px1 = px1 + cell_size * ms
    draw_rect(px1, py1, cell_size)

    print("A: {} {}".format(prow, pcol))

def movepd(event):
    global px1, py1, cell_size , prow, pcol, sound, movec
    print("B: {} {}".format(prow, pcol))
    del_rect()
    try:
        if map[prow][pcol + 1] == "f":
            if sound == 1:
                move.play()
            movec = 1
            px1 = px1 + cell_size
            pcol = pcol + 1
            finish()
    except:
        print("")
    try:
        if movec == 0:
            if map[prow][pcol + 1] == "g":
                if sound == 1:
                    move.play()
                movec = 1
                px1 = px1 + cell_size
                pcol = pcol + 1
    except:
        print("")
    try:
        if movec == 0:
            if map[prow][pcol + 1] == "r":
                if sound == 1:
                    move.play()
                movec = 1
                px1 = px1 + cell_size
                pcol = pcol + 1
                map[prow][pcol] = 'g'
                root.bind("<a>", movepd)
                root.bind("<KeyPress-Left>", movepd)
                root.bind("<KeyPress-Right>", movepa)
                root.bind("<w>", moveps)
                root.bind("<KeyPress-Up>", moveps)
                root.bind("<s>", movepw)
                root.bind("<KeyPress-Down>", movepw)
                root.bind("<d>", movepa)
    except:
         print("")   
    try:
        if movec == 0:
            if map[prow][pcol + 1] == "n":
                if sound == 1:
                    move.play()
                movec = 1
                px1 = px1 + cell_size
                pcol = pcol + 1
                map[prow][pcol] = 'g'
                root.bind("<a>", movepa)
                root.bind("<KeyPress-Left>", movepa)
                root.bind("<KeyPress-Right>", movepd)
                root.bind("<w>", movepw)
                root.bind("<KeyPress-Up>", movepw)
                root.bind("<s>", moveps)
                root.bind("<KeyPress-Down>", moveps)
                root.bind("<d>", movepd)
    except:
        if sound == 1:
            move.play()
        pcol = pcol - ms + 1
        ms2 = ms - 1
        px1 = px1 - cell_size * ms2
    draw_rect(px1, py1, cell_size)
    print("A: {} {}".format(prow, pcol))
    print("X = {} Y = {}".format(px1, py1))


def movepw(event):
    global px1, py1, cell_size , prow, pcol, sound, movec, recol
    print("B: {} {}".format(prow, pcol))
    del_rect()
    if map[prow - 1][pcol] == "f":
        if sound == 1:
            move.play()
            movec = 1
        py1 = py1 - cell_size
        prow = prow - 1
        finish()
    if movec == 0:
        if map[prow - 1][pcol] == "g":
            if sound == 1:
                move.play()
            movec = 1
            py1 = py1 - cell_size
            prow = prow - 1
    if movec == 0:
        if map[prow - 1][pcol] == "r":
            if sound == 1:
                move.play()
            movec = 1
            py1 = py1 - cell_size
            prow = prow - 1
            map[prow][pcol] = 'g'
            root.bind("<a>", movepd)
            root.bind("<KeyPress-Left>", movepd)
            root.bind("<KeyPress-Right>", movepa)
            root.bind("<w>", moveps)
            root.bind("<KeyPress-Up>", moveps)
            root.bind("<s>", movepw)
            root.bind("<KeyPress-Down>", movepw)
            root.bind("<d>", movepa)
    if movec == 0:
        if map[prow - 1][pcol] == "n":
            if sound == 1:
                move.play()
            movec = 1
            py1 = py1 - cell_size
            prow = prow - 1
            map[prow][pcol] = 'g'
            root.bind("<a>", movepa)
            root.bind("<KeyPress-Left>", movepa)
            root.bind("<KeyPress-Right>", movepd)
            root.bind("<w>", movepw)
            root.bind("<KeyPress-Up>", movepw)
            root.bind("<s>", moveps)
            root.bind("<KeyPress-Down>", moveps)
            root.bind("<d>", movepd)
    draw_rect(px1, py1, cell_size)
    print("A: {} {}".format(prow, pcol))


def moveps(event):
    global px1, py1, cell_size , prow, pcol, sound, movec
    print("B: {} {}".format(prow, pcol))
    del_rect()
    if map[prow + 1][pcol] == "f":
        if sound == 1:
            move.play()
        movec = 1
        py1 = py1 + cell_size
        prow = prow + 1
        finish()
    if movec == 0:
        if map[prow + 1][pcol] == "g":
            if sound == 1:
                move.play()
            py1 = py1 + cell_size
            prow = prow + 1
    if movec == 0:
        if map[prow + 1][pcol] == "r":
            if sound == 1:
                move.play()
            movec = 1
            py1 = py1 + cell_size
            prow = prow + 1
            map[prow][pcol] = 'g'
            root.bind("<a>", movepd)
            root.bind("<KeyPress-Left>", movepd)
            root.bind("<KeyPress-Right>", movepa)
            root.bind("<w>", moveps)
            root.bind("<KeyPress-Up>", moveps)
            root.bind("<s>", movepw)
            root.bind("<KeyPress-Down>", movepw)
            root.bind("<d>", movepa)
    if movec == 0:
        if map[prow + 1][pcol] == "n":
            if sound == 1:
                move.play()
            movec = 1
            py1 = py1 + cell_size
            prow = prow + 1
            map[prow][pcol] = 'g'
            root.bind("<a>", movepa)
            root.bind("<KeyPress-Left>", movepa)
            root.bind("<KeyPress-Right>", movepd)
            root.bind("<w>", movepw)
            root.bind("<KeyPress-Up>", movepw)
            root.bind("<s>", moveps)
            root.bind("<KeyPress-Down>", moveps)
            root.bind("<d>", movepd)
    draw_rect(px1, py1, cell_size)
    print("A: {} {}".format(prow, pcol))


def leveltwol():
    global ms, cell_size, bs, sound, ffs, map, row, col, warp, timel, leveln, time, loop
    leveln = "Chaoz"
    loop = 1
    if sound == 1:
        select.play()
    root.unbind("<Return>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    root.bind("<a>", movepa)
    root.bind("<KeyPress-Left>", movepa)
    root.bind("<KeyPress-Right>", movepd)
    root.bind("<w>", movepw)
    root.bind("<KeyPress-Up>", movepw)
    root.bind("<s>", moveps)
    root.bind("<KeyPress-Down>", moveps)
    root.bind("<d>", movepd)
    timel = Label(root, font = ("arial", 15), text = "Loading...", bg = "black", fg = "orange")
    timel.place(x = 20,y = 20)
    dev.pack_forget()
    logo.pack_forget()
    levelone.pack_forget()
    leveltwo.pack_forget()
    levelthree.pack_forget()
    back.pack_forget()
    ls.config(text = "Chaoz")
    if sound == 1:
        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load('./Music/Chaoz.ogg')
            pygame.mixer.music.play(-1)
        except:
            messagebox.showwarning("Music File Not Found Error", "Can not find the file Chaoz.ogg, make sure it is in the right directorie")
    ms = 15
    cell_size = 33

    map = [['w' for _ in range(ms)] for _ in range(ms)]
    
    l = open("./chaoz/y2.txt","r")
    r = l.read()
    row = 1
    col = 0
    for x in r:
        map[1][col] = x
        col = col + 1
    l = open("./chaoz/y3.txt","r")
    r = l.read()
    row = 2
    col = 0
    for x in r:
        map[2][col] = x
        col = col + 1
    l = open("./chaoz/y4.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[3][col] = x
        col = col + 1
    l = open("./chaoz/y5.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[4][col] = x
        col = col + 1
    l = open("./chaoz/y6.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[5][col] = x
        col = col + 1
    l = open("./chaoz/y7.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[6][col] = x
        col = col + 1
    l = open("./chaoz/y8.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[7][col] = x
        col = col + 1
    l = open("./chaoz/y9.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[8][col] = x
        col = col + 1
    l = open("./chaoz/y10.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[9][col] = x
        col = col + 1
    l = open("./chaoz/y11.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[10][col] = x
        col = col + 1
    l = open("./chaoz/y11.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[10][col] = x
        col = col + 1
    l = open("./chaoz/y12.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[11][col] = x
        col = col + 1
    l = open("./chaoz/y13.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[12][col] = x
        col = col + 1
    l = open("./chaoz/y14.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[13][col] = x
        col = col + 1
    l = open("./chaoz/y15.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[14][col] = x
        col = col + 1
    l = open("./chaoz/warp.txt","r")
    warp = l.read()
    canvas_side = ms*cell_size
    ffs = Canvas(root, width = canvas_side, height = canvas_side, bg = 'grey')
    ffs.pack()
    timer()
    create()

def levelthreel():
    global ms, cell_size, bs, sound, ffs, map, row, col, warp, timel, leveln, time, loop
    leveln = "Funky"
    loop = 1
    if sound == 1:
        select.play()
    root.unbind("<Return>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    root.bind("<a>", movepa)
    root.bind("<KeyPress-Left>", movepa)
    root.bind("<KeyPress-Right>", movepd)
    root.bind("<w>", movepw)
    root.bind("<KeyPress-Up>", movepw)
    root.bind("<s>", moveps)
    root.bind("<KeyPress-Down>", moveps)
    root.bind("<d>", movepd)
    timel = Label(root, font = ("arial", 15), text = "Loading...", bg = "black", fg = "orange")
    timel.place(x = 20,y = 20)
    dev.pack_forget()
    logo.pack_forget()
    levelone.pack_forget()
    leveltwo.pack_forget()
    levelthree.pack_forget()
    back.pack_forget()
    ls.config(text = "Funky")
    if sound == 1:
        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load('./Music/Funk.ogg')
            pygame.mixer.music.play(-1, 10.8)
        except:
            messagebox.showwarning("Music File Not Found Error", "Can not find the file Funk.ogg, make sure it is in the right directorie")
    ms = 20
    cell_size = 25

    map = [['w' for _ in range(ms)] for _ in range(ms)]
    
    l = open("./funky/y2.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[1][col] = x
        print("block loaded")
        col = col + 1
    l = open("./funky/y3.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[2][col] = x
        col = col + 1
    l = open("./funky/y4.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[3][col] = x
        col = col + 1
    l = open("./funky/y5.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[4][col] = x
        col = col + 1
    l = open("./funky/y6.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[5][col] = x
        col = col + 1
    l = open("./funky/y7.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[6][col] = x
        col = col + 1
    l = open("./funky/y8.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[7][col] = x
        col = col + 1
    l = open("./funky/y9.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[8][col] = x
        col = col + 1
    l = open("./funky/y10.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[9][col] = x
        col = col + 1
    l = open("./funky/y11.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[10][col] = x
        col = col + 1
    l = open("./funky/y11.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[10][col] = x
        col = col + 1
    l = open("./funky/y12.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[11][col] = x
        col = col + 1
    l = open("./funky/y13.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[12][col] = x
        col = col + 1
    l = open("./funky/y14.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[13][col] = x
        col = col + 1
    l = open("./funky/y15.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[14][col] = x
        col = col + 1
    l = open("./funky/y16.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[15][col] = x
        col = col + 1
    l = open("./funky/y17.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[16][col] = x
        col = col + 1
    l = open("./funky/y18.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[17][col] = x
        col = col + 1
    l = open("./funky/y19.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[18][col] = x
        col = col + 1
    l = open("./funky/y20.txt","r")
    r = l.read()
    col = 0
    for x in r:
        map[19][col] = x
        col = col + 1
    l = open("./funky/warp.txt","r")
    warp = l.read()
    canvas_side = ms*cell_size
    ffs = Canvas(root, width = canvas_side, height = canvas_side, bg = 'grey')
    ffs.pack()
    timer()
    create()



def finish():
    global loop, time, leveln, congrat, timef, levelbackb, sound
    if sound == 1:
        select.play()
    try:
        s = open("settings/{}.txt".format(leveln),"r")
        a = s.read()
        r = int(a)
        if time < r:
            s = open("settings/{}.txt".format(leveln),"w")
            s.write("{}".format(time))
    except:
        s = open("settings/{}.txt".format(leveln),"w")
        s.write("{}".format(time))
    root.unbind("<s>")
    root.unbind("<w>")
    root.unbind("<a>")
    root.unbind("<d>")
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Left>")
    loop = 0
    timel.place_forget()
    ffs.pack_forget()
    ls.config(text = "You have beat: {}".format(leveln))
    timef = Label(text = "Time: {} seconds".format(time), font = ("arial", 15), fg = "orange", bg = "black", pady = 30)
    timef.pack()
    congrat = Label(text = "Congradulations!", font = ("arial", 13), fg = "orange", bg = "black", pady = 20)
    congrat.pack()
    levelbackb = Button(text = "Back", bg = "Orange", fg = "Black", command = levelback, font = ("arial", 13))
    levelbackb.pack()
    time = 0
    root.bind("<Return>", lambda e: levelback())

def levelback():
    global ms, loop, time, leveln
    if sound == 1:
        select.play()
    loop = 0
    time = 0
    ls.config(text = "Level Select")
    ls.pack_forget()
    timef.pack_forget()
    congrat.pack_forget()
    levelbackb.pack_forget()
    root.unbind("<Return>")
    ms = 1
    logo.pack()
    ls.pack()
    levelone.pack()
    leveltwo.pack()
    levelthree.pack()
    back.pack()
    dev.pack(side = BOTTOM)
    if leveln == 'Bloom':
        root.bind("<Return>", lambda e: levelonel())
    if leveln == 'Chaoz':
        root.bind("<Return>", lambda e: leveltwol())
    if leveln == 'Funky':
        root.bind("<Return>", lambda e: levelthreel())
    
    root.bind("<KeyPress-Up>", lambda e: selectarrowu())
    root.bind("<KeyPress-Down>", lambda e: selectarrowd())
    if sound == 1:
        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load('./Music/Overflow.ogg')
            pygame.mixer.music.play(-1)
        except:
            messagebox.showwarning("Music File Not Found Error", "Can not find the file Overflow.ogg, make sure it is in the right directorie")

#level select

def menutwo():
    global select, levelone, back, ls, bs, leveltwo, levelthree
    if sound == 1:
        select.play()
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Left>")
    bg.pack_forget()
    play.place_forget()
    more.place_forget()
    settings.place_forget()
    logo.pack_configure(fill = NONE, expand = "false")
    dev.pack_configure(fill = NONE, expand ="false")
    ls = Label(root, text = "Level Select", fg = "Orange", pady = 30, bg = "black", font = ("arial", 15))
    ls.pack()
    levelone = Button(root, text = "Blooming", bg = "orange", fg = "black", font = ("arial", 13), pady = 10, command = levelonel)
    levelone.pack()
    leveltwo = Button(root, text = "Chaoz", bg = "black", fg = "orange", font = ("arial", 13), pady = 10, command = leveltwol)
    leveltwo.pack()
    levelthree = Button(root, text = "Funky", bg = "black", fg = "orange", font = ("arial", 13), pady = 10, command = levelthreel)
    levelthree.pack()
    back = Button(root, text = "Back", bg = "black", fg = "Orange", pady =10, font = ("arial", 13), command = selectback)
    back.pack()
    root.unbind("<Return>")
    root.bind("<Return>", lambda e: levelonel())
    root.bind("<KeyPress-Up>", lambda e: selectarrowu())
    root.bind("<KeyPress-Down>", lambda e: selectarrowd())

def selectback():
    global ls, levelone, back, select, leveltwo, bs
    if sound == 1:
        select.play()
    bg.pack(side=TOP, expand=YES, fill=BOTH)
    play.place (x = 225,y = 310)
    more.place(x = 330, y = 315)
    settings.place(x = 120, y = 315)
    root.bind("<Return>", lambda e: menutwo())
    root.unbind("<KeyPress-Down>")
    root.unbind("<KeyPress-Up>")
    root.bind("<KeyPress-Right>", lambda e: menuarrowr())
    root.bind("<KeyPress-Left>", lambda e: menuarrowl())
    ls.pack_forget()
    levelone.pack_forget()
    leveltwo.pack_forget()
    levelthree.pack_forget()
    back.pack_forget()
    bs = 1

def selectarrowu():
    global bs
    if sound == 1:
        select.play()
    bs = bs - 1
    if bs == 0:
        bs = bs + 1
    if bs == 5:
        bs = bs -1
    if bs == 1:
        levelone.config(bg = "orange", fg = "black")
        back.config(fg = "orange", bg = "black")
        leveltwo.config(fg = "orange", bg = "black")
        levelthree.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: levelonel())
    if bs == 2:
        leveltwo.config(bg = "orange", fg = "black")
        levelone.config(fg = "orange", bg = "black")
        levelthree.config(fg = "orange", bg = "black")
        back.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: leveltwol())
    if bs == 3:
        levelthree.config(bg = "orange", fg = "black")
        leveltwo.config(fg = "orange", bg = "black")
        levelone.config(fg = "orange", bg = "black")
        back.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: levelthreel())
    if bs == 4:
        back.config(bg = "orange", fg = "black")
        levelone.config(fg = "orange", bg = "black")
        leveltwo.config(fg = "orange", bg = "black")
        levelthree.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: selectback())

def selectarrowd():
    global bs
    if sound == 1:
        select.play()
    bs = bs + 1
    if bs == 0:
        bs = bs + 1
    if bs == 5:
        bs = bs -1
    if bs == 1:
        levelone.config(bg = "orange", fg = "black")
        back.config(fg = "orange", bg = "black")
        leveltwo.config(fg = "orange", bg = "black")
        levelthree.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: levelonel())
    if bs == 2:
        leveltwo.config(bg = "orange", fg = "black")
        levelone.config(fg = "orange", bg = "black")
        levelthree.config(fg = "orange", bg = "black")
        back.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: leveltwol())
    if bs == 3:
        levelthree.config(bg = "orange", fg = "black")
        leveltwo.config(fg = "orange", bg = "black")
        levelone.config(fg = "orange", bg = "black")
        back.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: levelthreel())
    if bs == 4:
        back.config(bg = "orange", fg = "black")
        levelone.config(fg = "orange", bg = "black")
        leveltwo.config(fg = "orange", bg = "black")
        levelthree.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: selectback())
    
#music menu

def menuthree():
    global msl, musicbone, musicbtwo, musicbthree, musicbfour, back2
    if sound == 1:
        select.play()
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Left>")
    music.place_forget()
    record.place_forget()
    how.place_forget()
    subbackb.place_forget()
    subl.pack_forget()
    discordb.pack_forget()
    logo.pack_configure(fill = NONE, expand = "false")
    dev.pack_configure(fill = NONE, expand ="false")
    msl = Label(root, text = "Music", fg = "Orange", pady = 30, bg = "black", font = ("arial", 15))
    msl.pack()
    musicbone = Button(root, text = "EnV - Bloom(Radio Edit)", bg = "orange", fg = "black", font = ("arial", 13), pady = 10, command = musicone)
    musicbone.pack()
    musicbtwo = Button(root, text = "ParagonX9 - Chaoz Impact", bg = "black", fg = "orange", font = ("arial", 13), pady = 10, command = musictwo)
    musicbtwo.pack()
    musicbthree = Button(root, text = "Lemkuuja - Ouais Ouais (ft. SlyLeaf)", bg = "black", fg = "orange", font = ("arial", 13), pady = 10, command = musicthree)
    musicbthree.pack()
    musicbfour = Button(root, text = "Onett - Overflowin4", bg = "black", fg = "orange", font = ("arial", 13), pady = 10, command = musicfour)
    musicbfour.pack()
    back2 = Button(root, text = "Back", bg = "black", fg = "orange", font = ("arial", 13), pady = 10, command = musicback)
    back2.pack()
    root.bind("<Return>", lambda e: musicone())
    root.bind("<KeyPress-Up>", lambda e: musicarrowu())
    root.bind("<KeyPress-Down>", lambda e: musicarrowd())

def musicone():
    global sound
    if sound == 1:
        select.play()
    if sound == 1:
        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load('./Music/Bloom.ogg')
            pygame.mixer.music.play(-1)
        except:
            messagebox.showwarning("Music File Not Found Error", "Can not find the file Bloom.ogg, make sure it is in the right directorie")

def musictwo():
    global sound
    if sound == 1:
        select.play()
    if sound == 1:
        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load('./Music/Chaoz.ogg')
            pygame.mixer.music.play(-1)
        except:
            messagebox.showwarning("Music File Not Found Error", "Can not find the file Chaoz.ogg, make sure it is in the right directorie")

def musicthree():
    global sound
    if sound == 1:
        select.play()
    if sound == 1:
        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load('./Music/Funk.ogg')
            pygame.mixer.music.play(-1, 10.8)
        except:
            messagebox.showwarning("Music File Not Found Error", "Can not find the file Funk.ogg, make sure it is in the right directorie")

def musicfour():
    global sound
    if sound == 1:
        select.play()
    if sound == 1:
        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load('./Music/Overflow.ogg')
            pygame.mixer.music.play(-1)
        except:
            messagebox.showwarning("Music File Not Found Error", "Can not find the file Overflow.ogg, make sure it is in the right directorie")

def musicback():
    global msl, musicbone, musicbtwo, musicbthree, musicbfour, back2, sound, mbs, mfs
    if sound == 1:
        select.play()
    msl.pack_forget()
    musicbone.pack_forget()
    musicbtwo.pack_forget()
    musicbthree.pack_forget()
    musicbfour.pack_forget()
    back2.pack_forget()
    subbackb.place(x = 310, y = 200)
    how.place(x = 220, y = 200)
    record.place(x = 150, y = 200)
    music.place(x = 20, y = 200)
    subl.pack()
    discordb.pack(side = BOTTOM)
    mfs = 1
    root.bind("<Return>", lambda e: menuthree())
    root.bind("<KeyPress-Left>", lambda e: subarrowl())
    root.bind("<KeyPress-Right>", lambda e: subarrowr())
    root.unbind("<KeyPress-Up>")
    root.unbind("<KeyPress-Down>")

    mbs = 1
    if sound == 1:
        pygame.mixer.music.stop()
        try:
            pygame.mixer.music.load('./Music/Overflow.ogg')
            pygame.mixer.music.play(-1)
        except:
            messagebox.showwarning("Music File Not Found Error", "Can not find the file Overflow.ogg, make sure it is in the right directorie")

def musicarrowd():
    global mbs
    if sound == 1:
        select.play()
    mbs = mbs + 1
    if mbs == 6:
        mbs = mbs - 1
    if mbs == 0:
        mbs = mbs + 1
    if mbs == 1:
        musicbone.config(bg = "orange", fg = "black")
        back2.config(fg = "orange", bg = "black")
        musicbtwo.config(fg = "orange", bg = "black")
        musicbthree.config(fg = "orange", bg = "black")
        musicbfour.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: musicone())
    if mbs == 2:
        musicbtwo.config(bg = "orange", fg = "black")
        back2.config(fg = "orange", bg = "black")
        musicbone.config(fg = "orange", bg = "black")
        musicbthree.config(fg = "orange", bg = "black")
        musicbfour.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: musictwo())
    if mbs == 3:
        musicbthree.config(bg = "orange", fg = "black")
        back2.config(fg = "orange", bg = "black")
        musicbone.config(fg = "orange", bg = "black")
        musicbtwo.config(fg = "orange", bg = "black")
        musicbfour.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: musicthree())
    if mbs == 4:
        musicbfour.config(bg = "orange", fg = "black")
        back2.config(fg = "orange", bg = "black")
        musicbone.config(fg = "orange", bg = "black")
        musicbtwo.config(fg = "orange", bg = "black")
        musicbthree.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: musicfour())
    if mbs == 5:
        back2.config(bg = "orange", fg = "black")
        musicbfour.config(fg = "orange", bg = "black")
        musicbone.config(fg = "orange", bg = "black")
        musicbtwo.config(fg = "orange", bg = "black")
        musicbthree.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: musicback())
    
def musicarrowu():
    global mbs
    if sound == 1:
        select.play()
    mbs = mbs - 1
    if mbs == 6:
        mbs = mbs - 1
    if mbs == 0:
        mbs = mbs + 1
    if mbs == 1:
        musicbone.config(bg = "orange", fg = "black")
        back2.config(fg = "orange", bg = "black")
        musicbtwo.config(fg = "orange", bg = "black")
        musicbthree.config(fg = "orange", bg = "black")
        musicbfour.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: musicone())
    if mbs == 2:
        musicbtwo.config(bg = "orange", fg = "black")
        back2.config(fg = "orange", bg = "black")
        musicbone.config(fg = "orange", bg = "black")
        musicbthree.config(fg = "orange", bg = "black")
        musicbfour.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: musictwo())
    if mbs == 3:
        musicbthree.config(bg = "orange", fg = "black")
        back2.config(fg = "orange", bg = "black")
        musicbone.config(fg = "orange", bg = "black")
        musicbtwo.config(fg = "orange", bg = "black")
        musicbfour.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: musicthree())
    if mbs == 4:
        musicbfour.config(bg = "orange", fg = "black")
        back2.config(fg = "orange", bg = "black")
        musicbone.config(fg = "orange", bg = "black")
        musicbtwo.config(fg = "orange", bg = "black")
        musicbthree.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: musicfour())
    if mbs == 5:
        back2.config(bg = "orange", fg = "black")
        musicbfour.config(fg = "orange", bg = "black")
        musicbone.config(fg = "orange", bg = "black")
        musicbtwo.config(fg = "orange", bg = "black")
        musicbthree.config(fg = "orange", bg = "black")
        root.unbind("<Return>")
        root.bind("<Return>", lambda e: musicback())

#settings

def settingsf():
    global sound, ss, sd, sds, sdon, sdoff, sback, pl, plc, plci, plchange, setcolb
    if sound == 1:
        select.play()
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Left>")
    soundg.set("Loading Setting...")
    #sound variable adjustemment for the gui
    if sound == 1:
        soundg.set("On")
    elif sound == 0:
        soundg.set("Off")
    else:
        soundg.set("Sound.py Error: {} is a invalid option".format(sound))
    bg.pack_forget()
    play.place_forget()
    more.place_forget()
    settings.place_forget()
    logo.pack_configure(fill = NONE, expand = "false")
    dev.pack_configure(fill = NONE, expand ="false")
    ss = Label(root, text = "Settings", fg = "Orange", bg = "black", font = ("arial", 25))
    ss.pack()
    sd = Label(root, text = "Sound:", fg = "Orange", pady = 10, bg = "black", font = ("arial", 12))
    sd.pack()
    sds = Label(root, textvar = soundg, fg = "Orange", pady = 20, bg = "black", font = ("arial", 12))
    sds.pack()
    sdon = Button(root, text = "Turn Sound On", command = soundon, bg = "Orange", fg = "Black")
    sdon.pack()
    sdoff = Button(root, text = "Turn Sound Off", command = soundoff, fg = "Orange", bg = "Black")
    sdoff.pack()
    sback = Button(root, text = "Back", command = setback, fg = "Orange", bg = "Black")
    pl = Label(root, text = "Player Color:", fg = "Orange", pady = 10, bg = "black", font = ("arial", 12))
    pl.pack()
    plc = Label(root, text = plcol, fg = "Orange", bg = "black", font = ("arial", 12))
    plc.pack()
    plci = Label(root, text = "Insert New Color Here:", fg = "orange", bg = "black", font = ("arial", 12))
    plci.pack()
    plchange = Entry(root, exportselection=0, bd = 5, bg = "white")
    plchange.pack()
    setcolb = Button(root, text = "Submit", bg="black", fg = "orange", command = setcolsubmit)
    setcolb.pack()
    sback.pack()
    root.bind("<Return>", lambda e: soundon())
    root.bind("<KeyPress-Up>", lambda e: setarrowu())
    root.bind("<KeyPress-Down>", lambda e: setarrowd())

def setcolsubmit():
    global sound, plcol, pcolt
    if sound == 1:
        select.play()
    plcolt = plchange.get()
    try:
        color.config(bg = plcolt)
    except:
        messagebox.showwarning("Player Color Error", "Invalid Color in Player Color Settings, using default untill changed")
        plcolt = 'white'
    plcol = plcolt
    if plcol.lower() == 'orange' or plcol.lower() == 'red' or plcol.lower() == 'black' or plcol.lower() == 'light blue' or plcol.lower() == 'yellow' or plcol.lower() == 'gold':
        messagebox.showwarning("Bad Color Selection for player", "Your selected color for your player will make the player extremely hard to see, switching to default")
        plcol = 'white'
    r = open("./settings/color.txt","w")
    r.write(plcol)
    plchange.delete(first=0, last=100)
    r = open("./settings/color.txt","r")
    ct = r.read()
    plc.config(text=plcol)

def setback():
    global sbs
    sbs = 1
    if sound == 1:
        select.play()
    ss.pack_forget()
    sd.pack_forget()
    sds.pack_forget()
    sdon.pack_forget()
    sdoff.pack_forget()
    sback.pack_forget()
    pl.pack_forget()
    plc.pack_forget()
    plci.pack_forget()
    plchange.pack_forget()
    setcolb.pack_forget()
    root.bind("<Return>", lambda e: settingsf())
    bg.pack(side=TOP, expand=YES, fill=BOTH)
    play.place (x = 225,y = 310)
    more.place(x = 330, y = 315)
    settings.place(x = 120, y = 315)
    root.bind("<KeyPress-Right>", lambda e: menuarrowr())
    root.bind("<KeyPress-Left>", lambda e: menuarrowl())

def setarrowu():
    global sbs
    if sound == 1:
        select.play()
    sbs = sbs - 1
    if sbs == 0:
        sbs = sbs + 1
    if sbs == 5:
        sbs = sbs - 1
    if sbs == 1:
        sdon.config(bg = "Orange", fg = "Black")
        sdoff.config(fg = "Orange", bg = "Black")
        setcolb.config(fg = "Orange", bg = "Black")
        sback.config(fg = "Orange", bg = "Black")
        root.bind("<Return>", lambda e: soundon())
    if sbs == 2:
        sdoff.config(bg = "Orange", fg = "Black")
        sdon.config(fg = "Orange", bg = "Black")
        setcolb.config(fg = "Orange", bg = "Black")
        sback.config(fg = "Orange", bg = "Black")
        root.bind("<Return>", lambda e: soundoff())
    if sbs == 3:
        setcolb.config(bg = "Orange", fg = "Black")
        sdon.config(fg = "Orange", bg = "Black")
        sdoff.config(fg = "Orange", bg = "Black")
        sback.config(fg = "Orange", bg = "Black")
        root.bind("<Return>", lambda e: setcolsubmit())
    if sbs == 4:
        sback.config(bg = "Orange", fg = "Black")
        sdon.config(fg = "Orange", bg = "Black")
        sdoff.config(fg = "Orange", bg = "Black")
        setcolb.config(fg = "Orange", bg = "Black")
        root.bind("<Return>", lambda e: setback())

def setarrowd():
    global sbs
    if sound == 1:
        select.play()
    sbs = sbs + 1
    if sbs == 0:
        sbs = sbs + 1
    if sbs == 5:
        sbs = sbs - 1
    if sbs == 1:
        sdon.config(bg = "Orange", fg = "Black")
        sdoff.config(fg = "Orange", bg = "Black")
        setcolb.config(fg = "Orange", bg = "Black")
        sback.config(fg = "Orange", bg = "Black")
        root.bind("<Return>", lambda e: soundon())
    if sbs == 2:
        sdoff.config(bg = "Orange", fg = "Black")
        sdon.config(fg = "Orange", bg = "Black")
        setcolb.config(fg = "Orange", bg = "Black")
        sback.config(fg = "Orange", bg = "Black")
        root.bind("<Return>", lambda e: soundoff())
    if sbs == 3:
        setcolb.config(bg = "Orange", fg = "Black")
        sdon.config(fg = "Orange", bg = "Black")
        sdoff.config(fg = "Orange", bg = "Black")
        sback.config(fg = "Orange", bg = "Black")
        root.bind("<Return>", lambda e: setcolsubmit())
    if sbs == 4:
        sback.config(bg = "Orange", fg = "Black")
        sdon.config(fg = "Orange", bg = "Black")
        sdoff.config(fg = "Orange", bg = "Black")
        setcolb.config(fg = "Orange", bg = "Black")
        root.bind("<Return>", lambda e: setback())


#sound stuff

def sounderror():
    global sound
    messagebox.showwarning("Sound Error", "Error in sound settings, open the settings to change them, currently using default settings")
    sound = 1
    pygame.mixer.music.load('./Music/Overflow.ogg')
    pygame.mixer.music.play(-1)
        
global soundc
soundc = 1

if sound == 1:
    try:
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.init()
    except:
        s = open("settings/sound.txt","w")
        s.write("0")
        sound = 0


if soundc == 1:
    if sound == 1:
        pygame.mixer.music.load('./Music/Overflow.ogg')
        pygame.mixer.music.play(-1)
    if sound < 0:
        sounderror()
    if sound > 1:
        sounderror()
        
#sound effects
if sound == 1:
    move = pygame.mixer.Sound('./sounds/move.wav')
    select = pygame.mixer.Sound('./sounds/select.wav')

#sound settings:
def soundoff():
    global sound
    if sound == 1:
        pygame.mixer.music.stop()
    s = open("settings/sound.txt","w")
    s.write("0")
    soundg.set("Off")
    sound = 0

def soundon():
    global sound, select, move
    if sound == 0:
        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.init()
        pygame.mixer.music.load('./Music/Overflow.ogg')
        pygame.mixer.music.play(-1)
        move = pygame.mixer.Sound('./sounds/move.wav')
        select = pygame.mixer.Sound('./sounds/select.wav')
    select.play()
    s = open("settings/sound.txt","w")
    s.write("1")
    soundg.set("On")
    sound = 1

def menufour():
    global sound, music, record, how, subbackb, subl, mfs, discordb
    if sound == 1:
        select.play()
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Left>")
    root.bind("<Return>", lambda e: menuthree())
    bg.pack_forget()
    play.place_forget()
    more.place_forget()
    settings.place_forget()
    logo.pack_configure(fill = NONE, expand = "false")
    dev.pack_configure(fill = NONE, expand ="false")
    music = Button(root, image = musicpic2, bg = "orange", command = menuthree)
    music.place(x = 20, y = 200)
    record = Button(root, image = recordpic2, bg = "blue", command = menufive)
    record.place(x = 150, y = 200)
    how = Button(root, image = howpic2, bg = "blue", command = menusix)
    how.place(x = 220, y = 200)
    subbackb = Button(root, text = "Back", bg = "black", fg = "orange", font = ("arial", 15), command = subback)
    subbackb.place(x = 310, y = 200)
    subl = Label(root, text = "More Options:", font = ("arial", 20), bg = "black", fg = "orange")
    subl.pack()
    discordb = Button(root, text = "Discord Server here!", font = ("arial", 20), bg = "black", fg = "orange", command = discord)
    discordb.pack(side = BOTTOM)
    root.bind("<KeyPress-Left>", lambda e: subarrowl())
    root.bind("<KeyPress-Right>", lambda e: subarrowr())


def discord():
    webbrowser.open_new('https://discord.gg/qqkwzgF')


def subarrowl():
    global mfs, sound
    if sound == 1:
        select.play()
    mfs = mfs - 1
    if mfs == 5:
        mfs = mfs - 1
    if mfs == 0:
        mfs = mfs + 1
    if mfs == 1:
        music.config(bg = "orange", fg = "blue")
        record.config(fg = "orange", bg = "blue")
        how.config(fg = "orange", bg = "blue")
        subbackb.config(fg = "orange", bg = "black")
        root.bind("<Return>", lambda e: menuthree())
    if mfs == 2:
        record.config(bg = "orange", fg = "black")
        music.config(fg = "orange", bg = "blue")
        how.config(fg = "orange", bg = "blue")
        subbackb.config(fg = "orange", bg = "black")
        root.bind("<Return>", lambda e: menufive())
    if mfs == 3:
        how.config(bg = "orange", fg = "black")
        music.config(fg = "orange", bg = "blue")
        record.config(fg = "orange", bg = "blue")
        subbackb.config(fg = "orange", bg = "black")
        root.bind("<Return>", lambda e: menusix())
    if mfs == 4:
        subbackb.config(bg = "orange", fg = "black")
        music.config(fg = "orange", bg = "blue")
        record.config(fg = "orange", bg = "blue")
        how.config(fg = "orange", bg = "blue")
        root.bind("<Return>", lambda e: subback())

def subarrowr():
    global mfs, sound
    if sound == 1:
        select.play()
    mfs = mfs + 1
    if mfs == 5:
        mfs = mfs - 1
    if mfs == 0:
        mfs = mfs + 1
    if mfs == 1:
        music.config(bg = "orange", fg = "black")
        record.config(fg = "orange", bg = "blue")
        how.config(fg = "orange", bg = "blue")
        subbackb.config(fg = "orange", bg = "black")
        root.bind("<Return>", lambda e: menuthree())
    if mfs == 2:
        record.config(bg = "orange", fg = "black")
        music.config(fg = "orange", bg = "blue")
        how.config(fg = "orange", bg = "blue")
        subbackb.config(fg = "orange", bg = "black")
        root.bind("<Return>", lambda e: menufive())
    if mfs == 3:
        how.config(bg = "orange", fg = "black")
        music.config(fg = "orange", bg = "blue")
        record.config(fg = "orange", bg = "blue")
        subbackb.config(fg = "orange", bg = "black")
        root.bind("<Return>", lambda e: menusix())
    if mfs == 4:
        subbackb.config(bg = "orange", fg = "black")
        music.config(fg = "orange", bg = "blue")
        record.config(fg = "orange", bg = "blue")
        how.config(fg = "orange", bg = "blue")
        root.bind("<Return>", lambda e: subback())
    




def menufive():
    global sound, rl, br, cr, fr, backr
    if sound == 1:
        select.play()
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Left>")
    how.place_forget()
    record.place_forget()
    music.place_forget()
    subbackb.place_forget()
    subl.pack_forget()
    discordb.pack_forget()
    rl = Label(root, text = "Records", bg = "black", fg = "orange", font = ("arial", 25))
    rl.pack()
    try:
        s = open("settings/bloom.txt","r")
        a = s.read()
        sec = a + ' sec'
    except:
        sec = 'Not Yet Completed'
    br = Label(text = "Bloom: {}".format(sec), font = ("arial",15), bg = "black", fg = "orange", pady = 20)
    br.pack()
    try:
        s = open("settings/chaoz.txt","r")
        a = s.read()
        sec = a + ' sec'
    except:
        sec = 'Not Yet Completed'
    cr = Label(text = "Chaoz: {}".format(sec), font = ("arial",15), bg = "black", fg = "orange", pady = 20)
    cr.pack()
    try:
        s = open("settings/Funky.txt","r")
        a = s.read()
        sec = a + ' sec'
    except:
        sec = 'Not Yet Completed'
    fr = Label(text = "Funky: {}".format(sec), font = ("arial",15), bg = "black", fg = "orange", pady = 20)
    fr.pack()
    backr = Button(text = "Back", font = ("arial", 15), bg = "orange", fg = "black", command = recordback)
    backr.pack()
    root.bind("<Return>", lambda e: recordback())

def recordback():
    global sound
    if sound == 1:
        select.play()
    rl.pack_forget()
    br.pack_forget()
    cr.pack_forget()
    fr.pack_forget()
    backr.pack_forget()
    subbackb.place(x = 310, y = 200)
    how.place(x = 220, y = 200)
    record.place(x = 150, y = 200)
    music.place(x = 20, y = 200)
    discordb.pack(side = BOTTOM)
    subl.pack()
    root.bind("<KeyPress-Left>", lambda e: subarrowl())
    root.bind("<KeyPress-Right>", lambda e: subarrowr())
    root.bind("<Return>", lambda e: menufive())

def menusix():
    global sound, howm, howi, howl, howbackb
    if sound == 1:
        select.play()
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Left>")
    how.place_forget()
    record.place_forget()
    music.place_forget()
    subbackb.place_forget()
    subl.pack_forget()
    discordb.pack_forget()
    howl = Label(root, text = "How to Play", font = ("arial", 25), bg = "black", fg = "orange")
    howl.pack()
    howi = Label(root, image = howtopic2, pady = 30)
    howi.pack()
    howm = Message(root, anchor = CENTER, text = "Welcome to the Maze Game by Fire Dev! You can play the game by going to the level select, and then press a level and use the arrow keys or w,a,s,d to move.", bg = "black", fg = "orange", font = ("arial", 15))
    howm.pack()
    howbackb = Button(root, text = "Back", bg = "orange", fg = "black", font = ("arial", 15), command = howback)
    howbackb.place(y = 300, x = 450)
    root.bind("<Return>", lambda e: howback())

def howback():
    global sound, mfs
    if sound == 1:
        select.play()
    howl.pack_forget()
    howi.pack_forget()
    howm.pack_forget()
    howbackb.place_forget()
    subbackb.place(x = 310, y = 200)
    how.place(x = 220, y = 200)
    record.place(x = 150, y = 200)
    music.place(x = 20, y = 200)
    discordb.pack(side = BOTTOM)
    subl.pack()
    root.bind("<Return>", lambda e: menusix())
    root.bind("<KeyPress-Left>", lambda e: subarrowl())
    root.bind("<KeyPress-Right>", lambda e: subarrowr())

def subback():
    global sound, mfs
    mfs = 1
    if sound == 1:
        select.play()
    root.unbind("<KeyPress-Right>")
    root.unbind("<KeyPress-Left>")
    how.place_forget()
    record.place_forget()
    music.place_forget()
    subbackb.place_forget()
    discordb.pack_forget()
    subl.pack_forget()
    root.bind("<Return>", lambda e: menufour())
    bg.pack(side=TOP, expand=YES, fill=BOTH)
    play.place (x = 225,y = 310)
    more.place(x = 330, y = 315)
    settings.place(x = 120, y = 315)
    root.bind("<KeyPress-Right>", lambda e: menuarrowr())
    root.bind("<KeyPress-Left>", lambda e: menuarrowl())

#starting screen:
if menu == 1:
    bgpic = PhotoImage(file =r"./Images/MAIN.gif")
    logopic = PhotoImage(file =r"./Images/Icon.gif")
    devpic = PhotoImage(file =r"./Images/FIREDEV.gif")
    playpic = PhotoImage(file =r"./Images/Play.gif")
    playpic2 = playpic.subsample(3,3)
    morepic = PhotoImage(file =r"./Images/More.gif")
    morepic2 = morepic.subsample(5,5)
    recordpic = PhotoImage(file =r"./Images/trophy.gif")
    recordpic2 = recordpic.subsample(4,4)
    howpic = PhotoImage(file = r"./Images/How.gif")
    howpic2 = howpic.subsample(5,5)
    howtopic = PhotoImage(file = r"./Images/HowPic.gif")
    howtopic2 = howtopic.subsample(3,3)
    logo = Label(root, image = logopic)
    logo.pack(side=TOP, expand=YES, fill=X)
    bg = Label(root, image = bgpic)
    bg.pack(side=TOP, expand=YES, fill=BOTH)
    dev = Label(root, image = devpic)
    dev.pack(side=BOTTOM, expand=YES, fill=BOTH)
    play = Button(root, image = playpic2, bg = "orange", command = menutwo)
    play.place (x = 225,y = 310)
    root.bind("<Return>", lambda e: menutwo())
    musicpic = PhotoImage(file =r"./Images/Music.gif")
    musicpic2 = musicpic.subsample(6,6)
    more = Button(root, image = morepic2, bg = "blue", command = menufour)
    more.place(x = 330, y = 315)
    settingspic = PhotoImage(file =r"./Images/Settings.gif")
    settingspic2 = settingspic.subsample(6,6)
    settings = Button(root, image = settingspic2, bg = "blue", command = settingsf)
    settings.place(x = 120, y = 315)
    root.bind("<KeyPress-Right>", lambda e: menuarrowr())
    root.bind("<KeyPress-Left>", lambda e: menuarrowl())

def menuarrowr():
    global mmbs, sound
    if sound == 1:
        select.play()
    mmbs = mmbs + 1
    if mmbs == 0:
        mmbs = mmbs + 1
    if mmbs == 4:
        mmbs = mmbs - 1
    if mmbs == 2:
        play.config(bg = "orange")
        more.config(bg = "blue")
        settings.config(bg = "blue")
        root.bind("<Return>", lambda e: menutwo())
    if mmbs == 3:
        more.config(bg = "orange")
        play.config(bg = "blue")
        settings.config(bg = "blue")
        root.bind("<Return>", lambda e: menufour())
    if mmbs == 1:
        settings.config(bg = "orange")
        play.config(bg = "blue")
        more.config(bg = "blue")
        root.bind("<Return>", lambda e: settings())

def menuarrowl():
    global mmbs, sound
    if sound == 1:
        select.play()
    mmbs = mmbs - 1
    if mmbs == 0:
        mmbs = mmbs + 1
    if mmbs == 4:
        mmbs = mmbs - 1
    if mmbs == 2:
        play.config(bg = "orange")
        more.config(bg = "blue")
        settings.config(bg = "blue")
        root.bind("<Return>", lambda e: menutwo())
    if mmbs == 3:
        more.config(bg = "orange")
        play.config(bg = "blue")
        settings.config(bg = "blue")
        root.bind("<Return>", lambda e: menufour())
    if mmbs == 1:
        settings.config(bg = "orange")
        play.config(bg = "blue")
        more.config(bg = "blue")
        root.bind("<Return>", lambda e: settingsf())


root.resizable(False, False)
root.iconbitmap('./Images/logo.ico')
root.wm_title("Maze Game!")
root.config(bg = "black")
root.geometry("520x600")
root.mainloop()
