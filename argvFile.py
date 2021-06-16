from sys import argv

command_list = ["r", "w", "c"]

# Prüft, ob die richtige Anzahl an Parametern übergeben wurde
if len(argv) != 2:
    print("Es muss genau ein Parameter angegeben werden!")
    exit(1)
mode = argv[1]
if mode == command_list[0]:
    print("Programm ist im Read-Mode")
elif mode == command_list[1]:
    print("Programm ist im Write-Mode")
elif mode == command_list[2]:
    print("Programm ist im Copy-Mode")
else:
    print("Ungültiger Parameter bitte wähle einen der folgenden:\n")
    for i in command_list:
        print(i)

