import random

print("\033[1;32m")

print("***********************************************'*'")

print("            TELEGRAM @MasteR_a8")

print("*************************************************")

print("            TIKTOK_abdullahassan15")

print("*************************************************")

print("            TEBENI PASSWORDAKAN COSTUMN")

print("*************************************************")

print("            AUTO PASSWORD GENERATOR")

print("*************************************************")

print("__________________ABDULLAHASSAN__________________")

print("**************************************************")

print("      ↓↓↓TKAYA TANHA BA ZHMARA HAL BZHERA↓↓↓")

print("*************************************************")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!£$%^&*(`)"

print("\033[1;31m")

while 1:

    password_len = int(input(" ♡{DATAWE PASSWORDAKANT CHAND PET BN} "))

    password_count = int(input(" ♡{ZHMARAY PASSWORDAKAN CHAND DANA BN} "))

    for x in range(0,password_count):

        password  = ""

        for x in range(0,password_len):

            password_char = random.choice(chars)

            password      = password + password_char

        print("    AWANA PASSWORDAKANN}♡ ", password)
