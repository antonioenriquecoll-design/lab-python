
#!/usr/bin/env python
# coding: utf-8

import time
import argparse

# ---- CLI args: --value ----
parser = argparse.ArgumentParser(description="Operación de reducción: suma de [0, N)")
parser.add_argument('--value', type=int, default=10**6, help='Número de elementos N')
args = parser.parse_args()
value = args.value

# ---- Python puro ----
def reduc_operation(a: int) -> int:
    """Compute the sum of the numbers in the range [0, a)."""
    x = 0
    for i in range(a):
        x += i
    return x

# ---- Numba opcional ----
try:
    from numba import njit

    @njit
    def reduc_numba(a: int) -> int:
        x = 0
        for i in range(a):
            x += i
        return x

    # warm-up para no contaminar medidas
    _ = reduc_numba(10)
    has_numba = True
except Exception:
    has_numba = False

print(f"[INFO] Ejecutando reducción con N={value}")

# Medición Python puro
t0 = time.time()
suma_py = reduc_operation(value)
t1 = time.time()
print(f"[Python] N={value} sum={suma_py} time={t1 - t0:.6f}s")

# Medición Numba (si disponible)
if has_numba:
    t0 = time.time()
    suma_nj = reduc_numba(value)
    t1 = time.time()
    print(f"[Numba ] N={value} sum={suma_nj} time={t1 - t0:.6f}s")

# Intento de usar %timeit si estamos bajo IPython
try:
    ip = get_ipython()  # type: ignore
    ip.run_line_magic('timeit', f'-r 2 reduc_operation({value})')
except Exception:
    pass

