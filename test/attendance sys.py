from pyzbar.pyzbar import decode
from PIL import Image
import cv2 , time
import csv
import datetime 
import pywhatkit 
from functools import lru_cache
import time
import subprocess
import platform
import os
#--------------------------------------------------------------------------------------------------------------------


student = []
p_student=[]
sname=[]
a_student=[]
mob_no=[]
a_mob_no=[]
p_mob_no=[]
#------------------------------------------------------------------------------------------------------------------------------------------

print('''

 
        
      █████╗ ██╗   ██╗████████╗ ██████╗  █████╗ ████████╗████████╗███████╗███╗   ██╗██████╗ 
     ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝████╗  ██║██╔══██╗
     ███████║██║   ██║   ██║   ██║   ██║███████║   ██║      ██║   █████╗  ██╔██╗ ██║██║  ██║
     ██╔══██║██║   ██║   ██║   ██║   ██║██╔══██║   ██║      ██║   ██╔══╝  ██║╚██╗██║██║  ██║
     ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║  ██║   ██║      ██║   ███████╗██║ ╚████║██████╔╝
     ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═══╝╚═════╝                                                                                       
  

Credits:-
Nikhil Utkarsha Marar Hari
Apurvam Arya
Shubham Gupta


''')
#-------------------------------------CSV WRITER----------------------------------------------------------------------------------
'''inf = [{'sno':1,'admission_no':1111,'name':'Nikhil','pno.': '+919472150880'},
{'sno':2,'admission_no':1112,'name':'Shubham','pno.': '+919122556471'},
{'sno':3,'admission_no':1113,'name':'Apurvam','pno.': '+919065558793'},
{'sno':4,'admission_no':1114,'name':'Lakshya','pno.': '+919472150880'},
{'sno':5,'admission_no':1115,'name':'Shalin','pno.': '+919122556471'}
]

with open("student.csv",mode='w') as csvfile:
  feildnames = inf[0].keys()
  writer = csv.DictWriter(csvfile, fieldnames= feildnames) 
  for row in inf:
    writer.writerow(row)

'''




#-------------------------------------CSV DATA EXTRACTOR----------------------------------------------------------------------------------
@lru_cache(maxsize=1)
def data_ext ():
 with open('student.csv','r') as file:
  reader = csv.reader(file)
  for row in reader:
    if row:
      student.append((row[1]))

 with open('student.csv','r') as file:
  reader = csv.reader(file)
  for row in reader:
    if row:
      sname.append((row[2]))

 with open('student.csv','r') as file:
  reader = csv.reader(file)
  for row in reader:
    if row:
      mob_no.append((row[3]))

data_ext()

#------------------------------------------------------------------------------------------------------
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FPS, 60)

while not video.isOpened():
    time.sleep(0.1)
print('Scanner opened successfully!!')    



while True:
    ret, frame = video.read()

    if not ret:
        print("Error: Unable to capture video from the webcam.")
        break

    #----------------------------BARCODE DECODE--------------------------------

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    decoded_objects = decode(gray_frame)
       

    cv2.imshow('Scanner', gray_frame)

    # Press 'Esc' to exit the scanner
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
   
    

        
    for obj in decoded_objects:
        name = decoded_objects[0].data.decode()      
        print(name)
        for x in student:
            if name == x:
                y=student.index(x)
                p_student.append(sname[y])
                print()
                print('present.....')
    

#-------------------------------------DUPLICATE INPUT REMOVER---------------------------------------------------------------------------------- 
def remove_duplicates(p_student):
  

  return list(set(p_student))


p_student= remove_duplicates(p_student)

def a_student(sname, p_student):
  

  def get_uncommon_elements():
    set1 = set(sname)
    set2 = set(p_student)
    uncommon = set1 ^ set2
    return list(uncommon)

  return get_uncommon_elements


uncommon_elements_function = a_student(sname, p_student)
a_student = uncommon_elements_function()


                


print('total students:',student)
print("present students:",p_student)
print("absent sudents:",a_student)



video.release()
cv2.destroyAllWindows()
#-------------------------------------ATTENDANCE TO CSV----------------------------------------------------------------------------------

def add_attendance_to_csv(p_student, a_student, csv_file):
  
  with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["Present Students"])
    writer.writerow(['-------------------'])
    for student in p_student:
      writer.writerow([student])
    writer.writerow(['====================='])
    writer.writerow(['                       '])


    writer.writerow(["Absent Students"])
    writer.writerow(['------------------'])
    for student in a_student:
      writer.writerow([student])
    writer.writerow(['====================='])
    writer.writerow(['                       '])

def create_new_csv_file(date):
 

  csv_file = f"attendance_{date}.csv"

  with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
  
    
  return csv_file

if __name__ == "__main__":
 
  date = datetime.date.today()
  csv_file = create_new_csv_file(date)

  add_attendance_to_csv(p_student, a_student, csv_file)

  print("Attendance has been added to the CSV file.")
#---------------------------------PHNO SORTING------------------------------------------------
for jk in sname:
   for kk in p_student:
    if jk == kk:
      y = sname.index(kk)
      p_mob_no.append(mob_no[y])
   for hh in  a_student:
      u = sname.index(hh) 
      a_mob_no.append(mob_no[u])

#-------------------------------MESSAGEING SYSTEM----------------------------------------------
def message():

 for taco in p_student:
   date1 = str(datetime.date.today())
   mmmm = p_student.index(taco)
   tt = "your ward "+ taco +" is present on "+ date1
   gg = p_student.index(taco)
   pywhatkit.sendwhatmsg_instantly( p_mob_no[gg] , tt )
   time.sleep(5)
  

 for kkk in a_student:
   date2 = str(datetime.date.today())
   mk = a_student.index(kkk)
   tt = "your ward "+ kkk +" is absent on "+ date2
   gg = a_student.index(kkk)
   pywhatkit.sendwhatmsg_instantly( a_mob_no[gg] , tt )
   time.sleep(5)


message()

def close_chrome():
      time.sleep(2)
      with open(os.devnull, 'w') as null_file:
        subprocess.run(['taskkill', '/F', '/IM', 'chrome.exe'], stdout=null_file, stderr=null_file, check=True)

close_chrome()
