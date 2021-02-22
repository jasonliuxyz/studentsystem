import os

filename = 'student.txt'
def main():
	while True:
		menu()
		choice = int(input('请选择'))
		if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
			if choice == 0:
				answer = input('您确定退出系统吗?y/n')
				if answer == 'y' or answer == 'Y':
					print('谢谢您的使用')
					break
				else:
					continue
			elif choice == 1:
				insert()
			elif choice == 2:
				search()
			elif choice == 3:
				delete()
			elif choice == 4:
				modify()
			elif choice == 5:
				sort()
			elif choice == 6:
				total()
			elif choice == 7:
				show()

def menu():
	print('======================学生信息管理系统===========================')
	print('-------------------------功能菜单-------------------------------')
	print('					1. 录入学生信息')
	print('					2. 查找学生信息')
	print('					3. 删除学生信息')
	print('					4. 修改学生信息')
	print('					5. 排序')
	print('					6. 统计学生总人数')
	print('					7. 显示所有学生信息')
	print('					0. 退出系统')
	print('-------------------------------------------------------------')

def insert():
	student_list = []
	while True:
		id = input('请输入学生ID(1001): ')
		name = input('请输入学生姓名: ')
		if id and name:
			try:
				english = int(input('请输入英语成绩: '))
				python = int(input('请输入python成绩: '))
				java = int(input('请输入java成绩: '))
			except:
				print('输入无效，不是整数类型，请重新输入')
				continue

		student= {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
		student_list.append(student)

		answer = input('是否继续录入？y/n')
		if answer == 'y' or answer == 'Y':
			continue
		else:
			break

	save(student_list)
	print('学生信息录入完成!!!')

def save(lst):
	if os.path.exists(filename):
		with open(filename, 'a', encoding='utf-8') as af:
			for item in lst:
				af.write(str(item)+'\n')
	else:
		with open(filename, 'w', encoding='utf-8') as wf:
			for item in lst:
				wf.write(str(item)+'\n')

def search():
	student_new = []
	while True:
		id = ''
		name = ''
		answer = input('请输入查询方式 1.ID查询 2.姓名查询：')
		if answer == '1':
			id = input('请输入学生ID：')
		elif answer == '2':
			name = input('请输入学生姓名：')
		else:
			print('查询方式不对，请重新输入')
			continue
		with open(filename, 'r', encoding='utf-8') as rfile:
			student_old = rfile.readlines()

		for item in student_old:
			student = dict(eval(item))
			if student['id'] == id or student['name'] == name:
				student_new.append(student)

		show_student(student_new)
		student_new.clear()

		answer = input('是否继续查找？y/n')
		if answer == 'y' or answer == 'Y':
			continue
		else:
			break

def show_student(lst):
	if len(lst) == 0:
		print('没有查询到学生信息, 无数据显示')
		return
	
	format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
	print(format_title.format('ID', '姓名', 'english成绩', 'python成绩', 'java成绩', '总成绩'))
	format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
	for item in lst:
		print(format_data.format(item.get('id'),
								item.get('name'),
								item.get('english'),
								item.get('python'),
								item.get('java'),
								int(item.get('english'))+int(item.get('python'))+int(item.get('java'))))

def delete():
	while True:
		student_new = []
		id = input('请输入要删除的学生ID(1001): ')
		if not id:
			continue
		else:
			if os.path.exists(filename):
				with open(filename, 'r', encoding='utf-8') as rf:
					student_old = rf.readlines()
			else:
				student_old = []

			flag = False

			if student_old:
				with open(filename, 'w', encoding='utf-8') as wf:
					d = {}
					for item in student_old:
						d = dict(eval(item))
						if d['id'] != id:
							wf.write(str(d)+'\n')
						else:
							flag = True
					if flag:
						print(f'id为{id}的学生信息已被删除！！！')
					else:
						print(f'没有找到ID为{id}的学生信息')
			else:
				print('无学生信息')
				break

			show()

			answer = input('是否继续?y/n')
			if answer == 'y' or answer == 'Y':
				continue
			else:
				break

def modify():
	show()
	if os.path.exists(filename):
		with open(filename, 'r', encoding='utf-8') as rf:
			student_old = rf.readlines()
	else:
		return

	id = input('请输入要修改的学生ID(1001): ')
	with open(filename, 'w', encoding='utf-8') as wf:
		for item in student_old:
			d = dict(eval(item))
			if d['id'] == id:
				print('找到学习信息，可以修改其相关信息了！')
				while True:
					try:
						d['name'] = input('请输入学生姓名: ')
						d['english'] = int(input('请输入英语成绩: '))
						d['python'] = int(input('请输入python成绩: '))
						d['java'] = int(input('请输入java成绩: '))
					except:
						print('输入无效，不是整数类型，请重新输入')
					else:
						break
				wf.write(str(d)+'\n')
				print('修改成功！！！')
			else:
				wf.write(str(d)+'\n')
	
		answer = input('是否继续?y/n')
		if answer == 'y' or answer == 'Y':
			modify()

def sort():
	show()
	if os.path.exists(filename):
		with open(filename, 'r', encoding='utf-8') as rfile:
			students = rfile.readlines()
			student_new = []
			for item in students:
				student_new.append(dict(eval(item)))
	else:
		print('无学生信息')

	asc_or_desc = input('请选择排序方式 (0.升序 1.降序)')
	if asc_or_desc == '0':
		flag = False
	elif asc_or_desc == '1':
		flag = True
	else:
		print('输入有误，请重新输入')
		sort()

	mode = input('请选择排序方式，(1.english成绩排序 2.python成绩排序 3.java成绩排序 0.总成绩排序)')
	if mode == '1':
		student_new.sort(key=lambda x : int(x['english']), reverse=flag)
	elif mode == '2':
		student_new.sort(key=lambda x : int(x['python']), reverse=flag)
	elif mode == '3':
		student_new.sort(key=lambda x : int(x['java']), reverse=flag)
	elif mode == '0':
		student_new.sort(key=lambda x : int(x['english']) + int(x['python']) + int(x['java']) , reverse=flag)
	else:
		print('输入有误，请重新输入')
		sort()

	show_student(student_new)

def total():
	if os.path.exists(filename):
		with open(filename, 'r', encoding='utf-8') as rfile:
			students = rfile.readlines()
			if students:
				student_num = len(students)
				print(f'一共有{student_num}名学生')
			else:
				print('无数据显示')
				
	else:
		print('无学生信息')

def show():
	student_new = []
	if os.path.exists(filename):
		with open(filename, 'r', encoding='utf-8') as rfile:
			students = rfile.readlines()
			for item in students:
				student = dict(eval(item))
				student_new.append(student)
			if student_new:
				show_student(student_new)
	else:
		print('无学生信息')

if __name__ == '__main__':
	main()
