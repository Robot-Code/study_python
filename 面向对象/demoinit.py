class DemoInit:
	def __init__(self,x,y=0):
		self.x = x
		self.y = y
	def mycacl(self):
		return self.x + self.y
dia = DemoInit(2)
print('调用mycacl方法的结果：1')
print(dia.mycacl())

dib = DemoInit(3,7)
print('调用mycacl方法的结果：2')
print(dib.mycacl())

input()