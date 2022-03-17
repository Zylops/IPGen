import random
import pyperclip
def generateIp():
    values = [str(random.randint(0,255)), str(random.randint(0,255)), str(random.randint(0,255)), str(random.randint(0,255))]
    ip = '.'.join(values)
    return ip

pyperclip.copy(generateIp())