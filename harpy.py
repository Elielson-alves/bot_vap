#pagina de login operado/admin

print('Olá, somos um progrma de teste, digite o seu user e chave de acesso quando solicitado')


credenciais = {'user01':'pass01','user02':'pass02'}
credenciais_admin = {'admin01':'pass01','admin02':'pass02'}


while True:
    
    login = input ('Digite o login: ')
    password = input('Digite password:')


    if login in credenciais and credenciais [login] == password:
        print('login efetuado com sucesso!')
        break
    
    elif login in credenciais_admin and credenciais_admin [login] == password:
         print('login admin efetuado com sucesso!')
         cadastrar = input('Deseja cadastrar um novo user ?')

         if cadastrar == "sim":
              novo_user = input('Digite o Login: ')
              novo_password = input('Digite o password: ')
              
              credenciais[novo_user] = novo_password
              print(credenciais)
              
              print('Cadastro realizado com sucesso.')
         break
     
    else:
        print('Login ou password não cadastrado na base de dados. ')
    segunda_tentiva = input('Erro de credenciais, deseja tentar novamente?')
    if segunda_tentiva.lower() == 'nao':
        
        continue
    else:
        print('saindo do programa...')
        
        pass

#verifica��o de dois fatores









