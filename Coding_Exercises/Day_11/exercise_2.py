def get_max():
    grades = [9.6, 9.2, 9.7]
    grade1 = max(grades)
    grade2 = min(grades)
    msg = f"Max: {grade1}, Min: {grade2}"
    return msg


g = get_max()
print(g)
