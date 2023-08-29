#Old Macdonald : write a function that capitalises the 1st and 4th letters of a name
def old_macdonald(name):
    first_letter=name[0]
    inbetween=name[1:3]
    fourth_letter=name[3]
    rest=name[4:]

    return first_letter.upper()+inbetween+fourth_letter.upper()+rest

print(old_macdonald("anmol"))