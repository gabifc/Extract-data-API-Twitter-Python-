# formato do dado que vem de resposta da biblioteca, preciso dele para processar o dado
import json
# bibliotecas do twitter para fazer as requisições de fato. 
from tweepy import OAuthHandler, Stream, StreamListener 
# importar a data completa com hrs, min e seg
from datetime import datetime

# Castrar as 4 chaves de acesso

# API KEY
consumer_key = " sua chave aqui "
# API secret key
consumer_secret = "sua chave aqui"

access_token = "sua chave aqui"

access_token_secret = "sua chave aqui"

# definir um arquivo de saída para armazenas os tweets coletados
# como o arquivo de saíde out só tem um nome, ele será sobrescrito ao encontrar um novo dado.
# importante colocar o datetime para que a variação de horas e datas não sobrescreva o dado anterior. Assim, sempre terá um segundo diferente que tornará o dado único e evitará a sobrescrição.
# date_today é a variavel, datetime agora e o strftime com os parametros do formato do dado data e hora
date_today = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
# o datetime é o f antes do () e depois do "" e tbm as {} no final do tweets{date_today}
out = open(f"collected_tweets_{date_today}.txt", "w")

# implementar uma classe para conexão com o Twitter
# a classe MyListener herda a StreamListener importada do tweepy pq vou modificar/reescrecer 2 métodos/ações desta classe. 1º o que esta classe vai fazer quando encontrar algum dado e 2° o que ela vai fazer quando der ero.
# a classe StreamListener estabelece conexão com a api stream do twitter. Diferente do modulo de requisição que agt pedo pro twitter dados que já estão lá. No Stream cria uma conexão com twitter e pedir/requisitar que retorne todos os novos twittes que aparecerem com uma determinada palavra chave ou alguma expressão que colocar para ser trackeada.

class MyListener(StreamListener):
    # reescrevo o metodo on_data e passo self que é a classe e data que é o dado
    def on_data(self, data):
    # quando ele achar um dado novo printo p testar - depois deve ser removido
    #crio uma string deste dado. pego o dado cru e indico ao python que este dado é um json
        # print(data)
        itemString = json.dumps(data)
    # chamo o out lá de cima e escrevo o dado nele
        out.write(itemString + "\n")
        return True
    # trato o erro - quando encontrar o erro printa o erro
    def on_error(self, status):
        print(status)

# implementar a função MAIN 
if __name__ == "__main__":
    l = MyListener()
# passando as chaves
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
# criando o stream - instância que escuta/traqueia os dados
# instanciando a classe e passo a autenticação e o l
    stream = Stream(auth, l)
# código que executa de fato o stream, passo o dado que quero monitorar
    stream.filter(track=["Kamala Harris"])