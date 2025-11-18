def split_before_each_uppercases(formula):
    pos = 0
    parts = []
    if len(formula) == 0:
        return []
    else:
        for idx in range(1, len(formula)):
            if formula[idx].isupper():
                parts.append(formula[pos:idx])
                pos = idx

    parts.append(formula[pos:])
    return parts



def split_at_first_digit(formula):
    digit_pos = -1

    for character in formula[1:]:
        if character.isdigit():
            break
        digit_pos += 1


    if digit_pos == len(formula):
        return formula, 1
    else:
        text_part = formula[:digit_pos]
        number_part = int(formula[digit_pos:])
        return text_part, number_part
