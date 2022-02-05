import tkinter as tk

frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x280')
lb = tk.Label(frame,text="Put comma (',') between numbers", font=("Times New Roman", 11, "bold"),fg="black")
lb.place(x=100,y=20)


def printInput():
	inp = inputtxt.get(1.0, "end-1c")
	odd = [x for x in inp.split(",") if int(x)%2 != 0]
	odd_str = ", ".join(odd)
	even = [x for x in inp.split(",") if int(x)%2 == 0]
	even_str = ", ".join(even)
	if even_str == "":
		even_str = "None"
	if odd_str == "":
		odd_str = "None"
	
	lbl.config(text = f"Output: \nOdd numbers: {odd_str} \nEven numbers: {even_str}")
	lbl.place(x=130,y=220)


inputtxt = tk.Text(frame,height = 7, width = 40)

inputtxt.place(x=50,y=50)


printButton = tk.Button(frame, text = "Print",command = printInput)
printButton.place(x=170,y=190)


lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()
