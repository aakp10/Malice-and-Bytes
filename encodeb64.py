'''
Can use the coreutils function as well
+ base64 import in python
'''
from string import ascii_lowercase,ascii_uppercase,digits

def b2b64encode(byte_str):
    #create base64 characters encoding table
    b64_table = ascii_uppercase + ascii_lowercase + digits + '+/'
    
    #create block of 3 bytes to fetch 4 b64 characters
    #check if they have bytes as multiple of 3bytes else we need to pad it
    pad = len(byte_str)%3
    print(len(byte_str))
    print(pad)
    if pad != 0:
        """"
        note: 0x00 has been used just to make sure that those bytes will
        be all 0 , if u specify anything in string then according to the 
        encoding used the byte will be different 
        """
        pad = 3 - pad
        byte_str += bytes([0x00]*pad)
        
        #ele of this list forms a byte array
    indices = []
    for i in range(0,len(byte_str),3):
        chunk = (byte_str[i]<<16) + (byte_str[i+1]<<8) +byte_str[i+2]
        mask = 0b111111000000000000000000
        for j in range(4):
            b64_index = (chunk & ((mask)>>(6*j)))>>((3-j)*6)
            indices.append(b64_index)
    byte_b64_enoded = bytearray()
    byte_b64_enoded.extend([ord(b64_table[i]) for i in indices])
    if pad != 0:
        byte_b64_enoded = byte_b64_enoded[:-(pad)] + bytes([ord("*")]*pad)
    return byte_b64_enoded

b2b64encode(b"Man is distinguished, not only by his reason")

