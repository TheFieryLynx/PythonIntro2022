#!/usr/bin/env python3
all_classes = {} 
L = {} 

def exit_mroc3():
	print('No')
	exit()
	
def check_in(item, lst):
	for i in range(1, len(lst)):
		if lst[i] == item:
			return True
	return False 

def mroC3(thisclass): 
	if len(all_classes[thisclass]) == 0: 
		return [thisclass] 
	merge_args = [] 
	for parent in all_classes[thisclass]: 
		merge_args.append(L[parent] if parent in L else mroC3(parent))
		
	merge_args.append(all_classes[thisclass]) 
	result = [] 
	while merge_args: 
		if len(merge_args) == 1: 
			for i in merge_args[0]:
				result.append(i)
			return [thisclass] + result 
		flag1 = True
		for LCX in range(len(merge_args[:-1])):
			if len(merge_args[LCX]) == 0:
				continue
#			Берётся нулевой элемент из первой линеаризации
			tmp = merge_args[LCX][0] 
			flag2 = True
#			Этот элемент ищется во всех других линеаризация
			for i in merge_args:
				if check_in(tmp, i):
					flag2 = False
					break 
			if flag2: 
#				Если элемент нигде не найден в позиции отличной от нулевой, то он добавляется в конец итогового списка линеаризации
				result.append(tmp) 
#				и удаляется из всех рассматриваемых списков (от L[C1] до L[CN])
				for i in merge_args: 
					if tmp in i: 
						i.remove(tmp) 
#				Если после удаления элемента остались пустые списки — они исключаются из объединения.
				while [] in merge_args: 
					merge_args.remove([]) 
				flag1 = False
				break 
		if flag1: 
			exit_mroc3()
	return [thisclass] + result 

while inp := input():
	if 'class' == inp[0:5]:
		declaration = inp.split(':')[0]
		declaration = declaration.replace(' ', '')
		declaration = declaration.split('class')[1]
		if '(' in declaration:
			i = declaration.find('(')
			thisclass = declaration[:i]
			parents = declaration[i + 1:-1].split(',')
		else:
			thisclass = declaration
			parents = []
#		print(thisclass, parents)
		all_classes[thisclass] = parents
#		print(parents)
		L[thisclass] = mroC3(thisclass) 

print('Yes') 
