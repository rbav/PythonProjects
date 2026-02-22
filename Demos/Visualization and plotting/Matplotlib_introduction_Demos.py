# Matplotlib Demos
# 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from colorama import init, Fore, Back, Style
init(autoreset=True)
#__________________Section 1______________________
#Simple plotting example
print(Back.GREEN + "=======SECTION 1=======")

plt.grid(True)
plt.plot(5,5,'o')
plt.ylabel('Y-axis title')
plt.xlabel('X-axis title')
plt.title('Plotting Example')
plt.show()

#__________________Section 1______________________
#plotting a df using NumPy
print(Back.RED + "=======SECTION 2=======")
from matplotlib.ticker import MaxNLocator
a = [[1980, 8880, 5123], [1981, 8670, 6682], [1982, 8147, 3308], [1983, 7338, 1863], [1984, 5704, 1527]]
india_china_df = pd.DataFrame(a, columns=['year', 'India', 'china'] )
india_china_df.set_index('year', inplace=True)
ax = india_china_df.plot(kind='line')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.show()
