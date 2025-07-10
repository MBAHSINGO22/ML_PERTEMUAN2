
kata = input('Masukkan sebuah kata: ')


jumlah_karakter = len(kata)
palindrome = True

for i in range(jumlah_karakter):
    if kata[i] != kata[jumlah_karakter - 1 - i]:
        palindrome = False
        break

if palindrome:
    print(kata, "merupakan PALINDROME")
else:
    print(kata, "bukan PALINDROME")