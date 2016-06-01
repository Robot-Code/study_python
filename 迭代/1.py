class MyIterator:
	def __init__ (self,x=2,xmax=100):
		self.__mull,self.__x = x,x
		self.__xmax = xmax
	def __iter (self):
		return self
	def __next__ (self):
		if self.__x and self.__x !=1:
			self.__mull *= self.__x
			if self.__mull <= self.__xmax:
				return self.__mull
			else:
				raise StopIteration
		else:
			raise StopIteration
if __name__ == '__main__':
	myiter = MyIterator()
	for i in myiter:
		print('迭代的数据元素为：',i)
		
		
		
		
	