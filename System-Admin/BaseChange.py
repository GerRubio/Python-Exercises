# Change a MAC address base.

mac = 'FF:01:CB:34:A2:EE'
splitted_mac = mac.split(':')

def simple_way():
    res = []

    for bytes in splitted_mac:
        res.append(str(int(bytes, base = 16)))

    new_mac = ':'.join(res)

    print(new_mac)

def complex_way():
    letters = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 1,
        '9': 1,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

    res = []

    for bytes in splitted_mac:
        num = 0
        exp = len(bytes) - 1
        
        for letter in bytes:
            num += letters[letter] * (16**(exp))
            exp -= 1
        
        res.append(str(num))

    new_mac = ':'.join(res)

    print(new_mac)

if __name__ == '__main__':
    simple_way()
    complex_way()