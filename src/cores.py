from random import choices

cores = ['amarelo', 'verde', 'azul', 'vermelho']

membros = ['mão direita', 'mão esquerda', 'pé direito', 'pé esquerdo']

combinas = [f'{m} {c}' for c in cores for m in membros]


print(choices(combinas))
