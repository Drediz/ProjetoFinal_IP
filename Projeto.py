# Legalmente existem diversos tipos de veículos, no entanto, para o contexto do problema, só se enquadram 6 deles
veiculos = list()

# Restaurar dados anteriores
pedido = input ("Pretende restaurar dados de uma utilização anterior (sim/não)?\n")
pedido = pedido.lower()
while pedido != "sim" and pedido != "não":
    pedido = input ("Resposta inválida. Pretende restaurar dados de uma utilização anterior (sim/não)?\n")

if pedido == "sim":
    fich = input ("Qual o nome do ficheiro que pretende abrir (com extensão)?\n")
### COMPLETAR

# Menu principal
while True:
    print ("" , "MENU PRINCIPAL" , "  Gestão de Viaturas (V)" , "  Gestão de Coimas (C)" , "  Guardar dados (G)" , "  Sair (S)" , sep = "\n")
    escolha_principal = input ("Escolha uma opção: ")
    escolha_principal = escolha_principal.lower()
    while escolha_principal != "v" and escolha_principal != "c" and escolha_principal != "g" and escolha_principal != "s":
        escolha_principal = input ("Opção inválida. Escolha uma opção: ")
        escolha_principal = escolha_principal.lower()
    
    # Menu gestão de viaturas
    if escolha_principal == "v":
        print ("" , "Gestão de viaturas" , "  Adicionar nova viatura (A)" , "  Consultar viaturas (C)" , "  Eliminar viaturas (E)" , "  Voltar atrás (V)" , sep = "\n")
        escolha_viatura = input ("Escolha uma opção: ")
        escolha_viatura = escolha_viatura.lower()
        while escolha_viatura != "a" and escolha_viatura != "c" and escolha_viatura != "e" and escolha_viatura != "v":
            escolha_viatura = input ("Opção inválida. Escolha uma opção: ")
            escolha_viatura = escolha_viatura.lower()

        if escolha_viatura == "a":
            while escolha_viatura == "a":
                print ("")
                matr = input ("Insira a matrícula do veículo: ")
                marca = input ("Insira a marca do veículo: ")
                mod = input ("Insira o modelo do veículo: ")
                tipo_veic = input ("Insira o tipo de veículo: ")
                ##while tipo_veic != 
                v = {"matricula":matr , "marca":marca , "modelo":mod , "tipo de veiculo":tipo_veic}
                veiculos.append(v)
                ## veiculos.append({"matricula":matr , "marca":marca , "modelo":mod , "tipo de veiculo":tipo_veic})

                adicionar_outra = input ("Pretende adicionar outra viatura (sim/não)? ")
                adicionar_outra = adicionar_outra.lower()
                while adicionar_outra != "sim" and adicionar_outra != "não":
                    adicionar_outra = input ("Opção inválida. Digite sim ou não? ")
                    adicionar_outra = adicionar_outra.lower()
                if adicionar_outra == "não":
                    escolha_viatura = ""
        
        if escolha_viatura == "c":
            print ("" , "Consulta de viaturas" , "  Todas as viaturas (T)" , "  Por matrícula (M)" , sep = "\n")
            consulta_viatura = input ("Escolha uma opção: ")
            consulta_viatura = consulta_viatura.lower()
            while consulta_viatura != "t" and consulta_viatura != "m":
                consulta_viatura = input ("Opção inválida. Escolha uma opção: ")
                consulta_viatura = consulta_viatura.lower()
                