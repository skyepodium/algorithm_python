import base64

class Base64:

    def __init__(self):
        self.table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    def encode(self, s:str):

        binary_list = self.__str_to_binary_list(s)

        binary_str = "".join(binary_list)

        hex_list = self.__binary_str_to_hext_list(binary_str)

        return "".join(self.__hex_list_to_ascii_list__(hex_list))

    def decode(self):
        return

    def __binary_str_to_hext_list(self, binary_str):
        hex_list = []
        for i in range(0, len(binary_str), 6):
            # hex_list.append(binary_str[i:i+6])
            hex_list.append(format(binary_str[i:i+6]).zfill(8))
        # print(hex_list)
        return hex_list

    def __hex_list_to_ascii_list__(self, hex_list):
        return [self.table[self.__binary_to_int(hex)] for hex in hex_list]

    def __str_to_binary_list(self, s:str):
        return [self.__int_to_binary__(ord(c)) for c in s]

    def __int_to_binary__(self, n:int):
        return "{0:b}".format(n).zfill(8)

    def __binary_to_int(self, b):
        return int(b, 2)


b = Base64()

s = "webisfree"
s = "E1L"
s = "a"

sitename_bytes = s.encode('ascii')
sitename_base64 = base64.b64encode(sitename_bytes)

print("res", sitename_base64)
print("myres", b.encode(s))

# sitename_base64_str = sitename_base64.decode('ascii')
# print('sitename_base64_str', sitename_base64_str)
