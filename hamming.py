'''
calculate the hamming or the bit diff
useful in deciding the key length for repeating XOR
'''

def str_to_bytes(str,base):
    byte_array = bytearray()
    byte_array.extend([ord(ch) for ch in str])
    return byte_array

def calc_hamming(str1,str2):
    bits1 = str_to_bytes(str1,1)
    bits2 = str_to_bytes(str2,1)
    print(bits1)
    print(bits2)
    ham = 0
    for (x,y) in zip(bits1,bits2):
        print(x,y)
        while x > 0 or y > 0:
            if x > 0 and y == 0 or x == 0 and y>0:
                ham += 1
            elif (int(x)%2)!=(int(y)%2):
                ham += 1
            x = int(x/2)
            y = int(y/2)
            print(ham)
    
calc_hamming("this is a test","wokka wokka!!!")
   