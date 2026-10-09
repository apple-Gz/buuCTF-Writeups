import base64
import string

str1 = "mTyqm7wjODkrNLcWl0eqO8K8gc1BPk1GNLgUpI=="

string1 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0987654321/+"
string2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

a=str1.translate(str.maketrans(string1,string2))#利用密码表还原成正常base64编码后的字符串
#print(str1.translate(str.maketrans(string1,string2)))

print(base64.b64decode(a).decode())#base64解码
