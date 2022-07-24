import re

"""
NOTE:
Argument 'flags=re.IGNORECASE' can be used with all functions.
Argument 'flags=re.MULTILINE' makes '^' and '$' match the start/end of each line.
Argument 'flags=re.DOTALL' makes dot also accept the '\n'.


'\d' == '[0-9]' # Matches any digit.
'\w' == '[a-zA-Z0-9_]' # Matches any alphanumeric.
'\s' == '[ \t\n\r\f\v]' # Matches any whitespace.

"""
################################################################################################
"""
<str> = re.sub(<regex>, new, text, count=0) # Substitutes all occurrences with 'new'.
"""
test_string = "The IP Address of machine MACHINE-01 is 10.23.44.235"
ipaddress_regex = re.compile(r'\d{1,2}.\d{1,2}.\d{1,2}.\d{1,3}')
new_string = ipaddress_regex.sub("10.10.10.10", test_string)
print("String before replace : {}".format(test_string))
print("New String after replacement : {}".format(new_string))

################################################################################################
"""
<list> = re.findall(<regex>, text) # Returns all occurrences as strings.
"""
test_string = "The IP Address of machine MACHINE-01 is 10.23.44.235, 10.23.44.25, 10.23.44.236 "
print(ipaddress_regex.findall(test_string))

################################################################################################
"""
<Match> = re.search(<regex>, text) # Searches for first occurrence of the pattern.
"""
print(ipaddress_regex.search(test_string).group())

################################################################################################
"""
<Match> = re.match(<regex>, text) # Searches only at the beginning of the text.
"""
test_string1 = "The IP Address of machine MACHINE-01 is 10.23.44.235, 10.23.44.25, 10.23.44.236"
test_string2 = "10.23.44.236 The IP Address of machine MACHINE-01 is 10.23.44.235, 10.23.44.25, 10.23.44.236"
print(ipaddress_regex.match(test_string2))
print(ipaddress_regex.match(test_string1))

################################################################################################
"""
<iter> = re.finditer(<regex>, text) # Returns all occurrences as match objects.
"""
match = ipaddress_regex.finditer(test_string2)
for item in match:
    print(item)
    print(item.group())
