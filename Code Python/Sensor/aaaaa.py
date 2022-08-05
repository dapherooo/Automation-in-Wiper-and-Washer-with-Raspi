from gpiozero import MCP3008

a = MCP3008(7)

while True:
    print(a.value)