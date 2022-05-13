import numpy as np
from statistics import mean, median, mode

stdin = [np.random.randint(0, 6) for i in range(10)]
stdout = round(sum(stdin)/len(stdin), 1)
print(stdout)
stdout = stdin.sort()


stdout = round(mean(stdin), 1)
print(stdout)
stdout = round(median(stdin), 1)
print(stdout)
stdout = mode(stdin)
print(stdout)


from statistics import mean, median, multimode


stdout = round(mean(s), 1)
print(stdout)
stdout = round(median(s), 1)
print(stdout)
stdout = mode(s)
print(stdout)