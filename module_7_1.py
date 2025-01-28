import os


class Product:
    def __init__(self, name, weight, category):
        # Инициализируем атрибуты продукта
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        # Возвращаем строку с атрибутами продукта
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        # Инкапсулируем имя файла
        self.__file_name = 'products.txt'
        # Удаляем файл, если он существует, и создаём новый
        if os.path.exists(self.__file_name):
            os.remove(self.__file_name)
        # Создаём файл
        open(self.__file_name, 'w').close()

    def get_products(self):
        # Считываем продукты из файла и возвращаем в виде строки
        with open(self.__file_name, 'r') as file:
            return file.read().strip()

    def add(self, *products):
        # Получаем текущие продукты в виде строки и разбиваем её на список
        current_products = self.get_products().splitlines()

        # Преобразуем список строк в список объектов Product
        existing_products = []
        for line in current_products:
            if line:
                name, weight, category = line.split(', ')
                existing_products.append(Product(name, float(weight), category))

        # Открываем файл для добавления данных
        with open(self.__file_name, 'w') as file:
            for product in products:
                found = False
                for existing_product in existing_products:
                    if product.name == existing_product.name and product.category == existing_product.category:
                        # Если продукт уже есть, увеличиваем его вес
                        existing_product.weight += product.weight
                        print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {existing_product.weight}')
                        found = True
                        break
                if not found:
                    # Если продукта нет, добавляем его в магазин
                    existing_products.append(product)

            # Записываем все (новые и обновлённые) продукты обратно в файл
            for product in existing_products:
                file.write(str(product) + '\n')


# Пример работы программы
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
