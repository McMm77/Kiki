from LIF_Variables import *

class MultiplyOperator:
	def __init__(self):
		pass

	def MayNotHandle(self, action_param):
		if action_param.CheckIfBool() or action_param.CheckIfString():
			raise Exception

	def ExecuteAction(self, action_param):
		self.MayNotHandle(action_param)

		product = action_param.LeftVar().Get() * action_param.RightVar().Get()
		action_param.ProdVar().Set(product)
		
class DivideOperator:
	def __init__(self):
		pass

	def MayNotHandle(self, action_param):
		if action_param.CheckIfBool() or action_param.CheckIfString():
			raise Exception

		if action_param.RightVar().Get() == 0:
			raise Exception

	def ExecuteAction(self, action_param):
		self.MayNotHandle(action_param)

		product = action_param.LeftVar().Get() / action_param.RightVar().Get()
		action_param.ProdVar().Set(product)

class AddOperator:
	def __init__(self):
		pass

	def MayNotHandle(self, action_param):
		if action_param.CheckIfBool() or action_param.CheckIfString():
			raise Exception

	def ExecuteAction(self, action_param):
		self.MayNotHandle(action_param)

		product = action_param.LeftVar().Get() + action_param.RightVar().Get()
		action_param.ProdVar().Set(product)

class MinusOperator:
	def __init__(self):
		pass

	def MayNotHanlde(self, action_param):
		if action_param.CheckIfBool() or action_param.CheckIfString():
			raise Exception

	def ExecuteAction(self, action_param):
		self.MayNotHandle(action_param)

		product = action_param.LeftVar().Get() - action_param.RightVar().Get()
		action_param.ProdVar().Set(product)


class OperatorAction(object):
	def __init__(self, operator, left_var, right_var, prod_var):
		self.left_var = left_var
		self.right_var = right_var
		self.prod_var = prod_var
		self.operator = operator
	
		if self.CheckIfBool() or self.CheckIfString():
			raise Exception

	def Execute(self):
		self.operator.ExecuteAction(self)

	def LeftVar(self):
		return self.left_var

	def RightVar(self):
		return self.right_var

	def ProdVar(self):
		return self.prod_var

	def CheckIfBool(self):
		if type(self.left_var) is bool or type(self.right_var) is bool or type(self.prod_var) is bool:
			raise Exception

	def CheckIfString(self):
		if type(self.left_var) is str or type(self.right_var) is str or type(self.prod_var) is str:
			raise Exception

	def CheckVarIfSameTypes(self):
		ta = type(self.left_var)
		tb = type(self.right_var)
		tc = type(self.prod_var)

		return ta == tb == tc

class IncrementAction(OperatorAction):
	def __init__(self, left_var, right_var, prod_var):
		super(IncrementAction, self).__init__(AddOperator(), left_var, right_var, prod_var)

class DecrementAction(OperatorAction):
	def __init__(self, left_var, right_var, prod_var):
		super(DecrementAction,self).__init__(MinusOperator(), left_var, right_var, prod_var)

class MultiplyAction(OperatorAction):
	def __init__(self, left_var, right_var, prod_var):
		super(MultiplyAction, self).__init__(MultiplyOperator(), left_var, right_var, prod_var)

class DivideAction(OperatorAction):
	def __init__(self, left_var, right_var, prod_var):
		super(DivideAction, self).__init__(DivideOperator(), left_var, right_var, prod_var)

		if self.RightVar() == 0:
			raise Exception

def ut():
	print "UT"
	int_a = IntegerVariable(1, 12)
	int_aa = IntegerVariable(3, 12)
	int_b = IntegerVariable(2, 35)

	int_c = IntegerVariable(3, 0)
        int_d = IntegerVariable(4, 0)
	int_f = FloatVariable(5, 12)
	int_divr = IntegerVariable(1,0)
	float_divr = FloatVariable(1,0)


	action_div = DivideAction(int_b, int_a, float_divr)
	action = IncrementAction(int_a, int_b, int_c)
	action1 = MultiplyAction(int_a, int_aa, int_d)

	action.Execute()
	action1.Execute()
	action_div.Execute()

	print "IntegerC = ", str(int_c.Get())
	print "IntegerD = ", str(int_d.Get())
	print "IntegerDiv = ", str(float_divr.Get())

if __name__ == '__main__':
	ut()
