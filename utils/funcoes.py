# from bradocs4py import CPF, Cnpj


# def mascarar_cpf(cpf: str) -> str:
#     return CPF(cpf)


# def mascarar_cnpj(cnpj: str) -> str:
#     return Cnpj(cnpj)


# def mascarar_cep(cep: str) -> str:
#     return '{}-{}'.format(cep[:5], cep[5:8])


# def mascarar_telefone(numero: str) -> str:
#     numero = numero.replace('-', '')
#     if len(numero) == 8:
#         return '{}-{}'.format(numero[:4], numero[4:8])
#     elif len(numero) == 9:
#         return '{}-{}'.format(numero[:5], numero[5:9])


# def capitalizar_nomes(name: str) -> str:
#     preps = ['da', 'das', 'de', 'di', 'do', 'dos', 'du', 'para', 'com', 'e']
#     items = []
#     for item in name.split():
#         if not item.lower() in preps:
#             item = item.capitalize()
#         else:
#             item = item.lower()
#         items.append(item)
#     return ' '.join(items)
