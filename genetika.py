import random
kamus = {
    "makan": "manre",
    "gunung": "bulu",
    "tidur": "mattinro",
    "rumah": "bola",
    "hujan": "bosi",
    "air": "wae",
    "pergi": "lao",
    "ikan": "bale",
    "baju": "haju",
    "rambut": "halua"
}

populasi = []
fitness_list = []
target = ""

def tampilkan_kamus():
    print("\n=== KAMUS BUGIS BONE ===")
    for i, j in kamus.items():
        print(f"{i} = {j}")

def cari_kata():
    kata = input("\nMasukkan kata Indonesia: ").lower()
    print("Bahasa Bugis Bone :", kamus.get(kata, "Kata tidak ditemukan"))

def buat_populasi():
    global populasi
    populasi = random.sample(list(kamus.values()), 4)

def tampilkan_populasi():
    print("\n=== POPULASI ===")
    for i, k in enumerate(populasi, 1):
        print(f"{i}. {k}")

def hitung_fitness():

    global fitness_list
    fitness_list = []

    print("\n=== HASIL FITNESS ===")

    for kata in populasi:

        fitness = 0

        for i in range(min(len(kata), len(target))):

            if kata[i] == target[i]:
                fitness += 1

        fitness_list.append(fitness)

        print(f"{kata} = {fitness}")

def seleksi_roulette():
    if sum(fitness_list) == 0:
        return random.choice(populasi)

    return random.choices(populasi, weights=fitness_list)[0]

def crossover(p1, p2):
    t = min(len(p1), len(p2)) // 2
    return p1[:t] + p2[t:], p2[:t] + p1[t:]

def mutasi(kata):
    kata = list(kata)
    i = random.randint(0, len(kata)-1)
    kata[i] = random.choice("abcdefghijklmnopqrstuvwxyz")
    return "".join(kata)

def generasi_baru():
    print("\n=== GENERASI BARU ===")

    p1 = seleksi_roulette()
    p2 = seleksi_roulette()

    print("Parent 1 :", p1)
    print("Parent 2 :", p2)

    c1, c2 = crossover(p1, p2)

    print("\nHasil Cross Over")
    print("Child 1 :", c1)
    print("Child 2 :", c2)

    c1 = mutasi(c1)
    c2 = mutasi(c2)

    print("\nHasil Mutasi")
    print("Mutasi 1 :", c1)
    print("Mutasi 2 :", c2)

def jalankan_ga():
    global target

    target = input("\nMasukkan target kata Bugis Bone: ").lower()

    buat_populasi()
    tampilkan_populasi()
    hitung_fitness()
    generasi_baru()

while True:

    print("\n===================================")
    print("      KAMUS BAHASA BUGIS BONE")
    print("===================================")

    print("1. Tampilkan Kamus")
    print("2. Cari Kata")
    print("3. Jalankan Algoritma Genetika")
    print("4. Tampilkan Populasi")
    print("5. Hasil Fitness")
    print("6. Seleksi Roulette")
    print("7. Cross Over")
    print("8. Mutasi")
    print("9. Generasi Baru")
    print("10. Keluar")

    pilih = input("\nPilih menu : ")

    if pilih == "1":
        tampilkan_kamus()

    elif pilih == "2":
        cari_kata()

    elif pilih == "3":
        jalankan_ga()

    elif pilih == "4":
        tampilkan_populasi()

    elif pilih == "5":
        hitung_fitness()

    elif pilih == "6":
        print("\nHasil Seleksi Roulette :", seleksi_roulette())

    elif pilih == "7":

        if len(populasi) < 2:
            print("Populasi belum cukup")

        else:
            p1, p2 = populasi[0], populasi[1]

            c1, c2 = crossover(p1, p2)

            print("\nParent 1 :", p1)
            print("Parent 2 :", p2)

            print("\nHasil Cross Over")
            print("Child 1 :", c1)
            print("Child 2 :", c2)

    elif pilih == "8":

        if not populasi:
            print("Populasi belum ada")

        else:
            print("\nSebelum Mutasi :", populasi[0])
            print("Sesudah Mutasi :", mutasi(populasi[0]))

    elif pilih == "9":

        if not populasi:
            print("Jalankan algoritma genetika dulu")

        else:
            generasi_baru()

    elif pilih == "10":
        print("\nTerima kasih telah menggunakan kamus ini")
        break

    else:
        print("\nPilihan tidak tersedia")