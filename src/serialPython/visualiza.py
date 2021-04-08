# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
#%%
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import pandas as pd
import numpy as np


style.use('fivethirtyeight')

fig = plt.figure(figsize=[50, 10])
ax1 = fig.add_subplot(1, 1, 1)
ax2 = fig.add_subplot(2, 1, 1)

df = pd.read_csv('valores.csv')
df2 = pd.read_csv('valores_1.csv')
print(df.shape)

print(df2.shape)

dfG = df[df['0'].str.contains('#G-C')]
sa = dfG['0'].str.slice_replace(stop=5, repl='     ')
dfG['0'] = sa
dfG.set_index('3')

dfG2 = df2[df2['0'].str.contains('#G-C')]
sa = dfG2['0'].str.slice_replace(stop=5, repl='     ')
dfG2['0'] = sa
dfG2.set_index('3')

dfA = df[df['0'].str.contains('#A-C')]
sb = dfA['0'].str.slice_replace(stop=5, repl='     ')
dfA['0'] = sb
dfA.set_index('3')

dfM = df[df['0'].str.contains('#M-C')]
sc = dfM['0'].str.slice_replace(stop=5, repl='     ')
dfM['0'] = sc
dfM.set_index('3')

print(dfG.head(100))
print(dfG.shape)

ax1.clear()
ax1.plot(dfG['3'], dfG['0'], c='g', label='xG', lineWidth=1)
ax1.plot(dfG['3'], dfG['1'], c='y', label='yG', lineWidth=1)
ax1.plot(dfG['3'], dfG['2'], c='r', label='zG', lineWidth=1)
ax1.legend()

ax2.clear()
ax2.plot(dfG2['3'], dfG2['0'], c='g', label='xG', lineWidth=1)
ax2.plot(dfG2['3'], dfG2['1'], c='y', label='yG', lineWidth=1)
ax2.plot(dfG2['3'], dfG2['2'], c='r', label='zG', lineWidth=1)
ax2.legend()

plt.show()

# df2 = df.shift(-1, axis=0)
# df3 = df2['time'] - df['time']
# df3.dropna(inplace=True)
# media_periodo = df3[0].mean()

# print(f'média dos intervalos de amostragem: {media_periodo} ms')

# F = 1/media_periodo
# print(f'{F} Hz')


#     df = pd.read_csv('valores.csv')
#     print(df.shape)
    
#     # df['x'] = df['x'] + 12
#     # df['y'] = df['y'] + 1
#     # df['z'] = df['z'] - 241

#     ax1.clear()
#     ax1.plot(df['time'], df['x'], c='g', label='eixo x', lineWidth=1)
#     ax1.plot(df['time'], df['y'], c='y', label='eixo y', lineWidth=1)
#     ax1.plot(df['time'], df['z'], c='r', label='eixo z', lineWidth=1)

    # df2 = df.shift(-1, axis=0)
    # df3 = df2['time'] - df['time']
    # df3.dropna(inplace=True)
    # media_periodo = df3[0].mean()

#     print(f'média dos intervalos de amostragem: {media_periodo} ms')

#     F = 1/media_periodo
#     print(f'{F} Hz')


# if __name__ == '__main__':
#     ani = animation.FuncAnimation(fig, animate, interval=0.11)
#     plt.show()


# %%
