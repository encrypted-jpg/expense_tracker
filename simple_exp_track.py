print("Importing Modules")
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.font as tkFont  # Importing the Modules
import datetime
import pickle
import os
print("Imported")
print("Starting")
storage = []
start_frame = Tk()
start_frame.geometry("300x170")
start_frame.title("Expense_Tracker")   # Layout of Starting Frame
user = Entry(start_frame)
user.grid(row = 2, column = 2)
passwd = Entry(start_frame, textvariable=StringVar(), show = "*")
passwd.grid(row = 3, column = 2)
n = 1

def check():   # Check if the username and password are matched
	x1 = user.get()
	x2 = passwd.get()
	if x1 == "test" and x2 == "1234":  # Change the username and password with your choice
		Label(start_frame, text = "Logging in..").grid(row = 6, column = 1)
		start_frame.destroy()  
		list_frame()
	else:
		Label(start_frame, text = "Invalid Credentials").grid(row = 6, column = 1,columnspan = 2)

def enter():
	global start_frame
	# Layout of start frame
	Label(start_frame, text = "       ").grid(row = 0, column = 0)
	Label(start_frame, text = "Enter your credentials").grid(row = 0, column = 1)
	Label(start_frame, text = "       ").grid(row = 1, column = 1)
	Label(start_frame, text = "       ").grid(row = 2, column = 0) 
	Label(start_frame, text = "       ").grid(row = 3, column = 0)
	Label(start_frame, text = "Enter Username: ").grid(row = 2, column = 1)
	Label(start_frame, text = "Enter Password: ").grid(row = 3, column = 1)
	Label(start_frame, text = "       ").grid(row = 4, column = 1)
	login = Button(start_frame,text = "Login",command = check,font=tkFont.Font(size=12))
	login.grid(column=1,row=5,columnspan=2)
	start_frame.mainloop()

def list_frame():
	# Layout of Options Frame
	flist = Tk()
	flist.title("Select a Command")
	flist.geometry("310x110")
	exp_add = Button(flist, text="Add an Expense", command = lambda : add_exp(flist))
	exp_add.grid(row = 0, column = 0)
	exp_list = Button(flist, text="List All the Expenses", command=lambda: list_exp(flist))
	exp_list.grid(row = 1, column = 1)
	exp_graph = Button(flist, text = "Show the Graph", command = show_graph)
	exp_graph.grid(row = 2,column = 2)
	back = Button(flist, text = "       Quit       ",command=lambda: go_back_save(flist))
	back.grid(row = 4, column = 1)
	flist.mainloop()

def save_exp(add_e,exp,exp1):
	global storage
	# This saves the added expense to the list
	load()
	name = exp.get()
	amount = exp1.get()
	exp.delete(0, END)
	exp1.delete(0, END)
	try:
		amt = float(amount)
	except:
		Label(add_e, text = "Invalid Input..").grid(row = 4, column = 1)
	else:
		x1 = datetime.datetime.now()
		x = str(x1.strftime("%x")) + " " + str(x1.strftime("%X"))
		element = {"Time": x,"Name": name, "Amount": amt}
		x = None
		x1 = None
		storage.append(element)
		add_e.destroy()
		save()
		list_frame()

def save():
	global storage	
	# This saves all the expenses to a file
	pickle_out = open("expenses.txt","wb")
	pickle.dump(storage,pickle_out)
		
def load():
	# This loads the file which stores the data of the expenses
	global storage
	global n
	if n == 1:
		if os.path.isfile('expenses.txt'):
			pickle_in = open("expenses.txt","rb")
			storage = pickle.load(pickle_in)
	else:
		storage = []
	return storage

storage = load()

def add_exp(flist):
	# Layout of Add an Expense Window
	flist.destroy()
	add_e = Tk()
	add_e.title("Add an Expense")
	add_e.geometry("400x100")
	Label(add_e, text = "Enter the Name of the Expense: ").grid(row = 0, column = 0)
	exp = Entry(add_e)
	exp.grid(row = 0, column = 1)
	Label(add_e, text = "Enter the Amount: ").grid(row = 1,column = 0)
	exp1 = Entry(add_e)
	exp1.grid(row = 1,column = 1)
	exp_a = Button(add_e, text="Add", command = lambda: save_exp(add_e,exp,exp1))
	exp_a.grid(row = 3, column = 2, columnspan = 2)
	back = Button(add_e, text = "Back", command = lambda : go_back(add_e))
	back.grid(row = 3, column=0, columnspan = 2)
	add_e.mainloop()


def list_exp(flist):
	# Layout of List all Expense Window
	global n
	global storage
	flist.destroy()
	list_e =Tk()
	list_e.title("All your Expenses")
	Label(list_e, text = "Time").grid(row = 0, column = 0)
	Label(list_e, text = "	").grid(row = 0, column = 1)
	Label(list_e, text = "Name").grid(row = 0, column = 2)
	Label(list_e, text = "	").grid(row = 0, column = 3)
	Label(list_e, text = "Amount").grid(row = 0,column = 4)
	y = 1
	total = 0
	for ele in storage:
		Label(list_e, text = ele["Time"]).grid(row = y, column = 0)
		Label(list_e, text = "	").grid(row = y, column = 1)
		Label(list_e, text = ele["Name"]).grid(row = y, column = 2)
		Label(list_e, text = "	").grid(row = y, column = 3)
		Label(list_e, text = ele["Amount"]).grid(row = y,column = 4)
		y += 1
		total += ele["Amount"]
	Label(list_e,text="Total").grid(row=y, column = 2)
	Label(list_e, text = total).grid(row=y, column = 4)
	back = Button(list_e, text = "Back", command = lambda : go_back(list_e))
	back.grid(row = (y+1), column= 1, columnspan = 2)
	list_e.geometry(f"350x{20*(y+3)}")
	list_e.mainloop()
	n +=1

def go_back(list_e):
	# to go back
	list_e.destroy()
	list_frame()

def go_back_save(flist):
	# to exit
	flist.destroy()
	save()
	print("Quiting..")

def show_graph():
	# To show the graph
	global storage
	dates = []
	for ele in storage:
		dt = ele["Time"][:8]
		if dt not in dates:
			dates.append(dt)
	totals = []
	for dts in dates:
		tot = 0
		for ele in storage:
			dt = ele["Time"][:8]
			if dt == dts:
				tot += ele["Amount"]
		totals.append(tot)
	plt.bar(dates,totals,label='Expenses',color='r')
	plt.xlabel('Dates')
	plt.ylabel('Amount')
	plt.title('Expenses By Date')
	plt.legend()
	plt.show()


enter()




