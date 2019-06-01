s1 = input()
s2 = input()
s5 = ''
for i in range(0,len(s1)):
  s3 = ord(s1[i])-96
  s4 = ord(s2[i])-96
  if s3+s4 < 26:
    s5 = s5+chr(ord(chr(s3+s4+96)))
  else:
    s5 = s5+chr(ord(chr(((s3+s4)-26)+96)))
print(s5)
