from collections import Counter
def obter_numero_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print(
                    "Erro: O valor deve ser maior do que zero. Tente novamente."
                )
                continue
            return valor
        except ValueError:
            print("Erro: Por favor, introduza um número válido (use . para decimais).")


def calcular_imc(peso, altura_cm):
    altura_m = altura_cm / 100
    return peso / (altura_m**2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Excesso de peso"
    else:
        return "Obesidade"


def exibir_resumo(consultas):
    total_consultas = len(consultas)
    
    if total_consultas == 0:
        print("Nenhuma consulta realizada.")
        return
    
    valores_imc = [consulta['imc'] for consulta in consultas]
    classificacoes = [consulta['classificacao'] for consulta in consultas]
    
    media_imc = sum(valores_imc) / total_consultas
    
    contador = Counter(classificacoes)
    classe_mais_comum = contador.most_common(1)[0][0]
    
    print("\n" + "=" * 40)
    print("Resumo das Consultas")
    print("=" * 40)
    print(f"Total de consultas: {total_consultas}")
    print(f"IMC médio: {media_imc:.2f}")
    print(f"Classificação mais comum: {classe_mais_comum}")


def main():
    historico_consultas = []
    
    print("Bem-vindo ao sistema de cálculo de IMC!")
    while True:
        print(f"\n--- Consulta nº {len(historico_consultas) + 1} ---")
        
        peso = obter_numero_positivo("Introduza o seu peso (em kg): ")
        altura_cm = obter_numero_positivo("Introduza a sua altura (em centímetros): ")
        
        imc = calcular_imc(peso, altura_cm)
        classificacao = classificar_imc(imc)
        
        print(f"O seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        
        historico_consultas.append({
            'imc': imc,
            'classificacao': classificacao
        })
        
        resposta = input("Deseja realizar outra consulta? (s/n): ").strip().lower()
        if resposta != 's':
            break
        
    exibir_resumo(historico_consultas)


if __name__ == "__main__":
    main()