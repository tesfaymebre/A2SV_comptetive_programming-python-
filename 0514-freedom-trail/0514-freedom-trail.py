class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        key_len = len(key)
        best_steps = {}

        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        def try_lock(ring_index, key_index):
            if (ring_index, key_index) in best_steps:
                return best_steps[(ring_index, key_index)]

            if key_index == key_len:
                best_steps[(ring_index, key_index)] = 0
                return 0

            min_steps = inf
            for char_index in range(ring_len):
                if ring[char_index] == key[key_index]:
                    min_steps = min(min_steps, 
                                    count_steps(ring_index, char_index)
                                    + 1
                                    + try_lock(char_index, key_index + 1))

            best_steps[(ring_index, key_index)] = min_steps
            return min_steps

        return try_lock(0, 0)