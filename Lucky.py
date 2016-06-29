T = [1024]
def lucky(n):
    if T[n] == -1:
        T[n] = 10 * lucky(n-1) - lucky(n-2)
        print T[n]
    return T[n]

def main():
    T[0] = 1
    T[1] = 10
    for i in range(2,1024):
        T[i] = -1
    n = input();
    print lucky(n)

main()
