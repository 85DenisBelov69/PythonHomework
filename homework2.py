# Задача 2. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,09
#A (7,-5); B (1,-1) -> 7,21



print("координаты первой точки")
х1 = int(input("введите х первой точки: "))
y1 = int(input("введите у первой точки: "))
print()
print("координаты второй точки")
х2 = int(input("введите х второй точки: "))
y2 = int(input("введите у второй точки: "))


lengthSegment = round((((х2 - х1) ** 2 + (y2 - y1) ** 2) ** (0.5)), 3)



print(f"длина отрезка: {lengthSegment}")