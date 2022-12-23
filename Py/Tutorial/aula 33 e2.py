def hora(h):
    a = h[0:2]
    b = h[3:5]
    c = int(a)
    d = int(b)

    if 0 <= c < 12:
        if c == 0 and d == 0:
            n = '12:00 AM'
        else:
            n = a + ':' + b + ' AM'
    elif 12 <= c < 24:
        if c == 12:
            n = a + ':' + b + ' PM'
        else:
            c = c - 12
            c = str(c)
            n = c + ':' + b + ' PM'
    return n


h = input("Coloque a hora no formato 24H : ")
print(hora(h))
