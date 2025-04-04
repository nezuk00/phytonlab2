try:
    data1 = float(input())
    data2 = float(input())
    if data2 == 0:
        print("нельзя делить на ноль")
        
    else:
        result = data1 / data2
        print(result)
        
except ValueError:
    print("недопустимые значения")
