"""Frequência mínima (issue #3)."""


def frequencia_ok(presencas, aulas):
    """Devolve True se o aluno esteve em pelo menos 75% das aulas.

    Exemplos:
        frequencia_ok(24, 32)  ->  True
        frequencia_ok(23, 32)  ->  False
    """
    if aulas <= 0:
        raise ValueError("o número de aulas precisa ser maior que zero")
    return 4 * presencas >= 3 * aulas
