# Gerador Quântico de Números Aleatórios

Projeto desenvolvido para a disciplina de Computação Quântica da PUCPR.

**Grupo 1**  
- Kelvin C. Ribas  
- Marcos P. Ruppel  
- Rafael A. Souza  
- Rafaelle Lemichka  

## Descrição

Este projeto implementa um **gerador quântico de números aleatórios** capaz de produzir inteiros no intervalo **0 a 1000**, explorando superposição e medição quântica.

Foram implementados dois cenários:

1. **Distribuição Uniforme**  
2. **Distribuição Tendenciosa para valores altos**

O objetivo é comparar o comportamento estatístico das duas abordagens através de simulação e análise gráfica.

---

## Tecnologias Utilizadas

- Python 3
- Qiskit
- Qiskit Aer Simulator
- NumPy
- Matplotlib

---

## Conceito Utilizado

Um número inteiro é gerado a partir da medição de um circuito com **10 qubits**, permitindo:

$ 2^{10} = 1024 $ combinações possíveis (0 a 1023).

Como o projeto exige números entre **0 e 1000**, os valores maiores que 1000 são descartados.

Cada bit medido compõe a representação binária do número gerado.

---

# Cenário 1: Distribuição Uniforme

## Abordagem

Foi aplicada uma porta Hadamard em cada qubit:

```python
qc.h(i)
```

A porta Hadamard coloca cada qubit em superposição:


$$ |0\rangle \rightarrow \frac{|0\rangle + |1\rangle}{\sqrt2} $$

produzindo:

- 50% de chance para medir 0
- 50% de chance para medir 1

Como todos os qubits possuem probabilidades iguais, todos os números válidos possuem distribuição aproximadamente uniforme.

## Resultado Esperado

- Frequências semelhantes para todos os números
- Média próxima de 500

---

# Cenário 2: Distribuição Tendenciosa

## Abordagem

A tendência foi definida pelo grupo utilizando a porta de rotação Ry no circuito `qc_biased`. 

Ao aplicar Ry com $\theta = \pi \div 1,5$, o estado de cada qubit é rotacionado de forma a favorecer significativamente a medição do estado $|1\rangle$. 

Como cadeias de bits com mais "1s" representam números decimais maiores, a distribuição final penderá fortemente para os valores mais altos.

## Resultado Esperado

- Histograma deslocado para a direita
- Média maior que 500
- Maior concentração de valores altos

---

## Execução

Instale as dependências:

```bash
pip install qiskit qiskit-aer matplotlib numpy
```

Execute:

```bash
python main.py
```

---

## Saída do Programa

O programa gera:

- Histograma da distribuição uniforme
- Histograma da distribuição tendenciosa
- Média dos números gerados em cada cenário

Exemplo:

```text
Média Uniforme: ~500
Média Tendenciosa: >500
```

---

## Estrutura do Projeto

```text
.
├── main.py
├── README.md
```

---

## Observações

- Foram utilizados **10.000 shots** para observar as distribuições estatísticas.
- O cenário tendencioso foi definido pelo grupo, conforme especificação do projeto.
- O viés foi construído com portas quânticas, e não manipulação clássica posterior dos resultados.

---

## Referência Teórica

O projeto baseia-se em:

- Superposição quântica
- Medição probabilística
- Rotações quânticas (Rz e Rx)
- Geração quântica de números aleatórios (QRNG)

---

## Autor(es)

Projeto acadêmico desenvolvido para fins educacionais na disciplina de Computação Quântica - PUCPR.