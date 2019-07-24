'''Login class'''
import tkinter as tk 
from tkinter.ttk import *
from tkinter import messagebox
from decimal import *
#from pricing_tool import PricingTool 
from paper import *
from admin import Admin
class Login(tk.Toplevel):
	'''This class creates the login window'''

	def __init__(self, new, *args, **kwargs):
		self.new = new
		self.messagebox = messagebox
		#new.geometry('1440x768')
		new.geometry('300x200')
		new.title("Administrative Login")

		#Created necessary labels, buttons, and entry fields
		Label(new, text="").pack()

		self.username_label = Label(new, text="Username", font=("Arial", 14))
		self.username_label.pack()
		self.username_entry = tk.Entry(new, font=("Arial", 12))
		self.username_entry.pack()

		self.password_label = Label(new, text="Password", font=("Arial", 14))
		self.password_label.pack()
		self.password_entry = tk.Entry(new, show='*', font=("Arial", 12))
		self.password_entry.pack()

		Label(new, text="").pack()

		btnlog = tk.Button(new, text="Login", width=12, height=2, bg="dodger blue", command=self.admin_screen)
		btnlog.pack()
		self.new.bind('<Return>', self.admin_screen)


	def admin_screen(self, event=None):

		'''This function gets the entry fields of username and password,
		   checks to see if they are correct and starts the admin window 
		   if they are'''
		
		#Makes it a wee bit harder to figure out the username and password ;)
		usercharacterList = [chr(97), chr(100), chr(109), chr(105), chr(110)]
		passcharacterList = [chr(112), chr(101), chr(97), chr(110), chr(117), chr(116), chr(50), chr(53)]
		correctUsername = "".join(usercharacterList)
		correctPassword = "".join(passcharacterList)
		
		username = self.username_entry.get()
		password = self.password_entry.get()

		#Still learning how to conceal sensitive info like this from my src
		if username == correctUsername and password == correctPassword:

			self.admin = tk.Toplevel(self.new)
			adminwindow = Admin(self.admin)
			self.new.withdraw()

		else:
			#Show a warning message and clear the username/password entries
			self.messagebox.showwarning('Error', 'Incorrect Username/Password. Try Again')
			self.username_entry.delete(0, 'end')
			self.password_entry.delete(0, 'end')
			self.new.deiconify()
