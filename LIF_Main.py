import sys, getopt
import os.path

from LIF_FileChecker import LIF_FileChecker
from LIF_FileParser import LIF_FileParser

def CheckInputParameters(argv):
	gl_in = ''
	gl_out = ''

	try:
		opts, args = getopt.getopt(argv, "i:o",["ifile=", "ofile="])
	
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		raise Exception("Wrong input parameters")

	for opt, arg in opts:
		if opt in ("-i", "--ifile"):
			gl_in = arg

		if opt in ("-o", "--ofile"):
			gl_out = arg

	if os.path.isfile(gl_in) == False:
		print "File does not exist"
		raise Exception("File does not exist")

	print "Returning file name:",gl_in
	gl_in = gl_in.replace(' ', '')
	return gl_in

def main():
	ifile = CheckInputParameters(sys.argv[1:])

	content = LIF_FileChecker(ifile)
	param = LIF_FileParser(content)

if __name__ == '__main__':
	main()

