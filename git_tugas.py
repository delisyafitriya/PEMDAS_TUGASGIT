data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# Menampilkan seluruh data
for lokasi, data in data_panen.items():
    print(f"Nama Lokasi: {data['nama_lokasi']}")
    print("Hasil Panen:")
    for komoditas, jumlah in data['hasil_panen'].items():
        print(f"  {komoditas.capitalize()}: {jumlah}")
    print()

# Menampilkan jumlah hasil panen jagung dari lokasi2
hasil_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Jumlah hasil panen jagung dari lokasi2: {hasil_jagung_lokasi2}")

# Tampilkan nama lokasi dari lokasi3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi3}\n")

# Masukkan jumlah hasil panen padi dan kedelai ke dalam variabel yang berbeda
hasil_padi = {}
hasil_kedelai = {}

for lokasi, data in data_panen.items():
    hasil_padi[lokasi] = data['hasil_panen']['padi']
    hasil_kedelai[lokasi] = data['hasil_panen']['kedelai']

print("Jumlah hasil panen padi per lokasi:", hasil_padi)
print("Jumlah hasil panen kedelai per lokasi:", hasil_kedelai, "\n")

# Percabangan untuk mengecek lokasi yang memerlukan perhatian khusus
print("Status Lokasi:")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    nama = data['nama_lokasi']
    
    if padi > 1300 or jagung > 800:
        print(f"Lokasi {nama} memerlukan perhatian khusus.")
    else:
        print(f"Lokasi {nama} dalam kondisi baik.")