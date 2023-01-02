#!/usr/bin/env python3

import sys, re

alphabet = r'[\x00-\x7FА-Я]+'

def check_koi8_r(encoded_string):
	try:
		decoded_string = encoded_string.decode('koi8-r')
	except:
		return False 
	try:
		if decoded_string.split()[0] == 'ПРОЦ':
			return True
		return False
	except:
		return False
	
encodings = 'cp037 cp1006 cp1250 cp1251 cp1253 cp1254 cp1255 cp1256 cp1257 cp1258 cp437 cp720 cp737 cp775 cp850 cp852 cp855 cp864 cp866 cp869 cp874 cp875 hp_roman8 iso8859_10 iso8859_16 iso8859_4 iso8859_5 koi8_r latin_1 mac_croatian mac_greek mac_iceland mac_latin2'.split()

inp = sys.stdin.read()
small_check = inp.split('\n')[0]

# из объяснений в чате:
# Можно вот так, чтоб совсем понятно:
# "ФЧж".encode('cp855').decode('cp855').encode('cp1251').decode('iso8859_5').encode('cp1251').decode('cp869').encode('mac_greek').decode('koi8-r')

for encoding1 in encodings:
	try:
		encoded_small_check1 = small_check.encode(encoding1)
	except:
		continue
	if check_koi8_r(encoded_small_check1):
		try:
			res = inp.encode(encoding1).decode('koi8-r')
		except:
			continue
		if re.fullmatch(alphabet, res):
			print(res.strip('%'))
			exit(0)
			break
	for encoding2 in encodings:
		if encoding1 != encoding2:
			try:
				encoded_small_check2 = encoded_small_check1.decode(encoding2)
			except:
				continue
			for encoding3 in encodings:
				if encoding2 != encoding3:
					try: 
						encoded_small_check3 = encoded_small_check2.encode(encoding3)
					except:
						continue
					if check_koi8_r(encoded_small_check3) :
						try:
							res = inp.encode(encoding1).decode(encoding2).encode(encoding3).decode('koi8-r')
						except:
							continue
						if re.fullmatch(alphabet, res):
							print(res.strip('%'))
							exit(0)
							break
					for encoding4 in encodings:
						if encoding3 != encoding4:
							try:
								encoded_small_check4 = encoded_small_check3.decode(encoding4)
							except:
								continue
							for encoding5 in encodings:
								if encoding4 != encoding5:
									try: 
										encoded_small_check5 = encoded_small_check4.encode(encoding5)
									except:
										continue
									if check_koi8_r(encoded_small_check5):
										try:
											res = inp.encode(encoding1).decode(encoding2).encode(encoding3).decode(encoding4).encode(encoding5).decode('koi8-r')
										except:
											continue
										if re.fullmatch(alphabet, res):
											print(res.strip('%'))
											exit(0)
											break
							