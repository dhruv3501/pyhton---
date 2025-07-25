dict ={'Dhruv': 45 , 'ridham': 50 , 'akash': 55}
key =input("Enter the student's name : ")

if key in dict:
    print(key,"'s Marks: " ,dict[key])
else:
    print("Student not found.")


