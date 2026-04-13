class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tamanho = len(nums)
        direita = [1] * tamanho
        acumulador_direita = 1

        for i in reversed(range(tamanho)):
            direita[i] = acumulador_direita
            acumulador_direita = acumulador_direita * nums[i]

        esquerda = [1] * tamanho
        acumulador_esquerda = 1
        for i in range(tamanho):
            esquerda[i] = acumulador_esquerda
            acumulador_esquerda = acumulador_esquerda * nums[i]
        
        resultado = [1] * tamanho
        for i in range(tamanho):
            resultado[i] = esquerda[i] * direita[i]
            
        return resultado