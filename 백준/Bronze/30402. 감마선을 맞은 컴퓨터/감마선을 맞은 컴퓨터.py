for _ in range(15):
    pix = list(map(str, input().split()))
    
    if 'w' in pix:
        cat = 'chunbae'
    elif 'b' in pix:
        cat = 'nabi'
    elif 'g' in pix:
        cat = 'yeongcheol'

print(cat)
