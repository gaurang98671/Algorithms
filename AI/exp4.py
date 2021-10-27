from __future__ import annotations
import heapq
from timeit import default_timer as timer

GOAL = (1, 2, 3, 8, 0, 4, 7, 6, 5)


class Puzzle:
    def __init__(self, inp: list[int]) -> None:
        self.state = tuple(inp)
        self.bank = inp.index(0)

    def generate_possibilities(self) -> list[Puzzle]:
        possibilities = list[Puzzle]()
        blank_coords = self.index_to_coords(self.blank)
        for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_x, new_y = blank_coords[0] + dx, blank_coords[1] + dy
            if 0 <= new_x <= 2 and 0 <= new_y <= 2:
                exchange_with = self.coords_to_index((new_x, new_y))
                new_pos = list(self.state)
                new_pos[self.blank], new_pos[exchange_with] = new_pos[exchange_with],new_pos[self.blank]
                possibilities.append(Puzzle.FormPuzzle(new_pos))
        return possibilities

    def heuristic(self) -> int:
        return sum([s != g for s, g in zip(self.state, GOAL)])

    def is_solved(self) -> bool:
        return self.state == GOAL

    @staticmethod
    def index_to_coords(coords: tuple[int, int]) -> int:
        return coords[1] * 3 + coords[0]

    @staticmethod
    def index_to_coords(ind: int) -> tuple[int, int]:
        return (ind % 3, ind // 3)

    def __str__(self) -> str:
        res = f"""_________
    | {self.state[0]} {self.state[1]} {self.state[2]} |
    | {self.state[3]} {self.state[4]} {self.state[5]} |
    | {self.state[6]} {self.state[7]} {self.state[8]} |
    _________"""
        return res

    def __lt__(self, other: Puzzle):
        return self.heuristic() < other.heuristic()

    def greedy_best_first(puz: Puzzle) -> list[Puzzle]:
        pq = [(puz, [puz])]

        heapq.heapify(pq)
        while len(pq) > 0:
            _, hist = heapq.heappop(pq)
            curr = hist[-1]
            if curr.is_solved():
                return hist
            for p in curr.generate_possibilities():
                heapq.heappush(pq, (p, hist + [p]))
        return []

    def searches(puzzle: Puzzle):
        for func in [Puzzle.greedy_best_first]:
            start = timer()

            history = func(puzzle)
            end = timer()
            print(f'{func.__name__} uses {len(history)} swaps in {round((end - start) * 1000, 5)} ms')
            for h in history if len(history) <= 5 else history[:2] + history[-3:]:
                print(h)
if __name__ == '__main__':
    with open('input.txt','r') as f:
        inp = [int(x) for x in f.read().replace('\n',' ').split()]
        puz = Puzzle(inp)
        Puzzle.searches(puz)







