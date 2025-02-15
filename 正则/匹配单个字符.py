import re

# match_obj = re.match("[t]ro",'tro')
# if match_obj:
#     result = match_obj.group()
#     print(result)
# else:
#     print('no')

# match_obj = re.match("^H.*", 'HTTP')
# if match_obj:
#         result = match_obj.group()
#         print(result)
# else:
#         print('no')
# match_obj = re.match(".*$", 'HTTP3')
# if match_obj:
#         result = match_obj.group()
#         print(result)
# else:
#         print('no')

# match_obj = re.match(".[^21]*", 'HTTP3')
# if match_obj:
#         result = match_obj.group()
#         print(result)
# else:
#         print('no')

#
# list =['app1','app2','app3','app4']
#
# for value in list :
#        match_obj = re.match('app3|app1',value)
#        if match_obj:
#                result =match_obj.group()
#                print('我想玩'+result)
#        else:
#                print('我不想玩'+value)
#

# match_obj = re.match("\\w{4,20}@(163|qq|xinlang)\\.com","hello@qq.com")#"^[A-Za-z0-9]{4,20}@(163|qq|xinlang)\.com$"
#
# if match_obj:
#         result = match_obj.group()
#         print(result)
# else:
#         print("输入错误")


# match_obj = re.match("qq:[1-9]\\d{4,11}","qq:1926456490")
#
# if match_obj:
#         result = match_obj.group()
#         qq = result.split(":")[1]
#         print(qq)
# else:
#         print("no")
match_obj = re.match("<([a-zA-Z]+)>.*</\\1>","<html>hh</html>")

if match_obj:
        result = match_obj.group()
        print(result)
else:
        print("no")

match_obj = re.match(r"<([a-zA-Z]+)><([a-zA-Z1-6]+)>.*</\2></\1>","<html><h6>hh</h6></html>")

if match_obj:
        result = match_obj.group()
        print(result)
else:
        print("no")
match_obj = re.match('<(?P<name1>[a-zA-Z]+)><(?P<name2>[a-zA-Z1-6]+)>.*</(?P=name2)></(?P=name1)>', "<html><h6>hh</h6></html>")  #必须P

if match_obj:
        result = match_obj.group()
        print(result)
else:
        print("no")