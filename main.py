# PUCPR - Escola Politécnica
# Computação Quântica - Gerador de números aleatórios
# Grupo 1: Kelvin C. Ribas, Marcos P. Ruppel, Rafael A. Souza, Rafaella Lemichka

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import numpy as np

# Parâmetros
NUM_QUBITS = 10
MAX_VALOR = 1000
SHOTS = 10000 # Executar diversas vezes para verificar a distribuição
simulator = AerSimulator()

def convert_counts_to_integers(counts):
    """Converte as cadeias de bits medidas em inteiros e filtra os valores > 1000."""
    valores_inteiros = []
    for bitstring, frequencia in counts.items():
        numero = int(bitstring, 2)
        # Filtra os números estritamente de 0 a 1000
        if numero <= MAX_VALOR:
            valores_inteiros.extend([numero] * frequencia)
    return valores_inteiros

# ==========================================
# Cenário 1: Distribuição Uniforme
# ==========================================
qc_uniform = QuantumCircuit(NUM_QUBITS, NUM_QUBITS)

# Aplica Hadamard em todos para distribuição igualitária
for i in range(NUM_QUBITS):
    qc_uniform.h(i)
qc_uniform.measure(range(NUM_QUBITS), range(NUM_QUBITS))

# Execução Uniforme
qc_uniform_transpiled = transpile(qc_uniform, simulator)
result_uniform = simulator.run(qc_uniform_transpiled, shots=SHOTS).result()
counts_uniform = result_uniform.get_counts()
dados_uniforme = convert_counts_to_integers(counts_uniform)

# ==========================================
# Cenário 2: Distribuição Tendenciosa
# ==========================================
# Definimos a tendência utilizando Rz entre portas H
theta = np.pi / 1.5  # Ângulo escolhido para favorecer o estado |1>
qc_biased = QuantumCircuit(NUM_QUBITS, NUM_QUBITS)

for i in range(NUM_QUBITS):
    qc_biased.h(i)
    qc_biased.rz(theta, i) # Porta Rz da dica do professor
    qc_biased.h(i)
qc_biased.measure(range(NUM_QUBITS), range(NUM_QUBITS))

# Execução Tendenciosa
qc_biased_transpiled = transpile(qc_biased, simulator)
result_biased = simulator.run(qc_biased_transpiled, shots=SHOTS).result()
counts_biased = result_biased.get_counts()
dados_tendenciosos = convert_counts_to_integers(counts_biased)

# ==========================================
# 4. Verificação das Distribuições (Gráficos)
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot Uniforme
ax1.hist(dados_uniforme, bins=50, color='skyblue', edgecolor='black')
ax1.set_title('Cenário 1: Distribuição Uniforme')
ax1.set_xlabel('Número Gerado (0 a 1000)')
ax1.set_ylabel('Frequência')

# Plot Tendencioso
ax2.hist(dados_tendenciosos, bins=50, color='salmon', edgecolor='black')
ax2.set_title('Cenário 2: Distribuição Tendenciosa (Valores Altos)')
ax2.set_xlabel('Número Gerado (0 a 1000)')
ax2.set_ylabel('Frequência')

plt.tight_layout()
plt.show()

print(f"Média Uniforme: {np.mean(dados_uniforme):.2f} (Esperado ~500)")
print(f"Média Tendenciosa: {np.mean(dados_tendenciosos):.2f} (Esperado > 500)")