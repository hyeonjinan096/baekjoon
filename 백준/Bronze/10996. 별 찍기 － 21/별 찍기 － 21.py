import sys
n = int(sys.stdin.readline())

for i in range(n):
    print("* "*(n-n//2))
    print(" *"*(n//2))

