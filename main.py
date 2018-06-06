import sys, os

cmd_list = ['pwd', 'man', 'cd']

def getCMDpwd(a):
	print os.path.abspath(os.path.dirname(a))

def getCMDPrinted(arg):
	if(arg not in cmd_list):
		print "Command not in domain list or invalid combination. Try from :\n"
		print cmd_list
	else:
		if(arg == 'pwd'):
			getCMDpwd('.')

def main(argv):
	sys.argv[0] = "pwd"
	getCMDPrinted(sys.argv[0])

if __name__ == "__main__":
	main(sys.argv[0])