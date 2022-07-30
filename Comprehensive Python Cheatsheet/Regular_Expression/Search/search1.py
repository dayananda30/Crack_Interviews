import re
string = "This is a simple sentence 31-08-1990 BVJPR1810 10.228.223.234"


dob_obj = re.compile(r'((\d+-){2}\d{4})')



match_dob = dob_obj.search(string)

if match_dob:
    #print(match_obj.groups())
    print("The DOB in the matched string is  : {}".format(match_dob.group(1)))
else:
    print("Doesnot Match anything in {} ".format(string))




pan_obj = re.compile(r'((\w){10})')

match_pan = pan_obj.search(string)
print(match_pan)

if match_pan:
    print("The PAN Number is {}".format(match_pan.groups()))
else:
    print("PAN expression doesnot match !!!")




ip_obj = re.compile(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
match_ip = ip_obj.search(string)

if match_ip:
    print("The IP Address is : {} ".format(match_ip.group(0)))




