seen = set()
with open('file1.txt') as f, open('file2.txt','w') as o:
    for line in f:
        li = line.strip('\n')
        if not line.isspace() and not li in seen:
            line1 = line.strip('\n').split(',')
            line1 = ','.join(line1[::-1])
            if not line1 in seen:
                o.write(line)
                seen.add(li)
