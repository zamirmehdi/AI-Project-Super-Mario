f = open('/Users/apple/Desktop/Mario.txt')

n = int(f.readline())
m = int(f.readline())

sc = list(f.readline().split())
x, y = int(sc[0]), int(sc[1])
print('x: %i, y: %i' % (x, y))

k = int(f.readline())

mario = dict()
for i in range(k):
    sc = list(f.readline().split())
    mario[int(sc[0]), int(sc[1])] = 'red'
for i in range(k):
    sc = list(f.readline().split())
    mario[int(sc[0]), int(sc[1])] = 'blue'

for line in f:
    if (line.strip() != ''):
        sc = list(line.split())
        mario[int(sc[0]), int(sc[1])] = 'block'

print(mario)


# '''nxpancpanc
# a ckadncp
#
# aaxax
# '''
