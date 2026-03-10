class Mobil: # kerangka untuk membuat objek
    #__init__ adalah fungsi khusus yang otomatis dipanggil saat objet di buat
    def __init__(self, merek, model, tahun): # memiliki 3 atribut, yaitu merek, model, dan tahun
        self.merek = merek
        self.model = model
        self.tahun = tahun
        # self berfungsi untuk merepresentasikan objek itu sendiri,
        # atau bisa di bilang properti yang dimiliki setiap objek

    def tampilkan_info(self): #ini adalah fungsi yang di miliki kelas mobil untuk menampilkan data mobil
        print(f"Mobil: {self.merek} {self.model}, Tahun: {self.tahun}")

#membuat beberapa objek contoh
mobil1 = Mobil("Toyota", "Avanza", 2020) 
mobil2 = Mobil("Honda", "Civic", 2018) 
mobil3 = Mobil("Suzuki", "Swift", 2022)
# masing masing objek memiliki data berbeda, tetapi berbagi metode yang sama

#menampilkan informasi tiap mobil
mobil1.tampilkan_info()
mobil2.tampilkan_info()
mobil3.tampilkan_info()

## dibuat oleh latip 20240040036