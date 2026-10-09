import binascii

str1 = "********CENSORED********"
qword_201060 = [0x410A4335494A0942, 0x0B0EF2F50BE619F0, 0x4F0A3A064A35282B]

flag = b'flag{'
for i in range(3):  #3的话是因为24/8=3---->********CENSORED********
    z = str1[i * 8 : (i + 1) * 8]                           #分成三份,也就是八个一组
    x = binascii.b2a_hex(z.encode('ascii')[::-1])  #将里面的元素转换为16进制的ascii
    y = binascii.a2b_hex(hex(int(x, 16) + qword_201060[i])[2:])[::-1]   #与201060的元素相加
    flag += y
print(flag + b'}')