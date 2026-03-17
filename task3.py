def task三_二十五(m, n):
    結果 = []

    for イ in range(1, n):
        和 = sum(int(番号) for 番号 in str(イ))
        if 和 * 和 == m:
            結果.append(イ)
    
    return 結果

m = 4
n = 100

print(f"桁の合計の二乗が{m}となる{n}未満の数: {task三_二十五(m, n)}")