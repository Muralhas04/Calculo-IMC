peso = float(input("Introduza o seu peso (em kg): "))
altura_cm = float(input("Introduza a sua altura (em centímetros): "))
altura_m = altura_cm / 100
imc = peso / (altura_m ** 2)
print(f"O seu IMC é: {imc:.2f}")

