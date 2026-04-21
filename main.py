import random

number = random.randint(1, 100)

attempts = 5
count = 0

while count < attempts:
    guess = int(input("Та таа: "))
    count += 1

    if guess == number:
        print(f"Зөв! Та {count} удаа оролдож таалаа")
        break
    elif guess < number:
        print("Их тоо оруулна уу")
    else:
        print("Бага бага тоо оруулна уу")

if guess != number:
    print(f"Та {attempts} удаа оролдсон ч олсонгүй")
    print(f"Зөв хариу: {number}")