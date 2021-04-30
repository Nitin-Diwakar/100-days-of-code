# Write a Python GUI program
# using tkinter module
# to input Miles in Entry widget
# that is in text box and convert
# to Kilometers Km on button click. 

import tkinter as tk


def main():
    window= tk.Tk()
    window.title("Miles to Kilometers Converter")
    window.geometry("375x200")
    
    # create a label with text Enter Miles
    label1 = tk.Label(window, text="Enter Miles:")
    
    # create a label with text Kilometers:
    label2 = tk.Label(window, text="Kilometers:")

    # place label1 in window at position x,y 
    label1.place(x=50,y=30)

    # create an Entry widget (text box) 
    
    textbox1 = tk.Entry(window, width=12)

    # place textbox1 in window at position x,y 
    textbox1.place(x=200,y=35)
    

    # place label2 in window at position x,y 
    label2.place(x=50,y=100)
    
    # create a label3 with empty text:
    label3 = tk.Label(window, text=" ")

    # place label3 in window at position x,y 
    label3.place(x=180,y=100)

         
    def btn1_click():
        kilometers = round(float(textbox1.get()) * 1.60934,5)
        label3.configure(text = str(kilometers)+ '  Kilometers')
        

    # create a button with text Button 1
    btn1 = tk.Button(window, text="Click Me To Convert", command=btn1_click)
    # place this button in window at position x,y 
    btn1.place(x=90,y=150)
    window.mainloop()
    

main()
