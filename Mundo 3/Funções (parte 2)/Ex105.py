# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai def notas(*nums, sit=False):
def notas(*nums, sit=False):
    """
    Calcula estatísticas com base em notas de alunos.

    Args:
        *nums (float): Uma série de notas dos alunos.
        sit (bool, opcional): Indica se deve calcular a situação do aluno. 
        Se True, a função calculará a situação com base na média. 
        Se False, apenas estatísticas básicas serão calculadas.

    Returns:
        dict: Um dicionário contendo as estatísticas calculadas.
            - 'total': Total de notas fornecidas.
            - 'maior': Maior nota.
            - 'menor': Menor nota.
            - 'média': Média das notas (excluindo a situação, se aplicável).
            - 'situação' (opcional): A situação do aluno (apenas se sit=True).
                Pode ser 'Boa', 'Regular' ou 'Ruim' com base na média.

    Example:
        >>> resp = notas(5.5, 2.5, 10, 6.5, 9, 8, sit=True)
        >>> print(resp)
        {'total': 6, 'maior': 10, 'menor': 2.5, 'média': 6.916666666666667, 'situação': 'Boa'}
    """
    dic = dict()
    dic['total'] = len(nums)
    dic['maior'] = max(nums)
    dic['menor'] = min(nums)
    if sit:
        dic['média'] = sum(nums) / len(nums[:-1])
    else:
        dic['média'] = sum(nums) / len(nums)

    if sit:
        if dic['média'] >= 7:
            dic['situação'] = 'Boa'
        elif dic['média'] >= 5:
            dic['situação'] = 'Regular'
        else:
            dic['situação'] = 'Ruim'

    return dic


resp = notas(5.5, 2.5, 10, 6.5, 9, 8, sit=True)
print(resp)

help(notas)