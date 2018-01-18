# -*- coding: UTF-8 -*-

text =  raw_input()



code_map = code_map.decode('utf-8')
ans_map  = ans_map.decode('utf-8')
dict1 = {u'\u2202': u'd', u'\u2206': u'j', u'\u220f': u'P', u'\u2211': u'w', u'\u0192': u'f', u'\xc5': u'A', u'\u221a': u'v', u'\xd2': u'L', u'\u221e': u'5', u'\xa1': u'1', u'\u2020': u't', u'\xa3': u'3', u'\u2122': u'2', u'\xa5': u'y', u'\xc7': u'C', u'\xa7': u'6', u'\xa9': u'g', u'\xa8': u'U', u'\u222b': u'b', u'\xaa': u'9', u'\xac': u'l', u'\xae': u'r', u'\u0131': u'B', u'\u2030': u'R', u'\xb5': u'm', u'\xb4': u'E', u'\xb6': u'7', u'\u2022': u'8', u'\xba': u'0', u'\xbf': u'?', u'\xc1': u'Y', u'\u03c0': u'p', u'\xc2': u'M', u'\u201e': u'W', u'\u02c7': u'T', u'\u02c6': u'I', u'\u2248': u'x', u'\u25ca': u'V', u'\xcd': u'S', u'\xcf': u'F', u'\xce': u'D', u'\u0153': u'q', u'\xa2': u'4', u'\xd4': u'J', u'\xb8': u'Z', u'\u02d9': u'h', u'\xd8': u'O', u'\u02db': u'X', u'\u02da': u'k', u'\u02dd': u'G', u'\u02dc': u'N', u'\xdf': u's', u'\xe5': u'a', u'\u2264': u',', u'\xe7': u'c', u'\u2265': u'.', u'\xd3': u'H', u'\u03a9': u'z', u'\u0152': u'Q', u'\xf8': u'o', u'\uf8ff': u'K'}


ans=""

for i in unicode(text,"utf-8"):

		ans+= dict1[i]


print ans



