
# 1194 - Prefixa, Infixa e Posfixa

def posfixa(prefixo, infixo):
    if not prefixo:
        return []
    raiz = prefixo[0]
    i = infixo.index(raiz)
    esq = posfixa(prefixo[1:i+1], infixo[:i])
    dir = posfixa(prefixo[i+1:], infixo[i+1:])
    return esq + dir + [raiz]

numberOfCases = int(input())

while numberOfCases > 0:
    try:
        str = input()
    except:
        break
    
    arrayStr = str.split()
    length = len(arrayStr)

    preorder = arrayStr[1] if length > 1 else ""
    inorder = arrayStr[2] if length > 1 else ""
    
    postorder = posfixa(preorder, inorder)
    result = ""
    
    for char in postorder:
        result = result + char
    
    print(result)
    
    arrayStr.clear()
    result = ""
    preorder = ""
    inorder = ""
    numberOfCases = numberOfCases - 1
    
   

