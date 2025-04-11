#import the required libraries
#tkinter library to create GUI
#random library because we're randomly selecting numbers
#MADE BY PIYUSH GHOSHI 

from tkinter import *
import random
import turtle
s=turtle.Turtle()
s.shape("turtle")
s.color("red")
s.speed(30)
wn= turtle.Screen()
wn.bgcolor("black")
s.color("black")
s.width(6)
#W
s.goto(-225,225)
s.color("red")
s.right(90)
s.forward(90)
s.left(135)
s.forward(45)
s.right(90)
s.forward(45)
s.left(135)
s.forward(90)


s.left(180)
s.forward(90)
s.left(90)
s.color("black")
#E
s.forward(20)
s.color("red")
s.left(90)
s.forward(90)
s.right(90)
s.forward(45)
s.left(180)
s.forward(45)
s.left(90)
s.forward(45)
s.left(90)
s.forward(40)
s.left(180)
s.forward(40)
s.left(90)
s.forward(45)
s.left(90)
s.forward(45)
s.color("black")


#L
s.forward(20)
s.color("red")
s.left(90)
s.forward(90)
s.left(180)
s.forward(90)
s.left(90)
s.forward(45)
s.color("black")

#C
s.forward(20)
s.color("red")
s.left(90)
s.forward(90)
s.right(90)
s.forward(45)
s.left(180)
s.forward(45)
s.left(90)
s.forward(90)
s.left(90)
s.forward(45)
s.color("black")

#O
s.forward(20)
s.color("red")
s.left(90)
s.forward(90)
s.right(90)
s.forward(45)
s.right(90)
s.forward(90)
s.right(90)
s.forward(45)
s.left(180)
s.forward(45)
s.color("black")


#M
s.forward(20)
s.color("red")
s.left(90)
s.forward(90)
s.right(135)
s.forward(45)
s.left(90)
s.forward(45)
s.right(135)
s.forward(90)
s.left(90)
s.color("black")


#E
s.forward(20)
s.color("red")
s.left(90)
s.forward(90)
s.right(90)
s.forward(45)
s.left(180)
s.forward(45)
s.left(90)
s.forward(45)
s.left(90)
s.forward(40)
s.left(180)
s.forward(40)
s.left(90)
s.forward(45)
s.left(90)
s.forward(50)
s.color("black")


s.right(90)
s.forward(30)
s.right(90)
s.forward(300)
s.color("red")
s.right(180)
#create tkinter instance
root=Tk()
#define geometry
root.geometry("1080x1920")
root.configure(bg="grey")


#GUI will have two basic components
#1.Button which will trigger the rolling of dice
#2.Dice label
l1=Label(root,font=("Helvetica",260))
 
def roll():
    #create a number variable in which the list of all the ASCII characters of the string will be stored
    #Use backslash because unicode must have a backslash 
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    #configure the label
    l1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    l1.pack()
     
b1=Button(root,text="Roll the Dice!",foreground='red',command=roll)
b1.configure(bg="black")
b1.place(x=300,y=200)
b1.pack()
 
root.mainloop()
