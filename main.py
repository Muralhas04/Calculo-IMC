peso = float(input("Introduza o seu peso (em kg): "))
altura_cm = float(input("Introduza a sua altura (em centímetros): "))
altura_m = altura_cm / 100
imc = peso / (altura_m ** 2)
print(f"O seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("excesso de peso")
else:
    print("Obesidade")