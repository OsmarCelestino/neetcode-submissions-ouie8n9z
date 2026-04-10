class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}  # Nossa "caderneta" (valor: indice)
    
        for i, num in enumerate(nums):
            complemento = target - num
            
            if complemento in vistos:
                return [vistos[complemento], i] # Retorna o índice do que já vimos e o atual
            
            vistos[num] = i # Guarda o número atual e onde ele está