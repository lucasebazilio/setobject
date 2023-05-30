from collections import defaultdict
from operator import itemgetter

mp = defaultdict(lambda: [0, 0])

while True:
    try:
        n, m = map(int, input().split())
        if n == -1: break
        else:
            mp[n][0] += m
            mp[n][1] += 1
    except EOFError:
        break

sorted_mp = [(k, v[0] / 50) for k, v in sorted(mp.items(), key=itemgetter(0))]

for p in sorted_mp:
    print(f"39321,{p[0]},{p[1]:.3f}")

print("SUM:")
sum = 0
for p in sorted_mp:
    sum += p[0] * p[1]

print(sum)
print("SUB:", sum - 65536.0)
