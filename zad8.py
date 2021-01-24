file = open("plik.txt", "w+")
file.write("zadanie 8")

file.seek(0)
print(file.read())
file.close()
	
