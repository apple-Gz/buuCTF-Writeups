from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# 模拟原始环境
KEY = os.urandom(16)  # 模拟服务器的随机 KEY
FLAG = "XMCTF{xxxxxx}"

def create_session(username):
    iv = os.urandom(16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    msg = f"user={username}".encode()
    ct = cipher.encrypt(pad(msg, 16))
    return iv + ct

def get_session_data(token_bytes):
    iv, ct = token_bytes[:16], token_bytes[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ct)
    return unpad(decrypted, 16).decode(errors='ignore')

# 普通用户 session
user_session = create_session("guest")  # 这里用 guest 模拟普通用户
print("原始 session 数据:", get_session_data(user_session))

# 要改成 admin
original = b"guest"
target = b"admin"

# 因为 user=guest -> 长度 10，user=admin 也是长度 10，所以可以直接替换
# 在 CBC 中修改前一个块的字节可以控制明文
# 这里 guest 在第一个块内，使用 iv 来翻转
iv = bytearray(user_session[:16])
for i in range(len(target)):
    iv[5+i] ^= original[i] ^ target[i]  # 'user=' 长度 5，所以从 iv[5] 开始翻

# 构造新的 session
admin_session = bytes(iv) + user_session[16:]

print("修改后的 session 数据:", get_session_data(admin_session))
print("FLAG:", FLAG if get_session_data(admin_session).startswith("user=admin") else "失败")