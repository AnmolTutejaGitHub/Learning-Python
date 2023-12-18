if __name__ == '__main__':
    s = input()

    if any(char.isalnum() for char in s):
        print('True')
    else:
        print('False')

    if 'a' in s.lower() or 'b' in s.lower() or 'c' in s.lower() or 'd' in s.lower() or 'e' in s.lower() or 'f' in s.lower() or 'g' in s.lower() or 'h' in s.lower() or 'i' in s.lower() or 'j' in s.lower() or 'k' in s.lower() or 'l' in s.lower() or 'm' in s.lower() or 'n' in s.lower() or 'o' in s.lower() or 'p' in s.lower() or 'q' in s.lower() or 'r' in s.lower() or 's' in s.lower() or 't' in s.lower() or 'u' in s.lower() or 'v' in s.lower() or 'w' in s.lower() or 'x' in s.lower() or 'y' in s.lower() or 'z' in s.lower():
        print('True')
    else:
        print('False')
    #print('0123456789' in s)
    if any(char.isdigit() for char in s):
        print('True')
    else:
        print('False')
    if any(char.islower() for char in s):
        print('True')
    else:
        print('False')
    if any(char.isupper() for char in s):
        print('True')
    else:
        print('False')
