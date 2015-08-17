
from Tkinter import *

def doNothing ():

	print ( "ok, I comply..." )


root = Tk ()


menu = Menu ( root )

root.config ( menu = menu )  


# ****** FILE Menu ****** #

fileMenu = Menu ( menu )  #Creates a menu item within the Main menu ( root ).


menu.add_cascade ( label = "File" , menu = fileMenu )  #Adds a dropdown menu and creates a File button.


# ****** New SubM ****** #

fileMenu.add_command ( label = "New" , command = doNothing )


# ****** Open SubM ****** #

fileMenu.add_command ( label = "Open..." , command = doNothing )


# ****** Save SubM ****** #

fileMenu.add_command ( label = "Save" , command = doNothing )


# ****** Save As SubM ****** #

fileMenu.add_command ( label = "Save As..." , command = doNothing )

fileMenu.add_separator ()


# ****** Page Setup SubM ****** #

fileMenu.add_command ( label = "Page Setup..." , command = doNothing )


# ****** Print SubM ****** #

fileMenu.add_command ( label = "Print..." , command = doNothing )

fileMenu.add_separator ()


# ****** Exit SubM ****** #

fileMenu.add_command ( label = "Exit" , command = doNothing )




# ****** EDIT Menu ****** #

editMenu = Menu ( menu )

menu.add_cascade ( label = "Edit" , menu = editMenu )


# ****** Undo SubM ****** #

editMenu.add_command ( label = "Undo" , command = doNothing )

editMenu.add_separator ()


# ****** Cut SubM ****** #

editMenu.add_command ( label = "Cut" , command = doNothing )


# ****** Copy SubM ****** #

editMenu.add_command ( label = "Copy" , command = doNothing )


# ****** Paste SubM ****** #

editMenu.add_command ( label = "Paste" , command = doNothing )


# ****** Delete SubM ****** #

editMenu.add_command ( label = "Delete" , command = doNothing )

editMenu.add_separator ()


# ****** Find SubM ****** #

editMenu.add_command ( label = "Find..." , command = doNothing )


# ****** Find Next SubM ****** #

editMenu.add_command ( label = "Find Next" , command = doNothing )


# ****** Replace SubM ****** #

editMenu.add_command ( label = "Replace..." , command = doNothing )


# ****** Go To ****** #

editMenu.add_command ( label = "Go To..." , command = doNothing )

editMenu.add_separator ()


# ****** Select All ****** #


editMenu.add_command ( label = "Select All" , command = doNothing )


# ****** Time/Date ****** #


editMenu.add_command ( label = "Time/Date" , command = doNothing )



# ****** FORMAT Menu ****** #


formatMenu = Menu ( menu )

menu.add_cascade ( label = "Format" , menu =formatMenu )


# ****** Word Wrap SubM ****** #

formatMenu.add_command ( label = "Word Wrap" , command = doNothing )


# ****** Font SubM ****** #

formatMenu.add_cascade ( label = "Font..." , command = doNothing )


# ****** View Menu ****** #

viewMenu = Menu ( menu )

menu.add_cascade( label = "View" , menu = viewMenu )


# ****** Status Bar SubM ****** #

viewMenu.add_command ( label = "Status Bar" , command = doNothing )



# ****** HELP Menu ****** #

helpMenu = Menu ( menu )

menu.add_cascade ( label = "Help" , menu = helpMenu )


# ****** View Help ****** #

helpMenu.add_command ( label = "View Help" , command = doNothing )

helpMenu.add_separator ()


# ****** About Notepad ****** #

helpMenu.add_command ( label = "About Notepad" , command = doNothing )


# ****** Notepad Title ****** #

root.title ( "Text Pad" )


# ****** Width and Length of my Notepad ****** #

root.geometry ( "350x400" )


root.mainloop ()


