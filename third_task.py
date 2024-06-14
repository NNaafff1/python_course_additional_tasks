def convertBytes(size):
    # Единицы измерения
    units = ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
    # Переменная для отслеживания текущего индекса единиц
    index = 0
    # Пока размер больше или равен 1024 и есть еще единицы измерения
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    # Возвращаем строку
    return f"{size:.1f} {units[index]}"

sizes = [12, 2048, 1234567899999, 1234567890123456789]
for size in sizes:
    print(f"{size} байт -> {convertBytes(size)}")
