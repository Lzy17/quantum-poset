import numpy as np

def tally(arr):
    out = [];
    for index1 in range(0, len(arr)):
        count = 0
        if(arr[index1] == []):
            continue
        for index2 in range(index1, len(arr)):
            if(len(arr[index1]) == len(arr[index2])):
                if(len(arr[index1] != 0)):
                    for item in range(0, len(arr[index1])):
                        if(arr[index1][item] != arr[index2][item]):
                            break
                        arr[index2] = []
                        count = count + 1

        out.append(count)
