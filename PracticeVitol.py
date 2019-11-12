# -*- coding: utf-8 -*-

txt = '''450
 00:17:53,457 --> 00:17:56,175
 Okay, but, um,
 thanks for being with us.

451
 00:17:56,175 --> 00:17:58,616
 But, um, if there's any
 college kids watching,

452
 00:17:58,616 --> 00:18:01,610
 But, um, but, um, but, um,
 out, um, but, um,

453
 00:18:01,610 --> 00:18:03,656
 We have to drink, professor.
454
 00:18:03,656 --> 00:18:07,507
 It's the rules.
 She said "But, um"

455
 00:18:09,788 --> 00:18:12,515
 But, um, but, um, but, um...
 god help us all.
 '''
import re
#print(re.findall('[b,B,o]ut, um', txt))
#print(re.search('but, um', txt).count())
xx = "guru99,education is fun"
r1 = re.findall(r"\w+", xx)
print(r1)
print((re.split(r'\s','we are splitting the words')))
print((re.split(r's','split the words')))


#################################
#pandas Crosstab example

