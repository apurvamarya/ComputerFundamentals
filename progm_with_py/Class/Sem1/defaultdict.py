from collections import defaultdict
name = "Dhananjay"
dd = defaultdict(int)
for ch in name:
    dd[ch]+=1
print(dd)