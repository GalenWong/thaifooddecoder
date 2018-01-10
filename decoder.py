# -*- coding: UTF-8 -*-

import sys

#text = sys.argv[1]

text = raw_input().decode('utf-8')

code_map="¡™£¢∞§¶•ªºœ∑´®†¥¨ˆøπåß∂ƒ©˙∆˚¬Ω≈ç√∫˜µ¿Œ„´‰ˇÁ¨ˆØ∏ÅÍÎÏ˝ÓÔÒ¸˛Ç◊ı˜Â≤≥"

ans_map ="1234567890qwertyuiopasdfghjklzxcvbnm?QWERTYUIOPASDFGHJKLZXCVBNM,."


ans_map = ans_map.decode('utf-8')

code_map = code_map.decode('utf-8')

ans = ""
for i in range(len(text)):
	found = False
	for j in range(len(code_map)):
		if(text[i]==code_map[j]):
			ans += ans_map[j]
			found = True
			break

	if(not found):
		ans+=text[i]



print ans



