def likes(names):
    lenNames = len(names)
    if lenNames == 1:
        return f"{names[0]} likes this"
    elif lenNames == 2:
        return f"{names[0]} and {names[1]} like this"
    elif lenNames == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif lenNames >= 4:
        return f"{names[0]}, {names[1]} and {len(names[2:])} others like this" 
    else:
        return "no one likes this"