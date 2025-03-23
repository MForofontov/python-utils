from typing import List, TypeVar, Generic

# Define a generic type variable
T = TypeVar('T')

class BinaryHeap(Generic[T]):
    """
    A Binary Heap data structure.

    Attributes
    ----------
    heap : List[T]
        A list representing the binary heap.
    is_min_heap : bool
        A flag indicating whether it's a min-heap or max-heap.

    Methods
    -------
    insert(value: T) -> None
        Inserts a value into the heap.
    extract() -> T
        Extracts the root value (min or max) from the heap.
    heapify() -> None
        Converts the list into a valid heap.
    """

    def __init__(self, is_min_heap: bool = True) -> None:
        self.heap: List[T] = []
        self.is_min_heap: bool = is_min_heap

    def insert(self, value: T) -> None:
        """
        Inserts a value into the heap.

        Parameters
        ----------
        value : T
            The value to insert into the heap.
        """
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract(self) -> T:
        """
        Extracts the root value (min or max) from the heap.

        Returns
        -------
        T
            The root value of the heap.

        Raises
        ------
        IndexError
            If the heap is empty.
        """
        if len(self.heap) == 0:
            raise IndexError("extract from empty heap")
        root_value = self.heap[0]
        last_value = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_value
            self._heapify_down(0)
        return root_value

    def _heapify_up(self, index: int) -> None:
        """
        Moves the element at the given index up to maintain the heap property.

        Parameters
        ----------
        index : int
            The index of the element to heapify.
        """
        parent = (index - 1) // 2
        while index > 0 and self._compare(self.heap[index], self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index: int) -> None:
        """
        Moves the element at the given index down to maintain the heap property.

        Parameters
        ----------
        index : int
            The index of the element to heapify.
        """
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        smallest_or_largest = index
        if left_child < len(self.heap) and self._compare(self.heap[left_child], self.heap[smallest_or_largest]):
            smallest_or_largest = left_child
        if right_child < len(self.heap) and self._compare(self.heap[right_child], self.heap[smallest_or_largest]):
            smallest_or_largest = right_child
        if smallest_or_largest != index:
            self.heap[index], self.heap[smallest_or_largest] = self.heap[smallest_or_largest], self.heap[index]
            self._heapify_down(smallest_or_largest)

    def _compare(self, a: T, b: T) -> bool:
        """
        Compares two elements based on the heap type (min-heap or max-heap).

        Parameters
        ----------
        a : T
            The first element.
        b : T
            The second element.

        Returns
        -------
        bool
            True if the heap property is satisfied, False otherwise.
        """
        if self.is_min_heap:
            return a < b
        else:
            return a > b
