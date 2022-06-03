def origem_destino_iguais(origem, destino, lista_de_erros):
    """ Verifica se os campos de Origem e Destino são iguais. """
    if origem == destino :
        lista_de_erros['destino'] = 'Origem e Destino não podem ser iguais.'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """ Verifica se existe algum caracter numérico no campo informado. """
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Nào inclua numeros neste campo.'

def data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros):
    """ Verifica se a Data de Ida é maior a Data de Volta. """
    if data_ida > data_volta :
        lista_de_erros['data_volta'] = 'Data de Volta não pode ser anterior a data de ida.'

def data_ida_menor_data_de_hoje(data_ida, data_pesquisa, lista_de_erros):
    """ Verifica se a Data de Ida é anterior a data da pesquisa. """
    if data_ida < data_pesquisa :
        lista_de_erros['data_ida'] = 'Data de ida não pode ser anterior a data de hoje.'
