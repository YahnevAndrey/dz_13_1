class Category:
    name: str
    description: str
    products: list

    category_count = 0
    products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.products += len(products)

    def __repr__(self):
        return (f"Категория - {self.name}, Описание - {self.description},"
                f" Продукты - {self.products}")
    