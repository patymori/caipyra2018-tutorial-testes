def formatar_nome_de_autor(nome_completo):
    nao_sobrenomes = ['FILHO', 'FILHA', 'NETO', 'NETA', 'SOBRINHO', 'SOBRINHA',
                      'JÚNIOR', 'JUNIOR']
    partes = nome_completo.split(' ')
    q_partes = len(partes)
    sobrenome = partes[-1].upper()
    nome = partes[:-1]
    if q_partes == 1:
        return sobrenome
    if sobrenome in nao_sobrenomes and q_partes > 2:
        sobrenome = ' '.join(partes[-2:]).upper()
        nome = partes[:-2]
    return sobrenome + ', ' + ' '.join(nome)
