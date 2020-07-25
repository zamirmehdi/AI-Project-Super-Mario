from array import *

n = int(input())
m = int(input())

sc = list(input().split())
x, y = int(sc[0]), int(sc[1])

k = int(input())

mario = dict()
for i in range(k):
    sc = list(input().split())
    mario[sc[0], sc[1]] = 'red'
for i in range(k):
    sc = list(input().split())
    mario[sc[0], sc[1]] = 'blue'

print(mario)
