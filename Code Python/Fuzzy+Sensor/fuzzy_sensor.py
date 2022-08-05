from gpiozero import MCP3008
from time import sleep

getar = MCP3008(0)


while True:
    adc = (getar.value)*1023
    print('Nilai ADC Getaran = ',adc)


    #Fuzzifikasi Input Getaran pada Kaca
    if adc <= 224: # Nilai Fuzzy Getaran 100% Sangat Kecil
        nilai_sk = 1;
        nilai_k = 0;
        nilai_s = 0;
        nilai_b = 0;
    if adc > 224 and adc < 284: # Nilai Fuzzy Getaran Antara Sangat Kecil & Kecil
        nilai_sk = (284 - adc)/(284 - 224);
        nilai_k = (adc - 224)/(284 - 224);
        nilai_s = 0;
        nilai_b = 0;
    if adc >= 284 and adc <= 424: # Nilai Fuzzy Getaran 100% Kecil
        nilai_sk = 0;
        nilai_k = 1;
        nilai_s = 0;
        nilai_b = 0;
    if adc > 424 and adc < 484: # Nilai Fuzzy Getaran Antara Kecil & Sedang
        nilai_sk = 0;
        nilai_k = (484 - adc)/(484 - 424);
        nilai_s = (adc - 424)/(484 - 424);
        nilai_b = 0;
    if adc >= 484 and adc <= 624: # Nilai Fuzzy Getaran 100% Sedang
        nilai_sk = 0;
        nilai_k = 0;
        nilai_s = 1;
        nilai_b = 0;
    if adc > 624 and adc < 800: # Nilai Fuzzy Getaran Antara Sedang & Besar
        nilai_sk = 0;
        nilai_k = 0;
        nilai_s = (684 - adc)/(684 - 624);
        nilai_b = (adc - 624)/(684 - 624);
    if adc >= 800: # Nilai Fuzzy Getaran 100% Besar
        nilai_sk = 0;
        nilai_k = 0;
        nilai_s = 0;
        nilai_b = 1;



    print(' ')
    print('Nilai Derajat Keanggotaan Input Getaran: ')
    print('Sangat Kecil = ', nilai_sk)
    print('Kecil = ', nilai_k)
    print('Sedang = ', nilai_s)
    print('Besar = ', nilai_b)


    #Inferensi Sistem
    b=[]

    def diam (var_g):
        if var_g != 0:
            keluaran = 1;
            b.append([keluaran,var_g])

    def lambat (var_g):
        if var_g != 0:
            keluaran = 50;
            b.append([keluaran,var_g])

    def sedang (var_g):
        if var_g != 0:
            keluaran = 80;
            b.append([keluaran,var_g])

    def cepat (var_g):
        if var_g != 0:
            keluaran = 100;
            b.append([keluaran,var_g])

    #Fuzzy Rules
    diam(nilai_sk)
    lambat(nilai_k)
    sedang(nilai_s)
    cepat(nilai_b)

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
    print(' ')
    print(' ')
    sleep(5)