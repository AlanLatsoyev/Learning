from random import randint

hidden_number = []


def think_of_a_number():
    global hidden_number

    while len(hidden_number) < 4:

        if hidden_number == []:
            added_digit = str(randint(1, 9))
            hidden_number.append(added_digit)
        else:
            added_digit = str(randint(0, 9))
            if added_digit not in hidden_number:
                hidden_number.append(added_digit)
            else:
                continue


def check_number(number):
    number_of_coincidences = {'bulls': 0, 'cows': 0}
    number = list(number)

    for i in hidden_number:
        for j in number:
            if i == j:
                number_of_coincidences['cows'] += 1
                if hidden_number.index(i) == number.index(j):
                    number_of_coincidences['bulls'] += 1

    return number_of_coincidences
