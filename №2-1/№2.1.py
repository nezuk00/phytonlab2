with open("data.txt", "r") as file:
    data = [int(x.strip()) for x in file]
print(data)

sum = sum(data)
average = sum/10
max = max(data)
min = min(data)

with open("result.txt", "w", encoding="utf-8") as file:
    file.write(f"Сумма: {sum}\n")
    file.write(f"Среднее: {average}\n")
    file.write(f"Максимум:{max}\n")
    file.write(f"Минимум: {min}\n")
file.close()
