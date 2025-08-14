import base64

while True:
    a=input()
    a = a.encode('utf-8')
    encoded = base64.b64encode(a)

    print(encoded)