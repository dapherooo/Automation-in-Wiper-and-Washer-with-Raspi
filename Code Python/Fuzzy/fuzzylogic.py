i = 0;

while i in range(0,1):
    #Inisialisasi Input
    getar = input('Input Getaran = ')
    g = float(getar)

    #Fuzzifikasi Input Getaran pada Kaca
    if g <= 224: # Nilai Fuzzy Getaran 100% Sangat Kecil
        nilai_sk = 1;
        nilai_k = 0;
        nilai_s = 0;
        nilai_b = 0;
        nilai_sb = 0;
    if g > 224 and g < 284: # Nilai Fuzzy Getaran Antara Sangat Kecil & Kecil
        nilai_sk = (284 - g)/(284 - 224);
        nilai_k = (g - 224)/(284 - 224);
        nilai_s = 0;
        nilai_b = 0;
        nilai_sb = 0;
    if g >= 284 and g <= 424: # Nilai Fuzzy Getaran 100% Kecil
        nilai_sk = 0;
        nilai_k = 1;
        nilai_s = 0;
        nilai_b = 0;
        nilai_sb = 0;
    if g > 424 and g < 484: # Nilai Fuzzy Getaran Antara Kecil & Sedang
        nilai_sk = 0;
        nilai_k = (484 - g)/(484 - 424);
        nilai_s = (g - 424)/(484 - 424);
        nilai_b = 0;
        nilai_sb = 0;
    if g >= 484 and g <= 624: # Nilai Fuzzy Getaran 100% Sedang
        nilai_sk = 0;
        nilai_k = 0;
        nilai_s = 1;
        nilai_b = 0;
        nilai_sb = 0;
    if g > 624 and g < 684: # Nilai Fuzzy Getaran Antara Sedang & Besar
        nilai_sk = 0;
        nilai_k = 0;
        nilai_s = (684 - g)/(684 - 624);
        nilai_b = (g - 624)/(684 - 624);
        nilai_sb = 0;
    if g >= 684 and g <= 824: # Nilai Fuzzy Getaran 100% Besar
        nilai_sk = 0;
        nilai_k = 0;
        nilai_s = 0;
        nilai_b = 1;
        nilai_sb = 0;
    if g > 824 and g < 884: # Nilai Fuzzy Getaran Antara Besar & Sangat Besar
        nilai_sk = 0;
        nilai_k = 0;
        nilai_s = 0;
        nilai_b = (684 - g)/(684 - 624);
        nilai_sb = (g - 624)/(684 - 624);
    if g >= 884 and g <= 1023: # Nilai Fuzzy Getaran 100% Sangat Besar
        nilai_sk = 0;
        nilai_k = 0;
        nilai_s = 0;
        nilai_b = 0;
        nilai_sb = 1;

    print(' ')
    print('Nilai Derajat Keanggotaan Input Getaran: ')
    print('Sangat Kecil = ', nilai_sk)
    print('Kecil = ', nilai_k)
    print('Sedang = ', nilai_s)
    print('Besar = ', nilai_b)
    print('Sangat Besar = ', nilai_sb)


    #Inferensi Sistem
    b=[]

    def diam (var_g):
        if var_g != 0:
            keluaran = 1;
            b.append([keluaran,var_g])

    def sekali (var_g):
        if var_g != 0:
            keluaran = 2;
            b.append([keluaran,var_g])

    def lambat (var_g):
        if var_g != 0:
            keluaran = 20;
            b.append([keluaran,var_g])

    def sedang (var_g):
        if var_g != 0:
            keluaran = 50;
            b.append([keluaran,var_g])

    def cepat (var_g):
        if var_g != 0:
            keluaran = 100;
            b.append([keluaran,var_g])

    #Fuzzy Rules
    diam(nilai_sk)
    sekali(nilai_k)
    lambat(nilai_s)
    sedang(nilai_b)
    cepat(nilai_sb)

    print('Gerak Wiper = ', b)
    print('')


    #Defuzzifikasi (Metode Weigth Average)
    x = 0;
    y = 0;

    for j in range (0, len(b)):
        c = b[j][0]*b[j][1]
        d = b[j][1]
        x = x + c
        y = y + d
        print('bj0 = ', b[j][0])
        print('bj1 = ', b[j][1])
        print(' ')
    z = x/y
    print('Gerakan Wiper = ', z)
    print(' ')