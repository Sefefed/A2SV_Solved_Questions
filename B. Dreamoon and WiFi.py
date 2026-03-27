s1 = input()
s2 = input()

target = s1.count('+') - s1.count('-')
n = len(s2)
k = s2.count('?')

def Dreamoon(i, pos):
  if i == n:
    return 1 if pos == target else 0
  if s2[i] == '+':
    return Dreamoon(i+1, pos+1)
  elif s2[i] == "-":
    return Dreamoon(i+1, pos-1)
  else:
    return Dreamoon(i+1, pos+1) + Dreamoon(i+1, pos - 1)
feasible = Dreamoon(0, 0)
cases = 2 ** k
print(feasible / cases)
