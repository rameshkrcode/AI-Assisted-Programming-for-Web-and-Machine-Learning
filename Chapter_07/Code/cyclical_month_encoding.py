
import numpy as np
df['Month_sin'] = np.sin(2 * np.pi * df['JoinMonth'] / 12)
df['Month_cos'] = np.cos(2 * np.pi * df['JoinMonth'] / 12)
