import requests
import json
from kivy.app import App
from kivy.uix.label import Label


class DolarApp(App):
    def build(self):
        # Obtém a cotação do dólar
        response = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados/ultimos/1?formato=json")
        data = json.loads(response.content.decode('utf-8'))
        cotacao = data[0]['valor']

        # Cria um rótulo para exibir a cotação
        label = Label(text=f"Cotação do Dólar: R${cotacao}",
                      font_size=30,
                      pos_hint={"center_x": 0.5, "center_y": 0.5})

        # Retorna o rótulo como conteúdo da aplicação
        return label


if __name__ == '__main__':
    DolarApp().run()
