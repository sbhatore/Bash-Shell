import sys, os
# This is the commands list.
cmd_list = ['cwd', 'pwd', 'man', 'cd']

class Command:
# This function is to print the output of the command.
	def printCMD(self, to_print):
		print(to_print)
# This function is for the folder name extraction.
	def getCWD(self):
		dirpath = os.getcwd()
		foldername = os.path.basename(dirpath)
		self.printCMD(foldername)
# This function is for present working directory extraction
	def getPWD(self):
		dirpath = os.getcwd()
		self.printCMD(dirpath)
# Constructor Function also taking care of what the input is
	def __init__(self, ip):
		if(ip not in cmd_list):
			print("Command is not in the domain list or it is an invalid combination. Try again please !!\n")
		elif(ip == "cwd"):
			self.getCWD()
		elif(ip == "pwd"):
			self.getPWD()

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

if __name__ == "__main__":
	main()
