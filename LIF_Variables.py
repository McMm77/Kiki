class Variable(object):
	def __init__(self, identifier, start_val):
		self.val = start_val
		self.id = identifier

	def Set(self, new_val):
		self.val = new_val

	def Get(self):
		return self.val

class IntegerVariable(Variable):
	def __init__(self, identifier, start_val):
		super(IntegerVariable, self).__init__(identifier, start_val)

	def Set(self, new_val):
		if type(new_val) is not int:
			if type(new_val) is not float:
				raise Exception

		super(IntegerVariable, self).Set(new_val)

	def ToStr(self):
		return str(self.val)

class FloatVariable(Variable):
	def __init__(self, identifier, start_val):
		super(FloatVariable, self).__init__(identifier, start_val)

	def Set(self, new_val):
		if type(new_val) is not float:
			if type(new_val) is not int:
				raise Exception

		super(FloatVariable, self).Set(new_val)

	def ToStr(self):
		return str(self.val)

class BoolVariable(Variable):
	def __init__(self, identifier, start_val):
		super(BoolVariable, self).__init__(identifier, start_val)

	def Set(self, new_val):
		if type(new_val) is not bool:
			raise Exception

		super(BoolVariable, self).Set(new_val)

	def ToStr(self):
		if self.val == True:
			return "True"
		return "False"

class StringVariable(Variable):
	def __init__(self, identifier, start_val):
		super(StringVariable, self).__init__(identifier, start_val)

	def Set(self, new_val):
		if type(new_val) is not str:
			raise Exception

		super(StringVariable, self).Set(new_val)

def UT():
	myString = StringVariable(1, 'HALLO WERELD')

	bool1 = BoolVariable(2, True)
	print bool1.ToStr()
	
	int1 = IntegerVariable(3, 324)
	print int1.ToStr()

	float1 = FloatVariable(4, 20.65)
	float2 = FloatVariable(5, 10.6)
	print float1.ToStr()

	float1.Set(10.6)
	print float1.ToStr()

	b = float1.Get() + float2.Get()

	bool1.Set(False)

	if bool1.Get() == True:
		print "TRUE:"
	else:
		print "TT"

	int1.Set(132)
	print int1.ToStr()

	
	print str(b)

	int1.Set(234324.65)

	

if __name__ == '__main__':
	UT()



	
