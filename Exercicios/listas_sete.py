#MaBe

par = []
ímpar = []
nums = [par, ímpar]

for v in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par.append(n)
    elif n % 2 != 0:
        ímpar.append(n)    
print(nums)
#nums.sort()

print(f'Os números pares são: {nums[0]}')
print(f'Os números ímpares são: {nums[1]}')
