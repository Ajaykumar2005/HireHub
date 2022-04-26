#Id.get() IS A STRING AND THE DATA WE WANT TO MATCH IS INTEGER
from tkinter import *
import tkinter.ttk as ttk
import sqlite3
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
#SIGN IN BOXcursor.execute("CREATE TABLE IF NOT EXISTS `Job_Aspirants` (ID INTEGER NOT NULL  PRIMARY KEY , Full_Name TEXT, Job_type TEXT, Age TEXT,Experience TEXT, Address TEXT,M_Number integer,Password varchar(45) )")
global l
l=["Dermatalogistn","PGT Maths","PGT English","PGT Science","Tuitor","Trail Truck Driver","Registered Nurse","Retail Salesperson","Software Developers","Marketing Managers","Agriculture Food Scientist","Animal Breeder","Conservation Scientist","Enviornmental Scientist","Farmer","Fish Hatchery Manager","Fisher","First-Line Supervisors of Food Preparation and Serving Workers","First-Line Supervisors of Office and Administrative Support Workers","Computer User Support Specialists","Computer Systems Analysts","Network and Computer Systems Administrators","Web Developers","Management Analysts","Medical and Health Services Managers","Accountants","Information Technology Project Managers","Sales Managers","Industrial Engineers","First-Line Supervisors of Production and Operating Workers","Nursing Assistants","Licensed Practical and Licensed Vocational Nurses","General and Operations Managers","Bookkeeping"," Accounting","Auditing Clerks","Managers", "All Other Financial Managers"," Branch or Department","Insurance Sales Agents","Sales Representatives", "Wholesale and Manufacturing", "Technical and Scientific ProductsSales Representative", "All Other Sales Agents", "Financial Services","Critical Care Nurses","Cashiers","Computer Systems Engineers/Architects","Market Research Analysts and Marketing Specialists","Physical Therapists","Medical Assistants","First-Line Supervisors of Non-Retail Sales Workers","Software Quality Assurance Engineers and Testers","First-Line Supervisors of Mechanics", "Installers","Repairers","Information Security Analysts","Medical Secretaries","Laborers and Freight", "Stock and Material Movers", "HandSecurity Guards","Family and General Practitioners"]
		
global ide
def employ(event):
	def final_resume_(event):		

		from tkinter import Text, Tk
		from tkinter.ttk import Progressbar
		#mainpage_.destroy()

		import tkinter.ttk as ttk
		global resume_f__
		#root.destroy()
		resume_f__= Tk()
		resume_f__.config(bg="#FFFFFF")
		resume_f__.title("CV (Resume)")
		resume_f__.iconbitmap("job.ico")
		resume_f__.resizable(False,False)
		resume_f__.geometry("795x680")
		#resume_.wm_attributes("-alpha",0.7)
		#r=Scale(resume_,from_=1,to=100000,orient=HORIZONTAL,bg="BLUE",fg="red")
		#r.pack()
		Name_tx=StringVar()
		Adress_tx=StringVar()
		Number_tx=StringVar()
		Email_tx=StringVar()
		Facebook_tx=StringVar()
		Twitter_tx=StringVar()
		Linkedin_tx=StringVar()
		Profile_tx=StringVar()
		Work1_From_tx=StringVar()
		Work1_To_tx=StringVar()
		Work1_Post_tx=StringVar()
		Work1_City_tx=StringVar()
		Work1_CompanyName_tx=StringVar()
		Work1_CompanyDesc_tx=StringVar()
		Work2_From_tx=StringVar()
		Work2_To_tx=StringVar()
		Work2_Post_tx=StringVar()
		Work2_City_tx=StringVar()
		Work2_CompanyName_tx=StringVar()

		Work2_CompanyDesc_tx=StringVar()
		Education1_From_tx=StringVar()
		Education1_To_tx=StringVar()
		Education1_Institute_tx=StringVar()
		Education1_City_tx=StringVar()
		Education1_Qualifications_tx=StringVar()
		Education2_From_tx=StringVar()
		Education2_To_tx=StringVar()
		Education2_Institute_tx=StringVar()
		Education2_City_tx=StringVar()
		Education2_Qualifications_tx=StringVar()
		Skill_1_tx=StringVar()
		Skill_2_tx=StringVar()
		Skill_3_tx=StringVar()
		Skill_4_tx=StringVar()
		lvl_1_tx=IntVar()
		lvl_2_tx=IntVar()
		lvl_3_tx=IntVar()
		lvl_4_tx=IntVar()
		#centr_=StringVar()
		conn=sqlite3.connect("resum.db")
		
		c=conn.cursor()
		c.execute("SELECT * FROM Resume3")
		dr=c.fetchall()
		#idel)
		
		#type(idel))


		for i in dr:
			#)
			#type(i[0]))

			#)
			if int(i[0])==ide:
				Name_tx.set(i[1])
				Adress_tx.set(i[2])
				Number_tx.set(i[3])

				Email_tx.set(i[4])
				Facebook_tx.set(i[5])
				Twitter_tx.set(i[6])
				Linkedin_tx.set(i[7])
				Profile_tx.set(i[8]) 
				Work1_From_tx.set(i[9])
				Work1_To_tx.set(i[10])
				Work1_Post_tx.set(i[11])
				Work1_City_tx.set(i[12])
				Work1_CompanyName_tx.set(i[13])
				Work1_CompanyDesc_tx.set(i[14])
				Work2_From_tx.set(i[15])
				Work2_To_tx.set(i[16])
				Work2_Post_tx.set(i[17])
				Work2_City_tx.set(i[18])
				Work2_CompanyName_tx.set(i[19])

				Work2_CompanyDesc_tx.set(i[20])
				Education1_From_tx.set(i[21])
				Education1_To_tx.set(i[22])
				Education1_Institute_tx.set(i[23])
				Education1_City_tx.set(i[24])
				Education1_Qualifications_tx.set(i[25])
				Education2_From_tx.set(i[26])
				Education2_To_tx.set(i[27])
				Education2_Institute_tx.set(i[28])
				Education2_City_tx.set(i[29])
				Education2_Qualifications_tx.set(i[30])
				Skill_1_tx.set(i[32])

				Skill_2_tx.set(i[33])
				Skill_3_tx.set(i[33])
				Skill_4_tx.set(i[34])
				lvl_1_tx.set(i[35])
				lvl_2_tx.set(i[36])
				lvl_3_tx.set(i[37])
				lvl_4_tx.set(i[38])
				#i[39])

				centr=i[39]
				#type(centr))
				
		#dr)
		conn.commit()
		conn.close()
		
		def progrs(event):
			progress['value']=50
		import os
				
		global bgm
		global img
		global img1
		l=Label(resume_f__,bg="white")
		#global c
		c=Canvas(l,width=600,height=1200,bd=0,bg="white",highlightthickness=0)
		#img1=PhotoImage(file="bgmp.png")
		img1=Image.open("back10.jpg")
		img=PhotoImage(master=c,file="Profile.png")

		img1=img1.resize((606,742),Image.ANTIALIAS)
		img3_=ImageTk.PhotoImage(img1,master=c)
		
		d1=c.create_image(320,310,image=img3_)
		d=c.create_image(150,30,image=img)

		c.pack()
		
		l.pack()
		l.place(x=220,y=0)
		
		global c1
		l1=Label(resume_f__)
		c1=Canvas(l1,width=250,height=1700,bd=0,highlightthickness=0)
		img_=PhotoImage(file="NAME21.png",master=c1)
		img2=Image.open("back8.jpg")
		submit_=PhotoImage(file="Submit__1.png",master=c1)
		submt_=c.create_image(900,100,image=submit_)
		
		img2=img2.resize((340,1000),Image.ANTIALIAS)
		img1_=ImageTk.PhotoImage(img2,master=c1)
		d1=c1.create_image(80,320,image=img1_)
		
		#img21=Image.open("bgm1.jpg")
		
		#3img21=img21.resize((300,700),Image.ANTIALIAS)
		#img11_=ImageTk.PhotoImage(img21,master=c1)
		#)
		#d11=c1.create_image(110,700,image=img11_)
		

		d2=c1.create_image(75,294,image=img_)
		
		c1.pack()
		#c1.place(x=0,y=0)
		l1.pack()
		l1.place(x=0,y=0)
		
		global n
		n="bg3.png"
		mag=Image.open(n)
		global frame1
		mag=mag.resize((110,110),Image.ANTIALIAS)
		mag1=ImageTk.PhotoImage(mag,master=c1)
		frame1=c1.create_image(90,70,image=mag1)
		#frame1.place(x=10,y=10)
		'''
		m="add-user.png"
		mag4=Image.open(m)
		mag4=mag4.resize((30,30),Image.ANTIALIAS)
		mag5=ImageTk.PhotoImage(mag4,master=c1)
		frame2=c1.create_image(170,110,image=mag5)
		c1.tag_bind(frame2,'<ButtonPress-1>',photo)
		'''
		#global centr
		Info_=PhotoImage(master=c1,file="INFO.png")
		Info=c1.create_image(92,254,image=Info_)
		conct=Image.open("user.png")
		conct=conct.resize((30,30),Image.ANTIALIAS)
		conct__=ImageTk.PhotoImage(conct,master=c1)
		
		conct_=c1.create_image(35,290,image=conct__)
		##centr)
		conn=sqlite3.connect("resum.db")
		
		cur=conn.cursor()
		cur.execute("SELECT * FROM Resume3")
		dr=cur.fetchall()
		

		global centr_
		for i in dr:
			#)
			#type(idel))
			if int(i[0])==ide:
				#type(i[0]))
				centr_=i[39]
				#centr_)
				break
		#centr_)
		rot3__=Image.open(centr_)
		
		rot3__=rot3__.resize((70,70),Image.ANTIALIAS)
		rot1__=ImageTk.PhotoImage(rot3__,master=c1)
		frame1=c1.create_image(90,70,image=rot1__)
			
		
		adres=Image.open("map.png")
		adres=adres.resize((30,30),Image.ANTIALIAS)
		adres_=ImageTk.PhotoImage(adres,master=c1)
		addres=c1.create_image(35,332,image=adres_)
		adress_img=PhotoImage(master=c1,file="Addressw.png")
		adress_w=c1.create_image(84,332,image=adress_img)


		


		phone=Image.open("telephone.png")
		phone=phone.resize((30,30),Image.ANTIALIAS)
		phone_=ImageTk.PhotoImage(phone,master=c1)
		phone_img=PhotoImage(master=c1,file="Phonew.png")
		phne_w=c1.create_image(75,373,image=phone_img)
		phoone=c1.create_image(35,368,image=phone_)
			


		Email1=Image.open("gmail.png")
		Email1=Email1.resize((30,30),Image.ANTIALIAS)
		Email_=ImageTk.PhotoImage(Email1,master=c1)
		
		Email_img=PhotoImage(master=c1,file="Emailw.png")
		Emai_w=c1.create_image(75,412,image=Email_img)
		Emaill=c1.create_image(35,412,image=Email_)
		#reds=c1.create_line(0,226,296,226,width=2)
		#reds1=c1.create_line(0,259,296,259,width=2)

	 
		
		social_=PhotoImage(master=c1,file="SOCIAL.png")
		Social=c1.create_image(95,480,image=social_)
		
		#reds=c1.create_line(0,459,296,459,width=2)
		#reds1=c1.create_line(0,494,296,494,width=2)
	 	
			

		
		fb=Image.open("facebook.png")
		fb=fb.resize((30,30),Image.ANTIALIAS)
		fb_=ImageTk.PhotoImage(fb,master=c1)
		facbk=c1.create_image(35,520,image=fb_)
		fb_img=PhotoImage(master=c1,file="Facebookw.png")
		fb_w=c1.create_image(90,520,image=fb_img)
	 
		
	 	
		
		twt=Image.open("twitter_.png")
		twt=twt.resize((30,30),Image.ANTIALIAS)
		twt_=ImageTk.PhotoImage(twt,master=c1)

		twt_img=PhotoImage(master=c1,file="Twitter.png")
		twt_w=c1.create_image(85,570,image=twt_img)
		twitwr=c1.create_image(35,570,image=twt_)


	 	
		lnk=Image.open("linkedin_.png")
		lnk=lnk.resize((30,30),Image.ANTIALIAS)
		lnk_=ImageTk.PhotoImage(lnk,master=c1)

		lnk_img=PhotoImage(master=c1,file="Linkedin.png")
		lnk_w=c1.create_image(85,620,image=lnk_img)
		lnkdin=c1.create_image(35,620,image=lnk_)
		profe=Image.open("user.png")
		profe=profe.resize((44,44),Image.ANTIALIAS)
		profe__=ImageTk.PhotoImage(profe,master=c1)
		profe_=c.create_image(75,30,image=profe__)
	 	
		
		wrke__img=PhotoImage(master=c,file="WORK-EXPERIENCE.png")
		wrke_im=c.create_image(210,140,image=wrke__img)
		wrke=Image.open("edit.png")
		wrke=wrke.resize((44,44),Image.ANTIALIAS)
		wrke__=ImageTk.PhotoImage(wrke,master=c)
		wrke_1=c.create_image(75,140,image=wrke__)
	 
		educ__img=PhotoImage(master=c,file="EDUCATION.png")
		educ_im=c.create_image(185,320,image=educ__img)
		educ=Image.open("graduation-hat.png")
		educ=educ.resize((44,44),Image.ANTIALIAS)
		educ__=ImageTk.PhotoImage(educ,master=c)
		educ_1=c.create_image(75,320,image=educ__)
		

		education1_num=c.create_text(110,345,text="1.",fill="Black",font=("comic sans ms",12))
		education1_from=c.create_text(144,355,text=Education1_From_tx.get(),fill="black",font=("comic sans ms",11))
		education1_to=c.create_text(198,355,fill="Black",text=Education1_To_tx.get(),font=("comic sans ms",11))
		education1_city=c.create_text(167,376,text=Education1_City_tx.get(),fill="Black",font=("comic sans ms",10))	
		education1_inst=c.create_text(290,340,text=Education1_Institute_tx.get(),width=200,justify=LEFT,anchor=NW ,fill="Black",font=("Segoe Print",12,"bold"))	
		education1_qual=c.create_text(290,360,text=Education1_Qualifications_tx.get(),fill="Black",width=200,justify=LEFT,anchor=NW ,font=("Segoe Print",10))
		
		work1_num=c.create_text(110,182,text="1.",fill="Black",font=("comic sans ms",12))
		work1_year_from=c.create_text(144,192,text=Work1_From_tx.get(),fill="Black",font=("comic sans ms",11))
		work1_year_to=c.create_text(198,192,text=Work1_To_tx.get(),fill="Black",font=("comic sans ms",11))
		work1_city=c.create_text(167,208,text=Work1_City_tx.get(),fill="Black",font=("comic sans ms",10))
		work1_position=c.create_text(290,160,text=Work1_Post_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("Segoe Print",12,"bold"))
		work1_company=c.create_text(290,180,text=Work1_CompanyName_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("comic sans ms",10))
		work1_desc=c.create_text(290,200,text=Work1_CompanyDesc_tx.get(),fill="Black",width=290,justify=LEFT,anchor=NW ,font=("comic sans ms",10))

		education2_num=c.create_text(110,410,text="2.",fill="Black",font=("comic sans ms",11))
		education2_from=c.create_text(144,420,fill="Black",text=Education2_From_tx.get(),font=("comic sans ms",11))
		education2_to=c.create_text(198,420,text=Education2_To_tx.get(),fill="Black",font=("comic sans ms",12))
		education2_city=c.create_text(167,438,text=Education2_City_tx.get(),fill="Black",font=("comic sans ms",10))
		education2_inst=c.create_text(290,400,fill="Black",text=Education2_Institute_tx.get(),width=200,justify=LEFT,anchor=NW ,font=("Segoe Print",12,"bold"))
		education2_qual=c.create_text(290,420,text=Education2_Qualifications_tx.get(),fill="Black",width=200,justify=LEFT,anchor=NW ,font=("comic sans ms",10))
		

		work2_num=c.create_text(110,242,text="2.",fill="Black",font=("comic sans ms",11))
		work2_year_from=c.create_text(144,252,text=Work2_From_tx.get(),fill="Black",font=("comic sans ms",11))
		work2_year_to=c.create_text(198,252,text=Work2_To_tx.get(),fill="Black",font=("comic sans ms", 12))
		work2_city=c.create_text(167,272,text=Work2_City_tx.get(),fill="Black",font=("comic sans ms", 10))
		work2_position=c.create_text(290,230,text=Work2_Post_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("Segoe Print",12,"bold"))
		work2_company=c.create_text(290,250,text=Work2_CompanyName_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("comic sans ms",10))
		work2_desc=c.create_text(290,270,text=Work2_CompanyDesc_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("comic sans ms",10))
		t=205
		profile_t=c.create_text(120,46,fill="Black",text=Profile_tx.get(),width=400,justify=LEFT,anchor=NW ,font=("Segoe Print",12,"bold"))
		ty=30
		ty_single=17
				
		name1=c1.create_text(123,160,text=Name_tx.get(),width=220,font=("Segoe Script", 18," bold"))
		lnk_t=c1.create_text(64,625,text=Linkedin_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		twt_t=c1.create_text(64,575,text=Twitter_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		phone_t=c1.create_text(64,377,text=Number_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		name_=c1.create_text(64,297,text=Name_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		adres_t=c1.create_text(64,335,text=Adress_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		Email_t=c1.create_text(64,419,text=Email_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		fb_t=c1.create_text(64,527,text=Facebook_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		c.create_line(165,241,176,241,width=3)
		c.create_line(165,181,176,181,width=3)
		c.create_line(168,412,179,412,width=3)
		c.create_line(168,347,179,347,width=3)
		def proges(event):
			import tkinter.ttk as ttk
			from tkinter import ttk
			i=440
			j=515
			e_=ttk.Style(resume_f__)
			e_.theme_use("default")
			e_.configure("#8AC91D_.Horizontal.TProgressbar",bordercolor="#8AC91D",lightcolor="#8AC91D",darkcolor="#8AC91D",background="#8AC91D")
			progress1_=Progressbar(resume_f__,style="#8AC91D_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress1_["value"]=int(lvl_1_tx.get())
			progress1_.pack()
			progress1_.place(x=i,y=j)
		def proges1(event):
			import tkinter.ttk as ttk
			i=440
			j=550
			e1_=ttk.Style(resume_f__)
			e1_.theme_use("default")
			e1_.configure("red1_.Horizontal.TProgressbar",bordercolor="#FB9A00",lightcolor="#FB9A00",darkcolor="#FB9A00",background="#FB9A00")
			progress2_=Progressbar(resume_f__,style="red1_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress2_["value"]=int(lvl_2_tx.get())
			progress2_.pack()
			progress2_.place(x=i,y=j)
		def proges2(event):
			import tkinter.ttk as ttk
			i=440
			j=590
			e2_=ttk.Style(resume_f__)
			e2_.theme_use("default")
			e2_.configure("red2_.Horizontal.TProgressbar",bordercolor="#1FB4E7",lightcolor="#1FB4E7",darkcolor="#1FB4E7",background="#1FB4E7")
			progress3_=Progressbar(resume_f__,style="red2_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress3_["value"]=int(lvl_3_tx.get())
			progress3_.pack()
			progress3_.place(x=i,y=j)
		def proges3(event):
			import tkinter.ttk as ttk
			i=440
			j=630
			e3_=ttk.Style(resume_f__)
			e3_.theme_use("default")
			e3_.configure("red3_.Horizontal.TProgressbar",bordercolor="red",lightcolor="red",darkcolor="red",background="red")
			progress4_=Progressbar(resume_f__,style="red3_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress4_["value"]=int(lvl_4_tx.get())
			progress4_.pack()
			progress4_.place(x=i,y=j)
		global eventr
		eventr=""
		proges3(eventr)
		proges2(eventr)
		proges(eventr)
		proges1(eventr)
		
		skill__img=PhotoImage(master=c,file="SKILLS-AND-EXPERTIZE.png")
		skill_im=c.create_image(245,480,image=skill__img)
		skil=Image.open("key-skills.png")
		skil=skil.resize((44,44),Image.ANTIALIAS)
		skil__=ImageTk.PhotoImage(skil,master=c)
		skil_1=c.create_image(75,475,image=skil__)
		
		  
		skill_1=c.create_text(144,530,text=Skill_1_tx.get(),width=230,font=("Segoe Print",12,"bold"))
		
		skill_2=c.create_text(144,565,text=Skill_2_tx.get(),width=230,font=("Segoe Print",12,"bold"))
		
		
		skill_3=c.create_text(144,610,text=Skill_3_tx.get(),width=230,font=("Segoe Print",12,"bold"))
		
		skill_4=c.create_text(144,650,text=Skill_4_tx.get(),width=230,font=("Segoe Print",12,"bold"))

		resume_f__.mainloop()
		#root.configure()
		#main()
	def final_resume__(event):		

		from tkinter import Text, Tk
		from tkinter.ttk import Progressbar
		#mainpage_.destroy()

		import tkinter.ttk as ttk
		global resume_f__
		#root.destroy()
		resume_f__= Tk()
		resume_f__.config(bg="#FFFFFF")
		resume_f__.title("CV (Resume)")
		resume_f__.iconbitmap("job.ico")
		resume_f__.resizable(False,False)
		resume_f__.geometry("795x680")
		#resume_.wm_attributes("-alpha",0.7)
		#r=Scale(resume_,from_=1,to=100000,orient=HORIZONTAL,bg="BLUE",fg="red")
		#r.pack()
		Name_tx=StringVar()
		Adress_tx=StringVar()
		Number_tx=StringVar()
		Email_tx=StringVar()
		Facebook_tx=StringVar()
		Twitter_tx=StringVar()
		Linkedin_tx=StringVar()
		Profile_tx=StringVar()
		Work1_From_tx=StringVar()
		Work1_To_tx=StringVar()
		Work1_Post_tx=StringVar()
		Work1_City_tx=StringVar()
		Work1_CompanyName_tx=StringVar()
		Work1_CompanyDesc_tx=StringVar()
		Work2_From_tx=StringVar()
		Work2_To_tx=StringVar()
		Work2_Post_tx=StringVar()
		Work2_City_tx=StringVar()
		Work2_CompanyName_tx=StringVar()

		Work2_CompanyDesc_tx=StringVar()
		Education1_From_tx=StringVar()
		Education1_To_tx=StringVar()
		Education1_Institute_tx=StringVar()
		Education1_City_tx=StringVar()
		Education1_Qualifications_tx=StringVar()
		Education2_From_tx=StringVar()
		Education2_To_tx=StringVar()
		Education2_Institute_tx=StringVar()
		Education2_City_tx=StringVar()
		Education2_Qualifications_tx=StringVar()
		Skill_1_tx=StringVar()
		Skill_2_tx=StringVar()
		Skill_3_tx=StringVar()
		Skill_4_tx=StringVar()
		lvl_1_tx=IntVar()
		lvl_2_tx=IntVar()
		lvl_3_tx=IntVar()
		lvl_4_tx=IntVar()
		#centr_=StringVar()
		conn=sqlite3.connect("resum.db")
		
		c=conn.cursor()
		c.execute("SELECT * FROM Resume3")
		dr=c.fetchall()
		#idel)
		
		#type(idel))


		for i in dr:
			#)
			#type(i[0]))

			#)
			if int(i[0])==ide:
				Name_tx.set(i[1])
				Adress_tx.set(i[2])
				Number_tx.set(i[3])

				Email_tx.set(i[4])
				Facebook_tx.set(i[5])
				Twitter_tx.set(i[6])
				Linkedin_tx.set(i[7])
				Profile_tx.set(i[8]) 
				Work1_From_tx.set(i[9])
				Work1_To_tx.set(i[10])
				Work1_Post_tx.set(i[11])
				Work1_City_tx.set(i[12])
				Work1_CompanyName_tx.set(i[13])
				Work1_CompanyDesc_tx.set(i[14])
				Work2_From_tx.set(i[15])
				Work2_To_tx.set(i[16])
				Work2_Post_tx.set(i[17])
				Work2_City_tx.set(i[18])
				Work2_CompanyName_tx.set(i[19])

				Work2_CompanyDesc_tx.set(i[20])
				Education1_From_tx.set(i[21])
				Education1_To_tx.set(i[22])
				Education1_Institute_tx.set(i[23])
				Education1_City_tx.set(i[24])
				Education1_Qualifications_tx.set(i[25])
				Education2_From_tx.set(i[26])
				Education2_To_tx.set(i[27])
				Education2_Institute_tx.set(i[28])
				Education2_City_tx.set(i[29])
				Education2_Qualifications_tx.set(i[30])
				Skill_1_tx.set(i[32])

				Skill_2_tx.set(i[33])
				Skill_3_tx.set(i[33])
				Skill_4_tx.set(i[34])
				lvl_1_tx.set(i[35])
				lvl_2_tx.set(i[36])
				lvl_3_tx.set(i[37])
				lvl_4_tx.set(i[38])
				#i[39])

				centr=i[39]
				#type(centr))
				
		#dr)
		conn.commit()
		conn.close()
		
		def progrs(event):
			progress['value']=50
		import os
				
		global bgm
		global img
		global img1
		l=Label(resume_f__,bg="white")
		#global c
		c=Canvas(l,width=600,height=1200,bd=0,bg="white",highlightthickness=0)
		#img1=PhotoImage(file="bgmp.png")
		img1=Image.open("back10.jpg")
		img=PhotoImage(master=c,file="Profile.png")

		img1=img1.resize((606,742),Image.ANTIALIAS)
		img3_=ImageTk.PhotoImage(img1,master=c)
		
		d1=c.create_image(320,310,image=img3_)
		d=c.create_image(150,30,image=img)

		c.pack()
		
		l.pack()
		l.place(x=220,y=0)
		
		global c1
		l1=Label(resume_f__)
		c1=Canvas(l1,width=250,height=1700,bd=0,highlightthickness=0)
		img_=PhotoImage(file="NAME21.png",master=c1)
		img2=Image.open("back8.jpg")
		submit_=PhotoImage(file="Submit__1.png",master=c1)
		submt_=c.create_image(900,100,image=submit_)
		
		img2=img2.resize((340,1000),Image.ANTIALIAS)
		img1_=ImageTk.PhotoImage(img2,master=c1)
		d1=c1.create_image(80,320,image=img1_)
		
		#img21=Image.open("bgm1.jpg")
		
		#3img21=img21.resize((300,700),Image.ANTIALIAS)
		#img11_=ImageTk.PhotoImage(img21,master=c1)
		#)
		#d11=c1.create_image(110,700,image=img11_)
		

		d2=c1.create_image(75,294,image=img_)
		
		c1.pack()
		#c1.place(x=0,y=0)
		l1.pack()
		l1.place(x=0,y=0)
		
		global n
		n="bg3.png"
		mag=Image.open(n)
		global frame1
		mag=mag.resize((110,110),Image.ANTIALIAS)
		mag1=ImageTk.PhotoImage(mag,master=c1)
		frame1=c1.create_image(90,70,image=mag1)
		#frame1.place(x=10,y=10)
		'''
		m="add-user.png"
		mag4=Image.open(m)
		mag4=mag4.resize((30,30),Image.ANTIALIAS)
		mag5=ImageTk.PhotoImage(mag4,master=c1)
		frame2=c1.create_image(170,110,image=mag5)
		c1.tag_bind(frame2,'<ButtonPress-1>',photo)
		'''
		#global centr
		Info_=PhotoImage(master=c1,file="INFO.png")
		Info=c1.create_image(92,254,image=Info_)
		conct=Image.open("user.png")
		conct=conct.resize((30,30),Image.ANTIALIAS)
		conct__=ImageTk.PhotoImage(conct,master=c1)
		
		conct_=c1.create_image(35,290,image=conct__)
		##centr)
		conn=sqlite3.connect("resum.db")
		
		cur=conn.cursor()
		cur.execute("SELECT * FROM Resume3")
		dr=cur.fetchall()
		

		global centr_
		for i in dr:
			#)
			#type(idel))
			if int(i[0])==ide:
				#type(i[0]))
				centr_=i[39]
				#centr_)
				break
		#centr_)
		rot3__=Image.open(centr_)
		
		rot3__=rot3__.resize((70,70),Image.ANTIALIAS)
		rot1__=ImageTk.PhotoImage(rot3__,master=c1)
		frame1=c1.create_image(90,70,image=rot1__)
			
		
		adres=Image.open("map.png")
		adres=adres.resize((30,30),Image.ANTIALIAS)
		adres_=ImageTk.PhotoImage(adres,master=c1)
		addres=c1.create_image(35,332,image=adres_)
		adress_img=PhotoImage(master=c1,file="Addressw.png")
		adress_w=c1.create_image(84,332,image=adress_img)


		


		phone=Image.open("telephone.png")
		phone=phone.resize((30,30),Image.ANTIALIAS)
		phone_=ImageTk.PhotoImage(phone,master=c1)
		phone_img=PhotoImage(master=c1,file="Phonew.png")
		phne_w=c1.create_image(75,373,image=phone_img)
		phoone=c1.create_image(35,368,image=phone_)
			


		Email1=Image.open("gmail.png")
		Email1=Email1.resize((30,30),Image.ANTIALIAS)
		Email_=ImageTk.PhotoImage(Email1,master=c1)
		
		Email_img=PhotoImage(master=c1,file="Emailw.png")
		Emai_w=c1.create_image(75,412,image=Email_img)
		Emaill=c1.create_image(35,412,image=Email_)
		#reds=c1.create_line(0,226,296,226,width=2)
		#reds1=c1.create_line(0,259,296,259,width=2)

	 
		
		social_=PhotoImage(master=c1,file="SOCIAL.png")
		Social=c1.create_image(95,480,image=social_)
		
		#reds=c1.create_line(0,459,296,459,width=2)
		#reds1=c1.create_line(0,494,296,494,width=2)
	 	
			

		
		fb=Image.open("facebook.png")
		fb=fb.resize((30,30),Image.ANTIALIAS)
		fb_=ImageTk.PhotoImage(fb,master=c1)
		facbk=c1.create_image(35,520,image=fb_)
		fb_img=PhotoImage(master=c1,file="Facebookw.png")
		fb_w=c1.create_image(90,520,image=fb_img)
	 
		
	 	
		
		twt=Image.open("twitter_.png")
		twt=twt.resize((30,30),Image.ANTIALIAS)
		twt_=ImageTk.PhotoImage(twt,master=c1)

		twt_img=PhotoImage(master=c1,file="Twitter.png")
		twt_w=c1.create_image(85,570,image=twt_img)
		twitwr=c1.create_image(35,570,image=twt_)


	 	
		lnk=Image.open("linkedin_.png")
		lnk=lnk.resize((30,30),Image.ANTIALIAS)
		lnk_=ImageTk.PhotoImage(lnk,master=c1)

		lnk_img=PhotoImage(master=c1,file="Linkedin.png")
		lnk_w=c1.create_image(85,620,image=lnk_img)
		lnkdin=c1.create_image(35,620,image=lnk_)
		profe=Image.open("user.png")
		profe=profe.resize((44,44),Image.ANTIALIAS)
		profe__=ImageTk.PhotoImage(profe,master=c1)
		profe_=c.create_image(75,30,image=profe__)
	 	
		
		wrke__img=PhotoImage(master=c,file="WORK-EXPERIENCE.png")
		wrke_im=c.create_image(210,140,image=wrke__img)
		wrke=Image.open("edit.png")
		wrke=wrke.resize((44,44),Image.ANTIALIAS)
		wrke__=ImageTk.PhotoImage(wrke,master=c)
		wrke_1=c.create_image(75,140,image=wrke__)
	 
		educ__img=PhotoImage(master=c,file="EDUCATION.png")
		educ_im=c.create_image(185,320,image=educ__img)
		educ=Image.open("graduation-hat.png")
		educ=educ.resize((44,44),Image.ANTIALIAS)
		educ__=ImageTk.PhotoImage(educ,master=c)
		educ_1=c.create_image(75,320,image=educ__)
		

		education1_num=c.create_text(110,345,text="1.",fill="Black",font=("comic sans ms",12))
		education1_from=c.create_text(144,355,text=Education1_From_tx.get(),fill="black",font=("comic sans ms",11))
		education1_to=c.create_text(198,355,fill="Black",text=Education1_To_tx.get(),font=("comic sans ms",11))
		education1_city=c.create_text(167,376,text=Education1_City_tx.get(),fill="Black",font=("comic sans ms",10))	
		education1_inst=c.create_text(290,340,text=Education1_Institute_tx.get(),width=200,justify=LEFT,anchor=NW ,fill="Black",font=("Segoe Print",12,"bold"))	
		education1_qual=c.create_text(290,360,text=Education1_Qualifications_tx.get(),fill="Black",width=200,justify=LEFT,anchor=NW ,font=("Segoe Print",10))
		
		work1_num=c.create_text(110,182,text="1.",fill="Black",font=("comic sans ms",12))
		work1_year_from=c.create_text(144,192,text=Work1_From_tx.get(),fill="Black",font=("comic sans ms",11))
		work1_year_to=c.create_text(198,192,text=Work1_To_tx.get(),fill="Black",font=("comic sans ms",11))
		work1_city=c.create_text(167,208,text=Work1_City_tx.get(),fill="Black",font=("comic sans ms",10))
		work1_position=c.create_text(290,160,text=Work1_Post_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("Segoe Print",12,"bold"))
		work1_company=c.create_text(290,180,text=Work1_CompanyName_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("comic sans ms",10))
		work1_desc=c.create_text(290,200,text=Work1_CompanyDesc_tx.get(),fill="Black",width=290,justify=LEFT,anchor=NW ,font=("comic sans ms",10))

		education2_num=c.create_text(110,410,text="2.",fill="Black",font=("comic sans ms",11))
		education2_from=c.create_text(144,420,fill="Black",text=Education2_From_tx.get(),font=("comic sans ms",11))
		education2_to=c.create_text(198,420,text=Education2_To_tx.get(),fill="Black",font=("comic sans ms",12))
		education2_city=c.create_text(167,438,text=Education2_City_tx.get(),fill="Black",font=("comic sans ms",10))
		education2_inst=c.create_text(290,400,fill="Black",text=Education2_Institute_tx.get(),width=200,justify=LEFT,anchor=NW ,font=("Segoe Print",12,"bold"))
		education2_qual=c.create_text(290,420,text=Education2_Qualifications_tx.get(),fill="Black",width=200,justify=LEFT,anchor=NW ,font=("comic sans ms",10))
		

		work2_num=c.create_text(110,242,text="2.",fill="Black",font=("comic sans ms",11))
		work2_year_from=c.create_text(144,252,text=Work2_From_tx.get(),fill="Black",font=("comic sans ms",11))
		work2_year_to=c.create_text(198,252,text=Work2_To_tx.get(),fill="Black",font=("comic sans ms", 12))
		work2_city=c.create_text(167,272,text=Work2_City_tx.get(),fill="Black",font=("comic sans ms", 10))
		work2_position=c.create_text(290,230,text=Work2_Post_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("Segoe Print",12,"bold"))
		work2_company=c.create_text(290,250,text=Work2_CompanyName_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("comic sans ms",10))
		work2_desc=c.create_text(290,270,text=Work2_CompanyDesc_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("comic sans ms",10))
		t=205
		profile_t=c.create_text(120,46,fill="Black",text=Profile_tx.get(),width=400,justify=LEFT,anchor=NW ,font=("Segoe Print",12,"bold"))
		ty=30
		ty_single=17
				
		name1=c1.create_text(123,160,text=Name_tx.get(),width=220,font=("Segoe Script", 18," bold"))
		lnk_t=c1.create_text(64,625,text=Linkedin_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		twt_t=c1.create_text(64,575,text=Twitter_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		phone_t=c1.create_text(64,377,text=Number_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		name_=c1.create_text(64,297,text=Name_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		adres_t=c1.create_text(64,335,text=Adress_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		Email_t=c1.create_text(64,419,text=Email_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		fb_t=c1.create_text(64,527,text=Facebook_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		c.create_line(165,241,176,241,width=3)
		c.create_line(165,181,176,181,width=3)
		c.create_line(168,412,179,412,width=3)
		c.create_line(168,347,179,347,width=3)
		def proges(event):
			import tkinter.ttk as ttk
			from tkinter import ttk
			i=440
			j=515
			e_=ttk.Style(resume_f__)
			e_.theme_use("default")
			e_.configure("#8AC91D_.Horizontal.TProgressbar",bordercolor="#8AC91D",lightcolor="#8AC91D",darkcolor="#8AC91D",background="#8AC91D")
			progress1_=Progressbar(resume_f__,style="#8AC91D_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress1_["value"]=int(lvl_1_tx.get())
			progress1_.pack()
			progress1_.place(x=i,y=j)
		def proges1(event):
			import tkinter.ttk as ttk
			i=440
			j=550
			e1_=ttk.Style(resume_f__)
			e1_.theme_use("default")
			e1_.configure("red1_.Horizontal.TProgressbar",bordercolor="#FB9A00",lightcolor="#FB9A00",darkcolor="#FB9A00",background="#FB9A00")
			progress2_=Progressbar(resume_f__,style="red1_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress2_["value"]=int(lvl_2_tx.get())
			progress2_.pack()
			progress2_.place(x=i,y=j)
		def proges2(event):
			import tkinter.ttk as ttk
			i=440
			j=590
			e2_=ttk.Style(resume_f__)
			e2_.theme_use("default")
			e2_.configure("red2_.Horizontal.TProgressbar",bordercolor="#1FB4E7",lightcolor="#1FB4E7",darkcolor="#1FB4E7",background="#1FB4E7")
			progress3_=Progressbar(resume_f__,style="red2_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress3_["value"]=int(lvl_3_tx.get())
			progress3_.pack()
			progress3_.place(x=i,y=j)
		def proges3(event):
			import tkinter.ttk as ttk
			i=440
			j=630
			e3_=ttk.Style(resume_f__)
			e3_.theme_use("default")
			e3_.configure("red3_.Horizontal.TProgressbar",bordercolor="red",lightcolor="red",darkcolor="red",background="red")
			progress4_=Progressbar(resume_f__,style="red3_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress4_["value"]=int(lvl_4_tx.get())
			progress4_.pack()
			progress4_.place(x=i,y=j)
		global eventr
		eventr=""
		proges3(eventr)
		proges2(eventr)
		proges(eventr)
		proges1(eventr)
		
		skill__img=PhotoImage(master=c,file="SKILLS-AND-EXPERTIZE.png")
		skill_im=c.create_image(245,480,image=skill__img)
		skil=Image.open("key-skills.png")
		skil=skil.resize((44,44),Image.ANTIALIAS)
		skil__=ImageTk.PhotoImage(skil,master=c)
		skil_1=c.create_image(75,475,image=skil__)
		
		  
		skill_1=c.create_text(144,530,text=Skill_1_tx.get(),width=230,font=("Segoe Print",12,"bold"))
		
		skill_2=c.create_text(144,565,text=Skill_2_tx.get(),width=230,font=("Segoe Print",12,"bold"))
		
		
		skill_3=c.create_text(144,610,text=Skill_3_tx.get(),width=230,font=("Segoe Print",12,"bold"))
		
		skill_4=c.create_text(144,650,text=Skill_4_tx.get(),width=230,font=("Segoe Print",12,"bold"))

		resume_f__.mainloop()
		#root.configure()
		#main()

	def main():
		sign_in.destroy()
		global root
		import tkinter.ttk as ttk
		root = Tk()
		root.config(bg="skyblue")
		root.iconbitmap("job.ico")
		
		root.title("Company List")
		root.geometry("715x700")
		root.resizable(False,False)
		global tree
		global Style_
		Style_=ttk.Style(root)
		#Style.configure("mystyle.Treeview",bd=2,font=("arial",12))
		Style_.configure("mystyle_.Treeview",bd=2,rowheight=40,font=("Segoe Script",10))
		
		width = 800
		height = 700
		
		TableMargin = Frame(root, width=870,bg="skyblue")
		TableMargin.pack()
		TableMargin.place(x=-15,y=130)
		scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
		scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
		
		#scrollbarx.pack(side=BOTTOM, fill=X)
		tree = ttk.Treeview(TableMargin, style="mystyle_.Treeview",columns=("Company ID", "Company Name", "Vacancy Status", "Contact Number"), height=13, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
		scrollbary.config(command=tree.yview)
		scrollbary.pack(side=RIGHT, fill=Y)
		scrollbarx.config(command=tree.xview)
		scrollbarx.pack(side=BOTTOM, fill=X)

		tree.heading('#0', text="pic", anchor=W)
		tree.heading('Company ID', text="ID", anchor=W)
		tree.heading('Company Name', text="C_Name", anchor=W)
	
		tree.heading('Vacancy Status', text="Vacancy Status", anchor=W)
		
		tree.heading('Contact Number', text="Contact Number", anchor=W)

		
		tree.column('#0', stretch=NO, minwidth=0, width=70)
		tree.column('#1', stretch=NO, minwidth=30, width=65)
		tree.column('#2', stretch=NO, minwidth=70, width=190)
		tree.column('#3', stretch=NO, minwidth=70, width=190)
		tree.column('#4', stretch=NO, minwidth=90, width=190)
		#tree.column('#5', stretch=NO, minwidth=90, width=200)
		
	

		tree.pack()
		def f(event):
			sc=tree.identify("item",event.x,event.y)
			#tree.item(sc))
		

		tree.bind('<Double-Button-1>',f)

		conn=sqlite3.connect("jobs.db")
		c=conn.cursor()
		c.execute("SELECT *,oid FROM Company ")
		ro=c.fetchall()
		#frt=PhotoImage(file="bg12.png")
		fr=Image.open("ach.png")
		fr=fr.resize((28,25),Image.ANTIALIAS)
		frt=ImageTk.PhotoImage(fr)
		#ro)
		for i in ro:
			tree.insert('','end',text="",image=frt,values=(i[0],i[1],i[3],i[4]),tags=('aj',))
		conn.commit()
		conn.close()
	
		im=PhotoImage(file="List-Of-Companies.png")
		im1=PhotoImage(file="Edit-Your-Data.png")
		frame2=LabelFrame(root)

		frame1=Label(frame2,image=im,bg="yellow")
		frame1.pack()
		frame2.pack()
		
		frame2.place(x=8,y=4)
		#button7=Button(root,text="create your resume",command=resume)
		#button7.pack()
		#button7.place(x=300,y=50)
		#button8=Button(root,text="your resume",command=final_resume)
		#button8.pack()
		#button8.place(x=400,y=100)
		
		frame10=Label(root,highlightthickness=0,highlightbackground="skyblue",borderwidth=0)
		frame10.pack()
		frame10.place(x=450,y=0)
		conct2=Image.open("cv (2).png")
		conct2=conct2.resize((40,40),Image.ANTIALIAS)
		show=ImageTk.PhotoImage(conct2)
		conct3=Image.open("edit (1).png")
		conct3=conct3.resize((40,40),Image.ANTIALIAS)
		dit=ImageTk.PhotoImage(conct3)
		conct4=Image.open("cv (3).png")
		conct4=conct4.resize((40,40),Image.ANTIALIAS)
		crte_resum=ImageTk.PhotoImage(conct4)
		
		cn=Canvas(frame10,width=300,height=100,bg="skyblue",highlightthickness=0,highlightbackground="skyblue")
		create14=cn.create_image(50,45,image=show)
		create16=cn.create_image(180,45,image=dit)
		create19=cn.create_image(120,45,image=crte_resum)
		
		cn.pack()



		cn.tag_bind(create19,'<Button-1>',resume)
		cn.tag_bind(create14,'<Button-1>',final_resume__)
		cn.tag_bind(create16,'<Button-1>',Edit1)
		im8=PhotoImage(file="ID3.png")
		
		Com_id=Label(root,image=im8,bg="skyblue")
		Com_id.pack()
		Com_id.place(x=0,y=123,width=135)
		im4=PhotoImage(file="Vacancy-status.png")
		im3=PhotoImage(file="Company-name-.png")
		Com_name=Label(root,image=im3,bg="skyblue")
		Com_name.pack()
		Com_name.place(x=105,y=123,width=150)
		im4=PhotoImage(file="Vacancy-status.png")
		
		Com_stat=Label(root,image=im4,bg="skyblue")
		Com_stat.pack()
		Com_stat.place(x=254,y=123,width=250)
		
		im5=PhotoImage(file="Contact-number-.png")
		
		Com_num=Label(root,image=im5,bg="skyblue")
		Com_num.pack()
		Com_num.place(x=460,y=123,width=254)
		root.mainloop()

	def main_():
		#sign_in.destroy()
		global root_
		import tkinter.ttk as ttk
		root_ = Tk()
		root_.config(bg="skyblue")
		root_.iconbitmap("job.ico")
		
		root_.title("Company List")
		root_.geometry("715x700")
		root_.resizable(False,False)
		global tree
		global Style_
		Style_=ttk.Style(root_)
		#Style.configure("mystyle.Treeview",bd=2,font=("arial",12))
		Style_.configure("mystyle_.Treeview",bd=2,rowheight=40,font=("Segoe Script",10))
		
		width = 800
		height = 700
		
		TableMargin = Frame(root_, width=870,bg="skyblue")
		TableMargin.pack()
		TableMargin.place(x=-15,y=130)
		scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
		scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
		
		#scrollbarx.pack(side=BOTTOM, fill=X)
		tree = ttk.Treeview(TableMargin, style="mystyle_.Treeview",columns=("Company ID", "Company Name", "Vacancy Status", "Contact Number"), height=13, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
		scrollbary.config(command=tree.yview)
		scrollbary.pack(side=RIGHT, fill=Y)
		scrollbarx.config(command=tree.xview)
		scrollbarx.pack(side=BOTTOM, fill=X)

		tree.heading('#0', text="pic", anchor=W)
		tree.heading('Company ID', text="ID", anchor=W)
		tree.heading('Company Name', text="C_Name", anchor=W)
	
		tree.heading('Vacancy Status', text="Vacancy Status", anchor=W)
		
		tree.heading('Contact Number', text="Contact Number", anchor=W)

		
		tree.column('#0', stretch=NO, minwidth=0, width=70)
		tree.column('#1', stretch=NO, minwidth=30, width=65)
		tree.column('#2', stretch=NO, minwidth=70, width=190)
		tree.column('#3', stretch=NO, minwidth=70, width=190)
		tree.column('#4', stretch=NO, minwidth=90, width=190)
		#tree.column('#5', stretch=NO, minwidth=90, width=200)
		
	

		tree.pack()
		def f(event):
			sc=tree.identify("item",event.x,event.y)
			#tree.item(sc))
		

		tree.bind('<Double-Button-1>',f)

		conn=sqlite3.connect("jobs.db")
		c=conn.cursor()
		c.execute("SELECT *,oid FROM Company ")
		ro=c.fetchall()
		#frt=PhotoImage(file="bg12.png")
		fr=Image.open("ach.png")
		fr=fr.resize((28,25),Image.ANTIALIAS)
		frt=ImageTk.PhotoImage(fr)
		#ro)
		for i in ro:
			tree.insert('','end',text="",image=frt,values=(i[0],i[1],i[3],i[4]),tags=('aj',))
		conn.commit()
		conn.close()
	
		im=PhotoImage(file="List-Of-Companies.png")
		im1=PhotoImage(file="Edit-Your-Data.png")
		frame2=LabelFrame(root_)

		frame1=Label(frame2,image=im,bg="yellow")
		frame1.pack()
		frame2.pack()
		
		frame2.place(x=8,y=4)
		#button7=Button(root,text="create your resume",command=resume)
		#button7.pack()
		#button7.place(x=300,y=50)
		#button8=Button(root,text="your resume",command=final_resume)
		#button8.pack()
		#button8.place(x=400,y=100)
		
		frame10=Label(root_,highlightthickness=0,highlightbackground="skyblue",borderwidth=0)
		frame10.pack()
		frame10.place(x=450,y=0)
		conct2=Image.open("cv (2).png")
		conct2=conct2.resize((40,40),Image.ANTIALIAS)
		show=ImageTk.PhotoImage(conct2)
		conct3=Image.open("edit (1).png")
		conct3=conct3.resize((40,40),Image.ANTIALIAS)
		dit=ImageTk.PhotoImage(conct3)
		conct4=Image.open("cv (3).png")
		conct4=conct4.resize((40,40),Image.ANTIALIAS)
		crte_resum=ImageTk.PhotoImage(conct4)
		
		cn=Canvas(frame10,width=300,height=100,bg="skyblue",highlightthickness=0,highlightbackground="skyblue")
		create14=cn.create_image(50,45,image=show)
		create16=cn.create_image(180,45,image=dit)
		create19=cn.create_image(120,45,image=crte_resum)
		
		cn.pack()



		cn.tag_bind(create19,'<Button-1>',resume_1)
		cn.tag_bind(create14,'<Button-1>',final_resume_)
		cn.tag_bind(create16,'<Button-1>',Edit1)
		im8=PhotoImage(file="ID3.png")
		
		Com_id=Label(root_,image=im8,bg="skyblue")
		Com_id.pack()
		Com_id.place(x=0,y=123,width=135)
		im4=PhotoImage(file="Vacancy-status.png")
		im3=PhotoImage(file="Company-name-.png")
		Com_name=Label(root_,image=im3,bg="skyblue")
		Com_name.pack()
		Com_name.place(x=105,y=123,width=150)
		im4=PhotoImage(file="Vacancy-status.png")
		
		Com_stat=Label(root_,image=im4,bg="skyblue")
		Com_stat.pack()
		Com_stat.place(x=254,y=123,width=250)
		
		im5=PhotoImage(file="Contact-number-.png")
		
		Com_num=Label(root_,image=im5,bg="skyblue")
		Com_num.pack()
		Com_num.place(x=460,y=123,width=254)
		root.mainloop()
	
	def resum_data(event):
		
		'''
		global skill_2			global skill_3			global skill_4			global skill_1
		global name_			global adres_t			global phone_t			global fb_t
		global twt_t			global lnk_t
		global profile_t		global work1_year_from	global work1_desc     	global work2_desc		
		global work1_year_to	global work2_position	global profile_t		global work1_city
		global work1_position	global work2_company	global work1_company	global education1_from	
		global education1_to	global education2_from	global education2_to	global education1_city 
		global education2_city  global education2_qual  global education1_qual  global education2_inst	
		global education1_inst	global work2_year_from	global work2_year_to	global work2_city
		
		'''
		if ide!=None and name_.get("1.0",END)!=None and adres_t.get("1.0",END)!=None and phone_t.get("1.0",END)!=None and Email_t.get("1.0",END) !=None and fb_t.get("1.0",END)!=None and twt_t.get("1.0",END)!=None and lnk_t.get("1.0",END)!=None and profile_t.get("1.0",END)!=None and work1_year_from.get("1.0",END)!=None and work1_year_to.get("1.0",END)!=None and work1_position.get("1.0",END)!=None and work1_city.get("1.0",END)!=None and work1_company.get("1.0",END)!=None and work1_desc.get("1.0",END)!=None and work2_year_from.get("1.0",END)!=None and work2_year_to.get("1.0",END)!=None and work2_position.get("1.0",END)!=None and work2_city.get("1.0",END) !=None and work2_company.get("1.0",END) !=None and work2_desc.get("1.0",END)!=None and education1_from.get("1.0",END) !=None and education1_to.get("1.0",END)!=None and education1_inst.get("1.0",END)!=None and education1_city.get("1.0",END)!=None and education1_qual.get("1.0",END)!=None and education2_from.get("1.0",END) !=None and education2_to.get("1.0",END)!=None and education2_inst.get("1.0",END) !=None and education2_city.get("1.0",END)!=None and education2_qual.get("1.0",END) !=None and skill_1.get("1.0",END)!=None and skill_2.get("1.0",END)!=None and skill_3.get("1.0",END)!=None and skill_4.get("1.0",END)!=None and rt.get()!=None and rt1.get()!=None and rt2.get()!=None and rt3.get()!=None and len(centr)>3:

			messagebox.showinfo("Resume Successfully Created","Your Resume was created Successfully")	
			conn=sqlite3.connect("resum.db")
			c=conn.cursor()
			#centr)
			c.execute("""CREATE TABLE IF NOT EXISTS `Resume3` (Id varchar(30),Name varchar(30),Adress varchar(100),Number_ varchar(40),
				Email varchar(50),Facebook varchar(45),Twitter varchar(45),Linkedin varchar(45),Profile varchar(450),
				Work1_From varchar(30),Work1_To varchar(30),Work1_Post varchar(300),Work1_City varchar(300),
				Work1_CompanyName varchar(300),Work1_CompanyDesc varchar(300),Work2_From varchar(30),Work2_To varchar
				(30),Work2_Post varchar(300),Work2_City varchar(300),Work2_CompanyName varchar(300),Work2_CompanyDesc
				 varchar(300),Education1_From varchar(30),Education1_To varchar(30),Education1_Institute varchar(300),
				 Education1_City varchar(300),Education1_Qualifications varchar(300),Education2_From varchar(30),
				 Education2_To varchar(30),Education2_Institute varchar(300),Education2_City varchar(300),
				 Education2_Qualifications varchar(300),Skill_1 varchar(100),Skill_2 varchar(100),Skill_3 varchar(100),
				 Skill_4 varchar(100),levl_1 integer,levl_2 integer,levl_3 integer,
				 levl_4 integer,image varchar(200)  )""")
			#c.execute("ALTER TABLE Job_Aspirants ADD GenderEXT")
			c.execute("""INSERT INTO 'Resume3' VALUES(:Id,:Name,:Adress,:Number_,
				:Email ,:Facebook ,:Twitter,:Linkedin,:Profile ,
				 :Work1_From,:Work1_To,:Work1_Post,:Work1_City ,
				 :Work1_CompanyName,:Work1_CompanyDesc ,:Work2_From ,:Work2_To,:Work2_Post ,:Work2_City ,:Work2_CompanyName ,
				 :Work2_CompanyDesc,:Education1_From  ,:Education1_To  ,:Education1_Institute  ,
				 :Education1_City  ,:Education1_Qualifications  ,:Education2_From  ,
				 :Education2_To  ,:Education2_Institute  ,:Education2_City  ,
				 :Education2_Qualifications  ,:Skill_1  ,:Skill_2  ,:Skill_3  ,
				 :Skill_4,:lvl_1,:lvl_2,:lvl_3,:lvl_4,:img)""",{"Id":ide,"Name":name_.get("1.0",END),"Adress":adres_t.get("1.0",END),
				 "Number_":phone_t.get("1.0",END),
				 "Email":Email_t.get("1.0",END) ,"Facebook":fb_t.get("1.0",END) ,"Twitter":twt_t.get("1.0",END),
				 "Linkedin":lnk_t.get("1.0",END),
				 "Profile":profile_t.get("1.0",END) ,"Work1_From":work1_year_from.get("1.0",END),
				 "Work1_To":work1_year_to.get("1.0",END),"Work1_Post":work1_position.get("1.0",END),"Work1_City":work1_city.get("1.0",END) 
				 ,"Work1_CompanyName":work1_company.get("1.0",END),"Work1_CompanyDesc":work1_desc.get("1.0",END) ,
				 "Work2_From":work2_year_from.get("1.0",END) ,"Work2_To":work2_year_to.get("1.0",END),
				 "Work2_Post":work2_position.get("1.0",END) ,"Work2_City":work2_city.get("1.0",END) ,
				 "Work2_CompanyName":work2_company.get("1.0",END) ,"Work2_CompanyDesc":work2_desc.get("1.0",END),
				 "Education1_From":education1_from.get("1.0",END)  ,"Education1_To":education1_to.get("1.0",END)
				 ,"Education1_Institute":education1_inst.get("1.0",END), "Education1_City":education1_city.get
				 ("1.0",END),"Education1_Qualifications":education1_qual.get("1.0",END)  ,"Education2_From":
				 education2_from.get("1.0",END) ,"Education2_To":education2_to.get("1.0",END)  ,"Education2_Institute"
				 :education2_inst.get("1.0",END)  ,"Education2_City":education2_city.get("1.0",END)  ,
				 "Education2_Qualifications":education2_qual.get("1.0",END) ,"Skill_1":skill_1.get("1.0",END)  ,
				 "Skill_2":skill_2.get("1.0",END)  ,"Skill_3":skill_3.get("1.0",END),"Skill_4":skill_4.get("1.0",END),
				 "lvl_1":rt.get(),"lvl_2":rt1.get(),"lvl_3":rt2.get(),"lvl_4":rt3.get(),"img":centr})
			
			c.execute("SELECT * FROM Resume3")
			
			dr=c.fetchall()
			conn.commit()
			conn.close()
			resume_.destroy()
			#main.destroy()
			main_()
		
		else:
			messagebox.showerror("Invalid Input","All fields are Required to be filled")
			resume("")

	def resum_data_(event):
		
		'''
		global skill_2			global skill_3			global skill_4			global skill_1
		global name_			global adres_t			global phone_t			global fb_t
		global twt_t			global lnk_t
		global profile_t		global work1_year_from	global work1_desc     	global work2_desc		
		global work1_year_to	global work2_position	global profile_t		global work1_city
		global work1_position	global work2_company	global work1_company	global education1_from	
		global education1_to	global education2_from	global education2_to	global education1_city 
		global education2_city  global education2_qual  global education1_qual  global education2_inst	
		global education1_inst	global work2_year_from	global work2_year_to	global work2_city
		
		'''
		if ide!=None and name_.get("1.0",END)!=None and adres_t.get("1.0",END)!=None and phone_t.get("1.0",END)!=None and Email_t.get("1.0",END) !=None and fb_t.get("1.0",END)!=None and twt_t.get("1.0",END)!=None and lnk_t.get("1.0",END)!=None and profile_t.get("1.0",END)!=None and work1_year_from.get("1.0",END)!=None and work1_year_to.get("1.0",END)!=None and work1_position.get("1.0",END)!=None and work1_city.get("1.0",END)!=None and work1_company.get("1.0",END)!=None and work1_desc.get("1.0",END)!=None and work2_year_from.get("1.0",END)!=None and work2_year_to.get("1.0",END)!=None and work2_position.get("1.0",END)!=None and work2_city.get("1.0",END) !=None and work2_company.get("1.0",END) !=None and work2_desc.get("1.0",END)!=None and education1_from.get("1.0",END) !=None and education1_to.get("1.0",END)!=None and education1_inst.get("1.0",END)!=None and education1_city.get("1.0",END)!=None and education1_qual.get("1.0",END)!=None and education2_from.get("1.0",END) !=None and education2_to.get("1.0",END)!=None and education2_inst.get("1.0",END) !=None and education2_city.get("1.0",END)!=None and education2_qual.get("1.0",END) !=None and skill_1.get("1.0",END)!=None and skill_2.get("1.0",END)!=None and skill_3.get("1.0",END)!=None and skill_4.get("1.0",END)!=None and rt.get()!=None and rt1.get()!=None and rt2.get()!=None and rt3.get()!=None and len(centr)>3:

			messagebox.showinfo("Resume Successfully Created","Your Resume was created Successfully")	
			conn=sqlite3.connect("resum.db")
			c=conn.cursor()
			#centr)
			c.execute("""CREATE TABLE IF NOT EXISTS `Resume3` (Id varchar(30),Name varchar(30),Adress varchar(100),Number_ varchar(40),
				Email varchar(50),Facebook varchar(45),Twitter varchar(45),Linkedin varchar(45),Profile varchar(450),
				Work1_From varchar(30),Work1_To varchar(30),Work1_Post varchar(300),Work1_City varchar(300),
				Work1_CompanyName varchar(300),Work1_CompanyDesc varchar(300),Work2_From varchar(30),Work2_To varchar
				(30),Work2_Post varchar(300),Work2_City varchar(300),Work2_CompanyName varchar(300),Work2_CompanyDesc
				 varchar(300),Education1_From varchar(30),Education1_To varchar(30),Education1_Institute varchar(300),
				 Education1_City varchar(300),Education1_Qualifications varchar(300),Education2_From varchar(30),
				 Education2_To varchar(30),Education2_Institute varchar(300),Education2_City varchar(300),
				 Education2_Qualifications varchar(300),Skill_1 varchar(100),Skill_2 varchar(100),Skill_3 varchar(100),
				 Skill_4 varchar(100),levl_1 integer,levl_2 integer,levl_3 integer,
				 levl_4 integer,image varchar(200)  )""")
			#c.execute("ALTER TABLE Job_Aspirants ADD GenderEXT")
			c.execute("""INSERT INTO 'Resume3' VALUES(:Id,:Name,:Adress,:Number_,
				:Email ,:Facebook ,:Twitter,:Linkedin,:Profile ,
				 :Work1_From,:Work1_To,:Work1_Post,:Work1_City ,
				 :Work1_CompanyName,:Work1_CompanyDesc ,:Work2_From ,:Work2_To,:Work2_Post ,:Work2_City ,:Work2_CompanyName ,
				 :Work2_CompanyDesc,:Education1_From  ,:Education1_To  ,:Education1_Institute  ,
				 :Education1_City  ,:Education1_Qualifications  ,:Education2_From  ,
				 :Education2_To  ,:Education2_Institute  ,:Education2_City  ,
				 :Education2_Qualifications  ,:Skill_1  ,:Skill_2  ,:Skill_3  ,
				 :Skill_4,:lvl_1,:lvl_2,:lvl_3,:lvl_4,:img)""",{"Id":ide,"Name":name_.get("1.0",END),"Adress":adres_t.get("1.0",END),
				 "Number_":phone_t.get("1.0",END),
				 "Email":Email_t.get("1.0",END) ,"Facebook":fb_t.get("1.0",END) ,"Twitter":twt_t.get("1.0",END),
				 "Linkedin":lnk_t.get("1.0",END),
				 "Profile":profile_t.get("1.0",END) ,"Work1_From":work1_year_from.get("1.0",END),
				 "Work1_To":work1_year_to.get("1.0",END),"Work1_Post":work1_position.get("1.0",END),"Work1_City":work1_city.get("1.0",END) 
				 ,"Work1_CompanyName":work1_company.get("1.0",END),"Work1_CompanyDesc":work1_desc.get("1.0",END) ,
				 "Work2_From":work2_year_from.get("1.0",END) ,"Work2_To":work2_year_to.get("1.0",END),
				 "Work2_Post":work2_position.get("1.0",END) ,"Work2_City":work2_city.get("1.0",END) ,
				 "Work2_CompanyName":work2_company.get("1.0",END) ,"Work2_CompanyDesc":work2_desc.get("1.0",END),
				 "Education1_From":education1_from.get("1.0",END)  ,"Education1_To":education1_to.get("1.0",END)
				 ,"Education1_Institute":education1_inst.get("1.0",END), "Education1_City":education1_city.get
				 ("1.0",END),"Education1_Qualifications":education1_qual.get("1.0",END)  ,"Education2_From":
				 education2_from.get("1.0",END) ,"Education2_To":education2_to.get("1.0",END)  ,"Education2_Institute"
				 :education2_inst.get("1.0",END)  ,"Education2_City":education2_city.get("1.0",END)  ,
				 "Education2_Qualifications":education2_qual.get("1.0",END) ,"Skill_1":skill_1.get("1.0",END)  ,
				 "Skill_2":skill_2.get("1.0",END)  ,"Skill_3":skill_3.get("1.0",END),"Skill_4":skill_4.get("1.0",END),
				 "lvl_1":rt.get(),"lvl_2":rt1.get(),"lvl_3":rt2.get(),"lvl_4":rt3.get(),"img":centr})
			
			c.execute("SELECT * FROM Resume3")
			
			dr=c.fetchall()
			conn.commit()
			conn.close()
			resume_.destroy()
			#main.destroy()
			main_()
		
		else:
			messagebox.showerror("Invalid Input","All fields are Required to be filled")
			resume("")
	
	def resume(event):
		from tkinter import Text, Tk
		from tkinter.ttk import Progressbar
		

		root.destroy()
		#mainpage_.destroy()
		global skill_2
		global skill_3
		
		global skill_4
		global skill_1
		global name_
		global adres_t
		global phone_t
		global fb_t
		global twt_t
		global lnk_t
		global profile_t		
		global work1_city
		global work1_desc
		global work2_year_from
		global work2_year_to
		global work2_city
		global work2_desc
		global profile_t
		global work1_year_from
		global work1_year_to
		global work2_position
		global work1_position
		global work2_company
		global work1_company
		global education1_from
		global education1_to
		global education2_from
		global education2_to
		global education1_city
		global education2_city
		global education2_qual
		global education1_qual
		global education2_inst
		global education1_inst


		global centr
		centr=""	
		global resume_
		import tkinter.ttk as ttk
		resume_ = Tk()
		resume_.config(bg="#FFFFFF")
		resume_.title("Create CV")
		resume_.geometry("795x700")
		resume_.iconbitmap("job.ico")
		resume_.resizable(False,False)
		resume_.config(bg="white")
		
		#resume_.wm_attributes("-alpha",0.7)
		#r=Scale(resume_,from_=1,to=100000,orient=HORIZONTAL,bg="BLUE",fg="red")
		#r.pack()
		def progrs(event):
			progress['value']=50
		def photo(event):
			import os
			global centr
			
			resume_.filename=filedialog.askopenfilename(initialdir="Desktop/" ,title="Select a Photo",filetypes=(("All Files","*.*"),("PNG files","*.png"),("JPEG files","*.jpeg"),("JPG files","*.jpg")))
			n=resume_.filename
			#n)
			file_name = os.path.splitext(n)[0] 
			extension = os.path.splitext(n)[1] 
			#file_name)
			centr=str(ide)+extension
			
			rot3__=Image.open(n)
			global frame1_
			rot3__.save(centr,"")
			rot3_=Image.open(centr)
			
			rot3__=rot3__.resize((70,70),Image.ANTIALIAS)
			rot1_=ImageTk.PhotoImage(rot3__,master=c1)
			frame1_=c1.create_image(90,70,image=rot1_)
			#resume_.configure()	
			
		global bgm
		global img
		global img1
		l=Label(resume_)
		global c
		c=Canvas(l,width=600,height=1200,bd=0,bg="white",highlightthickness=0)
		#img1=PhotoImage(file="bgmp.png")
		img1=Image.open("back10.jpg")
		img=PhotoImage(master=c,file="Profile.png")

		img1=img1.resize((606,742),Image.ANTIALIAS)
		img3_=ImageTk.PhotoImage(img1,master=c)
		
		d1=c.create_image(320,320,image=img3_)
		
		d=c.create_image(150,30,image=img)

		c.pack()
		
		l.pack()
		l.place(x=220,y=0)
		
		global c1
		l1=Label(resume_,bg="white")
		c1=Canvas(l1,width=250,height=1000,bd=0,highlightthickness=0,highlightbackground="white")
		img2=Image.open("back8.jpg")
		submit_=PhotoImage(file="Submit__1.png",master=c1)
		submt_=c.create_image(900,100,image=submit_)
		
		img2=img2.resize((340,1000),Image.ANTIALIAS)
		img1_=ImageTk.PhotoImage(img2,master=c1)
		d1=c1.create_image(80,320,image=img1_)
		
		c1.pack()
		#c1.place(x=0,y=0)
		l1.pack()
		l1.place(x=0,y=0)
		
		global n
		n="bg3.png"
		mag=Image.open(n)
		global frame1
		mag=mag.resize((110,110),Image.ANTIALIAS)
		mag1=ImageTk.PhotoImage(mag,master=c1)
		frame1=c1.create_image(90,70,image=mag1)
		#frame1.place(x=10,y=10)

		m="add-user.png"
		mag4=Image.open(m)
		mag4=mag4.resize((30,30),Image.ANTIALIAS)
		mag5=ImageTk.PhotoImage(mag4,master=c1)
		frame2=c1.create_image(170,110,image=mag5)
		c1.tag_bind(frame2,'<ButtonPress-1>',photo)


		name1=c1.create_text(123,160,text="Employee\nname",font=("Segoe Print", 20," bold"))
		'''
		bluet1=Image.open("blue_.jpg")
		bluet1=bluet1.resize((314,38),Image.ANTIALIAS)
		bl__1=ImageTk.PhotoImage(bluet1)
		bt1_=c1.create_image(95,244,image=bl__1)'''
		Info_=PhotoImage(master=c1,file="INFO.png")
		Info=c1.create_image(90,244,image=Info_)
		conct=Image.open("user.png")
		conct=conct.resize((30,30),Image.ANTIALIAS)
		conct__=ImageTk.PhotoImage(conct,master=c1)
		conct_=c1.create_image(35,290,image=conct__)
		
		def name1_(event):


			name_.tag_add(SEL,"1.0",END)
			name_.mark_set(INSERT,"1.0")
			name_.see(INSERT)
			return "break"
		
		img_=PhotoImage(master=c1,file="NAME21.png")
		
		d2=c1.create_image(75,294,image=img_)
		
		name_=Text(resume_,height=0,width=17,bd=1,fg="black",font=("Segoe Script",8))
		name_.pack()
		name_.place(x=64,y=305)
		name_.insert(END,"Enter Name")

		name_.bind("<FocusIn>",name1_)
		


		adres=Image.open("map.png")
		adres=adres.resize((30,30),Image.ANTIALIAS)
		adres_=ImageTk.PhotoImage(adres,master=c1)
		addres=c1.create_image(35,332,image=adres_)
		adress_img=PhotoImage(master=c1,file="Addressw.png")
		adress_w=c1.create_image(84,332,image=adress_img)


		def address1(event):


			adres_t.tag_add(SEL,"1.0",END)
			adres_t.mark_set(INSERT,"1.0")
			adres_t.see(INSERT)
			return "break"
		
		adres_t=Text(resume_,height=0,width=17,bd=1,font=("Segoe Script",8))
		adres_t.pack()
		adres_t.place(x=64,y=343)
		adres_t.insert(END,"Enter Address")
		adres_t.bind("<FocusIn>",address1)	
		


		phone=Image.open("telephone.png")
		phone=phone.resize((30,30),Image.ANTIALIAS)
		phone_=ImageTk.PhotoImage(phone,master=c1)
		phone_img=PhotoImage(master=c1,file="Phonew.png")
		phne_w=c1.create_image(75,373,image=phone_img)
		phoone=c1.create_image(35,368,image=phone_)
		def phone1(event):
			phone_t.tag_add(SEL,"1.0",END)
			phone_t.mark_set(INSERT,"1.0")
			phone_t.see(INSERT)
			return "break"
		
		phone_t=Text(resume_,height=0,width=17,bd=1,font=("Segoe Script",8))
		phone_t.pack()
		phone_t.place(x=64,y=385)
		phone_t.insert(END,"enter phone number")
		phone_t.bind("<FocusIn>",phone1)	
			

		Email1=Image.open("gmail.png")
		Email1=Email1.resize((30,30),Image.ANTIALIAS)
		Email_=ImageTk.PhotoImage(Email1,master=c1)
		def email1(event):
			Email_t.tag_add(SEL,"1.0",END)
			Email_t.mark_set(INSERT,"1.0")
			Email_t.see(INSERT)
			return "break"
		
		Email_img=PhotoImage(master=c1,file="Emailw.png")
		Emai_w=c1.create_image(75,412,image=Email_img)
		Emaill=c1.create_image(35,412,image=Email_)
		#reds=c1.create_line(0,226,296,226,width=2)
		#reds1=c1.create_line(0,259,296,259,width=2)
		global Email_t
		Email_t=Text(resume_,height=0,width=17,bd=1,font=("Segoe Script",8))
		Email_t.pack()
		Email_t.place(x=64,y=427)
		Email_t.insert(END,"Enter Email_Id")
		Email_t.bind("<FocusIn>",email1)	
		

		'''bluet=Image.open("blue_.jpg")
		bluet=bluet.resize((314,34),Image.ANTIALIAS)
		bl__=ImageTk.PhotoImage(bluet)
		bt_=c1.create_image(95,473,image=bl__)
		'''
		social_=PhotoImage(master=c1,file="SOCIAL.png")
		Social=c1.create_image(90,480,image=social_)
		
		#reds=c1.create_line(0,459,296,459,width=2)
		#reds1=c1.create_line(0,494,296,494,width=2)
		def fb1(event):
			fb_t.tag_add(SEL,"1.0",END)
			fb_t.mark_set(INSERT,"1.0")
			fb_t.see(INSERT)
			return "break"
		
			

		
		fb=Image.open("facebook.png")
		fb=fb.resize((30,30),Image.ANTIALIAS)
		fb_=ImageTk.PhotoImage(fb,master=c1)
		facbk=c1.create_image(35,520,image=fb_)
		fb_img=PhotoImage(master=c1,file="Facebookw.png")
		fb_w=c1.create_image(90,520,image=fb_img)
		fb_t=Text(resume_,height=1,bd=3,width=17,font=("Segoe Script",8))
		fb_t.pack()
		fb_t.place(x=64,y=537)
		fb_t.insert(END,"Enter Facebook_Id")
		fb_t.bind("<FocusIn>",fb1)	
		
		
		def twt1(event):
			twt_t.tag_add(SEL,"1.0",END)
			twt_t.mark_set(INSERT,"1.0")
			twt_t.see(INSERT)
			return "break"
		
		
		twt=Image.open("twitter_.png")
		twt=twt.resize((30,30),Image.ANTIALIAS)
		twt_=ImageTk.PhotoImage(twt,master=c1)

		twt_img=PhotoImage(master=c1,file="Twitter.png")
		twt_w=c1.create_image(85,570,image=twt_img)
		twitwr=c1.create_image(35,570,image=twt_)
		twt_t=Text(resume_,height=1,width=17,bd=3,font=("Segoe Script",8))
		twt_t.pack()
		twt_t.place(x=64,y=585)
		twt_t.insert(END,"Enter Twitter_Id")
		twt_t.bind("<FocusIn>",twt1)	
		
		def lnk1(event):
			lnk_t.tag_add(SEL,"1.0",END)
			lnk_t.mark_set(INSERT,"1.0")
			lnk_t.see(INSERT)
			return "break"
		
		lnk=Image.open("linkedin_.png")
		lnk=lnk.resize((30,30),Image.ANTIALIAS)
		lnk_=ImageTk.PhotoImage(lnk,master=c1)

		lnk_img=PhotoImage(master=c1,file="Linkedin.png")
		lnk_w=c1.create_image(85,620,image=lnk_img)
		lnkdin=c1.create_image(35,620,image=lnk_)

		lnk_t=Text(resume_,height=1,width=17,bd=3,font=("Segoe Script",8))
		lnk_t.pack()
		lnk_t.place(x=64,y=632)
		lnk_t.insert(END,"Enter Linkendin_Id")
		lnk_t.bind("<FocusIn>",lnk1)	
		
		def prof1(event):
			profile_t.tag_add(SEL,"1.0",END)
			profile_t.mark_set(INSERT,"1.0")
			profile_t.see(INSERT)
			return "break"
			
		profe=Image.open("user.png")
		profe=profe.resize((44,44),Image.ANTIALIAS)
		profe__=ImageTk.PhotoImage(profe,master=c1)
		profe_=c.create_image(75,30,image=profe__)
		profile_t=Text(resume_,height=3,width=47,bd=3,font=("Segoe Print",9))
		profile_t.pack()
		profile_t.place(x=334,y=42)
		profile_t.insert(END,"Enter Your Specialty And Eductional Skills in Short.")
		profile_t.bind("<FocusIn>",prof1)	
		
		
		
		wrke__img=PhotoImage(master=c,file="WORK-EXPERIENCE.png")
		wrke_im=c.create_image(210,140,image=wrke__img)
		wrke=Image.open("edit.png")
		wrke=wrke.resize((44,44),Image.ANTIALIAS)
		wrke__=ImageTk.PhotoImage(wrke,master=c)
		wrke_1=c.create_image(75,140,image=wrke__)
		#1 work area
		def wrkf1(event):
			work1_year_from.tag_add(SEL,"1.0",END)
			work1_year_from.mark_set(INSERT,"1.0")
			work1_year_from.see(INSERT)
			return "break"
		def wrkt1(event):
			work1_year_to.tag_add(SEL,"1.0",END)
			work1_year_to.mark_set(INSERT,"1.0")
			work1_year_to.see(INSERT)
			return "break"
		def wrkc1(event):
			work1_city.tag_add(SEL,"1.0",END)
			work1_city.mark_set(INSERT,"1.0")
			work1_city.see(INSERT)
			return "break"
		def wrkd1(event):
			work1_desc.tag_add(SEL,"1.0",END)
			work1_desc.mark_set(INSERT,"1.0")
			work1_desc.see(INSERT)
			return "break"
		def wrkp1(event):
			work1_position.tag_add(SEL,"1.0",END)
			work1_position.mark_set(INSERT,"1.0")
			work1_position.see(INSERT)
			return "break"

		def wrkcomp1(event):
			work1_company.tag_add(SEL,"1.0",END)
			work1_company.mark_set(INSERT,"1.0")
			work1_company.see(INSERT)
			return "break"	
		work1_year_from=Text(resume_,height=1,width=7,bd=3,font=("Segoe Print",8))
		work1_year_from.pack()
		work1_year_from.place(x=334,y=162)
		work1_year_from.insert(END,"From")
		work1_year_from.bind("<FocusIn>",wrkf1)	
		
		c.create_line(163,174,174,174,width=5)
		work1_year_to=Text(resume_,height=1,width=7,bd=3,font=("Segoe Print",8))
		work1_year_to.pack()
		work1_year_to.place(x=398,y=162)
		work1_year_to.insert(END,"to")
		work1_year_to.bind("<FocusIn>",wrkt1)	
		
		work1_city=Text(resume_,height=1,width=14,bd=3,font=("Segoe Print",8))
		work1_city.pack()
		work1_city.place(x=342,y=187)
		work1_city.insert(END,"Enter City")
		work1_city.bind("<FocusIn>",wrkc1)	
		work1_position=Text(resume_,height=1,width=37,bd=3,font=("Segoe Print",8,"bold"))
		work1_position.pack()
		work1_position.place(x=482,y=160)
		work1_position.insert(END,"Enter your Post in Company")
		work1_position.bind("<FocusIn>",wrkp1)	
		
		work1_company=Text(resume_,height=1,width=37,bd=3,font=("Segoe Print",8))
		work1_company.pack()
		work1_company.place(x=482,y=180)
		work1_company.insert(END,"Enter Company Name")
		work1_company.bind("<FocusIn>",wrkcomp1)	
		
		work1_desc=Text(resume_,height=1,width=37,bd=3,font=("Segoe Print",8))
		work1_desc.pack()
		work1_desc.place(x=482,y=200)
		work1_desc.insert(END,"Enter Description of 1st Work Experience ")
		work1_desc.bind("<FocusIn>",wrkt1)	
		
	#2 work area
		def wrkf2(event):
			work2_year_from.tag_add(SEL,"1.0",END)
			work2_year_from.mark_set(INSERT,"1.0")
			work2_year_from.see(INSERT)
			return "break"
		def wrkt2(event):
			work2_year_to.tag_add(SEL,"1.0",END)
			work2_year_to.mark_set(INSERT,"1.0")
			work2_year_to.see(INSERT)
			return "break"
		def wrkc2(event):
			work2_city.tag_add(SEL,"1.0",END)
			work2_city.mark_set(INSERT,"1.0")
			work2_city.see(INSERT)
			return "break"
		def wrkd2(event):
			work2_desc.tag_add(SEL,"1.0",END)
			work2_desc.mark_set(INSERT,"1.0")
			work2_desc.see(INSERT)
			return "break"

		def wrkp2(event):
			work2_position.tag_add(SEL,"1.0",END)
			work2_position.mark_set(INSERT,"1.0")
			work2_position.see(INSERT)
			return "break"

		def wrkcomp2(event):
			work2_company.tag_add(SEL,"1.0",END)
			work2_company.mark_set(INSERT,"1.0")
			work2_company.see(INSERT)
			return "break"
		work2_year_from=Text(resume_,height=1,width=7,bd=3,font=("comic sans ms",8))
		work2_year_from.pack()
		work2_year_from.place(x=334,y=232)
		c.create_line(163,234,174,234,width=5)
		work2_year_to=Text(resume_,height=1,width=7,bd=3,font=("comic sans ms",8))
		work2_year_to.pack()
		work2_year_to.place(x=398,y=232)
		work2_year_from.insert(END,"From")
		work2_year_from.bind("<FocusIn>",wrkf2)	
		work2_year_to.insert(END,"to")
		work2_year_to.bind("<FocusIn>",wrkt2)	
		
		work2_city=Text(resume_,height=1,width=14,bd=3,font=("comic sans ms",8))
		work2_city.pack()
		work2_city.place(x=342,y=257)
		work2_city.insert(END,"Enter City")
		work2_city.bind("<FocusIn>",wrkc2)	
		

		work2_position=Text(resume_,height=1,width=37,bd=3,font=("Segoe Print",8,"bold"))
		work2_position.pack()
		work2_position.place(x=482,y=236)
		
		work2_position.insert(END,"Enter your Post in Company")
		work2_position.bind("<FocusIn>",wrkp2)	
		
		work2_company=Text(resume_,height=1,width=37,bd=3,wrap=WORD,font=("Segoe Print",8))
		work2_company.pack()
		work2_company.place(x=482,y=256)
		work2_company.insert(END,"Enter Company Name")
		work2_company.bind("<FocusIn>",wrkcomp2)	
		
		work2_desc=Text(resume_,height=2,width=37,bd=3,font=("Segoe Print",8))
		work2_desc.pack()
		work2_desc.place(x=482,y=276)
		work2_desc.insert(END,"Enter Description of 2nd Work Experience ")
		work2_desc.bind("<FocusIn>",wrkt2)	
		

		educ__img=PhotoImage(master=c,file="EDUCATION.png")
		educ_im=c.create_image(185,320,image=educ__img)
		educ=Image.open("graduation-hat.png")
		educ=educ.resize((44,44),Image.ANTIALIAS)
		educ__=ImageTk.PhotoImage(educ,master=c)
		educ_1=c.create_image(75,320,image=educ__)
		
		def eduf1(event):
			education1_from.tag_add(SEL,"1.0",END)
			education1_from.mark_set(INSERT,"1.0")
			education1_from.see(INSERT)
			return "break"
		def edut1(event):
			education1_to.tag_add(SEL,"1.0",END)
			education1_to.mark_set(INSERT,"1.0")
			education1_to.see(INSERT)
			return "break"
		def educ1(event):
			education1_city.tag_add(SEL,"1.0",END)
			education1_city.mark_set(INSERT,"1.0")
			education1_city.see(INSERT)
			return "break"
		def edud1(event):
			education1_inst.tag_add(SEL,"1.0",END)
			education1_inst.mark_set(INSERT,"1.0")
			education1_inst.see(INSERT)
			return "break"
		def eduq1(event):
			education1_qual.tag_add(SEL,"1.0",END)
			education1_qual.mark_set(INSERT,"1.0")
			education1_qual.see(INSERT)
			return "break"
			

		def eduf2(event):
			education2_from.tag_add(SEL,"1.0",END)
			education2_from.mark_set(INSERT,"1.0")
			education2_from.see(INSERT)
			return "break"
		def edut2(event):
			education2_to.tag_add(SEL,"1.0",END)
			education2_to.mark_set(INSERT,"1.0")
			education2_to.see(INSERT)
			return "break"
		def educ2(event):
			education2_city.tag_add(SEL,"1.0",END)
			education2_city.mark_set(INSERT,"1.0")
			education2_city.see(INSERT)
			return "break"
		def edud2(event):
			education2_inst.tag_add(SEL,"1.0",END)
			education2_inst.mark_set(INSERT,"1.0")
			education2_inst.see(INSERT)
			return "break"
		def eduq2(event):
			education2_qual.tag_add(SEL,"1.0",END)
			education2_qual.mark_set(INSERT,"1.0")
			education2_qual.see(INSERT)
			return "break"
		
		education1_from=Text(resume_,height=1,width=7,bd=3,font=("comic sans ms",8))
		education1_from.pack()
		education1_from.place(x=334,y=345)
		education1_from.insert(END,"from")
		education1_from.bind("<FocusIn>",eduf1)	
		
		c.create_line(163,350,170,350,width=5)
		education1_to=Text(resume_,height=1,width=7,bd=3,font=("comic sans ms",8))
		education1_to.pack()
		education1_to.place(x=398,y=345)
		education1_to.insert(END,"to")
		education1_to.bind("<FocusIn>",edut1)	
		
		education1_city=Text(resume_,height=1,width=14,bd=3,font=("comic sans ms",8))
		education1_city.pack()
		education1_city.place(x=342,y=370)
		education1_city.insert(END,"Enter City")
		education1_city.bind("<FocusIn>",educ1)	
		

		education1_inst=Text(resume_,height=2,width=37,bd=2,font=("Segoe Print",8,"bold"))
		education1_inst.pack()
		education1_inst.place(x=482,y=340)
		education1_inst.insert(END,"Enter Name of Institute")
		education1_inst.bind("<FocusIn>",edud1)	
		
		education1_qual=Text(resume_,height=2,width=37,bd=2,font=("Segoe Print",8))
		education1_qual.pack()
		education1_qual.place(x=482,y=360)
		education1_qual.insert(END,"Enter Qualifications Achieved")
		education1_qual.bind("<FocusIn>",eduq1)	



		education2_from=Text(resume_,height=1,width=7,bd=3,font=("comic sans ms",8))
		education2_from.pack()
		education2_from.place(x=334,y=410)
		education2_from.insert(END,"from")
		education2_from.bind("<FocusIn>",eduf2)	
		
		c.create_line(163,415,170,415,width=5)
		education2_to=Text(resume_,height=1,width=7,bd=3,font=("comic sans ms",8))
		education2_to.pack()
		education2_to.place(x=398,y=410)
		education2_to.insert(END,"to")
		education2_to.bind("<FocusIn>",edut2)	
		
		education2_city=Text(resume_,height=1,width=14,bd=3,font=("comic sans ms",8))
		education2_city.pack()
		education2_city.place(x=342,y=435)
		education2_city.insert(END,"Enter City")
		education2_city.bind("<FocusIn>",educ2)	
		


		education2_inst=Text(resume_,height=2,width=37,bd=2,font=("Segoe Print",8))
		education2_inst.pack()
		education2_inst.place(x=482,y=410)
		education2_inst.insert(END,"Enter Name of Institute")
		education2_inst.bind("<FocusIn>",edud2)

		education2_qual=Text(resume_,height=2,width=37,bd=2,font=("Segoe Print",8,"bold"))
		education2_qual.pack()
		education2_qual.place(x=482,y=430)
		education2_qual.insert(END,"Enter Qualifications Achieved")
		education2_qual.bind("<FocusIn>",eduq2)	
		Style_=ttk.Style()

		#Style.configure("mystyle.Treeview",bd=2,font=("arial",12))
		Style_.configure("mystyle_.Treeview",bd=2,rowheight=40,font=("Segoe Script",10))

		

		def proges(event):
			import tkinter.ttk as ttk
			from tkinter import ttk
			i=410
			j=510
			e=ttk.Style()
			e.theme_use("default")
			e.configure("#8AC91D.Horizontal.TProgressbar",bordercolor="#8AC91D",lightcolor="#8AC91D",darkcolor="#8AC91D",background="#8AC91D")
			progress1=Progressbar(resume_,style="#8AC91D.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress1["value"]=rt.get()
			progress1.pack()
			progress1.place(x=i,y=j)
		def proges1(event):
			import tkinter.ttk as ttk
			i=410
			j=555
			e1=ttk.Style()
			e1.theme_use("default")
			e1.configure("red1.Horizontal.TProgressbar",bordercolor="#FB9A00",lightcolor="#FB9A00",darkcolor="#FB9A00",background="#FB9A00")
			progress2=Progressbar(resume_,style="red1.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress2["value"]=rt1.get()
			progress2.pack()
			progress2.place(x=i,y=j)
		def proges2(event):
			import tkinter.ttk as ttk
			i=410
			j=605
			e2=ttk.Style()
			e2.theme_use("default")
			e2.configure("red2.Horizontal.TProgressbar",bordercolor="#1FB4E7",lightcolor="#1FB4E7",darkcolor="#1FB4E7",background="#1FB4E7")
			progress3=Progressbar(resume_,style="red2.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress3["value"]=rt2.get()
			progress3.pack()
			progress3.place(x=i,y=j)
		def proges3(event):
			import tkinter.ttk as ttk
			i=410
			j=655
			e3=ttk.Style()
			e3.theme_use("default")
			e3.configure("red3.Horizontal.TProgressbar",bordercolor="red",lightcolor="red",darkcolor="red",background="red")
			progress4=Progressbar(resume_,style="red3.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress4["value"]=rt3.get()
			progress4.pack()
			progress4.place(x=i,y=j)
		
		skill__img=PhotoImage(master=c,file="SKILLS-AND-EXPERTIZE.png")
		skill_im=c.create_image(245,480,image=skill__img)
		skil=Image.open("key-skills.png")
		skil=skil.resize((44,44),Image.ANTIALIAS)
		skil__=ImageTk.PhotoImage(skil,master=c)
		skil_1=c.create_image(75,475,image=skil__)
		global rt
		global rt1
		global rt2
		global rt3
		
		
		u=350
		f=450
		
		rt=Scale(resume_,from_=1,to=100,width=7,length=325,orient=HORIZONTAL,command=proges,activebackground="blue",cursor="hand2",fg="red")
		rt.place(x=410,y=510)
		rt1=Scale(resume_,from_=1,to=100,width=7,length=325,orient=HORIZONTAL,command=proges1,activebackground="blue",cursor="hand2",fg="red")
		rt1.place(x=410,y=555)
		rt2=Scale(resume_,from_=1,to=100,width=7,length=325,orient=HORIZONTAL,command=proges2,activebackground="blue",cursor="hand2",fg="red")
		rt2.place(x=410,y=605)
		
		rt3=Scale(resume_,from_=1,to=100,width=7,length=325,orient=HORIZONTAL,command=proges3,activebackground="blue",cursor="hand2",fg="red")
		#rt3.get())

		rt3.place(x=410,y=655)
		def delt(event):


			skill_1.tag_add(SEL,"1.0",END)
			skill_1.mark_set(INSERT,"1.0")
			skill_1.see(INSERT)
			return "break"
		def delt2(event):


			skill_2.tag_add(SEL,"1.0",END)
			skill_2.mark_set(INSERT,"1.0")
			skill_2.see(INSERT)
			return "break"
		def delt3(event):


			skill_3.tag_add(SEL,"1.0",END)
			skill_3.mark_set(INSERT,"1.0")
			skill_3.see(INSERT)
			return "break"
		def delt4(event):


			skill_4.tag_add(SEL,"1.0",END)
			skill_4.mark_set(INSERT,"1.0")
			skill_4.see(INSERT)
			return "break"

		skill_1=Text(resume_,height=1,width=10,bd=3,font=("comic sans ms",8))
		skill_1.pack()
		skill_1.place(x=320,y=510)
		
		skill_1.insert(END,"enter skill 1")
		skill_1.bind("<FocusIn>",delt)

		skill_2=Text(resume_,height=1,width=10,bd=3,font=("comic sans ms",8))
		skill_2.pack()
		skill_2.place(x=320,y=555)

		skill_2.insert(END,"enter skill 2")
		skill_2.bind("<FocusIn>",delt2)


		skill_3=Text(resume_,height=1,width=10,bd=3,font=("comic sans ms",8))
		skill_3.pack()
		skill_3.place(x=320,y=605)
		skill_3.insert(END,"enter skill 3")
		skill_3.bind("<FocusIn>",delt3)


		skill_4=Text(resume_,height=1,width=10,bd=3,font=("comic sans ms",8))
		skill_4.pack()
		skill_4.place(x=320,y=655)
		skill_4.insert(END,"enter skill 4")
		skill_4.bind("<FocusIn>",delt4)
		eventy=""

		proges(eventy)

		proges1(eventy)

		proges2(eventy)



		proges3(eventy)
		submit_=PhotoImage(master=c,file="sub.png")
		submt_=c.create_image(520,25,image=submit_)
		c.tag_bind(submt_,'<ButtonPress-1>',resum_data)
		
		'''
		bluet2=Image.open("blue_.jpg")
		bluet2=bluet2.resize((90,1338),Image.ANTIALIAS)
		bl__2=ImageTk.PhotoImage(bluet2)
		bl2_=c.create_image(0,10,image=bl__2)'''
		resume_.mainloop()



	def resume_1(event):
		from tkinter import Text, Tk
		from tkinter.ttk import Progressbar
		
		root_.destroy()
		
		#mainpage_.destroy()
		global skill_2
		global skill_3
		
		global skill_4
		global skill_1
		global name_
		global adres_t
		global phone_t
		global fb_t
		global twt_t
		global lnk_t
		global profile_t		
		global work1_city
		global work1_desc
		global work2_year_from
		global work2_year_to
		global work2_city
		global work2_desc
		global profile_t
		global work1_year_from
		global work1_year_to
		global work2_position
		global work1_position
		global work2_company
		global work1_company
		global education1_from
		global education1_to
		global education2_from
		global education2_to
		global education1_city
		global education2_city
		global education2_qual
		global education1_qual
		global education2_inst
		global education1_inst


		global centr
		centr=""	
		global resume_
		import tkinter.ttk as ttk
		resume_ = Tk()
		resume_.config(bg="#FFFFFF")
		resume_.title("Create CV")
		resume_.geometry("795x700")
		resume_.iconbitmap("job.ico")
		resume_.resizable(False,False)
		resume_.config(bg="white")
		
		#resume_.wm_attributes("-alpha",0.7)
		#r=Scale(resume_,from_=1,to=100000,orient=HORIZONTAL,bg="BLUE",fg="red")
		#r.pack()
		def progrs(event):
			progress['value']=50
		def photo(event):
			import os
			global centr
			
			resume_.filename=filedialog.askopenfilename(initialdir="Desktop/" ,title="Select a Photo",filetypes=(("All Files","*.*"),("PNG files","*.png"),("JPEG files","*.jpeg"),("JPG files","*.jpg")))
			n=resume_.filename
			#n)
			file_name = os.path.splitext(n)[0] 
			extension = os.path.splitext(n)[1] 
			#file_name)
			centr=str(ide)+extension
			
			rot3__=Image.open(n)
			global frame1_
			rot3__.save(centr,"")
			rot3_=Image.open(centr)
			
			rot3__=rot3__.resize((70,70),Image.ANTIALIAS)
			rot1_=ImageTk.PhotoImage(rot3__,master=c1)
			frame1_=c1.create_image(90,70,image=rot1_)
			#resume_.configure()	
			
		global bgm
		global img
		global img1
		l=Label(resume_)
		global c
		c=Canvas(l,width=600,height=1200,bd=0,bg="white",highlightthickness=0)
		#img1=PhotoImage(file="bgmp.png")
		img1=Image.open("back10.jpg")
		img=PhotoImage(master=c,file="Profile.png")

		img1=img1.resize((606,742),Image.ANTIALIAS)
		img3_=ImageTk.PhotoImage(img1,master=c)
		
		d1=c.create_image(320,320,image=img3_)
		
		d=c.create_image(150,30,image=img)

		c.pack()
		
		l.pack()
		l.place(x=220,y=0)
		
		global c1
		l1=Label(resume_,bg="white")
		c1=Canvas(l1,width=250,height=1000,bd=0,highlightthickness=0,highlightbackground="white")
		img2=Image.open("back8.jpg")
		submit_=PhotoImage(file="Submit__1.png",master=c1)
		submt_=c.create_image(900,100,image=submit_)
		
		img2=img2.resize((340,1000),Image.ANTIALIAS)
		img1_=ImageTk.PhotoImage(img2,master=c1)
		d1=c1.create_image(80,320,image=img1_)
		
		c1.pack()
		#c1.place(x=0,y=0)
		l1.pack()
		l1.place(x=0,y=0)
		
		global n
		n="bg3.png"
		mag=Image.open(n)
		global frame1
		mag=mag.resize((110,110),Image.ANTIALIAS)
		mag1=ImageTk.PhotoImage(mag,master=c1)
		frame1=c1.create_image(90,70,image=mag1)
		#frame1.place(x=10,y=10)

		m="add-user.png"
		mag4=Image.open(m)
		mag4=mag4.resize((30,30),Image.ANTIALIAS)
		mag5=ImageTk.PhotoImage(mag4,master=c1)
		frame2=c1.create_image(170,110,image=mag5)
		c1.tag_bind(frame2,'<ButtonPress-1>',photo)


		name1=c1.create_text(123,160,text="Employee\nname",font=("Segoe Print", 20," bold"))
		'''
		bluet1=Image.open("blue_.jpg")
		bluet1=bluet1.resize((314,38),Image.ANTIALIAS)
		bl__1=ImageTk.PhotoImage(bluet1)
		bt1_=c1.create_image(95,244,image=bl__1)'''
		Info_=PhotoImage(master=c1,file="INFO.png")
		Info=c1.create_image(90,244,image=Info_)
		conct=Image.open("user.png")
		conct=conct.resize((30,30),Image.ANTIALIAS)
		conct__=ImageTk.PhotoImage(conct,master=c1)
		conct_=c1.create_image(35,290,image=conct__)
		
		def name1_(event):


			name_.tag_add(SEL,"1.0",END)
			name_.mark_set(INSERT,"1.0")
			name_.see(INSERT)
			return "break"
		
		img_=PhotoImage(master=c1,file="NAME21.png")
		
		d2=c1.create_image(75,294,image=img_)
		
		name_=Text(resume_,height=0,width=17,bd=1,fg="black",font=("Segoe Script",8))
		name_.pack()
		name_.place(x=64,y=305)
		name_.insert(END,"Enter Name")

		name_.bind("<FocusIn>",name1_)
		


		adres=Image.open("map.png")
		adres=adres.resize((30,30),Image.ANTIALIAS)
		adres_=ImageTk.PhotoImage(adres,master=c1)
		addres=c1.create_image(35,332,image=adres_)
		adress_img=PhotoImage(master=c1,file="Addressw.png")
		adress_w=c1.create_image(84,332,image=adress_img)


		def address1(event):


			adres_t.tag_add(SEL,"1.0",END)
			adres_t.mark_set(INSERT,"1.0")
			adres_t.see(INSERT)
			return "break"
		
		adres_t=Text(resume_,height=0,width=17,bd=1,font=("Segoe Script",8))
		adres_t.pack()
		adres_t.place(x=64,y=343)
		adres_t.insert(END,"Enter Address")
		adres_t.bind("<FocusIn>",address1)	
		


		phone=Image.open("telephone.png")
		phone=phone.resize((30,30),Image.ANTIALIAS)
		phone_=ImageTk.PhotoImage(phone,master=c1)
		phone_img=PhotoImage(master=c1,file="Phonew.png")
		phne_w=c1.create_image(75,373,image=phone_img)
		phoone=c1.create_image(35,368,image=phone_)
		def phone1(event):
			phone_t.tag_add(SEL,"1.0",END)
			phone_t.mark_set(INSERT,"1.0")
			phone_t.see(INSERT)
			return "break"
		
		phone_t=Text(resume_,height=0,width=17,bd=1,font=("Segoe Script",8))
		phone_t.pack()
		phone_t.place(x=64,y=385)
		phone_t.insert(END,"enter phone number")
		phone_t.bind("<FocusIn>",phone1)	
			

		Email1=Image.open("gmail.png")
		Email1=Email1.resize((30,30),Image.ANTIALIAS)
		Email_=ImageTk.PhotoImage(Email1,master=c1)
		def email1(event):
			Email_t.tag_add(SEL,"1.0",END)
			Email_t.mark_set(INSERT,"1.0")
			Email_t.see(INSERT)
			return "break"
		
		Email_img=PhotoImage(master=c1,file="Emailw.png")
		Emai_w=c1.create_image(75,412,image=Email_img)
		Emaill=c1.create_image(35,412,image=Email_)
		#reds=c1.create_line(0,226,296,226,width=2)
		#reds1=c1.create_line(0,259,296,259,width=2)
		global Email_t
		Email_t=Text(resume_,height=0,width=17,bd=1,font=("Segoe Script",8))
		Email_t.pack()
		Email_t.place(x=64,y=427)
		Email_t.insert(END,"Enter Email_Id")
		Email_t.bind("<FocusIn>",email1)	
		

		'''bluet=Image.open("blue_.jpg")
		bluet=bluet.resize((314,34),Image.ANTIALIAS)
		bl__=ImageTk.PhotoImage(bluet)
		bt_=c1.create_image(95,473,image=bl__)
		'''
		social_=PhotoImage(master=c1,file="SOCIAL.png")
		Social=c1.create_image(90,480,image=social_)
		
		#reds=c1.create_line(0,459,296,459,width=2)
		#reds1=c1.create_line(0,494,296,494,width=2)
		def fb1(event):
			fb_t.tag_add(SEL,"1.0",END)
			fb_t.mark_set(INSERT,"1.0")
			fb_t.see(INSERT)
			return "break"
		
			

		
		fb=Image.open("facebook.png")
		fb=fb.resize((30,30),Image.ANTIALIAS)
		fb_=ImageTk.PhotoImage(fb,master=c1)
		facbk=c1.create_image(35,520,image=fb_)
		fb_img=PhotoImage(master=c1,file="Facebookw.png")
		fb_w=c1.create_image(90,520,image=fb_img)
		fb_t=Text(resume_,height=1,bd=3,width=17,font=("Segoe Script",8))
		fb_t.pack()
		fb_t.place(x=64,y=537)
		fb_t.insert(END,"Enter Facebook_Id")
		fb_t.bind("<FocusIn>",fb1)	
		
		
		def twt1(event):
			twt_t.tag_add(SEL,"1.0",END)
			twt_t.mark_set(INSERT,"1.0")
			twt_t.see(INSERT)
			return "break"
		
		
		twt=Image.open("twitter_.png")
		twt=twt.resize((30,30),Image.ANTIALIAS)
		twt_=ImageTk.PhotoImage(twt,master=c1)

		twt_img=PhotoImage(master=c1,file="Twitter.png")
		twt_w=c1.create_image(85,570,image=twt_img)
		twitwr=c1.create_image(35,570,image=twt_)
		twt_t=Text(resume_,height=1,width=17,bd=3,font=("Segoe Script",8))
		twt_t.pack()
		twt_t.place(x=64,y=585)
		twt_t.insert(END,"Enter Twitter_Id")
		twt_t.bind("<FocusIn>",twt1)	
		
		def lnk1(event):
			lnk_t.tag_add(SEL,"1.0",END)
			lnk_t.mark_set(INSERT,"1.0")
			lnk_t.see(INSERT)
			return "break"
		
		lnk=Image.open("linkedin_.png")
		lnk=lnk.resize((30,30),Image.ANTIALIAS)
		lnk_=ImageTk.PhotoImage(lnk,master=c1)

		lnk_img=PhotoImage(master=c1,file="Linkedin.png")
		lnk_w=c1.create_image(85,620,image=lnk_img)
		lnkdin=c1.create_image(35,620,image=lnk_)

		lnk_t=Text(resume_,height=1,width=17,bd=3,font=("Segoe Script",8))
		lnk_t.pack()
		lnk_t.place(x=64,y=632)
		lnk_t.insert(END,"Enter Linkendin_Id")
		lnk_t.bind("<FocusIn>",lnk1)	
		
		def prof1(event):
			profile_t.tag_add(SEL,"1.0",END)
			profile_t.mark_set(INSERT,"1.0")
			profile_t.see(INSERT)
			return "break"
			
		profe=Image.open("user.png")
		profe=profe.resize((44,44),Image.ANTIALIAS)
		profe__=ImageTk.PhotoImage(profe,master=c1)
		profe_=c.create_image(75,30,image=profe__)
		profile_t=Text(resume_,height=3,width=47,bd=3,font=("Segoe Print",9))
		profile_t.pack()
		profile_t.place(x=334,y=42)
		profile_t.insert(END,"Enter Your Specialty And Eductional Skills in Short.")
		profile_t.bind("<FocusIn>",prof1)	
		
		
		
		wrke__img=PhotoImage(master=c,file="WORK-EXPERIENCE.png")
		wrke_im=c.create_image(210,140,image=wrke__img)
		wrke=Image.open("edit.png")
		wrke=wrke.resize((44,44),Image.ANTIALIAS)
		wrke__=ImageTk.PhotoImage(wrke,master=c)
		wrke_1=c.create_image(75,140,image=wrke__)
		#1 work area
		def wrkf1(event):
			work1_year_from.tag_add(SEL,"1.0",END)
			work1_year_from.mark_set(INSERT,"1.0")
			work1_year_from.see(INSERT)
			return "break"
		def wrkt1(event):
			work1_year_to.tag_add(SEL,"1.0",END)
			work1_year_to.mark_set(INSERT,"1.0")
			work1_year_to.see(INSERT)
			return "break"
		def wrkc1(event):
			work1_city.tag_add(SEL,"1.0",END)
			work1_city.mark_set(INSERT,"1.0")
			work1_city.see(INSERT)
			return "break"
		def wrkd1(event):
			work1_desc.tag_add(SEL,"1.0",END)
			work1_desc.mark_set(INSERT,"1.0")
			work1_desc.see(INSERT)
			return "break"
		def wrkp1(event):
			work1_position.tag_add(SEL,"1.0",END)
			work1_position.mark_set(INSERT,"1.0")
			work1_position.see(INSERT)
			return "break"

		def wrkcomp1(event):
			work1_company.tag_add(SEL,"1.0",END)
			work1_company.mark_set(INSERT,"1.0")
			work1_company.see(INSERT)
			return "break"	
		work1_year_from=Text(resume_,height=1,width=7,bd=3,font=("Segoe Print",8))
		work1_year_from.pack()
		work1_year_from.place(x=334,y=162)
		work1_year_from.insert(END,"From")
		work1_year_from.bind("<FocusIn>",wrkf1)	
		
		c.create_line(163,174,174,174,width=5)
		work1_year_to=Text(resume_,height=1,width=7,bd=3,font=("Segoe Print",8))
		work1_year_to.pack()
		work1_year_to.place(x=398,y=162)
		work1_year_to.insert(END,"to")
		work1_year_to.bind("<FocusIn>",wrkt1)	
		
		work1_city=Text(resume_,height=1,width=14,bd=3,font=("Segoe Print",8))
		work1_city.pack()
		work1_city.place(x=342,y=187)
		work1_city.insert(END,"Enter City")
		work1_city.bind("<FocusIn>",wrkc1)	
		work1_position=Text(resume_,height=1,width=37,bd=3,font=("Segoe Print",8,"bold"))
		work1_position.pack()
		work1_position.place(x=482,y=160)
		work1_position.insert(END,"Enter your Post in Company")
		work1_position.bind("<FocusIn>",wrkp1)	
		
		work1_company=Text(resume_,height=1,width=37,bd=3,font=("Segoe Print",8))
		work1_company.pack()
		work1_company.place(x=482,y=180)
		work1_company.insert(END,"Enter Company Name")
		work1_company.bind("<FocusIn>",wrkcomp1)	
		
		work1_desc=Text(resume_,height=1,width=37,bd=3,font=("Segoe Print",8))
		work1_desc.pack()
		work1_desc.place(x=482,y=200)
		work1_desc.insert(END,"Enter Description of 1st Work Experience ")
		work1_desc.bind("<FocusIn>",wrkt1)	
		
	#2 work area
		def wrkf2(event):
			work2_year_from.tag_add(SEL,"1.0",END)
			work2_year_from.mark_set(INSERT,"1.0")
			work2_year_from.see(INSERT)
			return "break"
		def wrkt2(event):
			work2_year_to.tag_add(SEL,"1.0",END)
			work2_year_to.mark_set(INSERT,"1.0")
			work2_year_to.see(INSERT)
			return "break"
		def wrkc2(event):
			work2_city.tag_add(SEL,"1.0",END)
			work2_city.mark_set(INSERT,"1.0")
			work2_city.see(INSERT)
			return "break"
		def wrkd2(event):
			work2_desc.tag_add(SEL,"1.0",END)
			work2_desc.mark_set(INSERT,"1.0")
			work2_desc.see(INSERT)
			return "break"

		def wrkp2(event):
			work2_position.tag_add(SEL,"1.0",END)
			work2_position.mark_set(INSERT,"1.0")
			work2_position.see(INSERT)
			return "break"

		def wrkcomp2(event):
			work2_company.tag_add(SEL,"1.0",END)
			work2_company.mark_set(INSERT,"1.0")
			work2_company.see(INSERT)
			return "break"
		work2_year_from=Text(resume_,height=1,width=7,bd=3,font=("comic sans ms",8))
		work2_year_from.pack()
		work2_year_from.place(x=334,y=232)
		c.create_line(163,234,174,234,width=5)
		work2_year_to=Text(resume_,height=1,width=7,bd=3,font=("comic sans ms",8))
		work2_year_to.pack()
		work2_year_to.place(x=398,y=232)
		work2_year_from.insert(END,"From")
		work2_year_from.bind("<FocusIn>",wrkf2)	
		work2_year_to.insert(END,"to")
		work2_year_to.bind("<FocusIn>",wrkt2)	
		
		work2_city=Text(resume_,height=1,width=14,bd=3,font=("comic sans ms",8))
		work2_city.pack()
		work2_city.place(x=342,y=257)
		work2_city.insert(END,"Enter City")
		work2_city.bind("<FocusIn>",wrkc2)	
		

		work2_position=Text(resume_,height=1,width=37,bd=3,font=("Segoe Print",8,"bold"))
		work2_position.pack()
		work2_position.place(x=482,y=236)
		
		work2_position.insert(END,"Enter your Post in Company")
		work2_position.bind("<FocusIn>",wrkp2)	
		
		work2_company=Text(resume_,height=1,width=37,bd=3,wrap=WORD,font=("Segoe Print",8))
		work2_company.pack()
		work2_company.place(x=482,y=256)
		work2_company.insert(END,"Enter Company Name")
		work2_company.bind("<FocusIn>",wrkcomp2)	
		
		work2_desc=Text(resume_,height=2,width=37,bd=3,font=("Segoe Print",8))
		work2_desc.pack()
		work2_desc.place(x=482,y=276)
		work2_desc.insert(END,"Enter Description of 2nd Work Experience ")
		work2_desc.bind("<FocusIn>",wrkt2)	
		

		educ__img=PhotoImage(master=c,file="EDUCATION.png")
		educ_im=c.create_image(185,320,image=educ__img)
		educ=Image.open("graduation-hat.png")
		educ=educ.resize((44,44),Image.ANTIALIAS)
		educ__=ImageTk.PhotoImage(educ,master=c)
		educ_1=c.create_image(75,320,image=educ__)
		
		def eduf1(event):
			education1_from.tag_add(SEL,"1.0",END)
			education1_from.mark_set(INSERT,"1.0")
			education1_from.see(INSERT)
			return "break"
		def edut1(event):
			education1_to.tag_add(SEL,"1.0",END)
			education1_to.mark_set(INSERT,"1.0")
			education1_to.see(INSERT)
			return "break"
		def educ1(event):
			education1_city.tag_add(SEL,"1.0",END)
			education1_city.mark_set(INSERT,"1.0")
			education1_city.see(INSERT)
			return "break"
		def edud1(event):
			education1_inst.tag_add(SEL,"1.0",END)
			education1_inst.mark_set(INSERT,"1.0")
			education1_inst.see(INSERT)
			return "break"
		def eduq1(event):
			education1_qual.tag_add(SEL,"1.0",END)
			education1_qual.mark_set(INSERT,"1.0")
			education1_qual.see(INSERT)
			return "break"
			

		def eduf2(event):
			education2_from.tag_add(SEL,"1.0",END)
			education2_from.mark_set(INSERT,"1.0")
			education2_from.see(INSERT)
			return "break"
		def edut2(event):
			education2_to.tag_add(SEL,"1.0",END)
			education2_to.mark_set(INSERT,"1.0")
			education2_to.see(INSERT)
			return "break"
		def educ2(event):
			education2_city.tag_add(SEL,"1.0",END)
			education2_city.mark_set(INSERT,"1.0")
			education2_city.see(INSERT)
			return "break"
		def edud2(event):
			education2_inst.tag_add(SEL,"1.0",END)
			education2_inst.mark_set(INSERT,"1.0")
			education2_inst.see(INSERT)
			return "break"
		def eduq2(event):
			education2_qual.tag_add(SEL,"1.0",END)
			education2_qual.mark_set(INSERT,"1.0")
			education2_qual.see(INSERT)
			return "break"
		
		education1_from=Text(resume_,height=1,width=7,bd=3,font=("comic sans ms",8))
		education1_from.pack()
		education1_from.place(x=334,y=345)
		education1_from.insert(END,"from")
		education1_from.bind("<FocusIn>",eduf1)	
		
		c.create_line(163,350,170,350,width=5)
		education1_to=Text(resume_,height=1,width=7,bd=3,font=("comic sans ms",8))
		education1_to.pack()
		education1_to.place(x=398,y=345)
		education1_to.insert(END,"to")
		education1_to.bind("<FocusIn>",edut1)	
		
		education1_city=Text(resume_,height=1,width=14,bd=3,font=("comic sans ms",8))
		education1_city.pack()
		education1_city.place(x=342,y=370)
		education1_city.insert(END,"Enter City")
		education1_city.bind("<FocusIn>",educ1)	
		

		education1_inst=Text(resume_,height=2,width=37,bd=2,font=("Segoe Print",8,"bold"))
		education1_inst.pack()
		education1_inst.place(x=482,y=340)
		education1_inst.insert(END,"Enter Name of Institute")
		education1_inst.bind("<FocusIn>",edud1)	
		
		education1_qual=Text(resume_,height=2,width=37,bd=2,font=("Segoe Print",8))
		education1_qual.pack()
		education1_qual.place(x=482,y=360)
		education1_qual.insert(END,"Enter Qualifications Achieved")
		education1_qual.bind("<FocusIn>",eduq1)	



		education2_from=Text(resume_,height=1,width=7,bd=3,font=("comic sans ms",8))
		education2_from.pack()
		education2_from.place(x=334,y=410)
		education2_from.insert(END,"from")
		education2_from.bind("<FocusIn>",eduf2)	
		
		c.create_line(163,415,170,415,width=5)
		education2_to=Text(resume_,height=1,width=7,bd=3,font=("comic sans ms",8))
		education2_to.pack()
		education2_to.place(x=398,y=410)
		education2_to.insert(END,"to")
		education2_to.bind("<FocusIn>",edut2)	
		
		education2_city=Text(resume_,height=1,width=14,bd=3,font=("comic sans ms",8))
		education2_city.pack()
		education2_city.place(x=342,y=435)
		education2_city.insert(END,"Enter City")
		education2_city.bind("<FocusIn>",educ2)	
		


		education2_inst=Text(resume_,height=2,width=37,bd=2,font=("Segoe Print",8))
		education2_inst.pack()
		education2_inst.place(x=482,y=410)
		education2_inst.insert(END,"Enter Name of Institute")
		education2_inst.bind("<FocusIn>",edud2)

		education2_qual=Text(resume_,height=2,width=37,bd=2,font=("Segoe Print",8,"bold"))
		education2_qual.pack()
		education2_qual.place(x=482,y=430)
		education2_qual.insert(END,"Enter Qualifications Achieved")
		education2_qual.bind("<FocusIn>",eduq2)	
		Style_=ttk.Style()

		#Style.configure("mystyle.Treeview",bd=2,font=("arial",12))
		Style_.configure("mystyle_.Treeview",bd=2,rowheight=40,font=("Segoe Script",10))

		

		def proges(event):
			import tkinter.ttk as ttk
			from tkinter import ttk
			i=410
			j=510
			e=ttk.Style()
			e.theme_use("default")
			e.configure("#8AC91D.Horizontal.TProgressbar",bordercolor="#8AC91D",lightcolor="#8AC91D",darkcolor="#8AC91D",background="#8AC91D")
			progress1=Progressbar(resume_,style="#8AC91D.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress1["value"]=rt.get()
			progress1.pack()
			progress1.place(x=i,y=j)
		def proges1(event):
			import tkinter.ttk as ttk
			i=410
			j=555
			e1=ttk.Style()
			e1.theme_use("default")
			e1.configure("red1.Horizontal.TProgressbar",bordercolor="#FB9A00",lightcolor="#FB9A00",darkcolor="#FB9A00",background="#FB9A00")
			progress2=Progressbar(resume_,style="red1.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress2["value"]=rt1.get()
			progress2.pack()
			progress2.place(x=i,y=j)
		def proges2(event):
			import tkinter.ttk as ttk
			i=410
			j=605
			e2=ttk.Style()
			e2.theme_use("default")
			e2.configure("red2.Horizontal.TProgressbar",bordercolor="#1FB4E7",lightcolor="#1FB4E7",darkcolor="#1FB4E7",background="#1FB4E7")
			progress3=Progressbar(resume_,style="red2.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress3["value"]=rt2.get()
			progress3.pack()
			progress3.place(x=i,y=j)
		def proges3(event):
			import tkinter.ttk as ttk
			i=410
			j=655
			e3=ttk.Style()
			e3.theme_use("default")
			e3.configure("red3.Horizontal.TProgressbar",bordercolor="red",lightcolor="red",darkcolor="red",background="red")
			progress4=Progressbar(resume_,style="red3.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress4["value"]=rt3.get()
			progress4.pack()
			progress4.place(x=i,y=j)
		
		skill__img=PhotoImage(master=c,file="SKILLS-AND-EXPERTIZE.png")
		skill_im=c.create_image(245,480,image=skill__img)
		skil=Image.open("key-skills.png")
		skil=skil.resize((44,44),Image.ANTIALIAS)
		skil__=ImageTk.PhotoImage(skil,master=c)
		skil_1=c.create_image(75,475,image=skil__)
		global rt
		global rt1
		global rt2
		global rt3
		
		
		u=350
		f=450
		
		rt=Scale(resume_,from_=1,to=100,width=7,length=325,orient=HORIZONTAL,command=proges,activebackground="blue",cursor="hand2",fg="red")
		rt.place(x=410,y=510)
		rt1=Scale(resume_,from_=1,to=100,width=7,length=325,orient=HORIZONTAL,command=proges1,activebackground="blue",cursor="hand2",fg="red")
		rt1.place(x=410,y=555)
		rt2=Scale(resume_,from_=1,to=100,width=7,length=325,orient=HORIZONTAL,command=proges2,activebackground="blue",cursor="hand2",fg="red")
		rt2.place(x=410,y=605)
		
		rt3=Scale(resume_,from_=1,to=100,width=7,length=325,orient=HORIZONTAL,command=proges3,activebackground="blue",cursor="hand2",fg="red")
		#rt3.get())

		rt3.place(x=410,y=655)
		def delt(event):


			skill_1.tag_add(SEL,"1.0",END)
			skill_1.mark_set(INSERT,"1.0")
			skill_1.see(INSERT)
			return "break"
		def delt2(event):


			skill_2.tag_add(SEL,"1.0",END)
			skill_2.mark_set(INSERT,"1.0")
			skill_2.see(INSERT)
			return "break"
		def delt3(event):


			skill_3.tag_add(SEL,"1.0",END)
			skill_3.mark_set(INSERT,"1.0")
			skill_3.see(INSERT)
			return "break"
		def delt4(event):


			skill_4.tag_add(SEL,"1.0",END)
			skill_4.mark_set(INSERT,"1.0")
			skill_4.see(INSERT)
			return "break"

		skill_1=Text(resume_,height=1,width=10,bd=3,font=("comic sans ms",8))
		skill_1.pack()
		skill_1.place(x=320,y=510)
		
		skill_1.insert(END,"enter skill 1")
		skill_1.bind("<FocusIn>",delt)

		skill_2=Text(resume_,height=1,width=10,bd=3,font=("comic sans ms",8))
		skill_2.pack()
		skill_2.place(x=320,y=555)

		skill_2.insert(END,"enter skill 2")
		skill_2.bind("<FocusIn>",delt2)


		skill_3=Text(resume_,height=1,width=10,bd=3,font=("comic sans ms",8))
		skill_3.pack()
		skill_3.place(x=320,y=605)
		skill_3.insert(END,"enter skill 3")
		skill_3.bind("<FocusIn>",delt3)


		skill_4=Text(resume_,height=1,width=10,bd=3,font=("comic sans ms",8))
		skill_4.pack()
		skill_4.place(x=320,y=655)
		skill_4.insert(END,"enter skill 4")
		skill_4.bind("<FocusIn>",delt4)
		eventy=""

		proges(eventy)

		proges1(eventy)

		proges2(eventy)



		proges3(eventy)
		submit_=PhotoImage(master=c,file="sub.png")
		submt_=c.create_image(520,25,image=submit_)
		c.tag_bind(submt_,'<ButtonPress-1>',resum_data_)
		
		'''
		bluet2=Image.open("blue_.jpg")
		bluet2=bluet2.resize((90,1338),Image.ANTIALIAS)
		bl__2=ImageTk.PhotoImage(bluet2)
		bl2_=c.create_image(0,10,image=bl__2)'''
		resume_.mainloop()



	def Update(event):
		conn=sqlite3.connect("jobs.db")
		c=conn.cursor()
		#if clicked.get()=="Choose Job Type":
		c.execute("""UPDATE Job_Aspirants
		 SET Full_Name=:name_,
		 Job_type=:jobtype_,
		 Age=:age,
		 Experience=:experience,
		 Address=:adress,
		 M_Number=:number_,
		 Password=:password_ 
		 WHERE ID=:Id """,
		 {"Id":Id.get(),
		 "name_":name_e.get(),
		 "jobtype_":jobtype_e.get(),
		 "age":age_e.get(),
		 "experience":experience_e.get(),
		 "adress":adress_e.get(),
		 "number_":number_e.get(),
		 "password_":password_e.get()
		 } )

		#Edit_.configure()
		messagebox.showinfo("Update Successfull","Your information was Successfully Updated")	
		#Edit_.destroy()
		conn.commit()
		conn.close()
	
	
	def submitemp(event):
		#sign_in.destroy()
#CHECKING FOR THE RECORD WHERE THE ENTE#1AADFF ID IS MATCHING		
		conn=sqlite3.connect("jobs.db")
		c=conn.cursor()
		c.execute("SELECT * FROM Job_Aspirants")
		ro=c.fetchall()
		##ro)
#Id.get() IS A STRING AND THE DATA WE WANT TO MATCH IS INTEGER
		global ide	
		ide=int(Id_em.get())
	#	#type(ide))
		global t
		t=int(password.get())
		##type(t))

		for i in ro:
			ck=i[0]
			##type(ck))
			if ck==ide:
	
				if t==int(i[8]):
					##type(i[8]))
				#messagebox.showinfo("JOBS","Nice Buddy"
					#Edit()
					main()	
					break

#DISPLAYING A TRY AGAIN MESSAGE WHEN ID IS INVALID
		else:
			messagebox.showerror("TRY AGAIN","Enter a valid ID")	

			#regtrr=can.create_image(400,100,image=regtr)


			Id_em.delete(0,END)
		
		
			password.delete(0,END)
		
			sign_in.destroy()
			sign_in_em_er("")
				
			#pass

		
		
		
		conn.commit()
		conn.close()
	def sign_in_em_er(event):
		#s.destroy()
		global sign_in
		sign_in=Tk()
		sign_in.configure()
		sign_in.title("Sign In Here")
		sign_in.iconbitmap("job.ico")
		
		#ID

		image1=Image.open("bgm1.jpg")
		image1=image1.resize((500,330),Image.ANTIALIAS)
		bj=ImageTk.PhotoImage(image1)
		global can
		global sign_in_
		sign_in_=Label(sign_in)
		sign_in_.pack()
		can=Canvas(sign_in_,width=1600,height=1600,bd=0,bg="white",highlightthickness=0)
		can.pack()

		sign_in_.place(x=0,y=0)
		#sign_in.resizable(False,False)

		image1=Image.open("wel_.jpg")
		image1=image1.resize((390,300),Image.ANTIALIAS)
		welc_=ImageTk.PhotoImage(image1)
		
		sn=PhotoImage(file="SIGN-IN___.png")
		
		cid=PhotoImage(file="id__.png")
		pass1=PhotoImage(file="Password_.png")
		sign_in.geometry("520x400")
		baground=can.create_image(250,140,image=bj)
		
		welcome=can.create_image(270,120,image=welc_)

		
		comid=can.create_image(65,265,image=cid)

		passwrd=can.create_image(140,305,image=pass1)
		
		sin_in=can.create_image(400,355,image=sn)
		can.tag_bind(sin_in,'<ButtonPress-1>',submitemp)
		#frame=LabelFrame(sign_in_,text="",padx=10,pady=1,height="100",bg="orange",relief=GROOVE,bd=5)
		#frame.pack(padx=0,pady=0)

		#welc=PhotoImage(file="")
		regtr=PhotoImage(file="Register_here_.png")
		reegestr=can.create_image(135,350,image=regtr)
		can.tag_bind(reegestr,'<ButtonPress-1>',register_r)
			
		global Id_em      
		Id_em=Entry(sign_in_,width=17,bd=3,justify="center",font=("arial",16))
		Id_em.pack(padx=2,pady=33,ipady=55)
		Id_em.place(x=280,y=245)
		Id_em.focus()
		#PASSWORD
		
		global password
		password=Entry(sign_in_,width=17,bd=3,justify="center",font=("arial",16))
		password.pack(padx=2,pady=33,ipady=55)
		password.place(x=280,y=290)
		#suBMIT BUTTON
		#frame3=LabelFrame(sign_in,text="",padx=10,pady=1,height="100",bg="green",relief=RIDGE,bd=1)
		#frame3.pack(padx=0,pady=0,fill=X)
		sign_in.resizable(False,False)
		Id_em.focus()	
		sign_in.configure()
		sign_in.mainloop()

	def sign_in_em(event):
		s.destroy()
			#s.destroy()
		global sign_in
		sign_in=Tk()
		sign_in.configure()
		sign_in.title("Sign In Here")
		sign_in.iconbitmap("job.ico")
		
		#ID

		image1=Image.open("bgm1.jpg")
		image1=image1.resize((500,330),Image.ANTIALIAS)
		bj=ImageTk.PhotoImage(image1)
		global can
		global sign_in_
		sign_in_=Label(sign_in)
		sign_in_.pack()
		can=Canvas(sign_in_,width=1600,height=1600,bd=0,bg="white",highlightthickness=0)
		can.pack()

		sign_in_.place(x=0,y=0)
		sign_in.resizable(False,False)

		image1=Image.open("wel_.jpg")
		image1=image1.resize((390,300),Image.ANTIALIAS)
		welc_=ImageTk.PhotoImage(image1)
		
		sn=PhotoImage(file="SIGN-IN___.png")
		
		cid=PhotoImage(file="id__.png")
		pass1=PhotoImage(file="Password_.png")
		sign_in.geometry("520x400")
		baground=can.create_image(250,140,image=bj)
		
		welcome=can.create_image(270,120,image=welc_)

		
		comid=can.create_image(65,265,image=cid)

		passwrd=can.create_image(140,305,image=pass1)
		
		sin_in=can.create_image(400,355,image=sn)
		can.tag_bind(sin_in,'<ButtonPress-1>',submitemp)
		#frame=LabelFrame(sign_in_,text="",padx=10,pady=1,height="100",bg="orange",relief=GROOVE,bd=5)
		#frame.pack(padx=0,pady=0)

		#welc=PhotoImage(file="")
		global Id_em      
		Id_em=Entry(sign_in_,width=17,bd=3,justify="center",font=("arial",16))
		Id_em.pack(padx=2,pady=33,ipady=55)
		Id_em.place(x=280,y=245)
		Id_em.focus()
		#PASSWORD
		
		global password
		password=Entry(sign_in_,width=17,bd=3,justify="center",font=("arial",16))
		password.pack(padx=2,pady=33,ipady=55)
		password.place(x=280,y=290)
		#suBMIT BUTTON
		#frame3=LabelFrame(sign_in,text="",padx=10,pady=1,height="100",bg="green",relief=RIDGE,bd=1)
		#frame3.pack(padx=0,pady=0,fill=X)
		#sign_in.resizable(False,False)
		Id_em.focus()	
		sign_in.configure()
		sign_in.mainloop()
	
	
	def submit(event):
		conn=sqlite3.connect("jobs.db")
		c=conn.cursor()
		c.execute("SELECT * FROM Job_Aspirants")
		rtu=c.fetchall()
		global id_list
		id_list=[]
		for i in rtu:
			id_list.append(str(i[0]))
		if Id.get() not in id_list :
			
			if Id.get()!=None and name_e.get()!=None and jobtype_e.get()!=None and age_e.get()!=None and Gender.get()!=None and experience_e.get()!=None and adress_e.get()!=None and number_e.get()!=None and password_e.get()!=None:
				#conn=sqlite3.connect("jobs.db")
				#c=conn.cursor()

				c.execute("CREATE TABLE IF NOT EXISTS `Job_Aspirants` (ID INTEGER NOT NULL PRIMARY KEY, Full_Name varchar(100), Job_type varchar(100), Age integer,Gender varchar(100) ,Experience varchar(35), Address varchar(100),M_Number integer,Password varchar(105) )")
				#c.execute("ALTER TABLE Job_Aspirants ADD Gender TEXT")
				c.execute("""INSERT INTO Job_Aspirants VALUES(:Id,:name_,:jobtype_,:age,:gender,:experience,:adress,:number_,
					:password)""",{"Id":Id.get(),"name_":name_e.get(),"jobtype_":jobtype_e.get(),"age":age_e.get(),"gender":
					Gender.get(),"experience":experience_e.get(),"adress":adress_e.get(),"number_":number_e.get(),"password"
					:password_e.get() } )
				#else:
				#		c.execute("INSERT INTO Job_Aspirants VALUES(:Id,:name_,:jobtype_,:age,:experience,:adress,:number_,:password)",{"Id":Id.get(),"name_":name_.get(),"jobtype_":clicked.get(),"age":age.get(),"experience":experience.get(),"adress":adress.get(),"number_":number_.get(),"password":password.get() } )
				
				
				#l.append(jobtype_.get())
				#for i in l:
				#if jobtype__.get() not in l:
				#	l.append(jobtype__.get())
				Id.delete(0,END)
				name_e.delete(0,END)
				jobtype__e.delete(0,END)
				adress_e.delete(0,END)
				number_e.delete(0,END)
				password_e.delete(0,END)
				experience_e.delete(0,END)
				age_e.delete(0,END)
				conn.commit()
				conn.close()
				register_.destroy()
				sign_in_em_er("")

			else:
				messagebox.showerror("Invalid Input","All fields are Required to be filled")
		else:
			messagebox.showerror("Invalid ID","Id is Already Taken")
			
		#r.destroy()

		#mainpage()
	def submit_r(event):
		
		conn=sqlite3.connect("jobs.db")
		c=conn.cursor()
		c.execute("SELECT * FROM Job_Aspirants")
		rtu=c.fetchall()
		global id_list
		id_list=[]
		for i in rtu:
			id_list.append(str(i[0]))
		if Id.get() not in id_list :
			
			if Id.get()!=None and name_e.get()!=None and jobtype_e.get()!=None and age_e.get()!=None and Gender.get()!=None and experience_e.get()!=None and adress_e.get()!=None and number_e.get()!=None and password_e.get()!=None:
				#conn=sqlite3.connect("jobs.db")
				#c=conn.cursor()

				c.execute("CREATE TABLE IF NOT EXISTS `Job_Aspirants` (ID INTEGER NOT NULL PRIMARY KEY, Full_Name varchar(100), Job_type varchar(100), Age integer,Gender varchar(100) ,Experience varchar(35), Address varchar(100),M_Number integer,Password varchar(105) )")
				#c.execute("ALTER TABLE Job_Aspirants ADD Gender TEXT")
				c.execute("""INSERT INTO Job_Aspirants VALUES(:Id,:name_,:jobtype_,:age,:gender,:experience,:adress,:number_,
					:password)""",{"Id":Id.get(),"name_":name_e.get(),"jobtype_":jobtype_e.get(),"age":age_e.get(),"gender":
					Gender.get(),"experience":experience_e.get(),"adress":adress_e.get(),"number_":number_e.get(),"password"
					:password_e.get() } )
				#else:
				#		c.execute("INSERT INTO Job_Aspirants VALUES(:Id,:name_,:jobtype_,:age,:experience,:adress,:number_,:password)",{"Id":Id.get(),"name_":name_.get(),"jobtype_":clicked.get(),"age":age.get(),"experience":experience.get(),"adress":adress.get(),"number_":number_.get(),"password":password.get() } )
				
				
				#l.append(jobtype_.get())
				#for i in l:
				#if jobtype__.get() not in l:
				#	l.append(jobtype__.get())
				Id.delete(0,END)
				name_e.delete(0,END)
				jobtype__e.delete(0,END)
				adress_e.delete(0,END)
				number_e.delete(0,END)
				password_e.delete(0,END)
				experience_e.delete(0,END)
				age_e.delete(0,END)
				conn.commit()
				conn.close()
				register_.destroy()
				sign_in_em("")

			else:
				messagebox.showerror("Invalid Input","All fields are Required to be filled")
		else:
			messagebox.showerror("Invalid ID","Id is Already Taken")
	def register_r(event):
		global register_
		#s.destroy()
		register_=Tk()
		register_.title("Register Here")
		register_.iconbitmap("job.ico")
		register_.geometry("423x400")
		global Id
		
		Id=Entry(register_,width=20,bd=3,justify="center")
		Id.grid(row=0,column=1)
		Id.focus()
		gender_=PhotoImage(master=register_,file="Gender.png")
		gender_b=Label(register_,image=gender_,bg="skyblue")
		gender_b.grid(row=2,column=0)
		
		#gender=Label(register_,text="3. Gender     ",bg="skyblue")
		#gender.grid(row=2,column=0)
		RadioGroup = Frame(register_)
		RadioGroup.place(x=210,y=72)

		global Gender
		Gender=StringVar()
		Male_=PhotoImage(master=register_,file="Male.png")
		Female_=PhotoImage(master=register_,file="Female.png")
		Male = Radiobutton(RadioGroup, image=Male_, variable=Gender, value="Male",bg="skyblue").pack(side=LEFT)
		
		Female = Radiobutton(RadioGroup, image=Female_, variable=Gender, value="Female",bg="skyblue").pack(side=LEFT)
		global l
		global jobtype_e
		global jobtype__e
		jobtype_e=StringVar()
		jobtype__e=ttk.Combobox(register_,width=17,textvariable=jobtype_e)
		#l=["Dermatalogistn","PGT Maths","PGT English","PGT Science","Tuitor",]
		jobtype__e["values"]=l
		
		jobtype__e.grid(row=5,column=1)
		global name_e
		name_e=Entry(register_,width=20,bd=3,justify="center")
		name_e.grid(row=1,column=1)

		register_.resizable(False,False)
		##jobtype__.get())
		#Id.focus()
		global age_e
		
		register_.resizable(False,False)
		register_.config(bg="skyblue")
		age_e=Entry(register_,width=20,bd=3,justify="center")
		age_e.grid(row=6,column=1)
		#frame=Label(register_,text="______________",bg="skyblue")	
		#frame.grid(row=9,column=0)	
		global experience_e
		#EXPERIENCE
		experience_e=Entry(register_,width=20,bd=3,justify="center")
		experience_e.grid(row=7,column=1)
		
	 #ADRESS
		address_=PhotoImage(master=register_,file="Address.png")
		address_b=Label(register_,image=address_,bg="skyblue")
		address_b.grid(row=8,column=0)
		
		#Adress=Label(register_,text="6. Adress      ",bg="skyblue")	
		#Adress.grid(row=8,column=0)	
		global adress_e
		adress_e=Entry(register_,width=20,bd=3,justify="center")
		adress_e.grid(row=8,column=1)

		global number_e
		number_e=Entry(register_,width=20,bd=3,justify="center")
		number_e.grid(row=9,column=1)
		global password_e
		password_e=Entry(register_,width=20,bd=3,justify="center")
		password_e.grid(row=10,column=1)



		#nameL=Label(register_,text="1. ID               ",bg="skyblue")
		#nameL.grid(row=0,column=0)
		Id_=PhotoImage(master=register_,file="ID.png")
		Id_b=Label(register_,image=Id_,bg="skyblue")
		Id_b.grid(row=0,column=0)
		name_=PhotoImage(master=register_,file="Full-Name.png")
		name_b=Label(register_,image=name_,bg="skyblue")
		name_b.grid(row=1,column=0)
		
		#nameL=Label(register_,text="2. Full Name",bg="skyblue")
		#nameL.grid(row=1,column=0)
		jobtype_=PhotoImage(master=register_,file="Job-Type.png")
		jobtype_b=Label(register_,image=jobtype_,bg="skyblue")
		jobtype_b.grid(row=5,column=0)
		
		#job_type=Label(register_,text="3. Job Type  ",bg="skyblue")
		#job_type.grid(row=5,column=0)	#AGE
		age_=PhotoImage(master=register_,file="Age.png")
		age_b=Label(register_,image=age_,bg="skyblue")
		age_b.grid(row=6,column=0)
		
		#Age=Label(register_,text="4. Age          ",bg="skyblue")
		#Age.grid(row=6,column=0)
		exp_=PhotoImage(master=register_,file="Experience.png")
		exp_b=Label(register_,image=exp_,bg="skyblue")
		exp_b.grid(row=7,column=0)
		
		#Experience=Label(register_,text="5. Experience",bg="skyblue")
		#Experience.grid(row=7,column=0)	
		number_=PhotoImage(master=register_,file="Contact-Number.png")
		number_b=Label(register_,image=number_,bg="skyblue")
		number_b.grid(row=9,column=0)
		
		#Number=Label(register_,text="7. P.Number",bg="skyblue")
		#Number.grid(row=8,column=0)	#PASSWORD
		pass_=PhotoImage(master=register_,file="Password.png")
		pass_b=Label(register_,image=pass_,bg="skyblue")
		pass_b.grid(row=10,column=0)
		global a
		global b
		global c
		global d
		global e
		global f
		global g
		global h1
		global i
		a=Id.get()
		b=name_e.get()
		c=str(jobtype_e.get())
		d=age_e.get()
		e=Gender.get()
		f=experience_e.get()
		g=adress_e.get()
		h=number_e.get()
		i=password_e.get()
		#Password=Label(register_,text="8. Password",bg="skyblue")
		#Password.grid(row=9,column=0)
		submit_=PhotoImage(master=register_,file="SUBMIT.png")
		submit_b=Label(register_,image=submit_,bg="skyblue")
		submit_b.grid(row=12,column=0,columnspan=2,padx=25,pady=10,ipadx=53)
		submit_b.bind("<Button-1>",submit_r)
		register_.configure()
		register_.mainloop()

	def register_2(event):
		global register_
		s.destroy()
		register_=Tk()
		register_.title("Register Here")
		register_.iconbitmap("job.ico")
		register_.geometry("423x400")
		global Id
		
		Id=Entry(register_,width=20,bd=3,justify="center")
		Id.grid(row=0,column=1)
		Id.focus()
		gender_=PhotoImage(file="Gender.png")
		gender_b=Label(register_,image=gender_,bg="skyblue")
		gender_b.grid(row=2,column=0)
		
		#gender=Label(register_,text="3. Gender     ",bg="skyblue")
		#gender.grid(row=2,column=0)
		RadioGroup = Frame(register_)
		RadioGroup.place(x=210,y=72)

		global Gender
		Gender=StringVar()
		Male_=PhotoImage(file="Male.png")
		Female_=PhotoImage(file="Female.png")
		Male = Radiobutton(RadioGroup, image=Male_, variable=Gender, value="Male",bg="skyblue").pack(side=LEFT)
		
		Female = Radiobutton(RadioGroup, image=Female_, variable=Gender, value="Female",bg="skyblue").pack(side=LEFT)
		
		global jobtype_e
		global jobtype__e
		jobtype_e=StringVar()
		jobtype__e=ttk.Combobox(register_,width=17,textvariable=jobtype_e)
		#l=["Dermatalogistn","PGT Maths","PGT English","PGT Science","Tuitor",]
		jobtype__e["values"]=l
		
		jobtype__e.grid(row=5,column=1)
		global name_e
		name_e=Entry(register_,width=20,bd=3,justify="center")
		name_e.grid(row=1,column=1)

		register_.resizable(False,False)
		##jobtype__.get())
		#Id.focus()
		global age_e
		
		register_.resizable(False,False)
		register_.config(bg="skyblue")
		age_e=Entry(register_,width=20,bd=3,justify="center")
		age_e.grid(row=6,column=1)
		#frame=Label(register_,text="______________",bg="skyblue")	
		#frame.grid(row=9,column=0)	
		global experience_e
		#EXPERIENCE
		experience_e=Entry(register_,width=20,bd=3,justify="center")
		experience_e.grid(row=7,column=1)
		
	 #ADRESS
		address_=PhotoImage(file="Address.png")
		address_b=Label(register_,image=address_,bg="skyblue")
		address_b.grid(row=8,column=0)
		
		#Adress=Label(register_,text="6. Adress      ",bg="skyblue")	
		#Adress.grid(row=8,column=0)	
		global adress_e
		adress_e=Entry(register_,width=20,bd=3,justify="center")
		adress_e.grid(row=8,column=1)

		global number_e
		number_e=Entry(register_,width=20,bd=3,justify="center")
		number_e.grid(row=9,column=1)
		global password_e
		password_e=Entry(register_,width=20,bd=3,justify="center")
		password_e.grid(row=10,column=1)



		#nameL=Label(register_,text="1. ID               ",bg="skyblue")
		#nameL.grid(row=0,column=0)
		Id_=PhotoImage(file="ID.png")
		Id_b=Label(register_,image=Id_,bg="skyblue")
		Id_b.grid(row=0,column=0)
		name_=PhotoImage(file="Full-Name.png")
		name_b=Label(register_,image=name_,bg="skyblue")
		name_b.grid(row=1,column=0)
		
		#nameL=Label(register_,text="2. Full Name",bg="skyblue")
		#nameL.grid(row=1,column=0)
		jobtype_=PhotoImage(file="Job-Type.png")
		jobtype_b=Label(register_,image=jobtype_,bg="skyblue")
		jobtype_b.grid(row=5,column=0)
		
		#job_type=Label(register_,text="3. Job Type  ",bg="skyblue")
		#job_type.grid(row=5,column=0)	#AGE
		age_=PhotoImage(file="Age.png")
		age_b=Label(register_,image=age_,bg="skyblue")
		age_b.grid(row=6,column=0)
		
		#Age=Label(register_,text="4. Age          ",bg="skyblue")
		#Age.grid(row=6,column=0)
		exp_=PhotoImage(file="Experience.png")
		exp_b=Label(register_,image=exp_,bg="skyblue")
		exp_b.grid(row=7,column=0)
		
		#Experience=Label(register_,text="5. Experience",bg="skyblue")
		#Experience.grid(row=7,column=0)	
		number_=PhotoImage(file="Contact-Number.png")
		number_b=Label(register_,image=number_,bg="skyblue")
		number_b.grid(row=9,column=0)
		
		#Number=Label(register_,text="7. P.Number",bg="skyblue")
		#Number.grid(row=8,column=0)	#PASSWORD
		pass_=PhotoImage(file="Password.png")
		pass_b=Label(register_,image=pass_,bg="skyblue")
		pass_b.grid(row=10,column=0)
		global a
		global b
		global c
		global d
		global e
		global f
		global g
		global h1
		global i
		a=Id.get()
		b=name_e.get()
		c=str(jobtype_e.get())
		if c not in l:
			l.append(c)
		d=age_e.get()
		e=Gender.get()
		f=experience_e.get()
		g=adress_e.get()
		h=number_e.get()
		i=password_e.get()
		#Password=Label(register_,text="8. Password",bg="skyblue")
		#Password.grid(row=9,column=0)
		submit_=PhotoImage(file="SUBMIT.png")
		submit_b=Label(register_,image=submit_,bg="skyblue")
		submit_b.grid(row=12,column=0,columnspan=2,padx=25,pady=10,ipadx=53)
		submit_b.bind("<Button-1>",submit)
		register_.configure()
		register_.mainloop()
		
	def Edit1(event):
		#import Tkinter as tk
	
		Edit_=Toplevel(root)
		Edit_.title("Edit Your Account Information")
		Edit_.iconbitmap("job.ico")
		Edit_.geometry("403x430")
		global Id
		
		Id=Entry(Edit_,width=20,justify="center")
		Id.grid(row=0,column=1)
		Id.focus()
		global jobtype_e
		global jobtype__e
		jobtype_e=StringVar()
		jobtype__e=ttk.Combobox(Edit_,width=17,textvariable=jobtype_e)
		#l=["Dermatalogistn","PGT Maths","PGT English","PGT Science","Tuitor",]

		jobtype__e["values"]=l
		
		jobtype__e.grid(row=2,column=1)
		global name_e
		name_e=Entry(Edit_,width=20,justify="center")
		name_e.grid(row=1,column=1)

		Edit_.resizable(False,False)
		##jobtype__.get())
		#Id.focus()
		global age_e
		
		#.resizable(False,False)
		Edit_.config(bg="skyblue")
		age_e=Entry(Edit_,width=20,justify="center")
		age_e.grid(row=3,column=1)
		global experience_e
		#EXPERIENCE

		experience_e=Entry(Edit_,width=20,justify="center")
		experience_e.grid(row=4,column=1)
	
		global adress_e
		adress_e=Entry(Edit_,width=20,justify="center")
		adress_e.grid(row=6,column=1)

		global number_e
		number_e=Entry(Edit_,width=20,justify="center")
		number_e.grid(row=5,column=1)
		global password_e
		password_e=Entry(Edit_,width=20,justify="center")
		password_e.grid(row=7,column=1)



		#nameL=Label(register_,text="1. ID               ",bg="skyblue")
		#nameL.grid(row=0,column=0)	address_=PhotoImage(file="Address.png")
		'''address_=PhotoImage(file="Address.png")
		address_b=Label(Edit_,image=address_,bg="skyblue")
		address_b.grid(row=6,column=0)'''
		global Id_
		Id_=PhotoImage(file="ID.png")
		Id_b=Label(Edit_,image=Id_,bg="skyblue")
		Id_b.grid(row=0,column=0)
		global name_
		name_=PhotoImage(file="Full-Name.png")
		name_b=Label(Edit_,image=name_,bg="skyblue")
		name_b.grid(row=1,column=0)
		global jobtype_
		#nameL=Label(register_,text="2. Full Name",bg="skyblue")
		#nameL.grid(row=1,column=0)
		jobtype_=PhotoImage(file="Job-Type.png")
		jobtype_b=Label(Edit_,image=jobtype_,bg="skyblue")
		jobtype_b.grid(row=2,column=0)
		global address_
		address_=PhotoImage(file="Address.png")
		address_b=Label(Edit_,image=address_,bg="skyblue")
		address_b.grid(row=6,column=0)
		global age_
		#job_type=Label(register_,text="3. Job Type  ",bg="skyblue")
		#job_type.grid(row=5,column=0)	#AGE
		age_=PhotoImage(file="Age.png")
		age_b=Label(Edit_,image=age_,bg="skyblue")
		age_b.grid(row=3,column=0)
		global exp_
		#Age=Label(register_,text="4. Age          ",bg="skyblue")
		#Age.grid(row=6,column=0)
		exp_=PhotoImage(file="Experience.png")
		exp_b=Label(Edit_,image=exp_,bg="skyblue")
		exp_b.grid(row=4,column=0)
		global number_
		#Experience=Label(register_,text="5. Experience",bg="skyblue")
		#Experience.grid(row=7,column=0)	
		number_=PhotoImage(file="Contact-Number.png")
		number_b=Label(Edit_,image=number_,bg="skyblue")
		number_b.grid(row=5,column=0)
		global pass_
		#Number=Label(register_,text="7. P.Number",bg="skyblue")
		#Number.grid(row=8,column=0)	#PASSWORD
		pass_=PhotoImage(file="Password.png")
		pass_b=Label(Edit_,image=pass_,bg="skyblue")
		pass_b.grid(row=7,column=0)
		global submit_
		submit_=PhotoImage(file="SUBMIT.png")
		submit_b=Label(Edit_,image=submit_,bg="skyblue")
		submit_b.grid(row=12,column=0,columnspan=2,padx=25,pady=10,ipadx=53)
		submit_b.bind("<Button-1>",Update)
		conn=sqlite3.connect("jobs.db")		
		c=conn.cursor()
		c.execute("SELECT * FROM Job_Aspirants")
		ro=c.fetchall()
		#ro)
		#ide=Id.get()
		for i in ro:
			ck=i[0]
			
			if ck==ide:
							
				
				#l)
				s=len(l)

				s=s-1
				Id.insert(0,i[0])
				name_e.insert(0,i[1])
				
				jobtype__e.current(s)
				rt_=jobtype__e.current(s)
				
				if rt_ not in l:
					l.append(rt_)
				age_e.insert(0,i[3])
					
				experience_e.insert(0,i[5])
 #Adressglob\\		
				adress_e.insert(0,i[6])
					
				number_e.insert(0,i[7])
				password_e.insert(0,i[8])
		conn.commit()
		conn.close()








	

	mainpage_.destroy()
	global s
	s=Tk()
	global a
	global b
	a="510"
	b="520"
	s.geometry(a+"x"+b)
	s.config(bg="white")
	s.title("A Job : Give or Get")
	s.iconbitmap("job.ico")
	def g(event):
		print()
	def f(event):
		signl=Label(r,image=sign1)
		signl.pack()
		signl.bind("<Button-1>",g)
	image=Image.open("12.png")
	image=image.resize((510,500),Image.ANTIALIAS)
	m=ImageTk.PhotoImage(image)
	s.resizable(False,False)
	bh=PhotoImage(file="start.png")
	sign=PhotoImage(file="Sign-in.png")
	sign1=PhotoImage(file="Sign-Up.png")
	sign2=PhotoImage(file="JOBS- (1).png")
	r=Label(s,image=m)
	r.pack()
	r.place(x=0,y=0)
	image1=Image.open("list.png")
	image1=image1.resize((50,50),Image.ANTIALIAS)
	m1=ImageTk.PhotoImage(image1)

	 
	r1=Label(s,image=m1,bg="white")
	r1.pack()
	r1.place(x=5,y=430)


	image2=Image.open("sign_up__.png")
	image2=image2.resize((50,50),Image.ANTIALIAS)
	m2=ImageTk.PhotoImage(image2)

	r2=Label(s,image=m2,bg="white")
	r2.pack()
	r2.place(x=280,y=430)
		
	job=Label(s,image=sign2,bg="white")
	job.pack()

	#signl=Button(r,image=sign,command=f)
	#signl.pack()
	job.place(x=130,y=2)
	#signl=Button(r,image=sign1,command=f,relief=GROOVE)
	#signl.pack()
	Signin=Label(s,image=sign,bg="white")
	Signin.pack()
	Signin.place(x=60,y=430)

	Signin.bind("<Button-1>",sign_in_em)
	
	r1.bind("<Button-1>",sign_in_em)

	signup=Label(s,image=sign1,bg="white")
	signup.pack()
	signup.place(x=330,y=430)

	signup.bind("<Button-1>",register_2)
	r2.bind("<Button-1>",register_2)
	
	s.mainloop()
def compa(event):
	def UpdateC():
		conn=sqlite3.connect("jobs.db")
		c=conn.cursor()
		#if clicked.get()=="Choose Job Type":
		c.execute("""UPDATE Company
		 SET Company_Id =:id_,
		 Company_Name=:name_,
		 Company_Adress=:address,
		 Vacancy=:vacant,
		 Contact_Number=:Cnum,
		 Employee_Number=:Enum,
		 Password=:password_ 
		 WHERE ID=:Id """,
		 {"id_":C_Id_.get(),
		 "name_":Cname_.get(),
		 "address":adress.get(),
		 "vacant":stats.get(),
		 "Cnum":Cnumber.get(),
		 "Enum":employee.get(),
		 "password_":pass_.get()
		 } )

		EditC.configure()
		messagebox.showinfo("Update Successfull","Your information was Successfully Updated")	
		EditC.destroy()
		conn.commit()
		conn.close()
	def EditC(event):
		o=Tk()
		o.title("Update Here")
		o.config(bg="#f46262")
		o.geometry('500x250')
		tl=Label(o,text="Make Changes in your Data                          ",font=("Seoge Print",20,"bold"),bg="#FFFF00")
		tl.grid(row=0,column=0,columnspan=2,rowspan=2)

		global noavail
		global avail
		global adress
		global Cname_
		global employee
		global C_Id_ 
		global pass_
		global stats
		global Cnumber
		C_Id=Label(o,text="1.Generate Company Id",bg="#f46262",font=("Seoge Print",9)	)
		C_Id.grid(row=2,column=0)	
		C_Id_=Entry(o,justify="center",font=("Seoge Print",9))
		C_Id_.grid(row=2,column=1)
		Cname=Label(o,text="2. Company Name      ",bg="#f46262",font=("Seoge Print",9))	
		Cname.grid(row=3,column=0)	
		Cname_=Entry(o,justify="center",font=("Seoge Print",9))
		Cname_.grid(row=3,column=1)
		
		Adress=Label(o,text="3. Company Main Branch Adress      ",bg="#f46262",font=("Seoge Print",9))	
		Adress.grid(row=4,column=0)	
		adress=Entry(o,justify="center",font=("Seoge Print",9))
		adress.grid(row=4,column=1)
		Employee=Label(o,text="4. Total Number of Employees",bg="#f46262",font=("Seoge Print",9))	
		Employee.grid(row=5,column=0)	
		employee=Entry(o,justify="center",font=("Seoge Print",9))
		employee.grid(row=5	,column=1)

		Employee=Label(o,text="5. Vacancy Status",bg="#f46262",font=("Seoge Print",9))	
		Employee.grid(row=6,column=0)	
		global stats
		RadioGroup1=Frame(o)
		RadioGroup1.grid(row=6,column=1)
		stats=StringVar()
		avail = Checkbutton(RadioGroup1, text="Available", variable=stats,onvalue="Yes"  , font=('Seoge Print', 8),bg="#f46262",command=yes1).pack(side=LEFT)
		noavail = Checkbutton(RadioGroup1, text="Unavailable", variable=stats,onvalue="No",  font=('Seoge Print', 8),bg="#f46262",command=no1).pack(side=LEFT)
		avail.deselect()
		noavail.deselect()
		num=Label(o,text="6. Contact Number",bg="#f46262",font=("Seoge Print",9))	
		num.grid(row=7,column=0)	
		
		Cnumber=Entry(o,justify="center",font=("Seoge Print",9))
		Cnumber.grid(row=7	,column=1)
		
		pass__=Label(o,text="7. Generate Password",bg="#f46262",font=("Seoge Print",9))	
		pass__.grid(row=8,column=0)	
		pass_=Entry(o,justify="center",font=("Seoge Print",9))
		pass_.grid(row=8,column=1)
		
		reg=Button(o,text="Submit",fg="Black",relief=SUNKEN,command=UpdateC,font=("Seoge Print",9))
		reg.grid(row=9,column=1)
		o.resizable(False,False)
		#employee=Entry(o,width=20,justify="center")
		#employee.grid(row=5	,column=1)
		conn=sqlite3.connect("jobs.db")
		c=conn.cursor()
		c.execute("SELECT *,oid FROM Company")
		ro=c.fetchall()
		
		for i in ro:
			ck=i[0]
		
			if ck==idec:
				
				
				
					
				Cname_.insert(0,i[1])
				employee.insert(0,i[5])	
					
				C_Id_.insert(0,i[0])
					
				#.insert(0,i[4])
 #Adressglob\\		
				adress.insert(0,i[2])
					
				Cnumber.insert(0,i[4])
				pass_.insert(0,i[6])


					


					
					#register_.quit()
				break		

		o.mainloop()
		
	def yes1():
		stats.set("Available")
		avail.select()

	def no1():
		stats.set("Unavailable")
		noavail.select()
	def submit1(event):
		if C_Id_.get()!="" and  Cname_.get()!="" and adress.get()!="" and Cnumber.get()!="" and employee.get()!="" and pass_.get()!="" :
			conn=sqlite3.connect("jobs.db")
			c=conn.cursor()
			c.execute("CREATE TABLE IF NOT EXISTS `Company` (Company_Id varchar(30), Company_Name varchar(60), Company_Adress varchar(100),Vacancy varchar(40),Contact_Number varchar(40),Employee_Number integer,Password varchar(45) )")
			#c.execute("ALTER TABLE Job_Aspirants ADD GenderEXT")
			c.execute("INSERT INTO 'Company' VALUES(:Id,:name_,:address_,:Vacancy,:contact,:number_,:password)",{"Id":C_Id_.get(),"name_":Cname_.get(),"address_":adress.get(),"Vacancy":stats.get(),"contact":Cnumber.get(),"number_":employee.get(),"password":pass_.get() } )
			#else:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa adress
															
			#l.append(jobtype_.get())
			#for i in l:
			#if jobtype__.get() not in l:
			#	l.append(jobtype__.get())
			#noavail.deselect()
			#avail.deselect()
			C_Id_.delete(0,END)
			Cname_.delete(0,END)
			pass_.delete(0,END)
			adress.delete(0,END)
			employee.delete(0,END)
			Cnumber.delete(0,END)
			
			conn.commit()
			conn.close()
			
			#r.destroy()
			signin23("")
		else:
			messagebox.showerror("Invalid Input","Fill all the Entries")

	def main1():
		global Gender1
		Gender1.set("Male")

	def main2():
		global Gender1
		Gender1.set("Female")
	def main():
	
		tree.delete(*tree.get_children())
		connn=sqlite3.connect("jobs.db")
		c=connn.cursor()
		c.execute("SELECT *,oid FROM Job_Aspirants WHERE  Gender=:gender AND Job_Type=:jobtype AND Experience BETWEEN :a AND :b AND Age BETWEEN :x AND :y",{"gender":Gender1.get(),"jobtype":jobtype__.get(),"a":fro3_.get(),"b":fro4_.get(),"x":fro1__.get(),"y":fro2__.get()} )
		ro=c.fetchall()
	
		
		re.configure()
		for i in ro:
			tree.insert('','end',values=(i))
		connn.commit()
		connn.close()
		##Gender1)
	#def spec():
	#	main()

	#	main()

	def specific(event):
		global re
		re=Tk()
		re.resizable(False,False)
		re.config(bg="skyblue")
		re.title("Contact List")
		re.geometry("330x300")
		t=Label(re,text="Apply Some Filters Give Below",bg="Blue",bd=10,fg="white",relief=GROOVE,font=("times new roman",17,"bold"))
		t.pack(fill=X)
		t.place(y=0,x=0)
		gender=Label(re,text=" Gender    :",width =15,bg="skyblue")
		gender.pack()
		gender.place(x=0,y=80)
		RadioGroup1= Frame(re)
		RadioGroup1.place(x=90,y=80)
		global Gender1
		Gender1=StringVar()
		Male = Checkbutton(RadioGroup1, text="Male", variable=Gender1,onvalue="Male"  , font=('arial', 8),bg="skyblue",command=main1).pack(side=LEFT)
		Female = Checkbutton(RadioGroup1, text="Female", variable=Gender1,onvalue="Female",  font=('arial', 8),bg="skyblue",command=main2).pack(side=LEFT)

		global y
		##Males.get())
		
		
		
		#global Gender_
		#Gender_=""
		#Male = Radiobutton(RadioGroup, text="Male", variable=Gender_, value="Male",  font=('arial', 8),bg="skyblue").pack(side=LEFT)

		#Female = Radiobutton(RadioGroup, text="Female", variable=Gender_, value="Female",  font=('arial', 8),bg="skyblue").pack(side=LEFT)
		#Female.place(x=40,y=40)
		
		
		global jobtype__
		jobtype_=StringVar()
		jobtype__=ttk.Combobox(re,width=17,textvariable=jobtype_)
		
		jobtype__["values"]=l
		jobtype__.pack()
		jobtype__.place(x=90,y=60)
		frame=Label(re,text="Jobtype   :",bg="skyblue")
		frame.pack(padx=0,pady=10)
		frame.place(x=25,y=60)
		age=Label(re,text="Age         : ",bg="skyblue")
		age.pack(padx=20,pady=20)
		age.place(x=30,y=104)
		bet=Label(re,text="To",bg="skyblue")
		bet.pack()
		bet.place(x=130,y=104)
		global fro1__
		fro1_=StringVar()
		fro1__=ttk.Combobox(re,width=2,textvariable=fro1_)
		cnt=[]
		for i in range(15,81):
			cnt.append(i)
		fro1__["values"]=cnt
		fro1__.pack()
		fro1__.place(x=90,y=104)
		global fro2__
		fro2_=StringVar()
		fro2__=ttk.Combobox(re,width=2,textvariable=fro2_)
		cnt=[]
		for i in range(15,81):
			cnt.append(i)
		fro2__.pack()
		fro2__["values"]=cnt
		fro2__.place(x=150,y=104)


		exp=Label(re,text="Experience :",bg="skyblue")
		exp.pack(padx=20,pady=20)
		exp.place(x=20,y=134)
		bet=Label(re,text="To",bg="skyblue")
		bet.pack()
		bet.place(x=130,y=134)
		bet=Label(re,text="(in years)",bg="skyblue")
		bet.pack()
		bet.place(x=185,y=134)
		global fro3_
		fro1=StringVar()
		fro3_=ttk.Combobox(re,width=2,textvariable=fro1)
		cnt=[]
		for i in range(15,81):
			cnt.append(i)


		fro3_["values"]=cnt
		fro3_.pack()
		#fro=Entry(r,width=2)
		#fro.pack()
		fro3_.place(x=90,y=134)
	#fro=Entry(r,width=2)
	#fro.pack()
		global fro4_
		fro2=StringVar()
		fro4_=ttk.Combobox(re,width=2,textvariable=fro2)
		cnt=[]
		for i in range(15,81):
			cnt.append(i)
		fro4_.pack()

		fro4_["values"]=cnt

		fro4_.place(x=150,y=134)
		srh=Button(re,text="search",relief=SUNKEN,width=25,bd=4		,bg="orange",fg="purple",command=main)
		srh.pack()
		srh.place(x=45,y=176)
	#global sign2
	#sign2=Entry(r,width=20)

	#sign.insert(0,"Enter Jobtype here")
	#sign2.pack()
	#sign2.place(x=82,y=3)

		re.mainloop()
	def z(event):
		tree1.delete(*tree1.get_children())
		conn=sqlite3.connect("jobs.db")
		c=conn.cursor()
		if jobtype__c.get()!="All Jobtypes":
			c.execute("SELECT *,oid FROM Job_Aspirants WHERE Job_type=:job",{"job":jobtype__c.get()})
		else:
			c.execute("SELECT *,oid FROM Job_Aspirants") 
		ro=c.fetchall()

		root1.configure()
		fr2=Image.open("officer.png")
		fr2=fr2.resize((28,25),Image.ANTIALIAS)
		frt2=ImageTk.PhotoImage(fr2,master=root1)

		for i in ro:
			tree1.insert('','end',text="",image=frt2,values=(i),tags=('aj',))
		root1.configure()
		conn.commit()
		conn.close()
	def final_resume__(event):		

		from tkinter import Text, Tk
		from tkinter.ttk import Progressbar
		#mainpage_.destroy()

		import tkinter.ttk as ttk
		global resume_f__
		#root.destroy()
		resume_f__= Tk()
		resume_f__.config(bg="#FFFFFF")
		resume_f__.title("CV (Resume)")
		resume_f__.iconbitmap("job.ico")
		resume_f__.resizable(False,False)
		resume_f__.geometry("795x680")
		#resume_.wm_attributes("-alpha",0.7)
		#r=Scale(resume_,from_=1,to=100000,orient=HORIZONTAL,bg="BLUE",fg="red")
		#r.pack()
		Name_tx=StringVar()
		Adress_tx=StringVar()
		Number_tx=StringVar()
		Email_tx=StringVar()
		Facebook_tx=StringVar()
		Twitter_tx=StringVar()
		Linkedin_tx=StringVar()
		Profile_tx=StringVar()
		Work1_From_tx=StringVar()
		Work1_To_tx=StringVar()
		Work1_Post_tx=StringVar()
		Work1_City_tx=StringVar()
		Work1_CompanyName_tx=StringVar()
		Work1_CompanyDesc_tx=StringVar()
		Work2_From_tx=StringVar()
		Work2_To_tx=StringVar()
		Work2_Post_tx=StringVar()
		Work2_City_tx=StringVar()
		Work2_CompanyName_tx=StringVar()

		Work2_CompanyDesc_tx=StringVar()
		Education1_From_tx=StringVar()
		Education1_To_tx=StringVar()
		Education1_Institute_tx=StringVar()
		Education1_City_tx=StringVar()
		Education1_Qualifications_tx=StringVar()
		Education2_From_tx=StringVar()
		Education2_To_tx=StringVar()
		Education2_Institute_tx=StringVar()
		Education2_City_tx=StringVar()
		Education2_Qualifications_tx=StringVar()
		Skill_1_tx=StringVar()
		Skill_2_tx=StringVar()
		Skill_3_tx=StringVar()
		Skill_4_tx=StringVar()
		lvl_1_tx=IntVar()
		lvl_2_tx=IntVar()
		lvl_3_tx=IntVar()
		lvl_4_tx=IntVar()
		#centr_=StringVar()
		conn=sqlite3.connect("resum.db")
		
		c=conn.cursor()
		c.execute("SELECT * FROM Resume3")
		dr=c.fetchall()
		#idel)
		
		#type(idel))


		for i in dr:
			#)
			#type(i[0]))

			#)
			if int(i[0])==ide1:
				Name_tx.set(i[1])
				Adress_tx.set(i[2])
				Number_tx.set(i[3])

				Email_tx.set(i[4])
				Facebook_tx.set(i[5])
				Twitter_tx.set(i[6])
				Linkedin_tx.set(i[7])
				Profile_tx.set(i[8]) 
				Work1_From_tx.set(i[9])
				Work1_To_tx.set(i[10])
				Work1_Post_tx.set(i[11])
				Work1_City_tx.set(i[12])
				Work1_CompanyName_tx.set(i[13])
				Work1_CompanyDesc_tx.set(i[14])
				Work2_From_tx.set(i[15])
				Work2_To_tx.set(i[16])
				Work2_Post_tx.set(i[17])
				Work2_City_tx.set(i[18])
				Work2_CompanyName_tx.set(i[19])

				Work2_CompanyDesc_tx.set(i[20])
				Education1_From_tx.set(i[21])
				Education1_To_tx.set(i[22])
				Education1_Institute_tx.set(i[23])
				Education1_City_tx.set(i[24])
				Education1_Qualifications_tx.set(i[25])
				Education2_From_tx.set(i[26])
				Education2_To_tx.set(i[27])
				Education2_Institute_tx.set(i[28])
				Education2_City_tx.set(i[29])
				Education2_Qualifications_tx.set(i[30])
				Skill_1_tx.set(i[32])

				Skill_2_tx.set(i[33])
				Skill_3_tx.set(i[33])
				Skill_4_tx.set(i[34])
				lvl_1_tx.set(i[35])
				lvl_2_tx.set(i[36])
				lvl_3_tx.set(i[37])
				lvl_4_tx.set(i[38])
				#i[39])

				centr=i[39]
				#type(centr))
				
		#dr)
		conn.commit()
		conn.close()
		
		def progrs(event):
			progress['value']=50
		import os
				
		global bgm
		global img
		global img1
		l=Label(resume_f__,bg="white")
		#global c
		c=Canvas(l,width=600,height=1200,bd=0,bg="white",highlightthickness=0)
		#img1=PhotoImage(file="bgmp.png")
		img1=Image.open("back10.jpg")
		img=PhotoImage(master=c,file="Profile.png")

		img1=img1.resize((606,742),Image.ANTIALIAS)
		img3_=ImageTk.PhotoImage(img1,master=c)
		
		d1=c.create_image(320,310,image=img3_)
		d=c.create_image(150,30,image=img)

		c.pack()
		
		l.pack()
		l.place(x=220,y=0)
		
		global c1
		l1=Label(resume_f__)
		c1=Canvas(l1,width=250,height=1700,bd=0,highlightthickness=0)
		img_=PhotoImage(file="NAME21.png",master=c1)
		img2=Image.open("back8.jpg")
		submit_=PhotoImage(file="Submit__1.png",master=c1)
		submt_=c.create_image(900,100,image=submit_)
		
		img2=img2.resize((340,1000),Image.ANTIALIAS)
		img1_=ImageTk.PhotoImage(img2,master=c1)
		d1=c1.create_image(80,320,image=img1_)
		
		#img21=Image.open("bgm1.jpg")
		
		#3img21=img21.resize((300,700),Image.ANTIALIAS)
		#img11_=ImageTk.PhotoImage(img21,master=c1)
		#)
		#d11=c1.create_image(110,700,image=img11_)
		

		d2=c1.create_image(75,294,image=img_)
		
		c1.pack()
		#c1.place(x=0,y=0)
		l1.pack()
		l1.place(x=0,y=0)
		
		global n
		n="bg3.png"
		mag=Image.open(n)
		global frame1
		mag=mag.resize((110,110),Image.ANTIALIAS)
		mag1=ImageTk.PhotoImage(mag,master=c1)
		frame1=c1.create_image(90,70,image=mag1)
		#frame1.place(x=10,y=10)
		'''
		m="add-user.png"
		mag4=Image.open(m)
		mag4=mag4.resize((30,30),Image.ANTIALIAS)
		mag5=ImageTk.PhotoImage(mag4,master=c1)
		frame2=c1.create_image(170,110,image=mag5)
		c1.tag_bind(frame2,'<ButtonPress-1>',photo)
		'''
		#global centr
		Info_=PhotoImage(master=c1,file="INFO.png")
		Info=c1.create_image(92,254,image=Info_)
		conct=Image.open("user.png")
		conct=conct.resize((30,30),Image.ANTIALIAS)
		conct__=ImageTk.PhotoImage(conct,master=c1)
		
		conct_=c1.create_image(35,290,image=conct__)
		##centr)
		conn=sqlite3.connect("resum.db")
		
		cur=conn.cursor()
		cur.execute("SELECT * FROM Resume3")
		dr=cur.fetchall()
		

		global centr_
		for i in dr:
			#)
			#type(idel))
			if int(i[0])==ide1:
				#type(i[0]))
				centr_=i[39]
				#centr_)
				break
		#centr_)
		rot3__=Image.open(centr_)
		
		rot3__=rot3__.resize((70,70),Image.ANTIALIAS)
		rot1__=ImageTk.PhotoImage(rot3__,master=c1)
		frame1=c1.create_image(90,70,image=rot1__)
			
		
		adres=Image.open("map.png")
		adres=adres.resize((30,30),Image.ANTIALIAS)
		adres_=ImageTk.PhotoImage(adres,master=c1)
		addres=c1.create_image(35,332,image=adres_)
		adress_img=PhotoImage(master=c1,file="Addressw.png")
		adress_w=c1.create_image(84,332,image=adress_img)


		


		phone=Image.open("telephone.png")
		phone=phone.resize((30,30),Image.ANTIALIAS)
		phone_=ImageTk.PhotoImage(phone,master=c1)
		phone_img=PhotoImage(master=c1,file="Phonew.png")
		phne_w=c1.create_image(75,373,image=phone_img)
		phoone=c1.create_image(35,368,image=phone_)
			


		Email1=Image.open("gmail.png")
		Email1=Email1.resize((30,30),Image.ANTIALIAS)
		Email_=ImageTk.PhotoImage(Email1,master=c1)
		
		Email_img=PhotoImage(master=c1,file="Emailw.png")
		Emai_w=c1.create_image(75,412,image=Email_img)
		Emaill=c1.create_image(35,412,image=Email_)
		#reds=c1.create_line(0,226,296,226,width=2)
		#reds1=c1.create_line(0,259,296,259,width=2)

	 
		
		social_=PhotoImage(master=c1,file="SOCIAL.png")
		Social=c1.create_image(95,480,image=social_)
		
		#reds=c1.create_line(0,459,296,459,width=2)
		#reds1=c1.create_line(0,494,296,494,width=2)
	 	
			

		
		fb=Image.open("facebook.png")
		fb=fb.resize((30,30),Image.ANTIALIAS)
		fb_=ImageTk.PhotoImage(fb,master=c1)
		facbk=c1.create_image(35,520,image=fb_)
		fb_img=PhotoImage(master=c1,file="Facebookw.png")
		fb_w=c1.create_image(90,520,image=fb_img)
	 
		
	 	
		
		twt=Image.open("twitter_.png")
		twt=twt.resize((30,30),Image.ANTIALIAS)
		twt_=ImageTk.PhotoImage(twt,master=c1)

		twt_img=PhotoImage(master=c1,file="Twitter.png")
		twt_w=c1.create_image(85,570,image=twt_img)
		twitwr=c1.create_image(35,570,image=twt_)


	 	
		lnk=Image.open("linkedin_.png")
		lnk=lnk.resize((30,30),Image.ANTIALIAS)
		lnk_=ImageTk.PhotoImage(lnk,master=c1)

		lnk_img=PhotoImage(master=c1,file="Linkedin.png")
		lnk_w=c1.create_image(85,620,image=lnk_img)
		lnkdin=c1.create_image(35,620,image=lnk_)
		profe=Image.open("user.png")
		profe=profe.resize((44,44),Image.ANTIALIAS)
		profe__=ImageTk.PhotoImage(profe,master=c1)
		profe_=c.create_image(75,30,image=profe__)
	 	
		
		wrke__img=PhotoImage(master=c,file="WORK-EXPERIENCE.png")
		wrke_im=c.create_image(210,140,image=wrke__img)
		wrke=Image.open("edit.png")
		wrke=wrke.resize((44,44),Image.ANTIALIAS)
		wrke__=ImageTk.PhotoImage(wrke,master=c)
		wrke_1=c.create_image(75,140,image=wrke__)
	 
		educ__img=PhotoImage(master=c,file="EDUCATION.png")
		educ_im=c.create_image(185,320,image=educ__img)
		educ=Image.open("graduation-hat.png")
		educ=educ.resize((44,44),Image.ANTIALIAS)
		educ__=ImageTk.PhotoImage(educ,master=c)
		educ_1=c.create_image(75,320,image=educ__)
		

		education1_num=c.create_text(110,345,text="1.",fill="Black",font=("comic sans ms",12))
		education1_from=c.create_text(144,355,text=Education1_From_tx.get(),fill="black",font=("comic sans ms",11))
		education1_to=c.create_text(198,355,fill="Black",text=Education1_To_tx.get(),font=("comic sans ms",11))
		education1_city=c.create_text(167,376,text=Education1_City_tx.get(),fill="Black",font=("comic sans ms",10))	
		education1_inst=c.create_text(290,340,text=Education1_Institute_tx.get(),width=200,justify=LEFT,anchor=NW ,fill="Black",font=("Segoe Print",12,"bold"))	
		education1_qual=c.create_text(290,360,text=Education1_Qualifications_tx.get(),fill="Black",width=200,justify=LEFT,anchor=NW ,font=("Segoe Print",10))
		
		work1_num=c.create_text(110,182,text="1.",fill="Black",font=("comic sans ms",12))
		work1_year_from=c.create_text(144,192,text=Work1_From_tx.get(),fill="Black",font=("comic sans ms",11))
		work1_year_to=c.create_text(198,192,text=Work1_To_tx.get(),fill="Black",font=("comic sans ms",11))
		work1_city=c.create_text(167,208,text=Work1_City_tx.get(),fill="Black",font=("comic sans ms",10))
		work1_position=c.create_text(290,160,text=Work1_Post_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("Segoe Print",12,"bold"))
		work1_company=c.create_text(290,180,text=Work1_CompanyName_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("comic sans ms",10))
		work1_desc=c.create_text(290,200,text=Work1_CompanyDesc_tx.get(),fill="Black",width=290,justify=LEFT,anchor=NW ,font=("comic sans ms",10))

		education2_num=c.create_text(110,410,text="2.",fill="Black",font=("comic sans ms",11))
		education2_from=c.create_text(144,420,fill="Black",text=Education2_From_tx.get(),font=("comic sans ms",11))
		education2_to=c.create_text(198,420,text=Education2_To_tx.get(),fill="Black",font=("comic sans ms",12))
		education2_city=c.create_text(167,438,text=Education2_City_tx.get(),fill="Black",font=("comic sans ms",10))
		education2_inst=c.create_text(290,400,fill="Black",text=Education2_Institute_tx.get(),width=200,justify=LEFT,anchor=NW ,font=("Segoe Print",12,"bold"))
		education2_qual=c.create_text(290,420,text=Education2_Qualifications_tx.get(),fill="Black",width=200,justify=LEFT,anchor=NW ,font=("comic sans ms",10))
		

		work2_num=c.create_text(110,242,text="2.",fill="Black",font=("comic sans ms",11))
		work2_year_from=c.create_text(144,252,text=Work2_From_tx.get(),fill="Black",font=("comic sans ms",11))
		work2_year_to=c.create_text(198,252,text=Work2_To_tx.get(),fill="Black",font=("comic sans ms", 12))
		work2_city=c.create_text(167,272,text=Work2_City_tx.get(),fill="Black",font=("comic sans ms", 10))
		work2_position=c.create_text(290,230,text=Work2_Post_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("Segoe Print",12,"bold"))
		work2_company=c.create_text(290,250,text=Work2_CompanyName_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("comic sans ms",10))
		work2_desc=c.create_text(290,270,text=Work2_CompanyDesc_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("comic sans ms",10))
		t=205
		profile_t=c.create_text(120,46,fill="Black",text=Profile_tx.get(),width=400,justify=LEFT,anchor=NW ,font=("Segoe Print",12,"bold"))
		ty=30
		ty_single=17
				
		name1=c1.create_text(123,160,text=Name_tx.get(),width=220,font=("Segoe Script", 18," bold"))
		lnk_t=c1.create_text(64,625,text=Linkedin_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		twt_t=c1.create_text(64,575,text=Twitter_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		phone_t=c1.create_text(64,377,text=Number_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		name_=c1.create_text(64,297,text=Name_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		adres_t=c1.create_text(64,335,text=Adress_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		Email_t=c1.create_text(64,419,text=Email_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		fb_t=c1.create_text(64,527,text=Facebook_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		c.create_line(165,241,176,241,width=3)
		c.create_line(165,181,176,181,width=3)
		c.create_line(168,412,179,412,width=3)
		c.create_line(168,347,179,347,width=3)
		def proges(event):
			import tkinter.ttk as ttk
			from tkinter import ttk
			i=440
			j=515
			e_=ttk.Style(resume_f__)
			e_.theme_use("default")
			e_.configure("#8AC91D_.Horizontal.TProgressbar",bordercolor="#8AC91D",lightcolor="#8AC91D",darkcolor="#8AC91D",background="#8AC91D")
			progress1_=Progressbar(resume_f__,style="#8AC91D_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress1_["value"]=int(lvl_1_tx.get())
			progress1_.pack()
			progress1_.place(x=i,y=j)
		def proges1(event):
			import tkinter.ttk as ttk
			i=440
			j=550
			e1_=ttk.Style(resume_f__)
			e1_.theme_use("default")
			e1_.configure("red1_.Horizontal.TProgressbar",bordercolor="#FB9A00",lightcolor="#FB9A00",darkcolor="#FB9A00",background="#FB9A00")
			progress2_=Progressbar(resume_f__,style="red1_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress2_["value"]=int(lvl_2_tx.get())
			progress2_.pack()
			progress2_.place(x=i,y=j)
		def proges2(event):
			import tkinter.ttk as ttk
			i=440
			j=590
			e2_=ttk.Style(resume_f__)
			e2_.theme_use("default")
			e2_.configure("red2_.Horizontal.TProgressbar",bordercolor="#1FB4E7",lightcolor="#1FB4E7",darkcolor="#1FB4E7",background="#1FB4E7")
			progress3_=Progressbar(resume_f__,style="red2_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress3_["value"]=int(lvl_3_tx.get())
			progress3_.pack()
			progress3_.place(x=i,y=j)
		def proges3(event):
			import tkinter.ttk as ttk
			i=440
			j=630
			e3_=ttk.Style(resume_f__)
			e3_.theme_use("default")
			e3_.configure("red3_.Horizontal.TProgressbar",bordercolor="red",lightcolor="red",darkcolor="red",background="red")
			progress4_=Progressbar(resume_f__,style="red3_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress4_["value"]=int(lvl_4_tx.get())
			progress4_.pack()
			progress4_.place(x=i,y=j)
		global eventr
		eventr=""
		proges3(eventr)
		proges2(eventr)
		proges(eventr)
		proges1(eventr)
		
		skill__img=PhotoImage(master=c,file="SKILLS-AND-EXPERTIZE.png")
		skill_im=c.create_image(245,480,image=skill__img)
		skil=Image.open("key-skills.png")
		skil=skil.resize((44,44),Image.ANTIALIAS)
		skil__=ImageTk.PhotoImage(skil,master=c)
		skil_1=c.create_image(75,475,image=skil__)
		
		  
		skill_1=c.create_text(144,530,text=Skill_1_tx.get(),width=230,font=("Segoe Print",12,"bold"))
		
		skill_2=c.create_text(144,565,text=Skill_2_tx.get(),width=230,font=("Segoe Print",12,"bold"))
		
		
		skill_3=c.create_text(144,610,text=Skill_3_tx.get(),width=230,font=("Segoe Print",12,"bold"))
		
		skill_4=c.create_text(144,650,text=Skill_4_tx.get(),width=230,font=("Segoe Print",12,"bold"))

		resume_f__.mainloop()
		#root.configure()
		#main()


	def final_resume___(event):		

		from tkinter import Text, Tk
		from tkinter.ttk import Progressbar
		#mainpage_.destroy()

		import tkinter.ttk as ttk
		global resume_f_
		#root.destroy()
		resume_f_= Tk()
		resume_f_.config(bg="#FFFFFF")
		resume_f_.title("CV (Resume)")
		resume_f_.iconbitmap("job.ico")
		resume_f_.resizable(False,False)
		resume_f_.geometry("795x680")
		#resume_.wm_attributes("-alpha",0.7)
		#r=Scale(resume_,from_=1,to=100000,orient=HORIZONTAL,bg="BLUE",fg="red")
		#r.pack()
		Name_tx=StringVar()
		Adress_tx=StringVar()
		Number_tx=StringVar()
		Email_tx=StringVar()
		Facebook_tx=StringVar()
		Twitter_tx=StringVar()
		Linkedin_tx=StringVar()
		Profile_tx=StringVar()
		Work1_From_tx=StringVar()
		Work1_To_tx=StringVar()
		Work1_Post_tx=StringVar()
		Work1_City_tx=StringVar()
		Work1_CompanyName_tx=StringVar()
		Work1_CompanyDesc_tx=StringVar()
		Work2_From_tx=StringVar()
		Work2_To_tx=StringVar()
		Work2_Post_tx=StringVar()
		Work2_City_tx=StringVar()
		Work2_CompanyName_tx=StringVar()

		Work2_CompanyDesc_tx=StringVar()
		Education1_From_tx=StringVar()
		Education1_To_tx=StringVar()
		Education1_Institute_tx=StringVar()
		Education1_City_tx=StringVar()
		Education1_Qualifications_tx=StringVar()
		Education2_From_tx=StringVar()
		Education2_To_tx=StringVar()
		Education2_Institute_tx=StringVar()
		Education2_City_tx=StringVar()
		Education2_Qualifications_tx=StringVar()
		Skill_1_tx=StringVar()
		Skill_2_tx=StringVar()
		Skill_3_tx=StringVar()
		Skill_4_tx=StringVar()
		lvl_1_tx=IntVar()
		lvl_2_tx=IntVar()
		lvl_3_tx=IntVar()
		lvl_4_tx=IntVar()
		#centr_=StringVar()
		conn=sqlite3.connect("resum.db")
		
		c=conn.cursor()
		c.execute("SELECT * FROM Resume3")
		dr=c.fetchall()
		#idel)
		
		#type(idel))


		for i in dr:
			#)
			#type(i[0]))

			#)
			if int(i[0])==idel:
				Name_tx.set(i[1])
				Adress_tx.set(i[2])
				Number_tx.set(i[3])

				Email_tx.set(i[4])
				Facebook_tx.set(i[5])
				Twitter_tx.set(i[6])
				Linkedin_tx.set(i[7])
				Profile_tx.set(i[8]) 
				Work1_From_tx.set(i[9])
				Work1_To_tx.set(i[10])
				Work1_Post_tx.set(i[11])
				Work1_City_tx.set(i[12])
				Work1_CompanyName_tx.set(i[13])
				Work1_CompanyDesc_tx.set(i[14])
				Work2_From_tx.set(i[15])
				Work2_To_tx.set(i[16])
				Work2_Post_tx.set(i[17])
				Work2_City_tx.set(i[18])
				Work2_CompanyName_tx.set(i[19])

				Work2_CompanyDesc_tx.set(i[20])
				Education1_From_tx.set(i[21])
				Education1_To_tx.set(i[22])
				Education1_Institute_tx.set(i[23])
				Education1_City_tx.set(i[24])
				Education1_Qualifications_tx.set(i[25])
				Education2_From_tx.set(i[26])
				Education2_To_tx.set(i[27])
				Education2_Institute_tx.set(i[28])
				Education2_City_tx.set(i[29])
				Education2_Qualifications_tx.set(i[30])
				Skill_1_tx.set(i[32])

				Skill_2_tx.set(i[33])
				Skill_3_tx.set(i[33])
				Skill_4_tx.set(i[34])
				lvl_1_tx.set(i[35])
				lvl_2_tx.set(i[36])
				lvl_3_tx.set(i[37])
				lvl_4_tx.set(i[38])
				#i[39])

				centr=i[39]
				#type(centr))
				
		#dr)
		conn.commit()
		conn.close()
		
		def progrs(event):
			progress['value']=50
		import os
				
		global bgm
		global img
		global img1
		l=Label(resume_f_,bg="white")
		#global c
		c=Canvas(l,width=600,height=1200,bd=0,bg="white",highlightthickness=0)
		#img1=PhotoImage(file="bgmp.png")
		img1=Image.open("back10.jpg")
		img=PhotoImage(master=c,file="Profile.png")

		img1=img1.resize((606,742),Image.ANTIALIAS)
		img3_=ImageTk.PhotoImage(img1,master=c)
		
		d1=c.create_image(320,310,image=img3_)
		d=c.create_image(150,30,image=img)

		c.pack()
		
		l.pack()
		l.place(x=220,y=0)
		
		global c1
		l1=Label(resume_f_)
		c1=Canvas(l1,width=250,height=1700,bd=0,highlightthickness=0)
		img_=PhotoImage(file="NAME21.png",master=c1)
		img2=Image.open("back8.jpg")
		submit_=PhotoImage(file="Submit__1.png",master=c1)
		submt_=c.create_image(900,100,image=submit_)
		
		img2=img2.resize((340,1000),Image.ANTIALIAS)
		img1_=ImageTk.PhotoImage(img2,master=c1)
		d1=c1.create_image(80,320,image=img1_)
		
		#img21=Image.open("bgm1.jpg")
		
		#3img21=img21.resize((300,700),Image.ANTIALIAS)
		#img11_=ImageTk.PhotoImage(img21,master=c1)
		#)
		#d11=c1.create_image(110,700,image=img11_)
		

		d2=c1.create_image(75,294,image=img_)
		
		c1.pack()
		#c1.place(x=0,y=0)
		l1.pack()
		l1.place(x=0,y=0)
		
		global n
		n="bg3.png"
		mag=Image.open(n)
		global frame1
		mag=mag.resize((110,110),Image.ANTIALIAS)
		mag1=ImageTk.PhotoImage(mag,master=c1)
		frame1=c1.create_image(90,70,image=mag1)
		#frame1.place(x=10,y=10)
		'''
		m="add-user.png"
		mag4=Image.open(m)
		mag4=mag4.resize((30,30),Image.ANTIALIAS)
		mag5=ImageTk.PhotoImage(mag4,master=c1)
		frame2=c1.create_image(170,110,image=mag5)
		c1.tag_bind(frame2,'<ButtonPress-1>',photo)
		'''
		#global centr
		Info_=PhotoImage(master=c1,file="INFO.png")
		Info=c1.create_image(92,254,image=Info_)
		conct=Image.open("user.png")
		conct=conct.resize((30,30),Image.ANTIALIAS)
		conct__=ImageTk.PhotoImage(conct,master=c1)
		
		conct_=c1.create_image(35,290,image=conct__)
		##centr)
		conn=sqlite3.connect("resum.db")
		
		cur=conn.cursor()
		cur.execute("SELECT * FROM Resume3")
		dr=cur.fetchall()
		

		global centr_
		for i in dr:
			#)
			#type(idel))
			if int(i[0])==idel:
				#type(i[0]))
				centr_=i[39]
				#centr_)
				break
		#centr_)
		rot3__=Image.open(centr_)
		
		rot3__=rot3__.resize((70,70),Image.ANTIALIAS)
		rot1__=ImageTk.PhotoImage(rot3__,master=c1)
		frame1=c1.create_image(90,70,image=rot1__)
			
		
		adres=Image.open("map.png")
		adres=adres.resize((30,30),Image.ANTIALIAS)
		adres_=ImageTk.PhotoImage(adres,master=c1)
		addres=c1.create_image(35,332,image=adres_)
		adress_img=PhotoImage(master=c1,file="Addressw.png")
		adress_w=c1.create_image(84,332,image=adress_img)


		


		phone=Image.open("telephone.png")
		phone=phone.resize((30,30),Image.ANTIALIAS)
		phone_=ImageTk.PhotoImage(phone,master=c1)
		phone_img=PhotoImage(master=c1,file="Phonew.png")
		phne_w=c1.create_image(75,373,image=phone_img)
		phoone=c1.create_image(35,368,image=phone_)
			


		Email1=Image.open("gmail.png")
		Email1=Email1.resize((30,30),Image.ANTIALIAS)
		Email_=ImageTk.PhotoImage(Email1,master=c1)
		
		Email_img=PhotoImage(master=c1,file="Emailw.png")
		Emai_w=c1.create_image(75,412,image=Email_img)
		Emaill=c1.create_image(35,412,image=Email_)
		#reds=c1.create_line(0,226,296,226,width=2)
		#reds1=c1.create_line(0,259,296,259,width=2)

	 
		
		social_=PhotoImage(master=c1,file="SOCIAL.png")
		Social=c1.create_image(95,480,image=social_)
		
		#reds=c1.create_line(0,459,296,459,width=2)
		#reds1=c1.create_line(0,494,296,494,width=2)
	 	
			

		
		fb=Image.open("facebook.png")
		fb=fb.resize((30,30),Image.ANTIALIAS)
		fb_=ImageTk.PhotoImage(fb,master=c1)
		facbk=c1.create_image(35,520,image=fb_)
		fb_img=PhotoImage(master=c1,file="Facebookw.png")
		fb_w=c1.create_image(90,520,image=fb_img)
	 
		
	 	
		
		twt=Image.open("twitter_.png")
		twt=twt.resize((30,30),Image.ANTIALIAS)
		twt_=ImageTk.PhotoImage(twt,master=c1)

		twt_img=PhotoImage(master=c1,file="Twitter.png")
		twt_w=c1.create_image(85,570,image=twt_img)
		twitwr=c1.create_image(35,570,image=twt_)


	 	
		lnk=Image.open("linkedin_.png")
		lnk=lnk.resize((30,30),Image.ANTIALIAS)
		lnk_=ImageTk.PhotoImage(lnk,master=c1)

		lnk_img=PhotoImage(master=c1,file="Linkedin.png")
		lnk_w=c1.create_image(85,620,image=lnk_img)
		lnkdin=c1.create_image(35,620,image=lnk_)
		profe=Image.open("user.png")
		profe=profe.resize((44,44),Image.ANTIALIAS)
		profe__=ImageTk.PhotoImage(profe,master=c1)
		profe_=c.create_image(75,30,image=profe__)
	 	
		
		wrke__img=PhotoImage(master=c,file="WORK-EXPERIENCE.png")
		wrke_im=c.create_image(210,140,image=wrke__img)
		wrke=Image.open("edit.png")
		wrke=wrke.resize((44,44),Image.ANTIALIAS)
		wrke__=ImageTk.PhotoImage(wrke,master=c)
		wrke_1=c.create_image(75,140,image=wrke__)
	 
		educ__img=PhotoImage(master=c,file="EDUCATION.png")
		educ_im=c.create_image(185,320,image=educ__img)
		educ=Image.open("graduation-hat.png")
		educ=educ.resize((44,44),Image.ANTIALIAS)
		educ__=ImageTk.PhotoImage(educ,master=c)
		educ_1=c.create_image(75,320,image=educ__)
		

		education1_num=c.create_text(110,345,text="1.",fill="Black",font=("comic sans ms",12))
		education1_from=c.create_text(144,355,text=Education1_From_tx.get(),fill="black",font=("comic sans ms",11))
		education1_to=c.create_text(198,355,fill="Black",text=Education1_To_tx.get(),font=("comic sans ms",11))
		education1_city=c.create_text(167,376,text=Education1_City_tx.get(),fill="Black",font=("comic sans ms",10))	
		education1_inst=c.create_text(290,340,text=Education1_Institute_tx.get(),width=200,justify=LEFT,anchor=NW ,fill="Black",font=("Segoe Print",12,"bold"))	
		education1_qual=c.create_text(290,360,text=Education1_Qualifications_tx.get(),fill="Black",width=200,justify=LEFT,anchor=NW ,font=("Segoe Print",10))
		
		work1_num=c.create_text(110,182,text="1.",fill="Black",font=("comic sans ms",12))
		work1_year_from=c.create_text(144,192,text=Work1_From_tx.get(),fill="Black",font=("comic sans ms",11))
		work1_year_to=c.create_text(198,192,text=Work1_To_tx.get(),fill="Black",font=("comic sans ms",11))
		work1_city=c.create_text(167,208,text=Work1_City_tx.get(),fill="Black",font=("comic sans ms",10))
		work1_position=c.create_text(290,160,text=Work1_Post_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("Segoe Print",12,"bold"))
		work1_company=c.create_text(290,180,text=Work1_CompanyName_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("comic sans ms",10))
		work1_desc=c.create_text(290,200,text=Work1_CompanyDesc_tx.get(),fill="Black",width=290,justify=LEFT,anchor=NW ,font=("comic sans ms",10))

		education2_num=c.create_text(110,410,text="2.",fill="Black",font=("comic sans ms",11))
		education2_from=c.create_text(144,420,fill="Black",text=Education2_From_tx.get(),font=("comic sans ms",11))
		education2_to=c.create_text(198,420,text=Education2_To_tx.get(),fill="Black",font=("comic sans ms",12))
		education2_city=c.create_text(167,438,text=Education2_City_tx.get(),fill="Black",font=("comic sans ms",10))
		education2_inst=c.create_text(290,400,fill="Black",text=Education2_Institute_tx.get(),width=200,justify=LEFT,anchor=NW ,font=("Segoe Print",12,"bold"))
		education2_qual=c.create_text(290,420,text=Education2_Qualifications_tx.get(),fill="Black",width=200,justify=LEFT,anchor=NW ,font=("comic sans ms",10))
		

		work2_num=c.create_text(110,242,text="2.",fill="Black",font=("comic sans ms",11))
		work2_year_from=c.create_text(144,252,text=Work2_From_tx.get(),fill="Black",font=("comic sans ms",11))
		work2_year_to=c.create_text(198,252,text=Work2_To_tx.get(),fill="Black",font=("comic sans ms", 12))
		work2_city=c.create_text(167,272,text=Work2_City_tx.get(),fill="Black",font=("comic sans ms", 10))
		work2_position=c.create_text(290,230,text=Work2_Post_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("Segoe Print",12,"bold"))
		work2_company=c.create_text(290,250,text=Work2_CompanyName_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("comic sans ms",10))
		work2_desc=c.create_text(290,270,text=Work2_CompanyDesc_tx.get(),width=290,justify=LEFT,anchor=NW ,fill="Black",font=("comic sans ms",10))
		t=205
		profile_t=c.create_text(120,46,fill="Black",text=Profile_tx.get(),width=400,justify=LEFT,anchor=NW ,font=("Segoe Print",12,"bold"))
		ty=30
		ty_single=17
				
		name1=c1.create_text(123,160,text=Name_tx.get(),width=220,font=("Segoe Script", 18," bold"))
		lnk_t=c1.create_text(64,625,text=Linkedin_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		twt_t=c1.create_text(64,575,text=Twitter_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		phone_t=c1.create_text(64,377,text=Number_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		name_=c1.create_text(64,297,text=Name_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		adres_t=c1.create_text(64,335,text=Adress_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		Email_t=c1.create_text(64,419,text=Email_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		fb_t=c1.create_text(64,527,text=Facebook_tx.get(),justify=LEFT,anchor=NW ,width=220,font=("Segoe Script",10))
		c.create_line(165,241,176,241,width=3)
		c.create_line(165,181,176,181,width=3)
		c.create_line(168,412,179,412,width=3)
		c.create_line(168,347,179,347,width=3)
		def proge1():
			i=440
			j=515
			e_=ttk.Style()
			e_.theme_use("default")
			e_.configure("#8AC91D_.Horizontal.TProgressbar",bordercolor="#8AC91D",lightcolor="#8AC91D",darkcolor="#8AC91D",background="#8AC91D")
			progress1_=Progressbar(resume_f_,style="#8AC91D_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress1_["value"]=int(lvl_1_tx.get())
			progress1_.pack()
			progress1_.place(x=i,y=j)
		def proge2():
			import tkinter.ttk as ttk
			i=440
			j=550
			e1_=ttk.Style()
			e1_.theme_use("default")
			e1_.configure("red1_.Horizontal.TProgressbar",bordercolor="#FB9A00",lightcolor="#FB9A00",darkcolor="#FB9A00",background="#FB9A00")
			progress2_=Progressbar(resume_f_,style="red1_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress2_["value"]=int(lvl_2_tx.get())
			progress2_.pack()
			progress2_.place(x=i,y=j)
			import tkinter.ttk as ttk
		def proge3():
			i=440
			j=590
			e2_=ttk.Style()
			e2_.theme_use("default")
			e2_.configure("red2_.Horizontal.TProgressbar",bordercolor="#1FB4E7",lightcolor="#1FB4E7",darkcolor="#1FB4E7",background="#1FB4E7")
			progress3_=Progressbar(resume_f_,style="red2_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress3_["value"]=int(lvl_3_tx.get())
			progress3_.pack()
			progress3_.place(x=i,y=j)
		def proge4():
			import tkinter.ttk as ttk
			i=440
			j=630
			e3_=ttk.Style()
			e3_.theme_use("default")
			e3_.configure("red3_.Horizontal.TProgressbar",bordercolor="red",lightcolor="red",darkcolor="red",background="red")
			progress4_=Progressbar(resume_f_,style="red3_.Horizontal.TProgressbar",orient=HORIZONTAL,length=325,mode="determinate")
			progress4_["value"]=int(lvl_4_tx.get())
			progress4_.pack()
			progress4_.place(x=i,y=j)
		proge1()
		proge2()
		proge3()
		proge4()
		global eventr
		eventr=""
		
		skill__img=PhotoImage(master=c,file="SKILLS-AND-EXPERTIZE.png")
		skill_im=c.create_image(245,480,image=skill__img)
		skil=Image.open("key-skills.png")
		skil=skil.resize((44,44),Image.ANTIALIAS)
		skil__=ImageTk.PhotoImage(skil,master=c)
		skil_1=c.create_image(75,475,image=skil__)
		
		  
		skill_1=c.create_text(144,530,text=Skill_1_tx.get(),width=230,font=("Segoe Print",12,"bold"))
		
		skill_2=c.create_text(144,565,text=Skill_2_tx.get(),width=230,font=("Segoe Print",12,"bold"))
		
		
		skill_3=c.create_text(144,610,text=Skill_3_tx.get(),width=230,font=("Segoe Print",12,"bold"))
		
		skill_4=c.create_text(144,650,text=Skill_4_tx.get(),width=230,font=("Segoe Print",12,"bold"))
		resume_f_.mainloop()
		
	def Edit2(event):
				
	#mainpage_=Tk()
		sign_in__.destroy()
		global root1
		import tkinter.ttk as ttk
		root1 = Tk()
		root1.config(bg="skyblue")
		root1.iconbitmap("job.ico")
		
		root1.title("Employee List")
		root1.geometry("965x700")
		root1.resizable(False,False)
		global tree1
		global Style_1
		
		width = 1200
		height = 700
		
		TableMargin = Frame(root1, width=870,bg="skyblue")
		TableMargin.pack()
		TableMargin.place(x=-15,y=130)
		scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
		scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
		Style_1=ttk.Style(root1)
		#Style.configure("mystyle.Treeview",bd=2,font=("arial",12))
		Style_1.configure("mystyle_1.Treeview.Heading",bd=2,fg="black",rowheight=45,font=("Segoe Script",14,"bold"))
		
		Style_1.configure("mystyle_1.Treeview",bd=2,fg="black",rowheight=30,font=("Segoe Print",9))
		
		#scrollbarx.pack(side=BOTTOM, fill=X)
		tree1 = ttk.Treeview(TableMargin, style="mystyle_1.Treeview",columns=("ID", "Full_Name", "Job_Type", "Age","Gender" ,"Experience", "Address", "Contact"), height=18, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
		scrollbary.config(command=tree1.yview)
		scrollbary.pack(side=RIGHT, fill=Y)
		scrollbarx.config(command=tree1.xview)
		scrollbarx.pack(side=BOTTOM, fill=X)

		tree1.heading('#0', text="", anchor=W)
		
		tree1.heading('ID', text="Id", anchor=W)
		tree1.heading('Full_Name', text="Full_Name", anchor=W)	
		tree1.heading('Job_Type', text="Job_Type", anchor=W)
		tree1.heading('Age', text="Age", anchor=W)
		tree1.heading('Gender', text="Gender", anchor=W)
		tree1.heading('Experience', text="Experience", anchor=W)
		tree1.heading('Address', text="Address", anchor=W)
		tree1.heading('Contact', text="Contact", anchor=W)
		tree1.column('#0', stretch=NO, minwidth=0, width=70)
		tree1.column('#1', stretch=NO, minwidth=30, width=45)
		tree1.column('#2', stretch=NO, minwidth=70, width=180)
		tree1.column('#3', stretch=NO, minwidth=60, width=130)
		tree1.column('#4', stretch=NO, minwidth=90, width=60)
		tree1.column('#5', stretch=NO, minwidth=80, width=90)
		tree1.column('#6', stretch=NO, minwidth=120, width=128)
		tree1.column('#7', stretch=NO, minwidth=90, width=130)
		tree1.column('#8', stretch=NO, minwidth=70, width=110)
		
		#tree.column('#5', stretch=NO, minwidth=90, width=200)
		
	

		tree1.pack()
		def f(event):
			sc=tree1.identify("item",event.x,event.y)
			eq=tree1.item(sc)
			rw=eq["values"]

			conn=sqlite3.connect("resum.db")
			c=conn.cursor()
			c.execute("SELECT * FROM Resume3")
			global ide1
			ide1=rw[0]
			dr=c.fetchall()
			#type(rw[0]))
			for i in dr:
				#type(i[0]))
				if i[0]==str(rw[0]):
					
					final_resume__("")
					break
			else:
				messagebox.showerror("oops!","User Has not Uploaded Resume")
						
		tree1.bind('<Double-Button-1>',f)
		conn=sqlite3.connect("jobs.db")
		c=conn.cursor()
		c.execute("SELECT *,oid FROM Job_Aspirants ")
		ro=c.fetchall()
		#frt=PhotoImage(file="bg12.png")
		fr=Image.open("officer.png")
		fr=fr.resize((28,25),Image.ANTIALIAS)
		frt=ImageTk.PhotoImage(fr,master=root1)
		#ro)
		for i in ro:
			tree1.insert('','end',image=frt,values=(i),tags=('aj',))
		conn.commit()
		conn.close()

		im=PhotoImage(master=root1,file="List-of-Employees.png")
		im1=PhotoImage(master=root1,file="Edit-Your-Data.png")
		frame2=LabelFrame(root1)

		frame1=Label(frame2,image=im,bg="yellow")
		frame1.pack()
		frame2.pack()
		
		frame2.place(x=8,y=4)
		frame10=Label(root1,highlightthickness=0,highlightbackground="skyblue",borderwidth=0)
		frame10.pack()
		frame10.place(x=700,y=0)
		cn1=Canvas(frame10,width=300,height=130,bg="skyblue",highlightthickness=0,highlightbackground="skyblue")
		

		cn1.pack()

		conct2=Image.open("loupe.png")
		conct2=conct2.resize((30,30),Image.ANTIALIAS)
		show=ImageTk.PhotoImage(conct2,master=cn1)
		conct3=Image.open("edit (1).png")
		conct3=conct3.resize((40,40),Image.ANTIALIAS)
		dit=ImageTk.PhotoImage(conct3,master=cn1)
		conct4=Image.open("filter.png")
		conct4=conct4.resize((28,28),Image.ANTIALIAS)
		crte_resum=ImageTk.PhotoImage(conct4,master=cn1)
		
		create14=cn1.create_image(168,42,image=show)
		
		create16=cn1.create_image(210,90,image=dit)
		create19=cn1.create_image(230,42,image=crte_resum)
		
		cn1.tag_bind(create19,'<Button-1>',specific)
		cn1.tag_bind(create16,'<Button-1>',EditC)
		
		global jobtype__c
		jobtype_c=StringVar()
		jobtype__c=ttk.Combobox(root1,width=30,textvariable=jobtype_c,font=("Seoge Print",10,"bold"))
		l1=["All Jobtypes","Dermatalogistn","PGT Maths","PGT English","PGT Science","Tuitor","Trail Truck Driver","Registered Nurse","Retail Salesperson","Software Developers","Marketing Managers","Agriculture Food Scientist","Animal Breeder","Conservation Scientist","Enviornmental Scientist","Farmer","Fish Hatchery Manager","Fisher","First-Line Supervisors of Food Preparation and Serving Workers","First-Line Supervisors of Office and Administrative Support Workers","Computer User Support Specialists","Computer Systems Analysts","Network and Computer Systems Administrators","Web Developers","Management Analysts","Medical and Health Services Managers","Accountants","Information Technology Project Managers","Sales Managers","Industrial Engineers","First-Line Supervisors of Production and Operating Workers","Nursing Assistants","Licensed Practical and Licensed Vocational Nurses","General and Operations Managers","Bookkeeping"," Accounting","Auditing Clerks","Managers", "All Other Financial Managers"," Branch or Department","Insurance Sales Agents","Sales Representatives", "Wholesale and Manufacturing", "Technical and Scientific ProductsSales Representative", "All Other Sales Agents", "Financial Services","Critical Care Nurses","Cashiers","Computer Systems Engineers/Architects","Market Research Analysts and Marketing Specialists","Physical Therapists","Medical Assistants","First-Line Supervisors of Non-Retail Sales Workers","Software Quality Assurance Engineers and Testers","First-Line Supervisors of Mechanics", "Installers","Repairers","Information Security Analysts","Medical Secretaries","Laborers and Freight", "Stock and Material Movers", "HandSecurity Guards","Family and General Practitioners"]

		jobtype__c["values"]=l1
		jobtype__c.insert(0,"Search for a particular Job_Type")
		#jobtype__.grid(row=2,column=1)
		
		jobtype__c.place(x=610,y=30)
		cn1.tag_bind(create14,'<Button-1>',z)
		
		root1.mainloop()

	def submit_c(event):
#CHECKING FOR THE RECORD WHERE THE ENTE#1AADFF ID IS MATCHING		
		conn=sqlite3.connect("jobs.db")
		c=conn.cursor()
		c.execute("SELECT * FROM Company")
		ro=c.fetchall()

		
#Id.get() IS A STRING AND THE DATA WE WANT TO MATCH IS INTEGER
		global idec
		idec=Id_c_.get()
		global tc
		tc=password_c.get()
		for i in ro:
			ckc=i[0]
			

			if str(ckc)==idec:
				
				
				if tc==str(i[6]):
					#messagebox.showinfo("JOBS","Nice Buddy"
					#Edit()
					
					Edit2("")	
					break

#DISPLAYING A TRY AGAIN MESSAGE WHEN ID IS INVALID
		else:
			messagebox.showerror("TRY AGAIN","Enter a valid ID")	
			conct21=PhotoImage(file="Sign-in (4).png",master=sign_in__)
			'''   
			Register__=Label(sign_in__,bg="#F6C447",image=conct21)
			Register__.pack()
			Register__.place(x=490,y=380)'''

			sign=Label(sign_in__,image=conct21 ,bg="#F6C447")
			sign.pack()
			sign.place(x=490,y=380)
			sign.bind("<Button-1>",submit_c)
			#sign_in__.configure()
			Id_c_.delete(0,END)
			
		
			password_c.delete(0,END)
		
		
		
		
		conn.commit()
		conn.close()
	def signin(event):
		s.destroy()
		global sign_in__
		sign_in__=Tk()
		sign_in__.title("Sign In Here")
		sign_in__.iconbitmap("job.ico")
		sign_in__.config(bg="skyblue")
		#ID
		image1=Image.open("17.png")

		image1=image1.resize((680,450),Image.ANTIALIAS)
		bj=ImageTk.PhotoImage(image1)
		
		sign_in_=Label(sign_in__,image=bj)
		sign_in_.pack()
		sign_in_.place(x=0,y=0)
		m=PhotoImage(file="WELCOME-BACK.png")

		sn=PhotoImage(file="Sign-in (4).png")
		
		cid=PhotoImage(file="Company-id (2).png")
		pass1=PhotoImage(file="password_.png")
		sign_in__.geometry("680x450")
		#frame=LabelFrame(sign_in_,text="",padx=10,pady=1,height="100",bg="orange",relief=GROOVE,bd=5)
		#frame.pack(padx=0,pady=0)

		#welc=PhotoImage(file="")
		wel=Label(sign_in__,image=m,bg="#F4C247")
		wel.pack()
		wel.place(x=240,y=45)
		nameL=Label(sign_in_,image=cid,bg="#F6C447")
		nameL.pack()
		nameL.place(x=200,y=180)
		global Id_c_          
		Id_c_=Entry(sign_in__,width=14,justify="center",font=("arial",20))
		Id_c_.pack(padx=2,pady=33,ipady=55)
		Id_c_.place(x=457,y=180)
		Id_c_.focus()
		#PASSWORD
		nameL1=Label(sign_in__,image=pass1,bg="#F6C447")
		nameL1.pack()
		nameL1.place(x=240,y=230)
		
		global password_c
		password_c=Entry(sign_in__,width=14,justify="center",font=("arial",20))
		password_c.pack(padx=2,pady=33,ipady=50)
		password_c.place(x=457,y=230)
		#suBMIT BUTTON
		#frame3=LabelFrame(sign_in,text="",padx=10,pady=1,height="100",bg="green",relief=RIDGE,bd=1)
		#frame3.pack(padx=0,pady=0,fill=X)
		sign=Label(sign_in__,image=sn,bg="#F6C447")
		sign.pack()
		sign.place(x=490,y=320)
		sign.bind("<Button-1>",submit_c)
		sign_in__.resizable(False,False)
		Id_c_.focus()	
		sign_in__.mainloop()
	def signin23(event):
		o.destroy()
		global sign_in__
		sign_in__=Tk()
		sign_in__.title("Sign In Here")
		sign_in__.iconbitmap("job.ico")
		sign_in__.config(bg="skyblue")
		#ID
		image1=Image.open("17.png")

		image1=image1.resize((680,450),Image.ANTIALIAS)
		bj=ImageTk.PhotoImage(image1,master=sign_in__)
		
		sign_in_=Label(sign_in__,image=bj)
		sign_in_.pack()
		sign_in_.place(x=0,y=0)
		m=PhotoImage(file="WELCOME-BACK.png",master=sign_in__)

		sn=PhotoImage(file="Sign-in (4).png",master=sign_in__)
		
		cid=PhotoImage(file="Company-id (2).png",master=sign_in__)
		pass1=PhotoImage(file="password_.png",master=sign_in__)
		sign_in__.geometry("680x450")
		#frame=LabelFrame(sign_in_,text="",padx=10,pady=1,height="100",bg="orange",relief=GROOVE,bd=5)
		#frame.pack(padx=0,pady=0)

		#welc=PhotoImage(file="")
		wel=Label(sign_in__,image=m,bg="#F4C247")
		wel.pack()
		wel.place(x=240,y=45)
		nameL=Label(sign_in_,image=cid,bg="#F6C447")
		nameL.pack()
		nameL.place(x=200,y=180)
		global Id_c_          
		Id_c_=Entry(sign_in__,width=15,justify="center",font=("arial",20))
		Id_c_.pack(padx=2,pady=33,ipady=55)
		Id_c_.place(x=440,y=180)
		Id_c_.focus()
		#PASSWORD
		nameL1=Label(sign_in__,image=pass1,bg="#F6C447")
		nameL1.pack()
		nameL1.place(x=240,y=230)
		
		global password_c
		password_c=Entry(sign_in__,width=13,justify="center",font=("arial",20))
		password_c.pack(padx=2,pady=33,ipady=50)
		password_c.place(x=460,y=230)
		#suBMIT BUTTON
		#frame3=LabelFrame(sign_in,text="",padx=10,pady=1,height="100",bg="green",relief=RIDGE,bd=1)
		#frame3.pack(padx=0,pady=0,fill=X)
		sign=Label(sign_in__,image=sn,bg="#F6C447")
		sign.pack()
		sign.place(x=490,y=320)
		sign.bind("<Button-1>",submit_c)
		sign_in__.resizable(False,False)
		Id_c_.focus()	
		sign_in__.mainloop()
	def regis(event):
		s.destroy()
		global o
		o=Tk()
		o.title("Register Here")
		o.config(bg="#1AADFF")
		o.geometry('535x470')
		image1=Image.open("bagro.jpg")
		image1=image1.resize((535,470),Image.ANTIALIAS)
		m21=ImageTk.PhotoImage(image1)
		#im23=PhotoImage(file="14.jpg",master=o)
		tl1=Label(o,image=m21)
		tl1.pack()
		tl1.place(x=0,y=0)
		
		im=PhotoImage(file="Register-Your-Company-He.png")
		tl=Label(tl1,image=im,bg="#feb500")
		tl.pack()
		tl.place(x=0,y=0)
		y1=PhotoImage(file="1-Generate-Company-ID.png")
		y2=PhotoImage(file="2-Company-Name.png")
		y3=PhotoImage(file="3-Company-Main-Branch-A.png")

		y4=PhotoImage(file="4-Total-Number-of-Emplo.png")
		y5=PhotoImage(file="5-Vacancy-Status.png")

		y6=PhotoImage(file="6-Contact-Number.png")
		y7=PhotoImage(file="7-Generate-Password.png")
		
		y8=PhotoImage(file="Available.png")
		y9=PhotoImage(file="Unavailable.png")
		
		sn=PhotoImage(file="Submit__1.png")
		
		#cid=PhotoImage(file="company-id.png")
		#pass1=PhotoImage(file="password_.png")
		#sign_in__.geometry("680x450")
		
		global noavail
		global avail
		global adress
		global Cname_
		global employee
		global C_Id_ 
		global pass_
		global stats
		global Cnumber
		C_Id=Label(tl1,image=y1,bg="#feb500")	
		C_Id.pack()	
		C_Id.place(x=0,y=70)
		C_Id_=Entry(tl1,justify="center",bd=3,relief=SUNKEN)
		C_Id_.pack()
		C_Id_.place(x=300,y=85)
		Cname=Label(tl1,image=y2,bg="#feb500")	
		Cname.pack()
		Cname.place(x=0,y=110)

		Cname_=Entry(tl1,justify="center",bd=3,relief=SUNKEN)
		Cname_.pack()
		Cname_.place(x=300,y=120)
		
		Adress=Label(tl1,image=y3,bg="#feb500")	
		Adress.pack()
		Adress.place(x=0,y=145)	
		adress=Entry(tl1,justify="center",bd=3,relief=SUNKEN)
		adress.pack()
		adress.place(x=300,y=155)
		Employee=Label(tl1,image=y4,bg="#feb500")	
		Employee.pack()	
		Employee.place(x=0,y=180)
		employee=Entry(tl1,justify="center",bd=3,relief=SUNKEN)
		employee.pack()
		employee.place(x=300,y=190)


		Employee=Label(tl1,image=y5,bg="#feb500")	
		Employee.pack()	
		Employee.place(x=0,y=215)	

		global stats
		RadioGroup1=Frame(tl1,bg="#feb500")
		RadioGroup1.pack()
		RadioGroup1.place(x=300,y=225)
		stats=StringVar()
		global avail
		global noavail
		avail = Checkbutton(RadioGroup1, image=y8, variable=stats,onvalue="Yes" ,bg="#feb500",command=yes1)
		avail.pack()
		noavail = Checkbutton(RadioGroup1,image=y9, variable=stats,onvalue="No",bg="#feb500",command=no1)
		noavail.pack()
		avail.deselect()
		noavail.deselect()
		num=Label(tl1,image=y6,bg="#feb500")	
		num.pack()
		num.place(x=0,y=300)	

		Cnumber=Entry(tl1,justify="center",bd=3,relief=SUNKEN)
		Cnumber.pack()
		Cnumber.place(x=300,y=315)

		
		pass__=Label(tl1,image=y7,bg="#feb500")	
		pass__.pack()
		pass__.place(x=0,y=335)	
		pass_=Entry(tl1,justify="center",bd=3,relief=SUNKEN)
		pass_.pack()
		pass_.place(x=300,y=350)
		
		reg=Label(tl1,image=sn,bg="#feb500")
		reg.pack()
		reg.place(x=420,y=400)
		o.resizable(False,False)
		reg.bind("<Button-1>",submit1)
		#employee=Entry(o,width=20,justify="center")
		#employee.grid(row=5	,column=1)
		o.mainloop()
	def yes1():
		stats.set("Available")
		avail.select()
		#noavail.deselect()
	def no1():
		stats.set("Unavailable")	
		
		#avail.select()
		noavail.select()
	mainpage_.destroy()
	global s
	s=Tk()
	global a
	global b
	a="530"
	b="500"
	s.geometry(a+"x"+b)
	s.config(bg="white")
	s.title("A Job : Give or Get")
	s.iconbitmap("job.ico")
	def g(event):
		print()
	def f(event):
		signl=Label(r,image=sign1)
		signl.pack()
		signl.bind("<Button-1>",g)
	image=Image.open("13.png")
	image=image.resize((530,500),Image.ANTIALIAS)
	m=ImageTk.PhotoImage(image)

	bh=PhotoImage(file="start.png")
	sign=PhotoImage(file="Sign-in_.png")
	sign1=PhotoImage(file="Sign-Up_.png")
	sign2=PhotoImage(file="Employees.png")
	r=Label(s,image=m)
	r.pack()
	r.place(x=0,y=0)


	job=Label(s,image=sign2,bg="white")
	job.pack()

	#signl=Button(r,image=sign,command=f)
	#signl.pack()
	job.place(x=45,y=2)
	#signl=Button(r,image=sign1,command=f,relief=GROOVE)
	#signl.pack()
	Signin=Label(s,image=sign,bg="white")
	Signin.pack()
	Signin.place(x=10,y=400)

	Signin.bind("<Button-1>",signin)
	signup=Label(s,image=sign1,bg="white")
	signup.pack()
	signup.place(x=300,y=400)

	signup.bind("<Button-1>",regis)
	s.mainloop()

	#mainpage_.destroy()
global mainpage_
mainpage_=Tk()
global a
global b

a="620"
b="510"
mainpage_.geometry(a+"x"+b)
mainpage_.config(bg="white")
mainpage_.title("A Job : Give or Get")
mainpage_.iconbitmap("job.ico")
mainpage_.resizable(False,False)
image=Image.open("job3.png")
image=image.resize((610,500),Image.ANTIALIAS)
m=ImageTk.PhotoImage(image)
j=PhotoImage(file="A-Job.png")
f=PhotoImage(file="An-Employee.png")

oR=PhotoImage(file="oR.png")

sign1=PhotoImage(file="What-ArE-you-Searching-f.png")


r=Label(mainpage_,image=m)
r.pack()
r.place(x=0,y=30)


job=Label(mainpage_,image=sign1,bg="white")
job.pack()

#signl=Button(r,image=sign,command=f)
#signl.pack()
job.place(x=0,y=10)
#signl=Button(r,image=sign1,command=f,relief=GROOVE)
#signl.pack()

or_=Label(mainpage_,image=oR,bg="white")
or_.pack()
or_.place(x=190,y=420)

Signin=Label(mainpage_,image=f,bg="white")
Signin.pack()
Signin.place(x=280,y=420)

Signin.bind("<Button-1>",compa)
signup=Label(mainpage_,image=j,bg="white")
signup.pack()
signup.place(x=2,y=385)

signup.bind("<Button-1>",employ)#employ)
mainpage_.mainloop()
'''
mainpage_=Tk()
mainpage_.title("A Job : Give or Get")
mainpage_.iconbitmap("job.ico")
mainpage_.geometry("450x350")
t=Label(mainpage_,text="To Proceed Further\nLet us know\nWhat do you Want.",bg="Blue",bd=10,fg="white",relief=GROOVE,font=("times new roman",30,"bold"))
t.pack(fill=X)

frame=LabelFrame(mainpage_,text="",padx=0,pady=1,height="500", relief=RIDGE, borderwidth=8)
frame.pack(padx=0,pady=10,side="left")
frame.place(x=20,y=200)
sign=Button(frame,text="1.  Search for an employee for your firm  ",fg="#1AADFF",command=compa)
sign.pack()

#SIGN IN
frame=LabelFrame(mainpage_,text="",padx=0,pady=1,height="100", relief=RIDGE, borderwidth=8)
frame.pack(padx=0,pady=10,side="right")
frame.place(x=20,y=250)
sign=Button(frame,text="2.  Search for a Job                                      ",fg="#1AADFF",command=employ)
sign.pack()

mainpage_.mainloop()	
'''