import timeit

from CalculateDistanceByBenchmark import CalcOfDistancesCartesian3D, CalcOfDistancesPolar2D\
    , CalcOfDistancesSphericalThroughTheSphereVolume, CalcOfDistancesSphericalOnTheSphereSurface

result_file_path = 'result.py'

# execution_time = timeit.timeit(stmt='CalcOfDistancesCartesian3D(20_000)', globals=globals(), number=1)
# print(f"Функция выполнена за {execution_time:.4f} секунд")

# execution_time = timeit.timeit(stmt='CalcOfDistancesPolar2D(20_000)', globals=globals(), number=1)
# print(f"Функция выполнена за {execution_time:.4f} секунд")

# execution_time = timeit.timeit(stmt='CalcOfDistancesSphericalThroughTheSphereVolume(20_000)', globals=globals(), number=1)
# print(f"Функция выполнена за {execution_time:.4f} секунд")

execution_time = timeit.timeit(stmt='CalcOfDistancesSphericalOnTheSphereSurface(20_000)', globals=globals(), number=1)
print(f"Функция выполнена за {execution_time:.4f} секунд")

results_array_name = 'CalcOfDistancesSphericalOnTheSphereSurface_results_array'
Count = 20000

try:
    with open(result_file_path, 'r') as file:
        file_content = file.read()
        data = {}
        exec(file_content, globals(), data)
except FileNotFoundError:
    data = {}
except Exception as e:
    raise RuntimeError(f"Не удалось прочитать файл: {e}")

if results_array_name not in data:
    data[results_array_name] = []

data[results_array_name].append([Count, execution_time])

with open(result_file_path, 'w') as file:
    for key, value in data.items():
        file.write(f'{key} = {value}\n')