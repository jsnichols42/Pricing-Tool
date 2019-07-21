'''Administrative class'''
import tkinter as tk 
from tkinter.ttk import *
from tkinter import messagebox
from decimal import *
from paper import *
import pickle
class Admin(tk.Toplevel):
	'''This class creates the adminstative page and its functions'''

	def __init__(self, master, *args, **kwargs):
		self.master = master
		self.messagebox = messagebox

		master.title("Administrative Screen")

		#Modify Prices Frame GUI
		frameMP = LabelFrame(master, text="Modify Prices", relief=tk.RIDGE)
		frameMP.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

		self.paperlb = tk.Label(frameMP, text="Choose Paper Type", padx=10, pady=5, font=("Arial", 11))
		self.paperlb.grid(column=0, row=0, sticky= tk.W + tk.N)

		self.satlb = tk.Label(frameMP, text="Saturation", padx=10, pady=5, font=("Arial", 11))
		self.satlb.grid(column=1, row=0, sticky= tk.W + tk.N)
		

		self.newprice = tk.Label(frameMP, text="Enter New Price", padx=10, pady=5, font=("Arial", 11))
		self.newprice.grid(column=2, row=0, sticky= tk.W + tk.N)

		self.paperlistbox = tk.Listbox(frameMP, height=6, width=42, exportselection=0)
		for item in ["46# Simple Bond WR(175gsm)", "8 Mil Production Gloss Photo Paper", "TOUGHCoat AquaVinyl PSA", "TOUGHCoat Thrifty Banner", "11 Mil Blockout Water Resistant Polypropylene", "Sunset Production Matte Canvas"]:
			self.paperlistbox.insert(tk.END, item)

		self.paperlistbox.grid(column=0, row=1, padx=10, pady=10)

		self.satlistbox = tk.Listbox(frameMP, height=2, exportselection=0)
		for item1 in ["Saturated", "Unsaturated"]:
			self.satlistbox.insert(tk.END, item1)

		self.satlistbox.grid(column=1, row=1, padx=10, pady=10, sticky=tk.N)

		self.modifiedprice = tk.Entry(frameMP, width=5, font=("Arial", 11))
		self.modifiedprice.grid(column=2, row=1, padx=10, pady=10, sticky=tk.N)

		self.modifybtn = tk.Button(frameMP, text="Update", width=8, height=2, font=("Arial Bold", 11), fg="white", bg="dodger blue", command=self.update_command)
		self.modifybtn.grid(column=2, row=2, pady=10)

		self.note = tk.Message(frameMP, text="Note: Please enter a DECIMAL as the new price.", font=("Arial Bold", 11), width=130)
		self.note.grid(column=0, row=2, pady=10)

		self.savebtn = tk.Button(master, text="Save", width=8, height=2, font=("Arial Bold", 11), fg="white", bg="green", command=self.save_command)
		self.savebtn.grid(column=0, row=6, padx=10, pady=20, sticky=tk.S + tk.E)

		self.quitbtn = tk.Button(master, text="Exit", width=8, height=2, font=("Arial Bold", 11), fg="white", bg="red", command=self.quit_command)
		self.quitbtn.grid(column=1, row=6, padx=10, pady=20, sticky=tk.S + tk.W)

		#Add/Remove Paper GUI
		frameAP = LabelFrame(master, text="Add/Remove Paper", relief=tk.RIDGE)
		frameAP.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky= tk.N + tk.W)

		self.newpaperlb = tk.Label(frameAP, text="Enter New Paper Name", padx=10, pady=5, font=("Arial", 11))
		self.newpaperlb.grid(column=0, row=0, sticky= tk.W + tk.N)

		self.newpaperentry = tk.Entry(frameAP, width=22, font=("Arial", 11))
		self.newpaperentry.grid(column=0, row=1, padx=10, pady=10)

		self.chklb = tk.Label(frameAP, text="Saturated?", font=("Arial", 11))
		self.chklb.grid(column=1, row=0, padx=10, pady=5, sticky= tk.W + tk.N)

		self.chk_state1 = tk.BooleanVar()
		self.chk_state1.set(False)
		self.chkSat = Checkbutton(frameAP, var=self.chk_state1)
		self.chkSat.grid(column=1, row=1, pady=10)

		self.paperprice = tk.Label(frameAP, text="Enter Desired Price", padx=10, pady=5, font=("Arial", 11))
		self.paperprice.grid(column=2, row=0, sticky= tk.W + tk.N)

		self.ppentry = tk.Entry(frameAP, width=5, font=("Arial", 11))
		self.ppentry.grid(column=2, row=1, padx=10, pady=10)

		self.addbtn = tk.Button(frameAP, text="Add", width=8, height=2, font=("Arial Bold", 11), fg="white", bg="dodger blue", command=self.add_command)
		self.addbtn.grid(column=3, row=1, pady=10, padx=10)

	def add_command(self):
		#Function is still being worked on
		#Eventually will create a new paper object and add it to the lists
		self.typeSat = self.chk_state1.get()
		self.paperentry = self.newpaperentry.get()
		self.pricePaper = self.ppentry.get()

		self.paperobject = Paper(self.paperentry, self.typeSat, self.pricePaper)

		pricing_gui.combo['values']= ("46# Simple Bond WR(175gsm)", "8 Mil Production Gloss Photo Paper", "TOUGHCoat AquaVinyl PSA", "TOUGHCoat Thrifty Banner", "11 Mil Blockout Water Resistant Polypropylene", "Sunset Production Matte Canvas", self.paperentry)
		self.paperlistbox.insert(tk.END, self.paperentry)

		self.newpaperentry.delete(0, 'end')
		self.ppentry.delete(0, 'end')
		self.chk_state1.set(False)

		self.messagebox.showinfo('Success!', "New paper was successfully added!")


	def quit_command(self):
		#Exits the admin window
		self.master.destroy()

	def change_price(self, papertype, satur, new_price):
		'''Modifies the price of a paper based on the name/type chosen 
		and the new price entered'''
		if self.satur == "Saturated":
			if self.papertype == "46# Simple Bond WR(175gsm)":
				Spaper0.modify_price(self.new_price)
			elif self.papertype == "8 Mil Production Gloss Photo Paper":
				Spaper1.modify_price(self.new_price)
			elif self.papertype == "TOUGHCoat AquaVinyl PSA":
				Spaper2.modify_price(self.new_price)
			elif self.papertype == "TOUGHCoat Thrifty Banner":
				Spaper3.modify_price(self.new_price)
			elif self.papertype == "11 Mil Blockout Water Resistant Polypropylene":
				Spaper4.modify_price(self.new_price)
			elif self.papertype == "Sunset Production Matte Canvas":
				Spaper5.modify_price(self.new_price)
			else:
				self.messagebox.showwarning('Error', "Please choose a Paper Type")
		elif self.satur == "Unsaturated":
			if self.papertype == "46# Simple Bond WR(175gsm)":
				Upaper0.modify_price(self.new_price)
			elif self.papertype == "8 Mil Production Gloss Photo Paper":
				Upaper1.modify_price(self.new_price)
			elif self.papertype == "TOUGHCoat AquaVinyl PSA":
				Upaper2.modify_price(self.new_price)
			elif self.papertype == "TOUGHCoat Thrifty Banner":
				Upaper3.modify_price(self.new_price)
			elif self.papertype == "11 Mil Blockout Water Resistant Polypropylene":
				Upaper4.modify_price(self.new_price)
			elif self.papertype == "Sunset Production Matte Canvas":
				Upaper5.modify_price(self.new_price)
			else:
				self.messagebox.showwarning('Error', "Please choose a Paper Type")
		else:
			self.messagebox.showwarning('Error', "Please choose the Saturation")


	def update_command(self):
		'''Calls the change_price function, clears all widget fields
		   in "modify prices" and lets you know the update was successful'''
		self.papertype = self.paperlistbox.get(tk.ACTIVE)
		self.satur = self.satlistbox.get(tk.ACTIVE)
		self.new_price = self.modifiedprice.get()
		
		self.change_price(self.papertype, self.satur, self.new_price)

		self.paperlistbox.selection_clear(0, tk.END)
		self.satlistbox.selection_clear(0, tk.END)
		self.modifiedprice.delete(0, 'end')

		self.messagebox.showinfo('Success!', "Update Was Successful!")
		self.master.deiconify()
		

	def save_command(self):
		#Save modified prices
		with open('paper_data.pkl', 'wb') as output:
			pickle.dump(Spaper0, output, pickle.HIGHEST_PROTOCOL)
			pickle.dump(Spaper1, output, pickle.HIGHEST_PROTOCOL)
			pickle.dump(Spaper2, output, pickle.HIGHEST_PROTOCOL)
			pickle.dump(Spaper3, output, pickle.HIGHEST_PROTOCOL)
			pickle.dump(Spaper4, output, pickle.HIGHEST_PROTOCOL)
			pickle.dump(Spaper5, output, pickle.HIGHEST_PROTOCOL)
			pickle.dump(Upaper0, output, pickle.HIGHEST_PROTOCOL)
			pickle.dump(Upaper1, output, pickle.HIGHEST_PROTOCOL)
			pickle.dump(Upaper2, output, pickle.HIGHEST_PROTOCOL)
			pickle.dump(Upaper3, output, pickle.HIGHEST_PROTOCOL)
			pickle.dump(Upaper4, output, pickle.HIGHEST_PROTOCOL)
			pickle.dump(Upaper5, output, pickle.HIGHEST_PROTOCOL)
			#pickle.dump(self.paperobject, output, pickle.HIGHEST_PROTOCOL)