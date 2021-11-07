import pandas as pd
from tabulate import tabulate
caption = {'Radius (in solar radii)':[0.017],'Mass (in solar masses)':[0.5]}
data = pd.DataFrame(caption)
print(tabulate(data,headers='keys',tablefmt='psql'))