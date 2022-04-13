YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'


print("    ██████╗░░█████╗░████████╗")
print("    ██╔══██╗██╔══██╗╚══██╔══╝")
print("    ██████╦╝██║░░██║░░░██║░░░")
print("    ██╔══██╗██║░░██║░░░██║░░░")
print("    ██████╦╝╚█████╔╝░░░██║░░░")
print("    ╚═════╝░░╚════╝░░░░╚═╝░░░")
print("██████╗░███████╗██████╗░░█████╗░██████╗░████████╗")
print("██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══ ")
print("██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░")
print("██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░")
print("██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░")
print("╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░")

print("\033[33m--------------------------------------")
print(YELLOW+"Autor    : dxlswb")
print("--------------------------------------")
print("INSTAGRAM: X Swagyy X")
print("--------------------------------------")
print("TIK TOK  : dxlswb")
print("-------------------------------------- \n")
print("escribe el numero de telefono junto\ncon el prefijo,para encontrar su tiktok y bannearlo ejemplo: +526621745707")


api_key = '7e1cadf1fc1587fd37db7ea1e6c29a50'

number = int(input(GREEN+"Numero de telefono: "+RESET))

data = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api_key, number))

for key, value in data.json().items():

    print("%s: %s" % (key, value))
