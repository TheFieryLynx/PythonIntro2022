#!/usr/bin/env python3

import tarfile, sys, io

tar = tarfile.open(fileobj=io.BytesIO(bytearray.fromhex(sys.stdin.read())))

size = 0;
cnt = 0
for i in tar.getmembers():
	size += i.size
	cnt += i.type == tarfile.REGTYPE

print(size, cnt)