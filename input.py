# # import random

# ====================================================
# --------------LONDON BANKERS------------------------
# ====================================================

# # person = ["abebe", "kebede", "jeilan", "tirunesh"]

# # print("lets see who is going to buy!!!!!")
# # buyer = random.randint(0, (len(person) - 1))
# # print(f"{person[buyer]}" + " is going to buy the meal")
# # =============================================
# #             THE FOR LOOP
# # =============================================
# # fruits = ["apple", "mango", "banana"]
# # for fru in fruits:
# #     print(fru)

# # =================================================
# # ----------------FIZZ BUZZ EXERSISE---------------
# # =================================================
# # for num in range(1, 101):
# #     if num % 3 == 0 and num % 5 == 0:
# #         print("fizz buzz")
# #     elif num % 3 == 0:
# #         print("fizz")
# #     elif num % 5 == 0:
# #         print("buzz")
# #     else:
# #         print(num)

# # =================================================
# # ----------PASSWORD GENERATOR---------------------
# # =================================================

# import random

# letters = ["A", "B", "C", "D", "E", "d", "a", "b", "c", "d"]
# symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "("]
# number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# i = int(input("how many letters:\n"))
# j = int(input("how many numbers:\n"))
# k = int(input("how many symbols:\n"))

# password = []
# mixed = []

# for l in range(i):
#     a = random.randint(0, len(letters) - 1)
#     b = letters[a]
#     password.append(b)
# for q in range(j):
#     a = random.randint(0, len(symbols) - 1)
#     b = symbols[a]

#     password.append(b)

# for s in range(k):
#     a = random.randint(0, len(number) - 1)
#     b = number[a]

#     password.append(b)
# print(password)
# random.shuffle(password)
# print("".join(password))

# =================================================
# -------PRIME NUMBER CHEAKER FUNCTION-------------
# =================================================

# number = int(input("what is your number:\n"))

# def prime_cheaker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False

#     if is_prime == True:
#         print("it is a prime number")
#     else:
#         print("it is not a composite number")


# prime_cheaker(number)

# =================================================
# -------------CHISER CIPHER-----------------------
# =================================================

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
# dxn = input("type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
# text = input("type your message:\n").lower()
# shift = int(input("type the shift number:\n"))


# def encrypt(plain_text, shfit_amount):
#     encrypted_text = ""
#     for letter in plain_text:
#         position = letters.index(letter)
#         new_position = position + shfit_amount
#         encrypted_text += letters[new_position]
#     print("your encrypted text is: " + encrypted_text)


# def decrypt(plain_text, shfit_amount):
#     decrypted_text = ""
#     for letter in plain_text:
#         position = letters.index(letter)
#         new_position = position - shfit_amount
#         decrypted_text += letters[new_position]
#     print("your decrypted text is: " + decrypted_text)


# if dxn == "decode":
#     decrypt(plain_text=text, shfit_amount=shift)
# elif dxn == "encode":
#     encrypt(plain_text=text, shfit_amount=shift)
# else:
#     print("i am not getting what you are saying!!!!!")


# ===============================================================
# --------------another way to do this---------------------------
# ===============================================================
# def cyper(start_text, shift_amount, dirction):
#     end_text = ""
#     for letter in start_text:
#         position = letters.index(letter)
#         if dirction == "decode":
#             shift_amount *= -1
#         new_position = position + shift_amount
#         end_text += letters[new_position]
#     print(f"your {dirction}d text is: " + end_text)


# cyper(start_text=text, shift_amount=shift, dirction=dxn)
# ========================================================
# --------------IMPROVE USER EXPERIANCE-------------------
# ========================================================
# print(
#     """
# ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
# 8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
#             88             88
#            ""             88
#                           88
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
# 8b         88 88       d8 88       88 8PP" 88
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
#               88
#               88 """
# )


# def cyper(start_text, shift_amount, dirction):
#     end_text = ""
#     for letter in start_text:
#         if letter in letters:
#             position = letters.index(letter)
#             if dirction == "decode":
#                 shift_amount *= -1
#             new_position = position + shift_amount
#             end_text += letters[new_position]
#         else:
#             end_text += letter

#     print(f"your {dirction}d text is: " + end_text)


# should_continue = True

# while should_continue:
#     dxn = input("type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
#     text = input("type your message:\n").lower()
#     shift = int(input("type the shift number:\n"))
#     shift = shift % 26
#     cyper(start_text=text, shift_amount=shift, dirction=dxn)

#     result = input(
#         'do you want to keep this program if you want say "yes", if you donot want to run it say"no" '
#     ).lower()
#     if result == "no":
#         print("good bye💖💖💖")
#         should_continue = False

# ================================================
#
# ================================================
fam = ["tsehay", "bedada", "abnew", "all families"]
for da in fam:
    print(da + " fuck you all who fucked up ,my life")
