# https://stackoverflow.com/questions/1825384/using-super-in-nested-classes

class Grammer: 
	class GrammerObject(object):
		def __init__(self, param_list):
			self.param_list = param_list

		def ExtractAndCheckParameters(self):
			print "Emtpy ExtractAndCheckParameters"
 
	class Parameters_GrammerObj(GrammerObject):
		def __init__(self, param_list):
			super(self.__class__, self).__init__(param_list)
			print "Create Parameters_GrammerObj"


	class ObjectItem_GrammerObj(GrammerObject):
		def __init__(self, param_list):
			super(self.__class__, self).__init__(param_list)

		def ExtractAndCheckParameters(self):
			pass

	class RealworldItem_GrammerObj(GrammerObject):
		def __init__(self, param_list):
			super(self.__class__, self).__init__(param_list)
		def ExtractAndCheckParameters(self):
			pass

	class RItem_GrammerObj(GrammerObject):
		def __init__(self, param_list):
			super(self.__class__, self).__init__(param_list)

		def ExtractAndCheckParameters(self):
			self.id = self.param_list['id']
			print self.id
			

			print " -----******------- "
			print self.param_list

	class SoftwareItem_GrammerObj(GrammerObject):
		def __init__(self, param_list):
			super(self.__class__, self).__init__(param_list)

		def ExtractAndCheckParameters(self):
			pass

	class SItem_GrammerObj(GrammerObject):
		def __init__(self, param_list):
			super(self.__class__, self).__init__(param_list)
		
		def ExtractAndCheckParameters(self):
			pass

	class ProgramItem_GrammerObj(GrammerObject):
		def __init__(self, param_list):
			super(self.__class__, self).__init__(param_list)

		def ExtractAndCheckParameters(self):
			pass

	class PItem_GrammerObj(GrammerObject):
		def __init__(self, param_list):
			super(self.__class__, self).__init__(param_list)

		def ExtractAndCheckParameters(self):
			pass

	class Variables_GrammerObj(GrammerObject):
		def __init__(self, param_list):
			super(self.__class__, self).__init__(param_list)

		def ExtractAndCheckParameters(self):
			pass

	class Var_GrammerObj(GrammerObject):
		def __init__(self, param_list):
			super(self.__class__, self).__init__(param_list)

		def ExtractAndCheckParameters(self):
			pass

	class Program_GrammerObj(GrammerObject):
		def __init__(self, param_list):
			super(self.__class__, self).__init__(param_list)
		
		def ExtractAndCheckParameters(self):
			pass

	class Action_GrammerObj(GrammerObject):
		def __init__(self, param_list):
			super(self.__class__, self).__init__(param_list)

		def ExtractAndCheckParameters(self):
			pass



