import hello
persegi_panjang_pertama = hello.mencari_luas_persegi_panjang(10, 5)
print(persegi_panjang_pertama)

print(hello.nama)


def greeting(nama):
    print(f"Halo {nama}")


greeting("mimu")


class Kalkulator:
    """kalkulator tambah kurang"""

    def __init__(self, _i):
        self.i = _i

    def tambah(self, _i): return self.i + _i
    def kurang(self, _i):
    return self.i - _i