"timeit module is used for measuring time of executing a code"
import timeit

"timeit.timeit(stmt, setup, timer, number)"

x = "[x for x in range(10)]"

print(timeit.timeit(x, number=1))