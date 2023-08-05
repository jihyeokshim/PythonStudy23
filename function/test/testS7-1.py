def isPrime(a):
    # 소수냐 아니냐
    for i in range(2, a // 2):
        if a % i == 0:
            return False
    return True


n = int(input("n값을 입력해 주세요."))
print("2부터 %d까지의 정수중 소수:" % n, end=" ")
for i in range(2, n + 1):
    if isPrime(i) == True:
        print(i, end=" ")
