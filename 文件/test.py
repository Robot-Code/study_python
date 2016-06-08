import os
dirs = os.getcwd()
print(dirs)
f = open(dirs+'/test.txt','r')
print(f.read())
#f.write('test')
#f.close()
exit(0)
num = 0
for i in f:
	num +=1
	#python是强类型语言，要把int类型转换为str类型
	f2 = open(dirs+"/test2/"+str(num)+".txt",'w')
	f2.write(i)
	f2.close()
#	print("第%s行的数据为"%num,i)

