# Shannon-Fano coding demo
from collections import Counter

def shannon_fano(symbols, code=''):
    if len(symbols) == 1:
        return {symbols[0][0]: code or '0'}
    total = sum(p for _, p in symbols)
    accum, split = 0.0, 0
    for i, (_, p) in enumerate(symbols):
        accum += p
        if accum >= total/2:
            split = i + 1
            break
    left = shannon_fano(symbols[:split], code + '0')
    right = shannon_fano(symbols[split:], code + '1')
    return {**left, **right}

def average_code_length(codebook, probs):
    return sum(len(codebook[s]) * p for s, p in probs)

if __name__ == '__main__':
    # Example symbol probabilities
    probs = [('A', 0.4), ('B', 0.2), ('C', 0.15), ('D', 0.15), ('E', 0.1)]
    codebook = shannon_fano(probs)
    print('Codebook:', codebook)
    avg_len = average_code_length(codebook, probs)
    print('Average code length:', round(avg_len, 4))
