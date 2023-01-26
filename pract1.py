"практика 1 вариант 2"

array: int = []

def func():
    length = int(input("Введите длину массива: "))

    if length <= 0:
        print("Неправильная длина")
        return

    minValue = 0

    for i in range(length):
        value = int(input("Введите новый элемент массива: "))
        array.append(value)

    minValue = array[0]

    for i in range(length):
        if minValue > array[i]:
            minValue = array[i]
    
    print(minValue, array.index(minValue))
func()







newArray: int = [-3,6,-4,-1,7,2,8]

def func():
    lessZeroArray: int = []
    aboveZeroArray: int = []
    for i in range(len(newArray)):
        if newArray[i] >= 0:
            aboveZeroArray.append(newArray[i])
        else:
            lessZeroArray.append(newArray[i])

    print(newArray)
    print(aboveZeroArray)
    print(lessZeroArray)

func()