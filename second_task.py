def get_long_pref_str(strs):
    if not strs:
        return ""
    # 1) Сортируем массив строк
    strs.sort()
    # 2) Берем первую и последнюю строку, так как они будут наиболее различны
    first = strs[0]
    last = strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]

# Чтение входного массива
print("Ввод массива:")
input_strs = ["flower","flow","flight"]
# Нахождение самой длинной общей префиксной строки
output_str = get_long_pref_str(input_strs)

print("Выходная строка:")
print(output_str)