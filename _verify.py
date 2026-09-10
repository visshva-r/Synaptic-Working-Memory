import numpy as np

DIM = 8
VAL = {'RED': 0, 'GREEN': 1, 'BLUE': 2}


def key(name, s):
    e = np.zeros(DIM)
    if name == 'A':
        e[0] = 1.0
        return e
    if name == 'C':
        e[2] = 1.0
        return e
    v = np.zeros(DIM)
    v[0] = s
    v[1] = np.sqrt(max(1e-6, 1 - s * s))
    return v / np.linalg.norm(v)


def val(n):
    v = np.zeros(DIM)
    v[VAL[n]] = 1.0
    return v


def run(stream, s, eta, gamma, probe='A'):
    W = np.zeros((DIM, DIM))
    for kn, vn in stream:
        W = (1 - gamma) * W + eta * np.outer(val(vn), key(kn, s))
    est = W @ key(probe, s)
    return {'RED': est[0], 'GREEN': est[1], 'BLUE': est[2]}


old = [('A', 'RED'), ('B', 'BLUE'), ('C', 'GREEN'), ('A', 'RED')]
new = [('A', 'RED'), ('C', 'GREEN'), ('B', 'BLUE'),
       ('C', 'GREEN'), ('B', 'BLUE'), ('C', 'GREEN')]

for label, stream in [('CURRENT preset', old), ('PROPOSED preset', new)]:
    print('==', label)
    for s in [0.10, 0.30, 0.40, 0.50, 0.72, 0.90]:
        r = run(stream, s, 0.55, 0.08)
        top = max(r, key=r.get)
        share = r[top] / sum(max(0.0, v) for v in r.values())
        flag = 'WRONG' if top != 'RED' else 'right'
        print('  sim=%.2f  RED=%.3f BLUE=%.3f GREEN=%.3f -> %-5s (%s, share %.2f)'
              % (s, r['RED'], r['BLUE'], r['GREEN'], top, flag, share))
    print()

# Where does the RED->BLUE crossover sit, and what actually moves it?
def crossover(eta, gamma, lo=0.0, hi=1.0):
    for _ in range(60):
        mid = (lo + hi) / 2
        r = run(new, mid, eta, gamma)
        if r['BLUE'] > r['RED']:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


print('== crossover similarity (empirical vs closed form u^4/(u^2+1), u = 1-gamma)')
for gamma in [0.00, 0.08, 0.25, 0.40]:
    u = 1 - gamma
    closed = u ** 4 / (u ** 2 + 1)
    for eta in [0.10, 0.55, 1.00]:
        print('  gamma=%.2f eta=%.2f -> empirical %.4f | closed form %.4f'
              % (gamma, eta, crossover(eta, gamma), closed))
print('  note: eta scales both traces equally, so it does NOT move the crossover.')
