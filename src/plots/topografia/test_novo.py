from novo import carrega_pontos, Ponto


def test_ponto_deve_ter_número_nome_xyz():
    ponto = Ponto(1, 'Referência', 0.5, 1.0, 1.0)
    esperado = 'número', 'nome', 'x', 'y', 'z'
    for atributo in esperado:
        assert getattr(ponto, atributo)


def test_um_arquivo_com_337_linhas_deve_ter_337_pontos():
    arquivo = 'pontos.txt'
    pontos: set = carrega_pontos(arquivo)
    esperado = 337
    assert len(pontos)
    for ponto in pontos:
        assert isinstance(ponto, Ponto)
