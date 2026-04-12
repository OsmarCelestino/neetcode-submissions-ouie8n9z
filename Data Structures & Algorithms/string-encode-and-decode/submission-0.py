import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for string in strs:
            encode += f"{len(string)}#{string}"
        return encode
    def decode(self, s: str) -> List[str]:
        resultado = []
        i = 0     
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            tamanho = int(s[i:j])
            palavra = s[j + 1 : j + 1 + tamanho]
            
            resultado.append(palavra)
            i = j + 1 + tamanho
            
        return resultado
