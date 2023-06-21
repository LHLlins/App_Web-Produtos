def write_notification(email:str, mensagem=''):
    with open('log.txt', 'w') as email_file:
        conteudo =f'Email:{email} -{mensagem}'
        email_file.write(conteudo)