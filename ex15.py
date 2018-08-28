from sys import argv

script, filename = argv

txt = open(filename) #Open the file name provided

print (f"Here's your file {filename}:") #Prints the filename
print (txt.read()) #Reads the file

print ("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
