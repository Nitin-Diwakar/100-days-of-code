class Roman:
    def __init__(self, num):
        self.num = num

    def int_to_roman(self):
        number = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        symbol = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ""
        i = 0
        while self.num > 0:
            for _ in range(self.num // number[i]):
                roman_num += symbol[i]
                self.num -= number[i]
            i += 1
        return roman_num




all_roman = Roman(15)
print(all_roman.int_to_roman())

