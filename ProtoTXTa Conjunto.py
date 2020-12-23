import os
Path = 'C:/Mallet/'

F1TXT = 'C1.txt'   # archivo de reemplazos
Pa1 = open(Path + F1TXT,'r', encoding='utf-8')
Li1 = Pa1.readlines()
Pa1.close()
Li1TXT = ''.join(Li1).strip()
Li1 = Li1TXT.split()
C1 = set()
for Lis in Li1:
    C1.add(Lis)

F1TXT = 'C2.txt'   # archivo de reemplazos
Pa1 = open(Path + F1TXT,'r', encoding='utf-8')
Li1 = Pa1.readlines()
Pa1.close()
Li1TXT = ''.join(Li1).strip()
Li1 = Li1TXT.split()
C2 = set()
for Lis in Li1:
    C2.add(Lis)

F1TXT = 'C3.txt'   # archivo de reemplazos
Pa1 = open(Path + F1TXT,'r', encoding='utf-8')
Li1 = Pa1.readlines()
Pa1.close()
Li1TXT = ''.join(Li1).strip()
Li1 = Li1TXT.split()
C3 = set()
for Lis in Li1:
    C3.add(Lis)

F1TXT = 'C4.txt'   # archivo de reemplazos
Pa1 = open(Path + F1TXT,'r', encoding='utf-8')
Li1 = Pa1.readlines()
Pa1.close()
Li1TXT = ''.join(Li1).strip()
Li1 = Li1TXT.split()
C4 = set()
for Lis in Li1:
    C4.add(Lis)

F1TXT = 'C5.txt'   # archivo de reemplazos
Pa1 = open(Path + F1TXT,'r', encoding='utf-8')
Li1 = Pa1.readlines()
Pa1.close()
Li1TXT = ''.join(Li1).strip()
Li1 = Li1TXT.split()
C5 = set()
for Lis in Li1:
    C5.add(Lis)
print('C1',len(C1),C1)
print('C2',len(C2),C2)
print('C3',len(C3),C3)
print('C4',len(C4),C4)
print('C5',len(C5),C5)

#print('C1+C2', len(C1.union(C2)),C1.union(C2))
# print('C1+C2+C3', len(C1.union(C2.union(C3))),C1.union(C2.union(C3)))
print('C1 INT C2', len(C1.intersection(C2)),C1.intersection(C2))
print('C1 INT C3', len(C1.intersection(C3)),C1.intersection(C3))
print('C1 INT C4', len(C1.intersection(C4)),C1.intersection(C4))
print('C1 INT C5', len(C1.intersection(C5)),C1.intersection(C5))

print('C2 INT C3', len(C2.intersection(C3)),C2.intersection(C3))
print('C2 INT C4', len(C2.intersection(C4)),C2.intersection(C4))
print('C2 INT C5', len(C2.intersection(C5)),C2.intersection(C5))

print('C3 INT C4', len(C3.intersection(C4)),C3.intersection(C4))
print('C3 INT C5', len(C3.intersection(C5)),C3.intersection(C5))
print('C4 INT C5', len(C4.intersection(C5)),C4.intersection(C5))
