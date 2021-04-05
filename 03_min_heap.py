def min_heapify(heap, index):
  left = 2 * index + 1
  right = 2 * index + 2

  length = len(heap) - 1
  
  smallest = index

  if left <= length and heap[index] > heap[left]:
      smallest = left
  if right <= length and heap[smallest] > heap[right]:
      smallest = right
  if smallest != index:
      heap[index], heap[smallest] = heap[smallest], heap[index]
      min_heapify(heap, smallest)

def build_min_heap(heap):

  for x in reversed(range(len(heap)//2)):
      min_heapify(heap, x)
  return heap


vetor = [5,6,8,3,7,9]

build_min_heap(vetor)

print(vetor)
