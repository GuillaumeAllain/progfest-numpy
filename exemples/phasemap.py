import numpy as np
import time
from fastphasemap import structure as faststructure
from slowphasemap import structure as slowstructure


def main(arr):
    tick = time.perf_counter()
    farr = faststructure(arr)
    print("Temps rapide:", time.perf_counter() - tick)
    print("  taille:", len(farr[0]))
    tick = time.perf_counter()
    sarr = slowstructure([arr])
    print("Temps lent:", time.perf_counter() - tick)
    print("  taille:", len(sarr[0]))
    breakpoint()


if __name__ == "__main__":
    phase_map = np.load("image_data_0.npy")
    phase_map[np.nonzero(phase_map == 0)] = np.nan
    main(phase_map[0, 0])
