mass = float(input())
weight = float(input())

IMT = mass / (weight * weight)

if 18.5 <= IMT <= 25:
    print("Оптимальная масса")
elif IMT < 18.5:
    print("Недостаточная масса")
else:
    print("Избыточная масса")