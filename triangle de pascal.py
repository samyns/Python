nlignes = int(input('combien de lignes ? '))
ligne_1 = [1] + [0]*(nlignes-1)

for i in range(1, nlignes+1):
    globals()[f'ligne_{i+1}'] = [1] + [0]*(nlignes-1)
    print(f"voici la {i} ème ligne : ", *globals()[f'ligne_{i}'])
    for j in range(1, nlignes):
        globals()[f'ligne_{i+1}'][j] = globals()[f'ligne_{i}'][j-1] + globals()[f'ligne_{i}'][j]