import tkinter as tk
from tkinter import ttk
from matplotlib import cm,colors
import time
from random import shuffle as sf

"""Creating the screen where the app is going to run"""
screen_width=600
screen_height=800
screen=tk.Tk()
screen.geometry("{}x{}".format(screen_width,screen_height))
#screen.configure(background='green')


"""Creating the frame that will select the options"""
frame = tk.Frame(screen, bg="#aeb7f2",width=screen_width, height=50)
generte_button= ttk.Button(frame,text="Generate Random",command=lambda:generate())
frame.grid_propagate(False)
frame.rowconfigure(0,weight=2)
frame.grid(row=0, column=0)
generte_button.grid(sticky="ens")




width=3
number =int((screen_width-2)/width)
rect_list=[]
height_list=[]

#number =5

"""Creating the pane that will contain all the rectangles with different heights"""
rectangle_pane=tk.Canvas(screen,width=screen_width,height=screen_width)
rectangle_pane.grid(row=1,column=0)
rectangle_pane.config(background='#b5e1f5')

"""creating the button that will bubble sort the list"""
sort_frame = tk.Frame(screen,width=screen_width, height=50)
sort_button= ttk.Button(sort_frame,text="Bubble sort",command=lambda:sort())
sort_frame.grid_propagate(False)
sort_frame.rowconfigure(0,weight=2)
sort_frame.grid(row=2, column=0)
sort_button.pack(side="left")

""""Creating the button that will use selection sort"""
sort_frame = tk.Frame(screen,width=screen_width, height=50)
sort_button= ttk.Button(sort_frame,text="Selection sort",command=lambda:sort())
sort_frame.grid_propagate(False)
sort_frame.rowconfigure(0,weight=2)
sort_frame.grid(row=2, column=0)
sort_button.pack(side="left")

def generate():
    """Generates a simple list with lineraly number representing the heights of rectangles"""
    global height_list,rect_list
    height_list.clear()
    rect_list.clear()
    rectangle_pane.delete("all")
    max_height=screen_width-4
    height_list=[int(max_height-(max_height-1)*(number-i)/number) for i in range(number)]
    sf(height_list)
    draw(height_list)

def draw(height_list):
    """Draws rectangles along the width of the rectangle pane with heights corresponding to the values in height list"""
    global rect_list,width
    for i in range(number):
        color=cm.YlOrBr((2*height_list[i]+300)/1200)
        rect_list.append(rectangle_pane.create_rectangle(width*i+2,screen_width-height_list[i],width*i+5,screen_width,fill=colors.to_hex(color),width=0))

def swap(i,f):
    """swaps two rectangles in the rect_list with the position in the rect list given as i and f"""
    global rect_list,height_list
    cords1=rectangle_pane.coords(rect_list[i])
    cords2=rectangle_pane.coords(rect_list[f])
    dist=cords2[0]-cords1[0]
    dist=dist/3
    k=0
    while k<dist:
        rectangle_pane.move(rect_list[i],3,0)
        rectangle_pane.move(rect_list[f],-3,0)
        k=k+1
        screen.update()
    temp=height_list[i]
    height_list[i]=height_list[f]
    height_list[f]=temp
    temp2=rect_list[i]
    rect_list[i]=rect_list[f]
    rect_list[f]=temp2

def sort():
    global height_list
    bubbleSort(height_list)

def bubbleSort(arr):
    global rect_list
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                swap(j,j+1)

def main():
    tk.mainloop()



if __name__=='__main__':
    main()
