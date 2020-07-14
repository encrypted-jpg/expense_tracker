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
users_list = []
file_name = ""
n = 1

def check(start_frame,user,passwd):
	# Check if the username and password are matched from the list of usernames and passwords stored
	global storage
	global users_list
	global file_name
	x1 = str(user.get())
	x2 = str(passwd.get())
	k = 0
	for users in users_list:
		if x1 == str(users["username"]) and x2 == str(users["password"]):
			Label(start_frame, text = "Logging in..").grid(row = 6, column = 1)
			try:
				start_frame.destroy()
			except :
				pass
			file_name = str(users["username"]) + ".txt"
			storage = load()
			list_frame()
			k +=1
	user = None
	passwd = None
	if k == 0:
		Label(start_frame, text = "Invalid Credentials").grid(row = 6, column = 1,columnspan = 2)

def enter():
	# Layout of Starting Frame
	start_frame = Tk()
	start_frame.geometry("300x200")
	start_frame.title("Expense_Tracker")
	user = Entry(start_frame)
	user.grid(row = 2, column = 2)
	passwd = Entry(start_frame, textvariable=StringVar(), show = "*")
	passwd.grid(row = 3, column = 2)
	Label(start_frame, text = "       ").grid(row = 0, column = 0)
	Label(start_frame, text = "Enter your credentials").grid(row = 0, column = 1)
	Label(start_frame, text = "       ").grid(row = 1, column = 1)
	Label(start_frame, text = "       ").grid(row = 2, column = 0)
	Label(start_frame, text = "       ").grid(row = 3, column = 0)
	Label(start_frame, text = "Enter Username: ").grid(row = 2, column = 1)
	Label(start_frame, text = "Enter Password: ").grid(row = 3, column = 1)
	Label(start_frame, text = "       ").grid(row = 4, column = 1)
	login = Button(start_frame,text = "Login",command = lambda : check(start_frame,user,passwd),font=tkFont.Font(size=12))
	login.grid(column=1,row=5)
	create = Button(start_frame,text = "Create Account",command = lambda :create_acc(start_frame),font=tkFont.Font(size=12))
	create.grid(row = 5, column=2)
	Label(start_frame, text = "           ").grid(row=6, column = 1)
	Exit = Button(start_frame, text = "Exit", command = lambda : go_back_save(start_frame),font=tkFont.Font(size=12))
	Exit.grid(row = 7, column = 1,columnspan = 2)
	try:
		start_frame.mainloop()
	except:
		pass

def list_frame():
	# Layout of Options Frame
	flist = Tk()
	flist.title("Select a Command")
	flist.geometry("310x110")
	exp_add = Button(flist, text="Add an Expense", command = lambda : add_exp(flist))
	exp_add.grid(row = 0, column = 0)
	logout = Button(flist, text= "Logout", command = lambda: log_out(flist))
	logout.grid(row = 0, column = 2)
	exp_list = Button(flist, text="List All the Expenses", command=lambda: list_exp(flist))
	exp_list.grid(row = 1, column = 1)
	exp_graph = Button(flist, text = "Show the Graph", command = show_graph)
	exp_graph.grid(row = 2,column = 2)
	back = Button(flist, text = "       Quit       ",command=lambda: go_back_save(flist))
	back.grid(row = 4, column = 1)
	flist.mainloop()

def log_out(flist):
	# Logging out is like starting the program entirely again by saving the data given
	global storage
	global file_name
	global users_list
	global n
	go_back_save(flist)
	storage = []
	users_list = load_users()
	file_name = ""
	n = 1
	enter()

def save_exp(add_e,exp,exp1):
	# This saves the added expense to the list
	global storage
	global file_name
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
		try:
			add_e.destroy()
		except:
			pass
		save(file_name)
		list_frame()

def save(file_name):
	# This saves all the expenses to a file
	global storage	
	if file_name != "":
		pickle_out = open(file_name,"wb")
		pickle.dump(storage,pickle_out)
	else:
		pass
		
def load():
	# This loads the file which stores the data of the expenses
	global storage
	global file_name
	global n
	if n == 1:
		if os.path.isfile(file_name):
			pickle_in = open(file_name,"rb")
			storage = pickle.load(pickle_in)
	else:
		storage = []
	return storage


def add_exp(flist):
	# Layout of Add an Expense Window
	try:
		flist.destroy()
	except:
		pass
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
	try:
		flist.destroy()
	except:
		pass
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
	try:
		list_e.destroy()
	except:
		pass
	list_frame()

def go_back_login(list_e):
	# to go back when not interested in creating an account
	try:
		list_e.destroy()
	except:
		pass
	enter()

def go_back_save(flist):
	# to exit
	global file_name
	try:
		flist.destroy()
	except:
		pass
	save(file_name)
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


def create_acc(start_frame):
	# Layout of Create an Account window
	global storage
	try:
		start_frame.destroy()
	except:
		pass
	create = Tk()
	create.geometry("320x120")
	create.title("Create a New Account")
	Label(create, text = "Enter your details below ").grid(row = 0,column = 1)
	Label(create, text = "       ").grid(row = 1, column =0)
	Label(create, text = "Enter Username: ").grid(row = 1, column = 1)
	ent = Entry(create)
	ent.grid(row = 1, column = 2)
	Label(create, text = "       ").grid(row = 2, column =0)
	Label(create, text = "Enter Password: ").grid(row=2, column = 1)
	ent1 = Entry(create, textvariable=StringVar(), show = "*")
	ent1.grid(row = 2, column = 2)
	crea = Button(create, text = "Sign Up",command = lambda : add_user(create,ent,ent1),font=tkFont.Font(size=12))
	crea.grid(row=4, column = 2,columnspan = 2)
	back = Button(create, text = "Back", command = lambda : go_back_login(create),font=tkFont.Font(size=12))
	back.grid(row = 4, column=0, columnspan = 2)
	create.mainloop()

def load_users():
	# Load the users list from the users.txt file
	if os.path.isfile('users.txt'):
			pickle_in = open("users.txt","rb")
			users_list = pickle.load(pickle_in)
	else:
		users_list = []
	return users_list

users_list = load_users()

def add_user(create,ent,ent1):
	# Function to create an account it's own expenses file and add to the users list
	global users_list
	global file_name
	global storage
	user1 = str(ent.get())
	pass1 = str(ent1.get())
	users_list.append({"username": user1,"password":pass1})
	pickle_out = open("users.txt","wb")
	pickle.dump(users_list,pickle_out)
	pickle_out.close()
	name = user1 +".txt"
	f = open(name,"wb")
	pickle.dump(storage,f)
	f.close()
	file_name = name
	storage = load()
	try:
		create.destroy()
	except:
		pass
	list_frame()


enter()




