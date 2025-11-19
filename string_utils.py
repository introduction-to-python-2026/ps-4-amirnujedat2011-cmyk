def split_before_each_uppercase(formula):
    if not formula:
        return []

    parts = []
    pos = 0
    for idx in range(1, len(formula)):
        if formula[idx].isupper():
            parts.append(formula[pos:idx])
            pos = idx
    parts.append(formula[pos:])
    return parts

def split_at_digit(formula):
    digit_location = 1   

    for ch in formula[1:]:
        if ch.isdigit():  
            break
        digit_location += 1   

    if digit_location == len(formula):
        return formula, 1  
        
    prefix = formula[:digit_location]
    number_part = int(formula[digit_location:])
    return prefix, number_part
