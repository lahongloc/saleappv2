def load_categories():
    return [
        {
            "id": 1,
            "name": "Mobile"
        },
        {
            "id": 2,
            "name": "Tablet"
        }
    ]


def load_products(kw=None):
    products = [
        {
            "id": 1,
            "name": "iPad Pro 2022",
            "price": 24000000,
            "image": "https://s.net.vn/Yc0w"
        },
        {
            "id": 1,
            "name": "iPad Pro 2023",
            "price": 24000000,
            "image": "https://s.net.vn/Yc0w"
        },
        {
            "id": 1,
            "name": "Samsung Galaxy S6",
            "price": 24000000,
            "image": "https://s.net.vn/Yc0w"
        },
        {
            "id": 1,
            "name": "Oppo i love u",
            "price": 14000000,
            "image": "https://s.net.vn/Yc0w"
        },
        {
            "id": 1,
            "name": "Iphone 15 Pro Max",
            "price": 30000000,
            "image": "https://s.net.vn/Yc0w"
        },
        {
            "id": 1,
            "name": "Xiaomi redmi note 9",
            "price": 45000000,
            "image": "https://s.net.vn/Yc0w"
        },
        {
            "id": 1,
            "name": "iphone XS max",
            "price": 24000000,
            "image": "https://s.net.vn/Yc0w"
        }
    ]

    if kw:
        products = [p for p in products if p["name"].lower().find(kw.lower()) >= 0]
    return products
