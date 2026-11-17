import json

class Dronestatus:
    def __init__(self, codigoIdentificador:str, nivelBateria:int, latitude:float, longitude:float,emMissao: bool):
        self.codigoIdentificador = codigoIdentificador
        self.nivelBateria = nivelBateria
        self.latitude = latitude
        self.longitude = longitude
        self.emMissao = emMissao

Drone_meu = Dronestatus(
    codigoIdentificador=777,
    nivelBateria= 89,
    latitude=90,
    longitude=80,
    emMissao= True
)
print('O numero identificador do seu drone é: ', Drone_meu.codigoIdentificador)
print('O nível de bateria do seu drone é: ', Drone_meu.nivelBateria)

dados = Drone_meu.__dict__
with open("status_drone.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4)
print("Arquivo status_drone.json salvo com sucesso")


with open("status_drone.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)

drone_lido = Dronestatus(**dados_lidos)

print("Dados do drone lido do arquivo:")
print("Código:", drone_lido.codigoIdentificador)
print("Bateria:", drone_lido.nivelBateria)
print("Latitude:", drone_lido.latitude)
print("Longitude:", drone_lido.longitude)
print("Em missão:", drone_lido.emMissao)