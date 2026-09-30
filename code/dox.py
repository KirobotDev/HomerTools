import webbrowser
from sont_selection import son_selection
from colorama import Fore

def dox() -> None:

    choixDox = input(f"""{Fore.RED}
                    ██╗  ██╗ ██████╗ ███╗   ███╗███████╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                    ██║  ██║██╔═══██╗████╗ ████║██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                    ███████║██║   ██║██╔████╔██║█████╗  ██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗
                    ██╔══██║██║   ██║██║╚██╔╝██║██╔══╝  ██╔══██╗       ██║   ██║   ██║██║   ██║██║     ╚════██║
                    ██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗██║  ██║       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

                                                            ===== TOOLS DOX =====
                                            1. Discord Lookup

                                            2. Identité Lookup

                                            3. Email lookup
        Choisis un tools de dox : {Fore.RED}{Fore.WHITE}""")

    if choixDox == "1":
        son_selection()
        url = "https://leak.fun/dashboard/searches/discord"
        webbrowser.open(url)
        return
    if choixDox == "2":
        son_selection()
        url = "https://leak.fun/dashboard/searches/breach"
        webbrowser.open(url)
        return
    if choixDox == "3":
        son_selection()
        url = "https://behindtheemail.com/"
        webbrowser.open(url)
        return

if __name__ == "__main__":
    dox()