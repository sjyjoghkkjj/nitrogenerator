import random, string 

amount = int(input('Сколько кодов генерируем: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('Codes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[СГЕНЕРИРОВАНО] {code}')
    value += 1

