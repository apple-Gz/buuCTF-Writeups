import base64

str_1 = "x2dtJEOmyjacxDemx2eczT5cVS9fVUGvWTuZWjuexjRqy24rV29q"
# 这是原题中修改过的Base64表
str_base = "yxzABCDEFGHIJKLMNOPQRSTUVWzyxabcdefghijklmnopqrstuvw0123456789+/"
str_zh_base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

# 确保两个字符串长度相等
print(f"str_base长度: {len(str_base)}")
print(f"str_zh_base长度: {len(str_zh_base)}")

if len(str_base) == len(str_zh_base):
    flag = base64.b64decode(str_1.translate(str.maketrans(str_base, str_zh_base)))
    print(flag)
else:
    print("长度不匹配，请检查自定义表")