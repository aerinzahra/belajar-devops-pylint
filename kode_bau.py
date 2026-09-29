"""Modul untuk pengujian code quality."""


def hitung_nilai(a, b, c, d, e, f):
    """Menghitung nilai dari beberapa parameter."""
    return a + b + c + d + e[0] + f


hasil = hitung_nilai(1, 2, 3, 4, [5], 6)
print(hasil)