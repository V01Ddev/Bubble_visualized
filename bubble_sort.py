#!/bin/python3 
from matplotlib import pyplot as plt



def num_in_list(arr):

    num_list = []
    num = 0

    for i in arr:
        num = num + 1 
        num_list.append(num)

    return num_list


def bubble_sort(array):

    array_size = len(array)
    
    no_swap = False


    #for every item in the array - 1
    for i in range(array_size - 1):

        print("-----")
        print(f"current index --> {i}")
        print("-----")

        for j in range(0, array_size - i - 1):

            print(f"the block is being moved to --> {j}")

            if array[j] > array[j+1]:

                temp = array[j]

                array[j] = array[j+1]

                array[j+1] = temp

                no_swap = False


                # DATA VIS
                index = num_in_list(array)
                 
                plt.xticks([])

                plt.title("BUBBLE SORT by v01d.dev")

                plt.xlabel("index")
                plt.ylabel("size")
                
                plt.bar(index, array)
                plt.pause(0.1)
                plt.cla()

    plt.show()



def main():
    

    my_array = [30, 40, 25, 14, 35, 37, 13, 12, 15, 9, 6, 3, 2, 8, 5]

    bubble_sort(my_array)



if __name__ == "__main__":

    main()
