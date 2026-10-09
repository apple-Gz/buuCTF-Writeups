#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decode_utf8_bytes(data):
    """
    解码UTF-8字节序列
    支持标准的UTF-8解码，包括overlong encoding
    """
    result = []
    i = 0
    length = len(data)
    
    while i < length:
        byte = data[i]
        
        # 1字节 UTF-8 (ASCII)
        if (byte >> 7) == 0:
            result.append(chr(byte))
            i += 1
        
        # 2字节 UTF-8: 110xxxxx 10xxxxxx
        elif (byte >> 5) == 0b110:
            if i + 1 >= length:
                break
            byte2 = data[i + 1]
            # 解码: (byte1 & 0x1F) << 6 | (byte2 & 0x3F)
            code_point = ((byte & 0x1F) << 6) | (byte2 & 0x3F)
            result.append(chr(code_point))
            i += 2
        
        # 3字节 UTF-8: 1110xxxx 10xxxxxx 10xxxxxx
        elif (byte >> 4) == 0b1110:
            if i + 2 >= length:
                break
            byte2 = data[i + 1]
            byte3 = data[i + 2]
            # 解码: (byte2 & 0x3F) << 6 | (byte3 & 0x3F)
            code_point = ((byte2 & 0x3F) << 6) | (byte3 & 0x3F)
            result.append(chr(code_point))
            i += 3
        
        # 4字节 UTF-8: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
        elif (byte >> 3) == 0b11110:
            if i + 3 >= length:
                break
            byte2 = data[i + 1]
            byte3 = data[i + 2]
            byte4 = data[i + 3]
            # 解码: (byte3 & 0x3F) << 6 | (byte4 & 0x3F)
            code_point = ((byte3 & 0x3F) << 6) | (byte4 & 0x3F)
            result.append(chr(code_point))
            i += 4
        
        else:
            # 无效的UTF-8字节
            result.append(f'\\x{byte:02x}')
            i += 1
    
    return ''.join(result)


def main():
    # 从.rdata段提取的字节数据
    raw_data = bytes([
        0xE0, 0x81, 0x89,  # 3字节 UTF-8
        0xC0, 0xA0,        # 2字节 UTF-8 (overlong encoding)
        0xC1, 0xAE,        # 2字节 UTF-8
        0xE0, 0x81, 0xA5,  # 3字节 UTF-8
        0xC1, 0xB6,        # 2字节 UTF-8
        0xF0, 0x80, 0x81, 0xA5,  # 4字节 UTF-8
        0xE0, 0x81, 0xB2,  # 3字节 UTF-8
        0xF0, 0x80, 0x80, 0xA0,  # 4字节 UTF-8
        0xE0, 0x81, 0xA2,  # 3字节 UTF-8
        0x72, 0x6F,        # 'r', 'o'
        0xC1, 0xAB,        # 2字节 UTF-8
        0x65,              # 'e'
        0xE0, 0x80, 0xA0,  # 3字节 UTF-8
        0xE0, 0x81, 0xB4,  # 3字节 UTF-8
        0xE0, 0x81, 0xA8,  # 3字节 UTF-8
        0xC1, 0xA5,        # 2字节 UTF-8
        0x20,              # 空格
        0xC1, 0xA5,        # 2字节 UTF-8
        0xE0, 0x81, 0xAE,  # 3字节 UTF-8
        0x63,              # 'c'
        0xC1, 0xAF,        # 2字节 UTF-8
        0xE0, 0x81, 0xA4,  # 3字节 UTF-8
        0xF0, 0x80, 0x81, 0xA9,  # 4字节 UTF-8
        0x6E,              # 'n'
        0xC1, 0xA7,        # 2字节 UTF-8
        0xC0, 0xBA,        # 2字节 UTF-8 (overlong encoding)
        0x20,              # 空格
        0x49,              # 'I'
        0xF0, 0x80, 0x81, 0x9F,  # 4字节 UTF-8
        0xC1, 0xA1,        # 2字节 UTF-8
        0xC1, 0x9F,        # 2字节 UTF-8
        0xC1, 0x8D,        # 2字节 UTF-8
        0xE0, 0x81, 0x9F,  # 3字节 UTF-8
        0xC1, 0xB4,        # 2字节 UTF-8
        0xF0, 0x80, 0x81, 0x9F,  # 4字节 UTF-8
        0xF0, 0x80, 0x81, 0xA8,  # 4字节 UTF-8
        0xC1, 0x9F,        # 2字节 UTF-8
        0xF0, 0x80, 0x81, 0xA5,  # 4字节 UTF-8
        0xE0, 0x81, 0x9F,  # 3字节 UTF-8
        0xC1, 0xA5,        # 2字节 UTF-8
        0xE0, 0x81, 0x9F,  # 3字节 UTF-8
        0xF0, 0x80, 0x81, 0xAE,  # 4字节 UTF-8
        0xC1, 0x9F,        # 2字节 UTF-8
        0xF0, 0x80, 0x81, 0x83,  # 4字节 UTF-8
        0xC1, 0x9F,        # 2字节 UTF-8
        0xE0, 0x81, 0xAF,  # 3字节 UTF-8
        0xE0, 0x81, 0x9F,  # 3字节 UTF-8
        0xC1, 0x84,        # 2字节 UTF-8
        0x5F,              # '_'
        0xE0, 0x81, 0xA9,  # 3字节 UTF-8
        0xF0, 0x80, 0x81, 0x9F,  # 4字节 UTF-8
        0x6E,              # 'n'
        0xE0, 0x81, 0x9F,  # 3字节 UTF-8
        0xE0, 0x81, 0xA7,  # 3字节 UTF-8
        0xE0, 0x81, 0x80,  # 3字节 UTF-8
        0xF0, 0x80, 0x81, 0xA6,  # 4字节 UTF-8
        0xF0, 0x80, 0x81, 0xAC,  # 4字节 UTF-8
        0xE0, 0x81, 0xA1,  # 3字节 UTF-8
        0xC1, 0xB2,        # 2字节 UTF-8
        0xC1, 0xA5,        # 2字节 UTF-8
        0xF0, 0x80, 0x80, 0xAD,  # 4字节 UTF-8
        0xF0, 0x80, 0x81, 0xAF,  # 4字节 UTF-8
        0x6E,              # 'n'
        0xC0, 0xAE,        # 2字节 UTF-8 (overlong encoding)
        0xF0, 0x80, 0x81, 0xA3,  # 4字节 UTF-8
        0x6F,              # 'o'
        0xF0, 0x80, 0x81, 0xAD,  # 4字节 UTF-8
        0x00               # null terminator
    ])
    
    # 解码UTF-8字符串
    decoded = decode_utf8_bytes(raw_data)
    
    print("=" * 60)
    print("解密结果:")
    print("=" * 60)
    print(f"原始解码文本: {decoded}")
    print(f"\n字符长度: {len(decoded)}")
    print(f"十六进制表示:")
    for i, ch in enumerate(decoded):
        print(f"  [{i:2d}] U+{ord(ch):04X} '{ch}'")
    
    print("\n" + "=" * 60)
    print("尝试翻转文本:")
    print("=" * 60)
    
    # 倒置字符映射表（将倒置字符转回正常）
    upside_down_map = {
        'ɐ': 'a', 'ɥ': 'h', 'ɯ': 'm', 'ɹ': 'r', 'ʇ': 't', 'ʎ': 'y',
        'ɲ': 'n', 'ɺ': 'l', 'ɶ': 'o', 'ɔ': 'c', 'p': 'd', 'q': 'b',
        'ƃ': 'g', 'ɟ': 'f', 'ʞ': 'k', 'ʌ': 'v', 'ʍ': 'w', 'x': 'x',
        'z': 'z', 's': 's', 'ǝ': 'e', 'ı': 'i', 'ɯ': 'm'
    }
    
    # 尝试反转整个字符串
    reversed_text = decoded[::-1]
    
    # 尝试将每个倒置字符翻转
    flipped = []
    for ch in reversed_text:
        if ch in upside_down_map:
            flipped.append(upside_down_map[ch])
        else:
            flipped.append(ch)
    
    normal_text = ''.join(flipped)
    print(f"倒序并翻转: {normal_text}")
    
    # 尝试直接翻转（不改变顺序，只翻转每个字符）
    direct_flip = []
    for ch in decoded:
        if ch in upside_down_map:
            direct_flip.append(upside_down_map[ch])
        else:
            direct_flip.append(ch)
    
    print(f"直接翻转每个字符: {''.join(direct_flip)}")
    
    print("\n" + "=" * 60)
    print("完整解码:")
    print("=" * 60)
    
    # 使用标准Python解码验证
    # 注意：需要过滤掉null terminator
    clean_data = raw_data[:-1]  # 移除最后的null
    try:
        python_decoded = clean_data.decode('utf-8', errors='replace')
        print(f"Python标准解码: {python_decoded}")
    except:
        print("Python标准解码失败（由于overlong encoding）")
    
    # 提供详细的字符信息
    print("\n" + "=" * 60)
    print("字符分析:")
    print("=" * 60)
    for i, ch in enumerate(decoded):
        if ch.isprintable():
            print(f"位置 {i:2d}: '{ch}' (U+{ord(ch):04X})")
        else:
            print(f"位置 {i:2d}: 控制字符 (U+{ord(ch):04X})")


if __name__ == "__main__":
    main()