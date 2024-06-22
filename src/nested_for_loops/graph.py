import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('results.csv')

plt.figure(figsize=(20, 8))
sns.scatterplot(data=df, x='Language', y='Time (seconds)', hue='Method', style='Method', palette='bright', s=100)

plt.yscale('log')

plt.xlabel('')
plt.ylabel('Time (seconds)')
plt.legend(title='Methods', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, which="both", ls="--")
plt.savefig('results.png', bbox_inches='tight', dpi=300)