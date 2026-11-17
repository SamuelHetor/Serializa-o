import csv

class LoteProducao:
    def __init__(self, numeroLote: int, tipoLiga: str, pesoTotal: float,
                 temperaturaFundicao: float, statusQualidade: str):
        self.numeroLote = numeroLote
        self.tipoLiga = tipoLiga
        self.pesoTotal = pesoTotal
        self.temperaturaFundicao = temperaturaFundicao
        self.statusQualidade = statusQualidade

# Passo 2: lista com 5 lotes (um turno)
lotes = [
    LoteProducao(1001, "Aço Inox 304", 1520.5, 1450.0, "Aprovado"),
    LoteProducao(1002, "Aço Carbono 1045", 1380.0, 1520.5, "Aprovado"),
    LoteProducao(1003, "Liga de Titânio", 980.75, 1670.0, "Reprovado"),
    LoteProducao(1004, "Aço Inox 316", 1610.2, 1475.5, "Aprovado"),
    LoteProducao(1005, "Liga de Alumínio", 1120.0, 660.0, "Em análise"),
]

# Passo 3: serializar a lista para CSV
campos = ["numeroLote", "tipoLiga", "pesoTotal", "temperaturaFundicao", "statusQualidade"]

with open("producao_turno.csv", "w", newline="", encoding="utf-8-sig") as arquivo:
    escritor = csv.writer(arquivo, delimiter=";")
    escritor.writerow(campos)  # cabeçalho
    for lote in lotes:
        escritor.writerow([
            lote.numeroLote,
            lote.tipoLiga,
            lote.pesoTotal,
            lote.temperaturaFundicao,
            lote.statusQualidade,
        ])

print("Arquivo producao_turno.csv salvo com sucesso")

# Passo 4: ler o CSV, reconstruir os objetos e calcular a média
lotes_lidos = []

with open("producao_turno.csv", "r", newline="", encoding="utf-8-sig") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    for linha in leitor:
        lote = LoteProducao(
            int(linha["numeroLote"]),
            linha["tipoLiga"],
            float(linha["pesoTotal"]),
            float(linha["temperaturaFundicao"]),
            linha["statusQualidade"],
        )
        lotes_lidos.append(lote)

print("\nLotes lidos do arquivo:")
for lote in lotes_lidos:
    print(f"Lote {lote.numeroLote} | {lote.tipoLiga} | {lote.pesoTotal} kg | "
          f"{lote.temperaturaFundicao} °C | {lote.statusQualidade}")

soma = sum(lote.temperaturaFundicao for lote in lotes_lidos)
media = soma / len(lotes_lidos)
print(f"\nMédia da temperatura de fundição: {media:.2f} °C")