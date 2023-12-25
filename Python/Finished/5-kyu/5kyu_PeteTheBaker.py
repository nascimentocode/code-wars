recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

def cakes(recipe, available):
    for i in recipe:
        if i not in available:
            return 0
        else:
            return min([available.get(i)//recipe.get(i)])

print(cakes(recipe, available))