
from LIF_GrammerObject import *

class Node(object):
	def __init__(self, content, parent_node):
		splitContent = self.split_node_parameters(content)

		self.parent_node = parent_node
		self.name = splitContent[0]
		self.param_list = self.create_param_list(splitContent[1:])
		self.grammer_obj = self.construct_grammer(self.name, self.param_list)
		print self.name
		self.grammer_obj.ExtractAndCheckParameters()

	def get_name(self):
		return self.name

	def split_node_parameters(self, content):
		return content.split()

	def create_param_list(self, param_list):
		dict_ke = {}
		for param in param_list:
			single_item=(param.replace("'","")).split('=')

			if len(single_item) != 2:
				print param_list
				raise Exception("Node::create_param_list - Un Assignment within parram list")
			

			# Check if key already exists. If so, throw exception
			if single_item[0] in dict_ke:
				raise Exception("Node::create_param_list - Key already exists")

			dict_ke[single_item[0]] = single_item[1]

		print param_list
		return dict_ke

	def construct_grammer(self, grammer_name, param_list):
		class_name = grammer_name + "_GrammerObj"
		targetClass = getattr(Grammer, class_name)
		instance = targetClass(param_list)

		return instance

class NormalNode(Node):
	def __init__(self, content, parent_node):
		super(NormalNode, self).__init__(content, parent_node)
		self.container = {}

	def close(self, name):
		if name[1:] != self.name:
			raise Exception("Wrong Tag Closure")

		return self.parent_node

	def add_node_to_container(self, node):
		if node.get_name() not in self.container:
			self.container[node.get_name()] = []

		self.container[node.get_name()].append(node)
		return node
				


class BaseNode(NormalNode):
	def __init__(self, content):
		print "BaseNode" + content
		super(BaseNode, self).__init__(content, None)


class EndNode(Node):
	def __init__(self, content, parent_node):
		content = content.replace('/','')
		super(EndNode, self).__init__(content, parent_node)

class GrammerDirector:
	def __init__(self):
		self.allClasses = []

	def construct(self, builderName, param_list):
		targetClass = getattr(Grammer, builderName)
		instance = targetClass(param_list)
		self.allClasses.append(instance)




def LIF_FileParser(fileContent):
	contentList = fileContent[1:-1].split("><")
	director = GrammerDirector()
	curr_node = None

	for content in contentList:
		if curr_node == None:
			curr_node = BaseNode(content)

		else:
			if content[-1] == '/' or content[0] == '/':
				if content[-1] == '/':
					node = EndNode(content, curr_node)
					curr_node.add_node_to_container(node)

				if content[0] == '/':
					curr_node = curr_node.close(content)
		
			else:
				node = NormalNode(content, curr_node)
				curr_node = curr_node.add_node_to_container(node)

