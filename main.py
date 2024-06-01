print("****ELECTRIC BILL CALCULATION****")


subscribernumber = input("Lütfen abone numaranızı giriniz :")

while True:
   try:
      tur = """ 
      1. Mesken İçin Tek Zamanlı Tarife
      2. Mesken İçin Çok Zamanlı Tarife 
      3. Ticarethane İçin Tek Zamanlı Tarife
      4. Ticarethane İçin Çok Zamanlı Tarife
      """


      islem = int(input(tur))

      if islem == 1:
         consumption = float(input("Lütfen Aylık Tüketim Miktarını Giriniz(kWh):"))
         readingday = int(input("Lütfen Okuma Gün Sayısını Giriniz:"))
         average = float(consumption / readingday)
         print("Günlük Ortalama Tüketim Miktarınız:", average,"kWh")
         if average <= 8:
            tutar1 = "1.124378"
            fatura = consumption * float(tutar1)
            print("Fatura Tutarınız: ",fatura,"TL")
         else:
            tutar1 = "1.28206897"
            tutar2 = "1.91499920"
            fatura1 = 240 * float(tutar1)
            fatura2 = ((consumption - 240) * float(tutar2)) + fatura1
            print("Fatura Tutarınız: ",fatura2,"TL")
            break

      elif islem == 2:
         day = float(input("Lütfen Toplam Gündüz(06.00-17.00) Tarifesi Tüketim Miktarını Giriniz: "))
         puant = float(input("Lütfen Toplam Puant(17.00.00-22.00) Tarifesi Tüketim Miktarını Giriniz: "))
         night = float(input("Lütfen Toplam Gece(22.00-06.00) Tarifesi Tüketim Miktarını Giriniz: "))
         aktiftuketim = day + puant + night
         readingday2 = int(input("Lütfen Okuma Gün Sayısını Giriniz:"))
         average2 = aktiftuketim / readingday2
         print("Aktif Tüketim Miktarınız : ",aktiftuketim,"kWh")
         print("Günlük Ortalama Tüketim Miktarınız:", average2,"kWh")
         tutarday = "0.5092"
         tutarpuant = "0.7479"
         tutarnight = "0.3184"
         fatura3 = (day * float(tutarday)) + (puant * float(tutarpuant)) + (night * float(tutarnight))
         print("Fatura Tutarınız : ",fatura3,"TL")
         break

      elif islem == 3:
         consumptiont = float(input("Lütfen Aylık Tüketim Miktarını Giriniz(kWh):"))
         readingday3 = int(input("Lütfen Okuma Gün Sayısını Giriniz:"))
         average3 = float(consumptiont / readingday3)
         print("Günlük Ortalama Tüketim Miktarınız:", average3, "kWh")
         tutar1t = "2.437383"
         faturat = consumptiont * float(tutar1t)
         print("Fatura Tutarınız: ", faturat,"TL")
         break

      elif islem == 4:
         dayt = float(input("Lütfen Toplam Gündüz(06.00-17.00) Tarifesi Tüketim Miktarını Giriniz: "))
         puantt = float(input("Lütfen Toplam Puant(17.00.00-22.00) Tarifesi Tüketim Miktarını Giriniz: "))
         nightt = float(input("Lütfen Toplam Gündüz(22.00-06.00) Tarifesi Tüketim Miktarını Giriniz: "))
         aktiftuketimt = dayt + puantt + nightt
         readingday4 = int(input("Lütfen Okuma Gün Sayısını Giriniz:"))
         average4 = aktiftuketimt / readingday4
         print("Aktif Tüketim Miktarınız : ", aktiftuketimt, "kWh")
         print("Günlük Ortalama Tüketim Miktarınız:", average4, "kWh")
         tutardayt = "0.5335"
         tutarpuantt = "0.7833"
         tutarnightt = "0.3347"
         fatura5 = (dayt * float(tutardayt)) + (puantt * float(tutarpuantt)) + (nightt * float(tutarnightt))
         print("Fatura Tutarınız : ", fatura5, "TL")
         break

      else:
         print("Hatalı bir seçim yaptınız. Lütfen tekrar seçiniz.")

   except ValueError:
      print("Lütfen Girdiğiniz Değerleri Kontrol Ediniz!")
      break