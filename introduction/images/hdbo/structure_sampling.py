import pandas as pd

iter = 1000

C_arr = {}
Ns = [50, 100, 200]
name = [ f'$\\nsamples={N}$' for N in Ns]

for C in [4, 8, 16]:
    C_arr[C] = []
    for N in Ns:
        C_arr[C].append(iter / C * N)
        
df = pd.DataFrame(dict(
    name=name,
    C4=C_arr[4],
    C8=C_arr[8],
    C16=C_arr[16],
))

print(df.to_latex(index=False, float_format="{:.0f}".format, header=['', '$C=4$', '$C=8$', '$C=16$']))