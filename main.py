import sys, os
# This is the commands list.
cmd_list = ['cwd', 'pwd', 'man', 'cd', 'ls']
class PrintCMD(Command):
	def __init__(self, command):
		self.final = command
		if(arg.type == list):
			self.final = ''
			for i in range(len(arg)):
				self.final = self.final + " " + arg[i]
# Print commands included
	def printCWD(self):
		print(self.final)
	def printPWD(self):
		print(self.final)		
	def printCD(self):
		print(self.final)
	def printLS(self):
		print(self.final)
# Processor class for processing data 
class Processor(Command):
	# This function is for the folder name extraction.
	def getCWD(self):
		dirpath = os.getcwd()
		foldername = os.path.basename(dirpath)
		prcInst.printCWD(foldername)
# This function is for present working directory, **pwd** extraction
	def getPWD(self):
		dirpath = os.getcwd()
		prcInst.printPWD(dirpath)
# This function is similar to **cd** in bash
	def getCD(self, path):
		path = path
		# Error Handling
		if(path == ''):
			path = '/home'
		os.chdir(path)
# This function is simlar to **ls** in bash
	def getLS(self, path):	
		path = path
		if(path == ''):
			prcInst.printLS(os.listdir('.'))
		prcInst.printLS(os.listdir(path))
#	Constructor class
	def __init__(self, cmd):
		prcInst = PrintCMD(cmd)
# Command class for taking in the relevant commands.
class Command:
	def getCWD(self):
		pass
	def getLS(self):
		pass
	def getPWD(self):
  		pass
	def getCD(self):
 		pass
	def printCWD(self):
		pass
	def printPWD(self):
 		pass
	def printCD(self):
		pass 
	def printLS(self):
		pass 
# Constructor Function also taking care of what the input is
	def __init__(self, ip):
		if(ip not in cmd_list):
			print("Command is not in the domain list or it is an invalid combination. Try again please !!\n")
		elif(ip == "cwd"):
			self.getCWD()
		elif(ip == "pwd"):
			self.getPWD()
		elif("cd" == ip[0:2]):
			path = ip[3:]
			self.getCD(path)
		elif("ls" == ip[0:2]):
			path = ip[3:]
			self.getLS(path)

def main():
	print("Welcome to \"Bash Shell\" by *Siddharth Bhatore*,\n **sbhatore95@gmail.com**. \n")
	print("This bash shell supports:" + "")
	for i in range(len(cmd_list)):
		print(cmd_list[i])
	print("\nEnter the commands below. Press enter to see what happens :) !!\n")
	while(1):
		print(">>")
		curr_input = input()
		cmdInst = Command(curr_input)
		procInst = Processor(cmdInst)
		procInst.printCMD()


if __name__ == "__main__":
	main()
