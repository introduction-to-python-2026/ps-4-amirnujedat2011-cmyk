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

def split_at_first_digit(formula):
    for idx, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:idx], int(formula[idx:])
    return formula, 1
