times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico - PR',
        'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
        'Bahia', 'Vasco da Gama', 'Atletico-MG', 'Fluminense', 'Botafogo',
        'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print(f'Os cinco primerios colocados são: {times[:5]}')
print(f'Os times na zona de rebaixamento são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
chape = times.index('Chapecoense') + 1
print(f'O time da Chape está na {chape}ª posição.')