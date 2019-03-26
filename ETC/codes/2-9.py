color = ['하얗고', '까맣고', '빨갛고', '노랗고']
taste = ['달콤한', '짭짤한', '매콤한', '고소한']
food = ['라면', '피자', '치킨', '햄버거']

for c in color:
    for t in taste:
        for f in food:
            print('{} {} {}'.format(c, t, f))
