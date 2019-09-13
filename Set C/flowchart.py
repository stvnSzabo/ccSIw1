numbers = []
leng = int(input("How many numbers: "))

for i in range(leng):
    numbers.append(int(input("Enter number: ")))
n = len(numbers)

m = 1
while m < n:
    j = 0
    while j <= n - 2:
        if numbers[j] > numbers [j+1]:
            temp = numbers[j+1]
            numbers[j+1] = numbers[j]
            numbers[j] = temp
        else:
            j += 1
    else:
        m += 1






print(numbers)
