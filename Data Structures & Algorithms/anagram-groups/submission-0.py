class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lista_final = {}
        for str in strs:
            texto = "".join(sorted(str))
            if texto not in lista_final:
                lista_final[texto] = []
            lista_final[texto].append(str)
        return list(lista_final.values())
            
