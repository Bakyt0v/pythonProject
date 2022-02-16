GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
del GeekTech['bag'],
GeekTech['courses'].insert(1, 'GeekCamp')
GeekTech['courses'].append('Fullstack')
GeekTech['address'] = 'Ibraimova 103'
GeekTech['contacts'] = 'call: +996770004630', 'instagramm: geektech__kg'
GeekTech['courses'] = tuple(GeekTech['courses'],)
for k, v in GeekTech.items():
    print(f'{k}: {v}')