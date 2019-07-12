'''
Match will start matching pattern from the brginning of the string or line. 
'''
import re
string = "This is a simple sentence 31-08-1990 BVJPR1810 10.228.223.234"


pattern_obj = re.compile('\w+')
match_obj = pattern_obj.match(string)

if match_obj:
    print(match_obj.group())




