from bublesort import bubleSort
def removeElement( nums: list[int], val: int) -> int:
        listaAux = []
        for i in nums:
            if i != val:
                listaAux.append(i)
        bubleSort(listaAux)
        
        return len(listaAux), listaAux

print(removeElement(nums=[0,1,2,2,3,0,4,2], val=2))