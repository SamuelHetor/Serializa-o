import xml.etree.ElementTree as ET
class Amostra:
    def __init_(self,idAmostra:str, tipoMaterial:str,dataColeta:str):
        self.idAmostra = idAmostra
        self.tipoMaterial = tipoMaterial
        self.dataColeta = dataColeta
class ResponsavelTecnico:
    def __init__(self,nomeCientista:str,registroProfissional:str):
        self.nomeCientista = nomeCientista
        self.registroProfissional = registroProfissional

class RelatorioAnalise:
    def __init__(self, amostra: Amostra, responsavel: ResponsavelTecnico, resultados:list):
        self.amostra = amostra
        self.responsavel = responsavel
        self.resultados = resultados 

# Passo 2: criar o objeto
amostra = Amostra("AM-2026-0042", "Tecido hepático", "2026-11-17")
responsavel = ResponsavelTecnico("Dra. Helena Duarte", "CRBM-12345")
relatorio = RelatorioAnalise(
    amostra,
    responsavel,
    ["Proteína X", "Enzima Y", "Anticorpo Z", "Lipoproteína A", "Glicoproteína B"]
)

print("Relatório criado para a amostra:", relatorio.amostra.idAmostra)

# Passo 3: serializar para XML
raiz = ET.Element("relatorio")

amostra_tag = ET.SubElement(raiz, "amostra")
ET.SubElement(amostra_tag, "idAmostra").text = relatorio.amostra.idAmostra
ET.SubElement(amostra_tag, "tipoMaterial").text = relatorio.amostra.tipoMaterial
ET.SubElement(amostra_tag, "dataColeta").text = relatorio.amostra.dataColeta

responsavel_tag = ET.SubElement(raiz, "responsavel")
ET.SubElement(responsavel_tag, "nomeCientista").text = relatorio.responsavel.nomeCientista
ET.SubElement(responsavel_tag, "registroProfissional").text = relatorio.responsavel.registroProfissional

resultados_tag = ET.SubElement(raiz, "resultados")
for componente in relatorio.resultados:
    ET.SubElement(resultados_tag, "componente").text = componente

arvore = ET.ElementTree(raiz)
ET.indent(arvore, space="    ")
arvore.write("relatorio_amostra.xml", encoding="utf-8", xml_declaration=True)

print("Arquivo relatorio_amostra.xml salvo com sucesso")

# Passo 4: ler o XML e exibir (auditoria)
arvore_lida = ET.parse("relatorio_amostra.xml")
raiz_lida = arvore_lida.getroot()

print("\n===== AUDITORIA DO ÓRGÃO REGULADOR =====")

print("\nDADOS DA AMOSTRA")
print("ID:", raiz_lida.findtext("amostra/idAmostra"))
print("Material:", raiz_lida.findtext("amostra/tipoMaterial"))
print("Data de coleta:", raiz_lida.findtext("amostra/dataColeta"))

print("\nRESPONSÁVEL TÉCNICO")
print("Cientista:", raiz_lida.findtext("responsavel/nomeCientista"))
print("Registro:", raiz_lida.findtext("responsavel/registroProfissional"))

print("\nRESULTADOS")
for componente in raiz_lida.findall("resultados/componente"):
    print("-", componente.text)