from tkinter import *
from PIL import Image , ImageTk
from tkinter import filedialog as fd 
from center_tk import Center_root
from config_tk import *
import json , sys

def setup_info():

	with open(sys.argv[1]) as json_meta: 
		umeta = json.load(json_meta)

	root.title(umeta['Full-Name'])
	try:
		img = Image.open(umeta['image-path'])
		uimage.update()
		img.thumbnail((uimage.winfo_width()+50,uimage.winfo_height()))
		image = ImageTk.PhotoImage(img)
		uimage['image'] = image
		uimage.image = image	
	except:
		uimage['text'] = 'No Image Found'

	uname["text"] = umeta['Full-Name']
	udob["text"] = 	udob["text"] + umeta['DOB']
	ucob['text'] =	ucob["text"] +umeta['COB']
	unat['text'] = unat["text"] +umeta['Nationality']
	usex['text'] = usex["text"] +umeta['Sex']
	ucc['text']  = ucc["text"]  + umeta['City/Country']
	uocc['text'] = uocc["text"]  + umeta['Occupation']
	uemail['text'] = uemail["text"] + umeta['Email']
	uadd['text'] = uadd["text"] + umeta['Address']
	uol['text'] = uol["text"] + umeta['Other-links']

root = Tk()
root['bg'] = root_bg
root.iconbitmap(icon)
center_r = Center_root(master = root ,geometry = (750 , 480) ) 

uimage = Label(relief = "solid",compound="center")
uimage.place(relx = 0.05 , rely = 0.05 , relwidth = 0.42 , relheight = 0.9)
uname = Label(font = ["Corbel" ,24 ] , fg = '#7BCEFF',bg = bg  )
uname.place(relx = 0.53 , rely = 0.05 )
udob = Label(text =  "Date of Birth: ", font = font,bg = bg , fg = fg )
udob.place(relx = 0.53 , rely = 0.15 )
ucob = Label(text = "City of Birth: " , font = font,bg = bg , fg = fg )
ucob.place(relx = 0.53 , rely = 0.22 )
unat = Label(text = "Naitonality: " , font = font,bg = bg , fg = fg )
unat.place(relx = 0.53 , rely = 0.29 )
usex = Label(text ="Sex:"  , font = font,bg = bg , fg = fg )
usex.place(relx = 0.53 , rely = 0.36 )
ucc = Label(text = "City/Country: " , font = font,bg = bg , fg = fg )
ucc.place(relx = 0.53 , rely = 0.43 )
uocc = Label(text = 'Occupation: ' , font = font,bg = bg , fg = fg )
uocc.place(relx = 0.53 , rely = 0.5 )
uemail = Label(text ="Email: "  , font = font,bg = bg , fg = fg )
uemail.place(relx = 0.53 , rely = 0.57 )
uadd = Label(text ="Address: "  , font = font ,bg = bg , fg = fg)
uadd.place(relx = 0.53 , rely = 0.64 )
uol = Label(text ="Other-links: "  , font = font,bg = bg , fg = fg )
uol.place(relx = 0.53 , rely = 0.71 )

try:
	setup_info()
except :
	for widget in [uimage , uname , udob , uemail ,uol, uadd , uocc , usex , unat , ucc , ucob] :
		widget["text"] =  widget["text"] + "Empty"
	root.title("Empty")

root.mainloop()