def even_number():
    result = []
    for number in range(1,51):
        if number % 2 == 0:
            result.append(number)
    
    return result
