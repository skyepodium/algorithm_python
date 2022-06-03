plain_text = "flag{CiphersAreAwesome}"

cyper_text = "gwox{RgqssihYspOntqpxs}"

key = "blorpy"

plain_text = "divert troops to east ridge"

cyper_text = "vstwbr lbmgzq ly cscr jsbyo"

key = "sky"



class vigenere:
    def __init__(self):
        self.__make_table()

    def __make_table(self):
        self.t = []
        for i in range(26):
            self.t.append([c if c < 26 else c - 26 for c in range(i, i+26)])

    def __get_base_by_is_upper(self, c):
        return ord('A') if c.isupper() else ord('a')

    def encode(self, s:str, key:str):
        # 1. init
        res = ""
        key_idx = 0

        # 2. loop
        for c in s:
            if not c.isalpha():
                res += c
            else:
                k = key[key_idx]
                key_idx += 1
                if key_idx >= len(key): key_idx = 0

                c_base = self.__get_base_by_is_upper(c)
                k_base = self.__get_base_by_is_upper(k)
                col_idx = ord(c) - c_base
                row_idx = ord(k) - k_base

                res += chr(self.t[row_idx][col_idx] + c_base)

        return res

    def decode(self, s:str, key:str):
        # 1. init
        res = ""
        key_idx = 0

        for c in s:
            if not c.isalpha():
                res += c
            else:
                k = key[key_idx]
                key_idx += 1
                if key_idx >= len(key): key_idx = 0

                c_base = self.__get_base_by_is_upper(c)
                k_base = self.__get_base_by_is_upper(k)
                row_idx = ord(k) - k_base
                col_idx = 0
                for c_idx, val in enumerate(self.t[row_idx]):
                    if chr(val + c_base) == c:
                        col_idx = c_idx
                        break

                res += chr(col_idx + c_base)

        return res

v = vigenere()

encrypt = v.encode(plain_text, key)

print("encrypt", encrypt)

print(encrypt == cyper_text)

decrypt = v.decode(cyper_text, key)

print("decrypt", decrypt)

print(decrypt == plain_text)

