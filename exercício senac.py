votos = []
candidatos = []
while True:
    print('bem vindo à urna eletrônica selecione uma opção \n 1.cadastrar candidatos \n 2.votar \n 3. ver resultado \n 4.sair')
    opção = int(input())
    if opção == 1:
         print('digite o nome do/da canditato/a 1')
         candidato1 = input()
         candidatos.append(candidato1)
         print('digite o nome do/da canditato/a 2')
         candidato2 = input()
         candidatos.append(candidato2)
         print('digite o nome do/da canditato/a 3')
         candidato3 = input()
         candidatos.append(candidato3)
         print('candidatos cadastrados com sucesso!!')
    if opção == 2:
         print('escolha quantos votos você quer dar para cada candidato!')
         print(f'digite 1 para o/a candidato/a {candidatos[0]}\n 2 para o/a candidato/a{candidatos[1]}\n 3 para o/a candidato/a{candidatos[2]}')
         print('faça seu primeiro voto')
         for voto in range(0,40):
             escolha = int(input())
             if voto < 39:
                 print('vote novamente')
             else:
                 print('votos computados')
             votos.append(escolha)
    if opção == 3:
         print('aqui está o resuldado das eleições')
         votoscandidato1=votos.count(1)
         votoscandidato2=votos.count(2)
         votoscandidato3=votos.count(3)
         porc1=float(votoscandidato1*2.5)
         porc2=float(votoscandidato2*2.5)
         porc3=float(votoscandidato3*2.5)
         print(f'candidato/a {candidatos[0]} --> {porc1}%\n candidato/a {candidatos[1]} --> {porc2}% \n candidato/a {candidatos[2]} --> {porc3}%')
    if opção == 4:
        break