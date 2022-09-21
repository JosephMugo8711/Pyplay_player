# Importing important libraries
# Imports the mixer module from pygame
# Helps control the music used in pygame programs
#from multiprocessing.  resource_share import stop

from pygame import mixer

# Import the font module from the tkinter library
# Import filedialog which has many application like opening a file or a directory
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

from pygame.mixer_music import pause, stop

from music import pause_button

# Create the project Layout

# Creating a root window
# Tk() is a top level widget that is used to create the main application window in which we will be building our python project.
root = Tk()

# title() method is used to give a name to python mp3 player application which is displayed at the top.
root.title('Pyplay Python MP3 Player App ')

# mixer.init() is used to initialize the mixer module so that we can use it’s various functions in our application.
#Initialize mixer
mixer.init()

#create the listbox to contain songs
# Listbox() widget is used to create a listbox in which we will store our songs
# I have passed various parameters, first is the root specifying that the widget should be placed in the python
# mp3 player window.
#Then, bg is for background color, fg is for foreground color.
# select background change the background and
# select foreground basically change foreground color of a particular item upon selecting it.
songs_list = Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial', 15),height=12,width=47,
                     selectbackground="gray",selectforeground='black')

# grid() widget is a geometry manager which organizes the widgets properly in a grid-based fashion
# before placing it in the root window.
# column span = 9 gives a space of 9 columns to our listbox widget.
songs_list.grid(columnspan=9)

#font is defined which is to be used for the button font
defined_font = font.Font(family='Helvetica')

# button() widget is used to create a button. We want the buttons in our main window so the input root is given.
# Then the text which will be displayed on the button is specified and at
# last in the command input a function is given which will be called when the button is clicked.
play_button = Button(root,text="Play",width=7, command=pause)
play_button['font'] = defined_font
pause_button.grid(row=1,column=1)


#stop button
class Stop:
    pass


stop_button = Button(root,text="stop",width=7,command=Stop)
stop_button['font'] = defined_font
stop.grip(row=1,column=3)

#resume_button
class Resume:
    pass


Resume_button = Button(root,text="Resume",width=7, command=Resume)
Resume_button['font']
Resume_button.grip(row=1,column=4)

#previous button
class Previous:
    pass


previous_button = Button(root,text="Stop",width=7,command=Previous)
previous_button['font'] = defined_font

#class Previous_button:
#pass

class Previous_Button:
    pass


Previous_button.grid(row=1,column=4)

#nextbutton
class Next:
    pass


next_button = Button(root,text="Next",width=7,command=Next)
next_button['font'] = defined_font
next_button.grid(row=1,column=5)

# Menu() widget is displayed just under the title bar, it is used to conveniently access various operations.
# I am going to access Add songs and Delete songs for our playlist, upon clicking add songs and delete song
# functions are called respectively

my_menu = Menu(root)
root.config(menu=my_menu)
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)

mainloop()
# Define play, pause and other music player functions
# add many songs to the playlist of python mp3 player
# add songs() is used to add songs in our listbox,
# filedialog.askopenfilenames() opens a dialog box corresponding to the folder whose path is provided.
# Then, we can select songs and store them in temp_song variable, after this we loop through the list to
# insert every item in the listbox.
def add_songs():
    # to open a file
    temp_song = filedialog.askopenfilenames(initialdir="Music/", title="Choose a song",
                                            filetypes=(("mp3 Files", "*.mp3"),))
    ##loop through every item in the list to insert in the listbox


for s in temp_song:
    s = s.replace("C:/Users/josep/Desktop/projects","")
songs_list.insert(END, s)


# delete song() is used to delete a selected song, songs_list.curselection() function returns a tuple in which the
# first element is the index of the selected song. Then, .delete() function is used to delete the song corresponding
# to the index which is passed.
def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])


def play():
    song = songs_list.get(ACTIVE)
    song = f'C:/Users/lenovo/Desktop/DataFlair/Notepad/Music/{song}'
    mixer.music.load(song)
    mixer.music.play()


# to pause the song
def pause():
    mixer.music.pause()


# to stop the  song
def stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)


# to resume the song
def resume():
    mixer.music.unpause()

