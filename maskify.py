def maskify(cc):
    return "*" * (len(cc) - 4) + cc[-4:]


print maskify('1234567891012141')