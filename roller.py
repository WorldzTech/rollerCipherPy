class RollerCipher:
    def __init__(self, n: int, m: int):
        self.__n = n
        self.__m = m

    @property
    def n(self) -> int:
        return self.__n

    @property
    def m(self) -> int:
        return self.__m
    
    def __get_keystream(self, length: int) -> list[int]:
        a = list(range(1, length + 1))
        b = list(range(1, length + 1))
        
        a = a[-self.n:] + a[:-self.n]
        b = b[-self.m:] + b[:-self.m]
        
        r = []
        for i in range(length):
            keystream_byte = a[i] + b[i]
            r.append(keystream_byte)

        return r

    def encrypt(self, s: str) -> str:
        r = self.__get_keystream(len(s))
        
        processed = [ord(s[i]) ^ r[i] for i in range(len(s))]
        return processed
    
    def decrypt(self, b: list[int]) -> str:
        r = self.__get_keystream(len(b))
        
        processed = [chr(b[i] ^ r[i]) for i in range(len(b))]
        return "".join(processed)