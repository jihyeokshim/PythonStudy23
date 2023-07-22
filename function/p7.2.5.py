def func(food):
    for x in food:
        print(x)


fruits = ["사과", "오렌지", "바나나"]

func(fruits)


def func(food):
    food.append("딸기")
    food.append("수박")


fruits = ["사과", "오렌지", "바나나"]
