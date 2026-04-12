class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        contagem = {}
        for num in nums:
            contagem[num] = contagem.get(num,0) +1
            itens_ordenados = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
            resultado = []
        for i in range(k):
            resultado.append(itens_ordenados[i][0])
            
        return resultado


        