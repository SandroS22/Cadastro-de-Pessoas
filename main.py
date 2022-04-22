from subclasses import Aluno, Funcionario
from pessoa import Pessoa
pessoas = list()
while True:
    print('1. Inserir\n'
          '2. Consultar\n'
          '3. Alterar\n'
          '4. Excluir\n'
          '5. Sair')
    escolhaMenu1 = int(input('Operação: '))
    if escolhaMenu1 == 1:  # Criação de um novo cadastro
        print('Novo cadastro\n'
              '1. Pessooa\n'
              '2. Aluno\n'
              '3. Funcionário')
        selecaoTipoPessoa = int(input('Qual tipo? '))
        if selecaoTipoPessoa == 1:  # Vai inserir uma pessoa genérica na lista
            nome = input('Nome:')
            cpf = int(input('CPF:'))
            p = Pessoa('', '')
            p.set_nome(nome)
            p.set_cpf(cpf)
            pessoas.append(p)
        elif selecaoTipoPessoa == 2:  # Vai inserir um aluno na lista
            nome = input('Nome:')
            cpf = int(input('CPF:'))
            matricula = int(input('Matrícula: '))
            curso = input('Curso: ')
            a = Aluno('', '', '', '')
            a.set_nome(nome)
            a.set_cpf(cpf)
            a.set_matricula(matricula)
            a.set_curso(curso)
            pessoas.append(a)
        elif selecaoTipoPessoa == 3:  # Vai inserir um Funcionário na lista
            nome = input('Nome:')
            cpf = int(input('CPF:'))
            idf = int(input('ID: '))
            f = Funcionario('', '', '')
            f.set_nome(nome)
            f.set_cpf(cpf)
            f.set_idf(idf)
            pessoas.append(f)
    elif escolhaMenu1 == 2:  # Consulta na lista
        print('1. Pessoa\n'
              '2. Aluno\n'
              '3. Funcionário')
        selecaoTipoPessoa = int(input('Operação: '))
        print('Meios de consulta\n'
              '1. Nome\n'
              '2. CPF\n'
              '3. Matricula\n'
              '4. ID')
        selecaoConsulta = int(input('Como deseja consultar? '))
        if selecaoTipoPessoa == 1:  # Consulta de pessoa genérica
            if selecaoConsulta == 1:  # Consultando pessoa genérica por nome
                consultaNome = input('Nome: ')
                for pes in pessoas:
                    if consultaNome == pes.get_nome():
                        print('Nome:', pes.get_nome())
                        print('CPF:', pes.get_cpf())
                    else:
                        print('Não há pessoas cadastradas com esse nome')
            elif selecaoConsulta == 2:  # Consultando pessoa genérica por CPF
                consultaCpf = int(input('CPF: '))
                for pes in pessoas:
                    if consultaCpf == pes.get_cpf():
                        print('Nome:', pes.get_nome())
                        print('CPF:', pes.get_cpf())
                    else:
                        print('Não há pessoas cadastradas com esse CPF')
            elif selecaoConsulta == 3:  # Se selecioar  a consulta por matrícula para uma pessoa genérica
                print('Está pessoa não é um aluno')
            elif selecaoConsulta == 4:  # Se selecionar a consulta por ID para uma pesoa genérica
                print('Está pessoa não é um funcionário')
        elif selecaoTipoPessoa == 2:  # Consulta de aluno
            if selecaoConsulta == 1:  # Consulta de aluno por nome
                consultaNome = input('Nome: ')
                for pes in pessoas:
                    if consultaNome == pes.get_nome():
                        print('Nome:', pes.get_nome())
                        print('CPF:', pes.get_cpf())
                        print('Matricula:', pes.get_matricula())
                    else:
                        print('Não há pessoas cadastradas com esse nome')
            elif selecaoConsulta == 2:  # Consulta de aluno por CPF
                consultaCpf = int(input('CPF: '))
                for pes in pessoas:
                    if consultaCpf == pes.get_cpf():
                        print('Nome:', pes.get_nome())
                        print('CPF:', pes.get_cpf())
                        print('Matricula:', pes.get_matricula())
                    else:
                        print('Não há pessoas cadastradas com esse nome')
            elif selecaoConsulta == 3:  # Consulta de aluno por matrícula
                consultaMatricula = input('Matrícula: ')
                for pes in pessoas:
                    if consultaMatricula == pes.get_matricula():
                        print('Nome:', pes.get_nome())
                        print('CPF:', pes.get_cpf())
                        print('Matricula:', pes.get_matricula())
                    else:
                        print('Não há pessoas cadastradas com essa matrícula')
            elif selecaoConsulta == 4:  # Se selecionar a consulta de ID para um aluno
                print('Está pessoa não é um funcionário')
        elif selecaoTipoPessoa == 3:  # Consulta de funcionário
            if selecaoConsulta == 1:  # Consulta de funcionário por nome
                consultaNome = input('Nome: ')
                for pes in pessoas:
                    if consultaNome == pes.get_nome():
                        print('Nome:', pes.get_nome())
                        print('CPF:', pes.get_cpf())
                        print('ID:'), pes.get_idf()
                    else:
                        print('Não há pessoas cadastradas com esse nome')
            elif selecaoConsulta == 2:  # Consulta de funcionário por CPF
                for pes in pessoas:
                    consultaCpf = int(input('CPF: '))
                    if consultaCpf == pes.get_cpf():
                        print('Nome:', pes.get_nome())
                        print('CPF:', pes.get_cpf())
                        print('ID', pes.get_idf())
                    else:
                        print('Não há pessoas cadastradas com esse CPF')
            elif selecaoConsulta == 3:  # Se selecionar a consulta por matrícula para o funcionário
                print('Está pessoa não é um aluno')
            elif selecaoConsulta == 4:
                consultaId = int(input('ID: '))
                for pes in pessoas:
                    if consultaId == pes.get_idf():
                        print('Nome:', pes.get_nome())
                        print('CPF:', pes.get_cpf())
                        print('ID:'), pes.get_idf()
                    else:
                        print('Não há pessoas cadastradas com esse ID')
    elif escolhaMenu1 == 3:  # Alteração de dados
        pessoaAlteracao = int(input('Digite o CPF de quem deseja fazer alterações: '))
        print('De que tipo é está pessoa?\n'
              '1. Pessoa\n'
              '2. Aluno\n'
              '3. Funcionário')
        selecaoTipoPessoa = int(input('Resposta: '))
        for p in pessoas:
            if pessoaAlteracao == p.get_cpf():
                if selecaoTipoPessoa == 1:  # Alteração de dados de uma pessoa genérica
                    print('1. Alterar nome\n'
                          '2. Alterar CPF\n')
                    escolhaAlteracao = int(input('O que deseja alterar? '))
                    if escolhaAlteracao == 1:
                        nome = input('Insira o novo nome: ')
                        p.set_nome(nome)
                    elif escolhaAlteracao == 2:
                        cpf = int(input('Insira o novo CPF: '))
                        p.set_cpf(cpf)
                elif selecaoTipoPessoa == 2:  # Alteração de dados de um aluno
                    print('1. Alterar nome\n'       
                          '2. Alterar CPF\n'
                          '3. Alterar matrícula\n'
                          '4. Alterar curso')
                    escolhaAlteracao = int(input('O que deseja alterar? '))
                    if escolhaAlteracao == 1:
                        nome = input('Insira o novo nome: ')
                        p.set_nome(nome)
                    elif escolhaAlteracao == 2:
                        cpf = int(input('Insira o novo CPF: '))
                        p.set_cpf(cpf)
                    elif escolhaAlteracao == 3:
                        matricula = int(input('Insira a nova matricula'))
                        p.set_matricula(matricula)
                    elif escolhaAlteracao == 4:
                        curso = input('Insira novo curso')
                        p.set_curso(curso)
                elif selecaoTipoPessoa == 3:  # Alteração de dados de um funcionráo
                    print('1. Alterar nome\n'
                          '2. Alterar CPF\n'
                          '3. Alterar ID')
                    escolhaAlteracao = int(input('O que deseja alterar? '))
                    if escolhaAlteracao == 1:
                        nome = input('Insira o novo nome: ')
                        p.set_nome(nome)
                    elif escolhaAlteracao == 2:
                        cpf = int(input('Insira o novo CPF: '))
                        p.set_cpf(cpf)
                    elif escolhaAlteracao == 3:
                        idf = int(input('Insira o novo ID: '))
                        p.set_idf(idf)
            else:
                print('Não há pessoas cadastradas com esse CPF')
    elif escolhaMenu1 == 4:  # Exclusão de alguém na lista
        cpf = int(input('Insira o CPF de quem deseja excluir: '))
        for i, j in enumerate(pessoas):  # Percorre a lista de pessoas
            if cpf == j.get_cpf():
                pessoas.pop(i)
                print("Exclusão efetuada com sucesso!")
            else:
                print('Não há pessoas cadastradas com esse CPF')
