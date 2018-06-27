letra = input("Dame una letra: ")

if letra == "a":
	print("Es la vocal a")
elif letra == "e":
	print("Es la volcal e")
elif letra == "i":
	print("Es la vocal i")
elif letra == "o":
	print("Es la vocal o")
elif letra == "u":
	print("Es la vocal u")
else:
	print("No es una vocal")

# No es necesario poner al final un else
# Cuando se cumple un elif, los demás ya no
# son evaluados