#模块文件
#文件名称：module_test.py
print('导入的测试模块的输出')
name = 'module_test'

def m_t_pr ():
	print('模块module_test中m_t_pr()')
if __name__=='__main__':
	m_t_pr()
	print(name)