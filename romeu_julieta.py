def dizer(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "romeu e julieta"
    if numero % 3 == 0:
        return "queijo"
    if numero % 5 == 0:
        return "goiabada"
    return str(numero)

if __name__ == '__main__':
    assert dizer(1) == "1"
    assert dizer(2) == "2"
    assert dizer(4) == "4"
    assert dizer(3) == "queijo"
    assert dizer(6) == "queijo"
    assert dizer(9) == "queijo"
    assert dizer(5) == "goiabada"
    assert dizer(10) == "goiabada"
    assert dizer(20) == "goiabada"
    assert dizer(15) == "romeu e julieta"
    assert dizer(30) == "romeu e julieta"
    assert dizer(45) == "romeu e julieta"
