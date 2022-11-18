#!/usr/bin/env python3
L = dict()
all_classes = {}

def exit_mroc3():
	print('No')
	exit()

def check_in(lst):
	for i in range(1, len(lst)):
		if lst[i] == tmp:
			return True
	return False 


def mroC3(thisclass):
#	print(thisclass)
	if len(all_classes[thisclass]) == 0:
		return [thisclass]
	merge_args = []
	for parent in all_classes[thisclass]:
		merge_args.append(L[parent].copy() if parent in L else mroC3(parent))
	merge_args.append(all_classes[thisclass])
#	print(merge_args)
	res = []
	while len(merge_args) != 1:
		for LCX in range(len(merge_args[:-1])):
			print(len(merge_args[:-1]), ":", merge_args[:-1])
	#		Берётся нулевой элемент из первой линеаризации
			tmp = merge_args[LCX][0]
	#		Этот элемент ищется во всех других линеаризация
			for i in range(len(merge_args[:-1])):
	#			Если этот элемент найден где-то вне начала списка 
				if check_in(merge_args[i]):
					break
			else:
	#			Если элемент нигде не найден в позиции отличной от нулевой, то он добавляется в конец итогового списка линеаризации
				res.append(tmp)
	#			и удаляется из всех рассматриваемых списков (от L[C1] до L[CN])
				for i in merge_args:
					if tmp in i:
						i.remove(tmp)
	#			Если после удаления элемента остались пустые списки — они исключаются из объединения.
				while [] in merge_args:
					merge_args.remove([])
				break
		else:
			exit_mroc3()
	return [thisclass] + res
	
while inp := input():
	if 'class' in inp:
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
		
		
#		L[C] = [C] + merge(L[C1], L[C2], …, L[CN], [C1, C2, …, CN])
#		L[C1] = [C1] + merge(...)
		L[thisclass] = mroC3(thisclass)
#		print(L)

print('Yes')
				