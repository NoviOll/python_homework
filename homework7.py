# Напечатать строку в одну линию - C:\WINDOWS\System32\drivers\etc\nst
print(r"C:\WINDOWS\System32\drivers\etc\nst")

# На входе a = [4, 3, -10, 1, 7, 12], получить на выходе из этого списка а=[4, -10, 12, 3, 1, 7]
a = [4, 3, -10, 1, 7, 12]
a.sort(key=lambda x: x%2)
print(a)