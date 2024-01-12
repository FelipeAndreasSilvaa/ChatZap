import flet as ft

def main(pagina):
    # texto
    texto = ft.Text("Chat Felipe")
    
    nome_usuario = ft.TextField(label="Escreva seu nome...")
    
    chat = ft.Column()

    
    def enviar_menssagem_tunel(informacoes):
        print(informacoes)
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_menssagem_tunel)
    
    campo_msg = ft.TextField(label="Escreva sua menssagem aqui...")
    
    def enviar_menssagem(evento):
        # colocar o nome do usuario na msg
        texto_campo_mensagem = f"Usuario: {nome_usuario.value}: Mensagem: {campo_msg.value}"
        pagina.pubsub.send_all(texto_campo_mensagem)
        
        # limpar o camppo_mensagem
        campo_msg.value = ""
        pagina.update()
        
    botao_enviar =  ft.ElevatedButton("Enviar", on_click=enviar_menssagem)
    
    def entrar_chat(evento):
        # feche o popup
        popup.open = False
        # tirar o botao  "Iniciar chat" da tela
        pagina.remove(botao_inicar)
        # adicionar chat
        pagina.add(chat)
        # criar campo de enviar menssagem
        linha_menssagem = ft.Row(
            [campo_msg, botao_enviar]
        )
        pagina.add(linha_menssagem)
        # botao de enviar menssagem
        pagina.add(botao_enviar)
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)

        pagina.update()
    
    popup = ft.AlertDialog(
        open = False, 
        modal = True, 
        title = ft.Text("Bem vindo ao Chat Felipe"),
        content = nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat) ]
    )
    
    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    botao_inicar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    
    pagina.add(texto)
    pagina.add(botao_inicar)

# ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)