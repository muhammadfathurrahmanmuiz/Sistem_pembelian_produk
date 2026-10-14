class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print(f"Nama Produk  : {self.nama}")
        print(f"Harga Produk : Rp{self.harga:,}")

    def hitung_total(self, jumlah):
        return self.harga * jumlah

    def hitung_diskon(self, total):
        if total > 5000:
            return total * 0.05
        return 0


# Program utama
daftar_produk = []
jumlah_produk = int(input("Masukkan jumlah produk yang dibeli: "))

total_pembelian = 0

for i in range(jumlah_produk):
    print(f"\n=== Produk ke-{i + 1} ===")

    nama = input("Nama produk: ")
    harga = int(input("Harga produk: Rp"))
    jumlah = int(input("Jumlah beli: "))

    produk = Produk(nama, harga)
    total = produk.hitung_total(jumlah)

    daftar_produk.append((produk, jumlah, total))
    total_pembelian += total

# Menampilkan hasil pembelian
print("\n=== HASIL PEMBELIAN ===")

for produk, jumlah, total in daftar_produk:
    produk.tampilkan_info()
    print(f"Jumlah Beli  : {jumlah}")
    print(f"Total Produk : Rp{total:,}")
    print("------------------------")

# Menghitung diskon dan total bayar
diskon = produk.hitung_diskon(total_pembelian)
total_bayar = total_pembelian - diskon

print(f"\nTotal Pembelian : Rp{total_pembelian:,}")
print(f"Diskon 5%       : Rp{diskon:,.0f}")
print(f"Total Bayar     : Rp{total_bayar:,.0f}")