#!/usr/bin/env python3

import sys
# import this

hexString = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
byteString = bytes.fromhex(hexString)

# test = chr(ords)
print("Here is your flag:")
print(byteString)

# print("".join(chr(o) for o in ords))
