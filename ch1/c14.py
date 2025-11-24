import os
#Specify the directory
dp = "c:/"

#list all files and directory
content = os.listdir(dp)

#printing 
for item in content:
    print(item)