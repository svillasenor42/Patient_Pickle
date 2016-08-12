# Get Started!

#     1. Paste your code, then name it on the right, or drag & drop a file in.

#     2. Share your link! (https://kobra.io/#/e/-KOAdHVl1Sdm4HY7ITPt)
    
    
# Get Started!

#     1. Paste your code, then name it on the right, or drag & drop a file in.

#     2. Share your link! (https://kobra.io/#/e/-KO6KV8m22O32c0RL97-)
    
#Let's Code Guyzzzzz
#add a health condition to review/customize patients
#3 types of breaches, but we're keeping it simple :)
import random
from random import randint

#---------List Code---------
name=["Sam", "Gale", "Riley", "Jordan", "Cam", "Dani", "Charlie", "Dakota", "Skylar", "Frankie", "Jessie", "Sage", "Quinn", "Peyton", "Avery", "Reese", "Taylor", "Morgan", "Ryan", "Carter"]
gender=["Female", "Male", "Other"]
age=[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
bloodtype=["A+", "A-", "B+", "B-", "AB+", "AB-"," O"]
meds=["Adderal", "Amoxicillin",  "Coumadin"]


#---------Class Code---------
class Patient():
	def __init__(self):
		self.Name=random.choice(name)
		self.Gender=random.choice(gender)
		self.Bloodtype=random.choice(bloodtype)
		self.Meds=random.choice(meds)
		self.Age=random.choice(age)
		self.Stats="Name: {} "+"\n"+"Age: {} "+"\n"+"Gender: {} "+"\n"+"Bloodtype: {} "+"\n"+"Medication: {} "
		
class Neo_natal(Patient):
	def __init__(self):
		Patient.__init__(self)
		self.premature=random.choice([0,0,0,0,0,0,0,0,0,1])
		self.breech=random.choice([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
		self.Age_range="neonatal"
		
class Infant(Patient):
	def __init__(self):
		Patient.__init__(self)
		self.Age_range="infant"
		
class Child(Patient):
	def __init__(self):
		Patient.__init__(self)
		self.Age_range="child"

class Adolescent(Patient):
	def __init__(self):
		Patient.__init__(self)
		self.Age_range="adolescent"
		
class Adult(Patient):
	def __init__(self):
		Patient.__init__(self)
		self.Age_range="adult"

class Senior(Patient):
	def __init__(self):
		Patient.__init__(self)
		self.Age_range="senior"
	
#---------Action Code---------
def make_patient(patient_name):
	patient_name=Patient()
	Patient_age=patient_name.Age
	
	if Patient_age==(-1) or Patient_age==(0):
		Patient_type=Neo_natal()
		return (["Neo-natal",str(patient_name.Age),str(patient_name.Gender),str(patient_name.Bloodtype),str(patient_name.Meds)])
	elif Patient_age>0 and Patient_age<=2:
		Patient_type=Infant()
		return (["Infant",str(patient_name.Age),str(patient_name.Gender),str(patient_name.Bloodtype),str(patient_name.Meds)])
	elif Patient_age>2 and Patient_age<13:
		Patient_type=Child()
		return (["Child",str(patient_name.Age),str(patient_name.Gender),str(patient_name.Bloodtype),str(patient_name.Meds)])
	elif Patient_age>=13 and Patient_age<18:
		Patient_type=Adolescent()
		return (["Adolescent",str(patient_name.Age),str(patient_name.Gender),str(patient_name.Bloodtype),str(patient_name.Meds)])
	elif Patient_age>=18 and Patient_age<60:
		Patient_type=Adult()
		return (["Adult",str(patient_name.Age),str(patient_name.Gender),str(patient_name.Bloodtype),str(patient_name.Meds)])
	else:
		Patient_type=Senior()
		return (["Senior",str(patient_name.Age),str(patient_name.Gender),str(patient_name.Bloodtype),str(patient_name.Meds)])

#--------Gameplay---------
Patient_list=dict()

while True:
	print(Patient_list)
	choice=input("Restart: 1" +"\n"+ "Add New: 2" +"\n"+ "Continue: 3" +"\n"+ "See All Notes: 4"+"\n")
		
	if choice=="1":
		Patient_list=dict()
	elif choice=="2":
		patient_name=random.choice(name)
		Patient_list[patient_name]=make_patient(patient_name)
	elif choice=="3":
		pass
		#when this is chosen, a new page would open that displays a list of the patients currently available
	elif choice=="4":
		pass
		#when this is chosen, a new page would open that displays a list of all notes.
	else:
		print("Please choose a number above")