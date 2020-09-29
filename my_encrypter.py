#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
try:
    from base64 import *
except ImportError:
    print("Base64 kütüphanesi içeriye aktarılamadı")
try:
    from argparse import ArgumentParser
except ImportError:
    print("Argparse kütüphanesi içeriye aktarılamadı")
try:
    import os
    from os.path import expanduser
except ImportError:
    print("OS kütüphanesi içeriye aktarılamadı")
try:
    from sys import *
except ImportError:
    print("SYS kütüphanesi içeriye aktarılamadı")
class s:
    def __init__(self):
        self.author = "ALPEREN ÇAVUŞ"
        self.nick_name = "BufferOverFlow"
        self.composite = self.author + self.nick_name

    def banner(self):
        print("""
    ____  ___   _____ ___________ __ __
   / __ )/   | / ___// ____/ ___// // /
  / __  / /| | \__ \/ __/ / __ \/ // /_
 / /_/ / ___ |___/ / /___/ /_/ /__  __/
/_____/_/  |_/____/_____/\____/  /_/""")
        #print("\n", self.author, "\n", "*"len(self.composite), "\n", sep="")

class ENC: #Sınıf oluştur   
    """ENC SINIFI"""


    def __init__(self):
        self.encoder = b85encode #Şifreleyici
        self.decrypter = b85decode #Deşifreleyici

    def encrypter(self, data, file_extensions):
        if file_extensions == "all":
            file_extensions = data.split(".")[-1]
        else:
            file_extensions = file_extensions

        with open(data, "rb+") as f1:
            readed_data = f1.read()
            file_ext = data.split(".")[-1]
            encoded_data = b85encode(readed_data)
            if readed_data.startswith(b"#"):
                print(f"{data} Dosyası zaten şifrelenmiş")
            elif file_ext != file_extensions:
                print(f"{data} Dosyası şifrelenmedi çünkü uzantısı .{file_extensions} değil")
                pass
            else:
                with open(f"{data}.xen", "wb+") as f2:
                    f2.write(encoded_data)
                    print(f"{data} Dosyası başarılı bir şekilde şifrelendi")
                    print(readed_data[0:2])

    def Decrypter(self, data):
        file_name = data.split(".")[-2]
        with open(data, "rb+") as f2:
            readed_data = f2.read()
            try:
                decoded_data = b85decode(readed_data)
                with open(f"{data}.{file_name}", "wb+") as d1:
                    d1.write(decoded_data)
                    print(f"{file_name} Dosyası başarılı bir şekilde çözüldü ")
                    print(data)
            except BaseException:
                print(f"HATA {data} dosyası deşifrelenemedi ")

def main():
    APELİ = ENC()
    root_dir = os.getcwd()
    K = s()
    K.banner()


    ap = ArgumentParser(description=K.banner)
    ap.add_argument("--action", "-a",  dest="action", metavar="a.txt/b.txt", required=True, help="Yapmak istediğiniz işlemi seçin encrypt/decrypt")
    ap.add_argument("--file", "-f", dest="file", metavar="a.txt/b.txt", required=True, help="Üstünde işlem yapılacak olan dosya/dosyalar seçin")
    ap.add_argument("--extension", "-e", dest="exten", metavar="png/txt/csv/jpg", required=True, help="Sadece belli uzantılı dosyaları şifrelemek için ")
    ap_var = ap.parse_args()



    if ap_var.action == "decrypt":
        if ap_var.file == "all":
            for root, _, files in os.walk(root_dir):
                for f in files:
                    saa = os.path.join(root, f)
                    APELİ.Decrypter(saa)
        else:
            APELİ.Decrypter(ap_var.file)

    elif ap_var.action == "encrypt":
        ALPEREN = ENC()
        A = ALPEREN.Decrypter
        if ap_var.file == "all":
            for root, _, files in os.walk(root_dir):
                for f in files:
                    saa = os.path.join(root, f)
                    APELİ.encrypter(saa, ap_var.exten)
        else:
            APELİ.encrypter(ap_var.file)

    else:
        print(f"Hatalı işlem {ap_var.action}")
if __name__ == "__main__":
    main()
