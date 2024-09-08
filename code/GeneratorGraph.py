import matplotlib.pyplot as plt
import numpy as np
from result import CalcOfDistancesCartesian3D_results_array, CalcOfDistancesPolar2D_results_array\
    , CalcOfDistancesSphericalThroughTheSphereVolume_results_array, CalcOfDistancesSphericalOnTheSphereSurface_results_array


CalcOfDistancesCartesian3D_results_array_value = sum([row[1] for row in CalcOfDistancesCartesian3D_results_array]) / len([row[1] for row in CalcOfDistancesCartesian3D_results_array])
CalcOfDistancesPolar2D_results_array_value = sum([row[1] for row in CalcOfDistancesPolar2D_results_array]) / len([row[1] for row in CalcOfDistancesPolar2D_results_array])
CalcOfDistancesSphericalThroughTheSphereVolume_results_array_value = sum([row[1] for row in CalcOfDistancesSphericalThroughTheSphereVolume_results_array]) / len([row[1] for row in CalcOfDistancesSphericalThroughTheSphereVolume_results_array])
CalcOfDistancesSphericalOnTheSphereSurface_results_array_value = sum([row[1] for row in CalcOfDistancesSphericalOnTheSphereSurface_results_array]) / len([row[1] for row in CalcOfDistancesSphericalOnTheSphereSurface_results_array])



# fig, ax = plt.subplots()
#
# fruits = ['Декартова система', 'Полярна система', "Сферична система через об'єм сфери", 'Сферична система по поверхні сфери']
# counts = [CalcOfDistancesCartesian3D_results_array_value, CalcOfDistancesPolar2D_results_array_value, CalcOfDistancesSphericalThroughTheSphereVolume_results_array_value, CalcOfDistancesSphericalOnTheSphereSurface_results_array_value]
# bar_labels = ['red', 'blue', '_red', 'orange']
# bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
#
# ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
#
# ax.set_ylabel('fruit supply')
# ax.set_title('Fruit supply by kind and color')
#
#
# plt.show()
# data from https://allisonhorst.github.io/palmerpenguins/

species = ('Декартова система', 'Полярна система', "Сферична система через об'єм сфери", 'Сферична система по поверхні сфери')
penguin_means = {'Flipper Length': (CalcOfDistancesCartesian3D_results_array_value, CalcOfDistancesPolar2D_results_array_value, CalcOfDistancesSphericalThroughTheSphereVolume_results_array_value, CalcOfDistancesSphericalOnTheSphereSurface_results_array_value)}

x = np.arange(len(species))  # the label locations
width = 0.5  # the width of the bars
multiplier = 1

fig, ax = plt.subplots()

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Час обчислення (Сек)')
ax.set_title('Розрахунок відстаней у кожній системі координат з масивом 20 000 пар точок')
ax.set_xticks(x + width, species)
# ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 5)

plt.show()