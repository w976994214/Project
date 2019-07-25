"""
权重
goods = [{"name": "good1", "price": 200, "sales": 100, "stars": 5, "comments": 400},
         {"name": "good2", "price": 300, "sales": 100, "stars": 1, "comments": 666},
         {"name": "good3", "price": 100, "sales": 200, "stars": 4, "comments": 400},
         {"name": "good4", "price": 111, "sales": 120, "stars": 5, "comments": 500},
         {"name": "good5", "price": 121, "sales": 120, "stars": 5, "comments": 5120}]

权重是100

价格权重是40%
销量权重是17%
评级权重是13%
评论权重是30%
"""

goods = [{"name": "good1", "price": 200, "sales": 100, "stars": 5, "comments": 400},
         {"name": "good2", "price": 300, "sales": 100, "stars": 1, "comments": 666},
         {"name": "good3", "price": 100, "sales": 200, "stars": 4, "comments": 400},
         {"name": "good4", "price": 111, "sales": 120, "stars": 5, "comments": 500},
         {"name": "good5", "price": 121, "sales": 120, "stars": 5, "comments": 5120}]

# sorted() 进行排序


def my_sorted(arg):
    price = arg['price']
    sales = arg['sales']
    stars = arg['stars']
    comment = arg['comments']
    data = price * 0.4 + sales * 0.17 + stars * 0.13 + comment * 0.3
    return data


print(sorted(goods, key=my_sorted))

r = sorted(goods, key=lambda x: x['price'] * 0.4 + x['sales'] * 0.17 + x['stars'] * 0.13 + x['comments'] * 0.3, reverse=True)
print(r)
