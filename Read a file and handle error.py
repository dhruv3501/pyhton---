try:
    file = open ('Sample.txt')
    print("Reading file Content : ")
    reading_file = file.read()
    print(reading_file)
    file.close()

except FileNotFoundError:
    print(" Error : The file" ,'Sample.txt',"not found")