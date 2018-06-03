#calculate the hamming or the bit diff

def str_to_bytes(str,base):
    byte_array = bytearray()
    byte_array.extend([ord(ch) for ch in str])
    return byte_array

def calc_hamming(str1,str2):
    bits1 = str_to_bytes(str1,1)
    bits2 = str_to_bytes(str2,1)
    ham = 0
    for (x,y) in zip(bits1,bits2):
        z = x^y
        while z!=0:
            if z&1 == 1:
                ham += 1
            z = z>>1
    return ham
    
assert(calc_hamming("this is a test","wokka wokka!!!") == 37)
   