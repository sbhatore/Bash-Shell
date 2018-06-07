import sys, os

class PrintCMD < Command:
	def __init__(self, arg):

	def printCWD(self):

	def printPWD(self):

	def printCD(self):

	def printLS(self):

class Processor < Command:
	def __init__(self, arg):


class Command:
# This is the commands list.
	cmd_list = ['cwd', 'pwd', 'man', 'cd', 'ls']
# This function is to print the output of the command.
	def printCMD(self, to_print):
		print(to_print)
# This function is for the folder name extraction.
	def getCWD(self):
		dirpath = os.getcwd()
		foldername = os.path.basename(dirpath)
		self.printCMD(foldername)
# This function is for present working directory, **pwd** extraction
	def getPWD(self):
		dirpath = os.getcwd()

		self.printCMD(dirpath)
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
			printCMD(os.listdir('.'))
		printCMD(os.listdir(path))
# Constructor Function also taking care of what the input is
	def __init__(self, ip):
		empty_list = []
		procInst = Processor(self)
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
		printInst = PrintCMD(procInst)


if __name__ == "__main__":
	main()
