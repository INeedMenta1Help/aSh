from sys import *
from pathlib import Path

class aSh:
	ver = "1.0.0"
	def __init__(self, filename, filename2):
		self.cls()
		self.load()
		self.loop(filename, filename2)
		self.load()

	def load(self):
		print("aSh-lib: A Shell Library: Version", self.ver)

	def println(self, s):
		print("\t>> " + s)

	def cls(self):
		for i in range(0, 100):
			print("\n")

	def loop(self, filename, filename2):
		f = open(filename, "r").read()
		f = list(f)

		p = open(filename2, "r").read()
		p = list(p)

		users = []
		passwrds = []

		tok = ""
		for char in f:
			if char == " " or char == ";":
				users.append(tok)
				tok = ""
			else:
				tok += char

		tok = ""
		for char in p:
			if char == " " or char == ";":
				passwrds.append(tok)
				tok = ""
			else:
				tok += char

		#print(users)
		#print(passwrds)

		Login = False
		while Login == False:
			user_input_user = input("Username >> ")
			user_input_pass = input("Password >> ")
			for i in range(0, len(users)):
				if user_input_user == users[i]:
					if user_input_pass == passwrds[i]:
						self.println("Login Sucsessful")
						print("")
						Login = True
						break
					else:
						self.println("Incorrect Username Or Password")
						break
				else:
					self.println("Incorrect Username Or Password")
					break

		while True:
			user_input_shell = input("aSh >> ")

			if user_input_shell == "cls":
				self.cls()
			elif user_input_shell == "exit":
				break
#Println
			elif user_input_shell[:9] == "println: ":
				self.println(user_input_shell[9:])
#FileRead
			elif user_input_shell[:10]  == "fileread: ":
				filereading = open(user_input_shell[10:], "r").read()
				self.println(user_input_shell[10:])
				print("\n", filereading)
#writefile
			elif user_input_shell[:11] == "filewrite: ":
				file_name = user_input_shell[11:]
				my_file = Path(file_name)
				if my_file.is_file():
    				# file exists
					writefile = open(file_name, "a")
					while True:
						user_input_filewrite = input("Write2File >> ")
						if user_input_filewrite == "close:":
							break
						elif user_input_filewrite == "newline:":
							writefile.write("\n")
						else:
							writefile.write(user_input_filewrite)
							writefile.write("\n")
							self.println("Succsessfully Written: " + user_input_filewrite + ", To File")
					writefile.close()

				else:
					self.println("File does not exist")

#CleanFile
			elif user_input_shell[:7] == "clean: ":
				file_name = user_input_shell[7:]
				cleanfile = open(file_name, "w+")
				cleanfile.write("Cleaned By aSh-lib Version: " + self.ver)
				self.println("Succsessfully Cleaned: " + file_name)




			else:
				self.println("Unknown Command")
			print("")


aSh = aSh("users/users.txt", "users/pass.txt")