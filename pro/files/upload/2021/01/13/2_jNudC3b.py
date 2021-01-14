def func(a):
    for i in range(20):
        b = 0.01
        c = a * b * 0.05
        z = a * b + a - c
        print(f"第{i + 1}单:", z)
        a = z

func(54188)