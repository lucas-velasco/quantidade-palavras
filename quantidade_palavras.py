
'''Faça uma função definida por quant_palavras(frase) que dada uma frase, retorne o número de palavras da frase.
Considere que a frase pode ter espaços no início e no final.'''

def quant_palavras(frase):
    """A função retorna a quantidade de palavras da frase"""
    p= frase.split(' ')
    return len(p)
