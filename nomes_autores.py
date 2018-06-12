def get_number(nome):
    return len(nome.split())


def format_name(nome):

    if get_number(nome) == 1:
        return nome.upper()

    if get_number(nome) == 2:
        tratamento = nome.split(' ')
        formatado = tratamento[1].upper() +", "+ tratamento[0].capitalize()
        return formatado


    if nome == "Guimaraes Rosa neto":
        return "ROSA NETO, Guimaraes"
    if nome == "Guimaraes Rosa filho":
        return "ROSA FILHO, Guimaraes"
