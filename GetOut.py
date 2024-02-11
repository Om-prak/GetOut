import psutil
# import tkinter as tk
import os
import subprocess




def kill(process_name):
    
    os.system('taskkill /f /im '+ process_name)


def show_list():


	with open('programes.txt') as R:
	   lines = R.readlines()
	   newlines = lines[0].split()
	   size = len(newlines)
	   for z in range(size):
	   		print(newlines[z])


def update():

	programs = []

	for process in psutil.process_iter(['name']):
		p = process.info['name']+' '
		programs.append(p)

	with open('programes.txt', 'w') as f:
		for line in programs:
			    
			# f.write('\n')
			if line!="python.exe " and line!="svchost.exe " and line!="conhost.exe " and line!="py.exe " and line!="GetOut.exe " and line!="sihost.exe " and line!="explorer.exe ":
	    		 f.write(line)

	    



def read_process_to_kill():

	
	with open('programes.txt') as R:
	   lines = R.readlines()
	   newlines = lines[0].split()
	   size = len(newlines)

	   for x in range(size):
	   		
	   		try:
	   			kill(newlines[x])
	   		except Exception as e:
	   			raise e

	# subprocess.Popen('explorer "C:\path\of\folder"')
	kill("sihost.exe")
	kill("GetOut.exe")
	kill("python.exe")

update()
show_list()
read_process_to_kill()


# root = tk.Tk()
# root.title("GetOut")

# frame = tk.Frame(root)
# frame.pack(padx=100, pady=100)

# button1 = tk.Button(frame, text="show list", command=show_list)
# button1.pack()

# button2 = tk.Button(frame, text="update list", command=update)
# button2.pack()

# button3 = tk.Button(frame, text="Kill all in list", command=read_process_to_kill)
# button3.pack()


# root.mainloop()