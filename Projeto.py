##### Legalmente existem diversos tipos de veículos, no entanto, para o contexto do problema, só se enquadram 6 deles
veiculos = list()
coimas = list()

##### Restaurar dados anteriores
pedido = input ("Pretende restaurar dados de uma utilização anterior (sim/não)?\n")
pedido = pedido.lower()
while pedido != "sim" and pedido != "não":
    pedido = input ("Resposta inválida. Pretende restaurar dados de uma utilização anterior (sim/não)?\n")
    pedido = pedido.lower()

if pedido == "sim":
    fich = input ("Qual o nome do ficheiro que pretende abrir (com extensão)?\n")
##### COMPLETAR

##### Menu principal
while True:
    ver = 0
    quantidade_por_veiculo = 0
    quantidade_por_gravidade = 0
    print ("" , "MENU PRINCIPAL" , "  Gestão de Viaturas (V)" , "  Gestão de Coimas (C)" , "  Guardar dados (G)" , "  Sair (S)" , sep = "\n")
    escolha_principal = input ("Escolha uma opção: ")
    escolha_principal = escolha_principal.lower()
    while escolha_principal != "v" and escolha_principal != "c" and escolha_principal != "g" and escolha_principal != "s":
        escolha_principal = input ("Opção inválida. Escolha uma opção: ")
        escolha_principal = escolha_principal.lower()
    
    ##### Menu gestão de viaturas
    if escolha_principal == "v":
        print ("" , "GESTÃO DE VIATURAS" , "  Adicionar nova viatura (A)" , "  Consultar viaturas (C)" , "  Eliminar viaturas (E)" , "  Voltar atrás (V)" , sep = "\n")
        escolha_viatura = input ("Escolha uma opção: ")
        escolha_viatura = escolha_viatura.lower()
        while escolha_viatura != "a" and escolha_viatura != "c" and escolha_viatura != "e" and escolha_viatura != "v":
            escolha_viatura = input ("Opção inválida. Escolha uma opção: ")
            escolha_viatura = escolha_viatura.lower()

        # Adicionar uma nova viatura
        if escolha_viatura == "a":
            while escolha_viatura == "a":
                print ("")
                matr = input ("Insira a matrícula do veículo: ")
                marca = input ("Insira a marca do veículo: ")
                mod = input ("Insira o modelo do veículo: ")
                print ("Insira o tipo de veículo dentre as seguintes opções." , "Ligeiro de passageiros (LP)" , "Ligeiro de mercadorias (LM)" , "Pesado de mercadorias (PM)" , sep = "\n")
                tipo_veic = input ()
                tipo_veic = tipo_veic.lower()
                while tipo_veic != "lp" and tipo_veic != "lm" and tipo_veic != "pm":
                    print ("Resposta inválida. Insira o tipo de veículo entre as seguintes opções." , "Ligeiro de passageiros (LP)" , "Ligeiro de mercadorias (LM)" , "Pesado de mercadorias (PM)" , sep = "\n")
                    tipo_veic = input ()
                    tipo_veic = tipo_veic.lower()
                v = {"matricula":matr , "marca":marca , "modelo":mod , "tipo de veiculo":tipo_veic}
                veiculos.append(v)
                ## veiculos.append({"matricula":matr , "marca":marca , "modelo":mod , "tipo de veiculo":tipo_veic})
                print (veiculos)

                adicionar_outra = input ("Pretende adicionar outra viatura (sim/não)? ")
                adicionar_outra = adicionar_outra.lower()
                while adicionar_outra != "sim" and adicionar_outra != "não":
                    adicionar_outra = input ("Opção inválida. Digite sim ou não. ")
                    adicionar_outra = adicionar_outra.lower()
                if adicionar_outra == "não":
                    escolha_viatura = ""
        
        # Consultar viaturas
        if escolha_viatura == "c":
            print ("" , "Consulta de viaturas" , "  Todas as viaturas (T)" , "  Por matrícula (M)" , sep = "\n")
            consulta_viatura = input ("Escolha uma opção: ")
            consulta_viatura = consulta_viatura.lower()
            while consulta_viatura != "t" and consulta_viatura != "m":
                consulta_viatura = input ("Opção inválida. Escolha uma opção: ")
                consulta_viatura = consulta_viatura.lower()
            if consulta_viatura == "t":
                for x in range(len(veiculos)):
                    print ("\nMatrícula: " , veiculos[x]["matricula"] , "\nMarca: " , veiculos[x]["marca"] , "\nModelo" , veiculos[x]["modelo"] , "\nTipo de veículo: " , veiculos[x]["tipo de veiculo"] , sep = "")
            if consulta_viatura == "m":
                matr = input ("Insira a matrícula a procurar: ")
                for x in range(len(veiculos)):
                    if matr == veiculos[x]["matricula"]:
                        print ("\nMatrícula: " , veiculos[x]["matricula"] , "\nMarca: " , veiculos[x]["marca"] , "\nModelo: " , veiculos[x]["modelo"] , "\nTipo de veículo: " , veiculos[x]["tipo de veiculo"] , sep = "")
                        ver = 1
                if ver != 1:
                    print ("\nNão foi encontrada nenhuma viatura com a matrícula indicada.")
        
        # Eliminar viaturas
        if escolha_viatura == "e":
            matr = input ("Insira a matrícula da viatura a eliminar: ")
            for x in range(len(veiculos)):
                if matr == veiculos[x]["matricula"]:
                    veiculos.pop(x)
                    print ("\nViatura eliminada com sucesso.")
                    ver = 1
            if ver != 1:
                print ("\nNão foi encontrada nenhuma viatura com a matrícula indicada.")

        # Voltar atrás
        if escolha_viatura == "v":
            continue
    
    ##### Menu gestão de coimas
    if escolha_principal == "c":
        print ("" , "GESTÃO DE COIMAS" , "  Adicionar nova coima (A)" , "  Consultar coimas (C)" , "  Eliminar coimas (E)" , "  Voltar atrás (V)" , sep = "\n")
        escolha_coima = input ("Escolha uma opção: ")
        escolha_coima = escolha_coima.lower()
        while escolha_coima != "a" and escolha_coima != "c" and escolha_coima != "e" and escolha_coima != "v":
            escolha_coima = input ("Opção inválida. Escolha uma opção: ")
            escolha_coima = escolha_coima.lower()
        
        # Adicionar uma nova coima
        if escolha_coima == "a":
            print ("")
            data = input ("Insira a data da infração: ")
            hora = input ("Insira a hora da infração: ")
            idc = input ("Insira o ID da coima: ")
            matr = input ("Insira a matrícula do veículo multado: ")
            
            nome_estr = input ("Insira o nome da estrada: ")
            print ("Insira o tipo de estrada entre as seguintes opções." , "  Dentro da localidade(L)" , "  Fora da localidade(F)" , "  Vias reservadas(R)" , "  Auto-estradas(A)" , sep = "\n")
            tipo_estr = input ()
            tipo_estr = tipo_estr.lower()
            while tipo_estr != "l" and tipo_estr != "f" and tipo_estr != "r" and tipo_estr != "a":
                print ("Opção inválida. Insira o tipo de estrada entre as seguintes opções." , "  Dentro da localidade(L)" , "  Fora da localidade(F)" , "  Vias reservadas(R)" , "  Auto-estradas(A)" , sep = "\n")
                tipo_estr = input ()
                tipo_estr = tipo_estr.lower()
            
            print ("Insira o tipo de veículo dentre as seguintes opções." , "  Ligeiro de passageiros (LP)" , "  Ligeiro de mercadorias (LM)" , "  Pesado de mercadorias (PM)" , sep = "\n")
            tipo_veic = input ()
            tipo_veic = tipo_veic.lower()
            while tipo_veic != "lp" and tipo_veic != "lm" and tipo_veic != "pm":
                print ("Opção inválida. Insira o tipo de veículo entre as seguintes opções." , "  Ligeiro de passageiros (LP)" , "  Ligeiro de mercadorias (LM)" , "  Pesado de mercadorias (PM)" , sep = "\n")
                tipo_veic = input ()
                tipo_veic = tipo_veic.lower()
            
            if tipo_estr == "l":
                lim_vel = 50
            if tipo_estr == "f":
                if tipo_veic == "lp":
                    lim_vel = 90
                if tipo_veic == "lm" or tipo_veic == "pm":
                    lim_vel = 80
            if tipo_estr == "r":
                if tipo_veic == "lp":
                    lim_vel = 100
                if tipo_veic == "lm":
                    lim_vel = 90
                if tipo_veic == "pm":
                    lim_vel = 80
            if tipo_estr == "a":
                if tipo_veic == "lp":
                    lim_vel = 120
                if tipo_veic == "lm":
                    lim_vel = 110
                if tipo_veic == "pm":
                    lim_vel = 90
            
            vel_det = float (input ("Insira a velocidade detetada do veículo (km/h): "))
            dif_vel = vel_det-lim_vel
            
            if tipo_veic == "lp" or tipo_veic == "lm":
                if tipo_estr == "l":
                    if dif_vel <= 20:
                        gravidade = "leve"
                    if 20 <= dif_vel < 40:
                        gravidade = "grave"
                    if 40 <= dif_vel < 60:
                        gravidade = "muito grave"
                    if dif_vel >= 60:
                        gravidade = "crime"
                if tipo_estr == "f" or tipo_estr == "r" or tipo_estr == "a":
                    if dif_vel <= 30:
                        gravidade = "leve"
                    if 30 <= dif_vel < 60:
                        gravidade = "grave"
                    if 60 <= dif_vel < 80:
                        gravidade = "muito grave"
                    if dif_vel >= 80:
                        gravidade = "crime"
            if tipo_veic == "pm":
                if tipo_estr == "l":
                    if dif_vel <= 10:
                        gravidade = "leve"
                    if 10 <= dif_vel < 20:
                        gravidade = "grave"
                    if 20 <= dif_vel < 40:
                        gravidade = "muito grave"
                    if dif_vel >= 40:
                        gravidade = "crime"
                if tipo_estr == "f" or tipo_estr == "r" or tipo_estr == "a":
                    if dif_vel <= 20:
                        gravidade = "leve"
                    if 20 <= dif_vel < 40:
                        gravidade = "grave"
                    if 40 <= dif_vel < 60:
                        gravidade = "muito grave"
                    if dif_vel >= 60:
                        gravidade = "crime"

            for x in range(len(coimas)):
                if matr == coimas[x]["matricula"] and ver != 1:
                    if gravidade == "leve":
                        gravidade == "grave"
                        ver = 1
                    if gravidade == "grave":
                        gravidade == "muito grave"
                        ver = 1
                    if gravidade == "muito grave":
                        gravidade == "crime"
                        ver = 1
        
            c = {"data":data , "hora":hora , "idcoima":idc , "matricula":matr , "nomeestrada":nome_estr , "tipoestrada":tipo_estr , "tipoveiculo":tipo_veic , "dvel":dif_vel , "gravidade":gravidade}
            coimas.append(c)

        # Consultar coimas
        if escolha_coima == "c":
            print ("" , "Consulta de coimas" , "  Todas as coimas (T)" , "  Por matrícula (M)" , "  Por ID de coima (I)", "  Por tipo de veículo (V)", "  Por gravidade de coima (C)" , "Mensais em um ano expecífico (A)" , sep = "\n")
            consulta_coima = input ("Escolha uma opção: ")
            consulta_coima = consulta_coima.lower()
            while consulta_coima != "t" and consulta_coima != "m" and consulta_coima != "i" and consulta_coima != "v" and consulta_coima != "c" and consulta_coima != "a":
                consulta_coima = input ("Opção inválida. Escolha uma opção: ")
                consulta_coima = consulta_coima.lower()

            if consulta_coima == "t":
                for x in range(len(coimas)):
                    print ("\nData da coima: " , coimas[x]["data"] , "\nHora da coima: " , coimas[x]["hora"] , "\nID da coima: " , coimas[x]["idcoima"] , "\nMatrícula: " , coimas[x]["matricula"] , "\nNome da estrada: " , coimas[x]["nomeestrada"] , "\nGravidade: " , coimas[x]["gravidade"] , sep = "")

            if consulta_coima == "m":
                matr = input ("Insira a matrícula a procurar: ")
                for x in range(len(coimas)):
                    if matr == coimas[x]["matricula"]:
                        print ("\nData da coima: " , coimas[x]["data"] , "\nHora da coima: " , coimas[x]["hora"] , "\nID da coima: " , coimas[x]["idcoima"] , "\nNome da estrada: " , coimas[x]["nomeestrada"] , "\nGravidade: " , coimas[x]["gravidade"] , sep = "")
                        ver = 1
                if ver != 1:
                    print ("\nNão foi encontrada nenhuma coima com a matrícula indicada.")

            if consulta_coima == "i":
                idc= input("Insira o ID a procurar: ")
                for x in range(len(coimas)):
                    if idc == coimas[x]["idcoima"]:
                        print ("\nData da coima: " , coimas[x]["data"] , "\nHora da coima: " , coimas[x]["hora"] , "\nMatrícula: " , coimas[x]["matricula"] , "\nNome da estrada: " , coimas[x]["nomeestrada"] , "\nGravidade: " , coimas[x]["gravidade"] , sep = "")
                        ver = 1
                if ver != 1:
                    print ("\nNão foi encontrada nenhuma coima com o ID indicado.")

            if consulta_coima == "v":
                tipo_veic= input ("Insira o tipo de veículo: ")
                tipo_veic = tipo_veic.lower()
                while tipo_veic != "lp" and tipo_veic != "lm" and tipo_veic != "pm":
                    print ("Resposta inválida. Insira o tipo de veículo entre as seguintes opções." , "  Ligeiro de passageiros (LP)" , "  Ligeiro de mercadorias (LM)" , "  Pesado de mercadorias (PM)" , sep = "\n")
                    tipo_veic = input ()
                    tipo_veic = tipo_veic.lower()
                print ("" , "  Lista (L)" , "  Quantidade (Q)" , sep = "\n")
                escolha_consulta_veiculo = input ("Escolha uma opção: ")
                escolha_consulta_veiculo = escolha_consulta_veiculo.lower()
                while escolha_consulta_veiculo != "l" and escolha_consulta_veiculo != "q":
                    escolha_consulta_veiculo = input ("Opção inválida. Escolha uma opção: ")
                    escolha_consulta_veiculo = escolha_consulta_veiculo.lower()
                if escolha_consulta_veiculo == "l":
                    for x in range(len(coimas)):
                        if tipo_veic == coimas[x]["tipoveiculo"]:
                            print ("\nData da coima: " , coimas[x]["data"] , "\nHora da coima: " , coimas[x]["hora"] , "\nID da coima: " , coimas[x]["idcoima"] , "\nNome da estrada: " , coimas[x]["nomeestrada"] , "\nMatrícula: " , coimas[x]["matricula"] , "\nGravidade: " , coimas[x]["gravidade"] , sep = "")
                            ver = 1
                    if ver != 1:
                        print ("\nNão foi encontrada nenhuma coima com o tipo de veículo indicado.")
                if escolha_consulta_veiculo == "q":
                    for x in range(len(coimas)):
                        if tipo_veic == coimas[x]["tipoveiculo"]:
                            quantidade_por_veiculo += 1
                            ver = 1
                    if ver == 1:
                        print ("\nHá" , quantidade_por_veiculo , "coimas associadas ao tipo de veículo indicado.")
                    if ver != 1:
                        print ("\nNão foi encontrada nenhuma coima com o tipo de veículo indicado.")

            if consulta_coima == "c":
                print ("" , "  Leve (L)" , "  Grave (G)" , "  Muito Grave (MG)" , "Crime (C)" , sep = "\n")
                consulta_gravidade = input ("Insira a gravidade a procurar: ")
                consulta_gravidade = consulta_gravidade.lower()
                while consulta_gravidade != "l" and consulta_gravidade != "g" and consulta_gravidade != "mg" and consulta_gravidade != "c":
                    consulta_gravidade = input ("Opção inválida. Insira a gravidade a procurar: ")
                    consulta_gravidade = consulta_gravidade.lower()
                while consulta_gravidade == "l" and consulta_gravidade == "g" and consulta_gravidade == "mg" and consulta_gravidade == "c":
                    if consulta_gravidade == "l":
                        consulta_gravidade == "leve"
                    if consulta_gravidade == "g":
                        consulta_gravidade == "grave"
                    if consulta_gravidade == "mg":
                        consulta_gravidade == "muito grave"
                    if consulta_gravidade == "c":
                        consulta_gravidade == "crime"
                print ("" , "  Lista (L)" , "  Quantidade (Q)" , sep = "\n")
                escolha_consulta_gravidade = input ("Escolha uma opção: ")
                escolha_consulta_gravidade = escolha_consulta_gravidade.lower()
                while escolha_consulta_gravidade != "l" and escolha_consulta_gravidade != "q":
                    escolha_consulta_gravidade = input ("Opção inválida. Escolha uma opção: ")
                    escolha_consulta_gravidade = escolha_consulta_gravidade.lower()
                if escolha_consulta_gravidade == "l":
                    for x in range(len(coimas)):
                        if gravidade == coimas[x]["gravidade"]:
                            print ("\nData da coima: " , coimas[x]["data"] , "\nHora da coima: " , coimas[x]["hora"] , "\nID da coima: " , coimas[x]["idcoima"] , "\nNome da estrada: " , coimas[x]["nomeestrada"] , "\nMatrícula: " , coimas[x]["matricula"] , "\nGravidade: " , coimas[x]["gravidade"] , sep = "")
                            ver = 1
                    if ver != 1:
                        print ("\nNão foi encontrada nenhuma coima com a gravidade indicada.")
                if escolha_consulta_gravidade == "q":
                    for x in range(len(coimas)):
                        if gravidade == coimas[x]["gravidade"]:
                            quantidade_por_gravidade += 1
                            ver = 1
                    if ver == 1:
                        print ("\nHá" , quantidade_por_gravidade , "coimas associadas à gravidade indicada.")
                    if ver != 1:
                        print ("\nNão foi encontrada nenhuma coima com a gravidade indicada.")
            
            if consulta_coima == "a":
                ano = int ("Insira o ano a apresentar: ")

        # Opção Eliminar
        if escolha_coima == "e":
            print ("" , "Consulta de coimas" , "  Por matrícula (M)" , "  Por ID de coima (I)" , sep = "\n")
            eliminar_coima = input ("Escolha uma opção: ")
            eliminar_coima = eliminar_coima.lower()
            while eliminar_coima != "m" and eliminar_coima != "i":
                eliminar_coima = input ("Escolha uma opção: ")
                eliminar_coima = eliminar_coima.lower()

                matr = input ("Insira a matrícula associada à coima a eliminar: ")
        
        # Voltar atrás
        if escolha_coima == "v":
            continue
    
    ##### Opção Guardar
    #if escolha_principal == "g":


    ##### Opção sair
    if escolha_principal == "s":
        break