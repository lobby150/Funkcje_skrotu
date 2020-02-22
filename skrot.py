import hashlib
import time


def haszowanie_md5(tekst):
    start = time.time()
    wynik = hashlib.md5(tekst.encode("utf8")).hexdigest()
    end = time.time() - start
    print("Skrot wygenerowany dzieki funkcji MD5: " + wynik + ", czas generacji to: " + str(end*1000)+ " ms" + ", a dlugosc ciagu wyjsciowego to: " + str(len(wynik)))

def haszowanie_sha1(tekst):
    start = time.time()
    wynik = hashlib.sha1(tekst.encode("utf8")).hexdigest()
    end = time.time() - start
    print("Skrot wygenerowany dzieki funkcji SHA-1: " + wynik + ", czas generacji to: " + str(end*1000)+ " ms" + ", a dlugosc ciagu wyjsciowego to: " + str(len(wynik)))

def haszowanie_sha224(tekst):
    start = time.time()
    wynik = hashlib.sha224(tekst.encode("utf8")).hexdigest()
    end = time.time() - start
    print("Skrot wygenerowany dzieki funkcji SHA2-224: " + wynik + ", czas generacji to: " + str(end*1000)+ " ms" + ", a dlugosc ciagu wyjsciowego to: " + str(len(wynik)))

def haszowanie_sha256(tekst):
    start = time.time()
    wynik = hashlib.sha256(tekst.encode("utf8")).hexdigest()
    end = time.time() - start
    print("Skrot wygenerowany dzieki funkcji SHA2-256: " + wynik + ", czas generacji to: " + str(end*1000)+ " ms" + ", a dlugosc ciagu wyjsciowego to: " + str(len(wynik)))

def haszowanie_sha384(tekst):
    start = time.time()
    wynik = hashlib.sha384(tekst.encode("utf8")).hexdigest()
    end = time.time() - start
    print("Skrot wygenerowany dzieki funkcji SHA2-384: " + wynik + ", czas generacji to: " + str(end*1000)+ " ms" + ", a dlugosc ciagu wyjsciowego to: " + str(len(wynik)))

def haszowanie_sha512(tekst):
    start = time.time()
    wynik = hashlib.sha512(tekst.encode("utf8")).hexdigest()
    end = time.time() - start
    print("Skrot wygenerowany dzieki funkcji SHA2-512: " + wynik + ", czas generacji to: " + str(end*1000)+ " ms" + ", a dlugosc ciagu wyjsciowego to: " + str(len(wynik)))


def haszowanie_sha3_224(tekst):
    start = time.time()
    wynik = hashlib.sha3_224(tekst.encode("utf8")).hexdigest()
    end = time.time() - start
    print("Skrot wygenerowany dzieki funkcji SHA3-224: " + wynik + ", czas generacji to: " + str(end*1000)+ " ms" + ", a dlugosc ciagu wyjsciowego to: " + str(len(wynik)))

def haszowanie_sha3_256(tekst):
    start = time.time()
    wynik = hashlib.sha3_256(tekst.encode("utf8")).hexdigest()
    end = time.time() - start
    print("Skrot wygenerowany dzieki funkcji SHA3-256: " + wynik + ", czas generacji to: " + str(end*1000)+ " ms" + ", a dlugosc ciagu wyjsciowego to: " + str(len(wynik)))

def haszowanie_sha3_384(tekst):
    start = time.time()
    wynik = hashlib.sha3_384(tekst.encode("utf8")).hexdigest()
    end = time.time() - start
    print("Skrot wygenerowany dzieki funkcji SHA3-384: " + wynik + ", czas generacji to: " + str(end*1000)+ " ms" + ", a dlugosc ciagu wyjsciowego to: " + str(len(wynik)))

def haszowanie_sha3_512(tekst):
    start = time.time()
    wynik = hashlib.sha3_512(tekst.encode("utf8")).hexdigest()
    end = time.time() - start
    print("Skrot wygenerowany dzieki funkcji SHA3-512: " + wynik + ", czas generacji to: " + str(end*1000) + " ms" + ", a dlugosc ciagu wyjsciowego to: " + str(len(wynik)))

def haszowanie_shake_128(tekst):
    start = time.time()
    wynik = hashlib.shake_128(tekst.encode("utf8")).hexdigest(16)
    end = time.time() - start
    print("Skrot wygenerowany dzieki funkcji SHAKE-128: " + wynik + ", czas generacji to: " + str(end*1000) + " ms" + ", a dlugosc ciagu wyjsciowego to: " + str(len(wynik)))

def haszowanie_shake_256(tekst):
    start = time.time()
    wynik = hashlib.shake_256(tekst.encode("utf8")).hexdigest(32)
    end = time.time() - start
    print("Skrot wygenerowany dzieki funkcji SHAKE-256: " + wynik + ", czas generacji to: " + str(end*1000) + " ms" + ", a dlugosc ciagu wyjsciowego to: " + str(len(wynik)))

hamletx2 = open("hamlet2x.txt","r+")
hamletx2 = hamletx2.read()
hamletx3 = open("hamlet3x.txt","r+")
hamletx3 = hamletx3.read()

print("Dlugosc pliku z dwoma kopiami Hamleta: " + str(len(hamletx2))+ "\n")
print("Dlugosc pliku z trzema kopiami Hamleta: " + str(len(hamletx3))+ "\n")


print("Najpier haszowanie tresci pliku zawierajacego dwie kopie Hamleta \n")
haszowanie_md5(hamletx2)
haszowanie_sha1(hamletx2)
haszowanie_sha224(hamletx2)
haszowanie_sha256(hamletx2)
haszowanie_sha384(hamletx2)
haszowanie_sha512(hamletx2)
haszowanie_sha3_224(hamletx2)
haszowanie_sha3_256(hamletx2)
haszowanie_sha3_384(hamletx2)
haszowanie_sha3_512(hamletx2)
haszowanie_shake_128(hamletx2)
haszowanie_shake_256(hamletx2)
print("\n")
print("Nastepnie haszowanie tresci pliku zawierajacego trzy kopie Hamleta \n")
haszowanie_md5(hamletx3)
haszowanie_sha1(hamletx3)
haszowanie_sha224(hamletx3)
haszowanie_sha256(hamletx3)
haszowanie_sha384(hamletx3)
haszowanie_sha512(hamletx3)
haszowanie_sha3_224(hamletx3)
haszowanie_sha3_256(hamletx3)
haszowanie_sha3_384(hamletx3)
haszowanie_sha3_512(hamletx3)
haszowanie_shake_128(hamletx3)
haszowanie_shake_256(hamletx3)
haszowanie_md5("pies")