#!/usr/bin/python

# Program to convert Celsius to Fahrenheit using a simple
# graphical interface.

from graphics import *

def main() :
    win = GraphWin( "Celsius Converter" , 400 , 300)
    win.setCoords (0.0, 0.0 , 3.0, 4.0)
    win.setBackground("white")
    
    # Draw the interface
    label1 = Text(Point(1,3), " Celsius Temperature : "). draw(win)
    label2 = Text(Point(1,1), "Fahrenheit Temperature : "). draw(win)
    label1.setTextColor("purple")
    label2.setTextColor("purple")

    inputText = Entry(Point(2.25,3),6)
    inputText.setText("0.0")
    inputText.setFill("azure")
    inputText.draw(win)

    outputText = Text(Point(2.25,1)," ")
    outputText.draw(win)

    button = Text(Point(1.5,2.0),"Convert It ")
    button.draw(win)
    
    box = Rectangle(Point(1,1.5),Point(2,2.5)).draw(win)
    
    # wait for a mouse click
    win.getMouse ()
    # convert input
    celsius = float(inputText.getText())
    fahrenheit = 9.0/5.0 * celsius + 32
    # display output and change button
    outputText.setText(round(fahrenheit,2))
    outputText.setText(round(fahrenheit,2))
    button.setText("Quit ")
    # wait for click and then quit
    win.getMouse ()
    win.close()

main()

if __main__==__name__:
    main()