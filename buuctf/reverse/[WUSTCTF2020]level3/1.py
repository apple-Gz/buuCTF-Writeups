# Python 版本的 Base64 表重排
base64_table = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

for i in range(10):  # i 从 0 到 9
    v1 = base64_table[i]
    base64_table[i] = base64_table[19 - i]
    base64_table[19 - i] = v1

print(''.join(base64_table))