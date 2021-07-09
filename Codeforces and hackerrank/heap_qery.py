
def heapify(index):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < len(heap) and heap[left] < heap[smallest]:
        smallest = left
    if right < len(heap) and heap[right] < heap[smallest]:
        smallest = right

    if smallest != index:
        heap[index], heap[smallest] = heap[smallest], heap[index]
        heapify(smallest)


def createHeap():
    mid = len(heap) // 2
    for i in range(mid, -1, -1):
        heapify(i)


heap = []
for _ in range(int(input())):
    query = input().split(' ')

    if query[0] == '1':
        heap.append(int(query[1]))
        createHeap()

    elif query[0] == '2':
        try:
            heap.remove(int(query[1]))
            createHeap()
        except:
            pass


    else:
        print(heap[0])