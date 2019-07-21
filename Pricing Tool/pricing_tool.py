'''Author: Joshua Nichols
   Date: 7/9/2019
   Project: Pricing Tool 2.0
'''
"""GUI Classes include: PricingTool, Admin, Print(not yet added), Login
   Normal Classes include: Paper, etc.. (more to be added)
"""
import tkinter as tk 
from tkinter.ttk import *
from tkinter import messagebox
from decimal import *
import pickle
from paper import *
from login import Login


class PricingTool(tk.Frame):
	"""This class creates the main pricing tool gui"""
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		
		self.master = master
		self.messagebox = messagebox
		master.geometry('1440x768')
		master.title("Wide Format Pricing Tool")


		###################################
		###### Wide Format Paper GUI ######
		###################################

		self.menu = tk.Menu(master)
		self.filemenu = tk.Menu(self.menu, tearoff=0)
		self.filemenu.add_command(label='Print')
		self.menu.add_cascade(label='File', menu=self.filemenu)
		self.adminmenu = tk.Menu(self.menu, tearoff=0)
		self.adminmenu.add_command(label='Login', command=self.login_window)
		self.menu.add_cascade(label='Admin', menu=self.adminmenu)

		master.config(menu=self.menu)


		self.sep = Separator(master, orient=tk.VERTICAL)
		self.sep.grid(column=2, row=0, rowspan=40, sticky='ns', padx=80)

		self.lb = tk.Label(master, text="Wide Format Paper", padx=50, pady=20, font=("Arial Bold", 24))
		self.lb.grid(column=0, row=0)

		self.lb1 = tk.Label(master, text="Saturation:", padx=20, pady=20, font=("Arial", 16))
		self.lb1.grid(column=0, row=4)

		self.lb2 = tk.Label(master, text="Paper Type:", padx=20, pady=20, font=("Arial", 16))
		self.lb2.grid(column=0, row=8)

		self.lb3 = tk.Label(master, text="Measurement Type:", padx=20, pady=20, font=("Arial", 16))
		self.lb3.grid(column=0, row=12)

		self.lb4 = tk.Label(master, text="Width:", padx=20, pady=20, font=("Arial", 16))
		self.lb4.grid(column=0, row=16)

		self.lb5 = tk.Label(master, text="Height:", padx=20, pady=20, font=("Arial", 16))
		self.lb5.grid(column=0, row=20)

		self.lb6 = tk.Label(master, text="Number of Grommets:", padx=20, pady=20, font=("Arial", 16))
		self.lb6.grid(column=0, row=24)

		self.lb7 = tk.Label(master, text="Mounting:", padx=20, pady=20, font=("Arial", 16))
		self.lb7.grid(column=0, row=28)

		self.anslb = tk.Label(master, text="Total Price:", padx=20, pady=20, font=("Arial Bold", 18))
		self.anslb.grid(column=0, row=36)

		self.radiovar1 = tk.StringVar()
		self.radiovar2 = tk.StringVar()

		self.radiovar1.set(0)
		self.radiovar2.set(0)

		self.sat = tk.Radiobutton(master, text='Saturated', variable=self.radiovar1, value=1, font=("Arial", 12))
		self.unsat = tk.Radiobutton(master, text='Unsaturated', variable=self.radiovar1, value=2, font=("Arial", 12))
		self.sat.grid(column=1, row=4)
		self.unsat.grid(column=1, row=5)

		self.inch = tk.Radiobutton(master, text='Inches', variable=self.radiovar2, value=3, font=("Arial", 12))
		self.feet = tk.Radiobutton(master, text='Feet', variable=self.radiovar2 ,value=4, font=("Arial", 12))
		self.inch.grid(column=1, row=12)
		self.feet.grid(column=1, row=13)

		self.combo = Combobox(master, width=30, font=("Arial", 12))
		self.combo['values']= ("46# Simple Bond WR(175gsm)", "8 Mil Production Gloss Photo Paper", "TOUGHCoat AquaVinyl PSA", "TOUGHCoat Thrifty Banner", "11 Mil Blockout Water Resistant Polypropylene", "Sunset Production Matte Canvas")
		self.combo.set('Please Choose a Paper Type')
		self.combo.grid(column=1, row=8)
		self.master.option_add('*TCombobox*Listbox.font', ("Arial", 12))


		self.chk_state = tk.BooleanVar()
		self.chk_state.set(False)
		self.chk = Checkbutton(master, var=self.chk_state)
		self.chk.grid(column=1, row=28)

		self.var1 = tk.StringVar(master)
		self.var1.set("0")
		self.spin = Spinbox(master, from_=0, to=500, width=5, textvariable=self.var1, font=("Arial", 12))
		self.spin.grid(column=1, row=24)

		self.widtxt = tk.Entry(master, width=5, font=("Arial", 16))
		self.heitxt = tk.Entry(master, width=5, font=("Arial", 16))
		self.widtxt.grid(column=1, row=16)
		self.heitxt.grid(column=1, row=20)

		self.btn1 = tk.Button(master, text="Calculate",width = 15, height=2, font=("Arial Bold", 16), fg="white", bg="green", command=self.calculateWideFormat)
		self.btn1.grid(column=0, row=32)

		self.btn2 = tk.Button(master, text="Clear", width = 15, height=2, font=("Arial Bold", 16), fg="white", bg="red", command=self.clear)
		self.btn2.grid(column=1, row=32)

		self.answer = tk.Entry(master, width=10, font=("Arial Bold", 18))
		self.answer.grid(column=1, row=36)

		#############################
		####### BluePrint GUI #######
		#############################

		self.var2 = tk.StringVar(master)
		self.var2.set("0")
		self.var3 = tk.StringVar(master)
		self.var3.set("0")
		self.var4 = tk.StringVar(master)
		self.var4.set("0")


		self.spin2 = Spinbox(master, from_=0, to=500, width=5, textvariable=self.var2, font=("Arial", 12))
		self.spin2.grid(column=4, row=12)

		self.spin3 = Spinbox(master, from_=0, to=500, width=5, textvariable=self.var3, font=("Arial", 12))
		self.spin3.grid(column=4, row=16)

		self.spin4 = Spinbox(master, from_=0, to=500, width=5, textvariable=self.var4, font=("Arial", 12))
		self.spin4.grid(column=4, row=20)

		self.widtxt1 = tk.Entry(master, width=5, font=("Arial", 16))
		self.heitxt1 = tk.Entry(master, width=5, font=("Arial", 16))
		self.widtxt1.grid(column=4, row=4)
		self.heitxt1.grid(column=4, row=8)

		self.answerBP = tk.Entry(master, width=10, font=("Arial Bold", 18))
		self.answerBP.grid(column=4, row=36)

		self.btn3 = tk.Button(master, text="Calculate", width = 15, height=2, font=("Arial Bold", 16), fg="white", bg="green", command=self.calculateBluePrint)
		self.btn3.grid(column=3, row=32)

		self.btn4 = tk.Button(master, text="Clear", width = 15, height=2, font=("Arial Bold", 16), fg="white", bg="red", command=self.clearBP)
		self.btn4.grid(column=4, row=32)

		self.lb8 = tk.Label(master, text="Blueprints", padx=50, pady=20, font=("Arial Bold", 24))
		self.lb8.grid(column=3, row=0)

		self.lb9 = tk.Label(master, text="Width in Inches:", font=("Arial", 16))
		self.lb9.grid(column=3, row=4)

		self.lb10 = tk.Label(master, text="Height in Inches:", font=("Arial", 16), padx=20)
		self.lb10.grid(column=3, row=8)

		self.lb11 = tk.Label(master, text="Pages per Set:", pady=20, font=("Arial", 16), padx=20)
		self.lb11.grid(column=3, row=12)

		self.lb12 = tk.Label(master, text="Number of Sets:", pady=20, font=("Arial", 16), padx=20)
		self.lb12.grid(column=3, row=16)

		self.lb13 = tk.Label(master, text="Blueprint Bindings:", pady=20, padx=20, font=("Arial", 16))
		self.lb13.grid(column=3, row=20)

		self.lb14 = tk.Label(master, text="Total Blueprint Price:", pady=20, padx=20, font=("Arial Bold", 18))
		self.lb14.grid(column=3, row=36)

	##################################################
	###### Functions needed to run the main GUI ######
	##################################################
	def login_window(self):
		self.login = tk.Toplevel(self.master)
		loginwindow = Login(self.login)
		

	def measurementType(self, measurement):
		'''This function returns a boolean based measurement type'''
		if measurement == '3':
			return True
	
		elif measurement == '4':
			return False

		else:
			self.messagebox.showwarning('Error', 'You MUST choose a Measurement Type!')

	def definePaper(self):
		if self.typeS == "1":

			if self.name == 0:
				return Decimal(Spaper0.price)

			elif self.name == 1:
				return Decimal(Spaper1.price)

			elif self.name == 2:
				return Decimal(Spaper2.price)

			elif self.name == 3:
				return Decimal(Spaper3.price)

			elif self.name == 4:
				return Decimal(Spaper4.price)

			elif self.name == 5:
				return Decimal(Spaper5.price)

			else:
				self.messagebox.showwarning('Error', 'You MUST choose the Paper Type!')

		elif self.typeS == "2":

			if self.name == 0:
				return Decimal(Upaper0.price)

			elif self.name == 1:
				return Decimal(Upaper1.price)

			elif self.name == 2:
				return Decimal(Upaper2.price)

			elif self.name == 3:
				return Decimal(Upaper3.price)

			elif self.name == 4:
				return Decimal(Upaper4.price)

			elif self.name == 5:
				return Decimal(Upaper5.price)

			else:
				self.messagebox.showwarning('Error', 'You MUST choose the Paper Type!')

		else:
			self.messagebox.showwarning('Error', 'You MUST choose Saturated or Unsaturated!')	


	def calculateWideFormat(self):

		self.name = self.combo.current()          #Used to get combobox selection
		mount = self.chk_state.get()         #Used to get true or false from checkbox selection
		self.typeS = self.radiovar1.get()         #Used to get currently selected radio button value of Saturated/Unsaturated
		measurement = self.radiovar2.get()   #Used to get currently selected radio button value of Feet/Inches
		height = self.heitxt.get()			#Used to get the height that has been typed in
		width = self.widtxt.get()			#Used to get the width that has been typed in
		grommets = self.spin.get()			#Used to get number of grommets chosen

		define = self.definePaper()
		mt = self.measurementType(measurement)

		if mount == True:
		
			if mt == False:
				x = (Decimal(height) * Decimal(width))
				sfoot = (x * define) + (3*x)
				solution = "$" + str(round(sfoot + Decimal(grommets), 2)) 

			elif mt == True:

				x = ((Decimal(height)* Decimal(width))/144)
				
				if Decimal(height) and Decimal(width) < 12 and self.name == 5:
					solution = "$" + str(round(Decimal(20.00) + Decimal(grommets) + (3*x), 2))

				else:
					sfoot = (x * define) + (3*x)
					solution = "$" + str(round(sfoot + Decimal(grommets), 2))


		else:
			if mt == False:
				x = (Decimal(height) * Decimal(width))
				sfoot = (x * define)
				solution = "$" + str(round(sfoot + Decimal(grommets), 2)) 

			elif mt == True:
				x = ((Decimal(height)* Decimal(width))/144)

				if Decimal(height) and Decimal(width) < 12 and self.name == 5:
					solution = "$" + str(round(Decimal(20.00) + Decimal(grommets), 2))

				else:
					sfoot = (x * define)
					solution = "$" + str(round(sfoot + Decimal(grommets), 2))


		self.answer.delete(0, 'end')
		Entry.insert(self.answer, 0, solution)
		print(solution)

	def calculateBluePrint(self):
		width1 = self.widtxt1.get()	
		height1 = self.heitxt1.get()	
		pages = self.spin2.get()
		sets = self.spin3.get()
		bindings = self.spin4.get()

		bpSquareFoot = ((Decimal(height1) * Decimal(width1))/144) * Decimal(0.75)
		setPrice = bpSquareFoot * Decimal(pages)
		bpSolution = "$" + str(round((setPrice * Decimal(sets)) + (2 * Decimal(bindings)), 2))

		self.answerBP.delete(0, 'end')
		Entry.insert(self.answerBP, 0, bpSolution)
	

	def clear(self):
		self.widtxt.delete(0, 'end')
		self.spin.delete(0, 'end')
		self.spin.insert(0, '0')
		self.heitxt.delete(0, 'end')
		self.answer.delete(0, 'end')
		self.combo.set('Please Choose A Paper Type')
		self.radiovar1.set(0)
		self.radiovar2.set(0)
		self.chk_state.set(False)

	def clearBP(self):
		self.widtxt1.delete(0, 'end')
		self.spin2.delete(0, 'end')
		self.spin2.insert(0, '0')
		self.spin3.delete(0, 'end')
		self.spin3.insert(0, '0')
		self.heitxt1.delete(0, 'end')
		self.spin4.delete(0, 'end')
		self.spin4.insert(0, '0')
		self.answerBP.delete(0, 'end')

#Load the previously saved paper objects
with open('paper_data.pkl', 'rb') as input:
	Spaper0 = pickle.load(input)
	Spaper1 = pickle.load(input)
	Spaper2 = pickle.load(input)
	Spaper3 = pickle.load(input)
	Spaper4 = pickle.load(input) 
	Spaper5 = pickle.load(input)
	Upaper0 = pickle.load(input)
	Upaper1 = pickle.load(input)
	Upaper2 = pickle.load(input)
	Upaper3 = pickle.load(input)
	Upaper4 = pickle.load(input)
	Upaper5 = pickle.load(input)



root = tk.Tk()
pricing_gui = PricingTool(root)
root.mainloop()