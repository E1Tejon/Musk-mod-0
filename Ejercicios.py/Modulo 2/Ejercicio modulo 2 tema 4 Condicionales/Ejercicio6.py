# 6º Haz un programa que añada un segundo en una hora del día, dadas sus horas, minutos y segundos. 

H = int(input("Hora: "))
M = int(input("Minuto: "))
S = int(input("Segundo: "))

if S + 1 > 59:
    S = 0
    M += 1
    if M + 1 > 59:
        M = 0
        H += 1
        if H + 1 > 23:
            H = 0
else:
    S += 1
print(f"h: {H} m: {M} s: {S}")
