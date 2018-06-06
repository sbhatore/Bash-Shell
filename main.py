import sys, os

cmd_list = ['pwd', 'man', 'cd']

class Command:

	def printCMD(self, to_print):
		print(to_print)

	def getPWD(self):
		dirpath = os.getcwd()
		foldername = os.path.basename(dirpath)
		self.printCMD(foldername)

	def __init__(self, ip):
		if(ip not in cmd_list):
			print("Command is not in the domain list or it is an invalid combination. Try again please !!\n")
		elif(ip == "pwd"):
			self.getPWD()

# def getCMDPrinted(arg):
# 	if(arg not in cmd_list):
# 		print("Command not in domain list or invalid combination. Try again please. :)\n")
# 		print(cmd_list)
# 	else:
# 		if(arg == 'pwd'):
# 			getCMDpwd('.')

def main():
	print("Welcome to Bash Shell by *Siddharth Bhatore* \n")
	print("This bash shell supports:" + "\n")
	for i in range(len(cmd_list)):
		print(cmd_list[i] + "\n")
	print("Enter the commands below. Press enter to see what happens :) !!\n")
	while(1):
		curr_input = input()
		cmdInst = Command(curr_input)
		# getCMDPrinted(curr_input)

if __name__ == "__main__":
	main()