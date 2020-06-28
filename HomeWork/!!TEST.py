flag = "MSKCTF_"
s = ""

print(n)
for i in range(len(flag)):
    s += chr((ord(flag[i]) * 7 + 11) % 26 + 65)
print(s)
