import numpy as np


def paddown(array, value):
    if value == 0:
        return array
    elif value > 0:
        return padup(array, value)
    return np.pad(
        array, ((0, -value), (0, 0)), mode="constant", constant_values=np.nan
    )[-value:, :]


def padup(array, value):
    if value == 0:
        return array
    elif value < 0:
        return paddown(array, value)
    return np.pad(array, ((value, 0), (0, 0)), mode="constant", constant_values=np.nan)[
        :-value, :
    ]


def padright(array, value):
    if value == 0:
        return array
    elif value < 0:
        return padleft(array, value)
    return np.pad(array, ((0, 0), (value, 0)), mode="constant", constant_values=np.nan)[
        :, :-value
    ]


def padleft(array, value):
    if value == 0:
        return array
    elif value > 0:
        return padright(array, value)
    return np.pad(
        array, ((0, 0), (0, -value)), mode="constant", constant_values=np.nan
    )[:, -value:]


def meanDifferencefDistance(arrayList):
    """Takes a mean value from all the dots situated at a certain distance"""
    dfD = DifferencefDistance(arrayList)
    changeIndex = np.append(
        np.concatenate(([0], np.where(np.diff(dfD[:, 0]))[0] + 1)), -1
    )
    return np.array(
        [
            (dfD[changeIndex[i], 0], dfD[changeIndex[i] : changeIndex[i + 1], 1].mean())
            for i in range(len(changeIndex) - 1)
        ]
    )


def calculateDifferences(array, distance):
    """takes distance (x,y) and returns (padded array, distance) removes nan also from the retturned ravelised array"""
    paddedarray = (array - padup(padright(array, distance[0]), distance[1])).ravel()
    paddedarray = paddedarray[~np.isnan(paddedarray)]
    return (paddedarray, np.sqrt(distance[0] ** 2 + distance[1] ** 2))


def DifferencefDistance(arrayList):
    """From a phase mask, returns the square of all possible phase difference on the arrays."""
    differencesfDistance = []
    for phase_map in arrayList:
        for x in range(-phase_map.shape[0] + 1, phase_map.shape[0]):
            for y in range(0, phase_map.shape[0]):
                if np.sign(x) + np.sign(y) >= 0 and not x == y == 0:
                    temp_diff = calculateDifferences(phase_map, (x, y))
                    temp_distances = np.linspace(
                        temp_diff[1], temp_diff[1], len(temp_diff[0])
                    )
                    temp_differences = np.abs(temp_diff[0]) ** 2
                    differencesfDistance.extend(zip(temp_distances, temp_differences))
    return np.array(sorted(differencesfDistance, key=lambda tup: tup[0]))


def structure(arr, d_max=4):
    mdfd = meanDifferencefDistance(arr)
    structureFunction = (mdfd[:, 1])[0:d_max]
    distanceList = (mdfd[:, 0])[0:d_max]
    return distanceList, structureFunction
