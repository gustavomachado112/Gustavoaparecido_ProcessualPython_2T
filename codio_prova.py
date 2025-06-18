import random

nomes = [
    "ADRIAN  A", "ANGELO  P", "ARTHUR O", "CARLOS  M", "CHRISTOPHER  V",
    "INVALIDO", "EMANUELLY A", "EVERSON M", "GABRIEL  N", "GUILHERME L",
    "GUSTAVO  P", "GUSTAVO F", "ISABELLA N", "JAMILE B", "JOAO M",
    "PEQUIM", "JOAQUIM  R", "KALIKEY G", "LUIS  BONETE", "MARIA L",
    "PEDRO F", "PEDRO P", "RAFAEL N", "XANDAO", "ROBERTO K",
    "SOFIA B", "STEPHANIE S"
]

gustavo = "GUSTAVO M"
raphael = "RAPHAEL S"
lado_a_lado = [gustavo, raphael]
random.shuffle(lado_a_lado)
nomes = [n for n in nomes if n not in lado_a_lado]
random.shuffle(nomes)

pos = random.randint(0, len(nomes))
nomes[pos:pos] = lado_a_lado  

largura = max(len(nome) for nome in nomes) + 4

linha_topo = "".join("+" + "-" * largura for _ in nomes) + "+"
linha_meio = "".join("|" + nome.center(largura) for nome in nomes) +"|"
linha_base = "".join("+" + "-" * largura for _ in nomes) + "+"

print(linha_topo)
print(linha_meio)
print(linha_base)
