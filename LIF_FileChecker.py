import re

class FileChecker:
	def __init__(self, file_content):
		self.fcontent = file_content

	def CheckForUnwantedChars(self):
		self.CheckForCharsBetweenBracks()
		self.CheckFirstAndLastChar()
		self.CheckForEndBracks()
		self.CheckForBrackContent()

		return self.fcontent

	def CheckFirstAndLastChar(self):
		if(not self.fcontent.startswith('<') or not self.fcontent.endswith('>')):
			raise Exception("FAILED")

	def CheckForStringError(self, strBase, strCmp):
		if strBase.find(strCmp) != -1:
			raise Exception("Failed")
			
	def CheckForBrackContent(self):
		tempBuff = self.fcontent;

		tempBuff = tempBuff.replace('/', '')
		tempBuff = re.sub(r'(?!<|>)\b([\S\s]+?)(\b|$)', lambda x: (x.end() - x.start())*'_', tempBuff)

		self.CheckForStringError(tempBuff, '<>')

		tempBuff = tempBuff.replace('_', '')

		self.CheckForStringError(tempBuff, '<<')
		self.CheckForStringError(tempBuff, '>>')

	def CheckForEndBracks(self):
		index = self.fcontent.find('/')

		while(index != -1 and index < len(self.fcontent) and index > 0):
			if self.fcontent[index-1] != '<' and self.fcontent[index+1] != '>':
				raise Exception("FAILED")

			index = self.fcontent.find('/', (index + 1))
			
	def CheckForCharsBetweenBracks(self):
		str_size = len(self.fcontent) -1
		index = self.fcontent.find('>')

		while(index != -1 and index < str_size):
			if(self.fcontent[index+1]!='<'):
				raise Exception("FAILED")

			index = self.fcontent.find('>', (index+1))

class FileCleaner:
	def __init__(self, file_content):
		self.fcontent = file_content

	def RemoveTabsAndNewLines(self):
		self.fcontent = self.fcontent.replace('\t', ' ')
		self.fcontent = self.fcontent.replace('\n', ' ')
		self.ReplaceMultiWhiteSpace()
		self.fcontent = self.fcontent.replace('> <', '><')
		self.fcontent = self.fcontent.replace(' <', '<')
		self.fcontent = self.fcontent.replace('> ', '>')

		return self.fcontent

	def ReplaceMultiWhiteSpace(self):
		while(self.fcontent.find('  ') != -1):
			self.fcontent = self.fcontent.replace('  ', ' ')

class CFile:
	def __init__(self, fileName):
		self.fcontent = ""
		with open(fileName) as f:
			self.fcontent = f.read()

	def content(self):
		return self.fcontent

def LIF_FileChecker(fileName):
	try:
		lif_file = CFile(fileName)
		file_content = lif_file.content()

		cleaner = FileCleaner(file_content)
		file_content = cleaner.RemoveTabsAndNewLines()

		verifier = FileChecker(file_content)
		file_content = verifier.CheckForUnwantedChars()

	except:
		print "Unknown Error"

	return file_content

