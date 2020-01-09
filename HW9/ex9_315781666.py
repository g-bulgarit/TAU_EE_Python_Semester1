''' Exercise #9. Python for Engineers.'''

import numpy as np
import imageio
import matplotlib.pyplot as plt


#########################################
# Question 1 - do not delete this comment
#########################################

def load_training_data(filename):
    with open(filename,'rb') as fp:
        table = np.genfromtxt(fp, delimiter=',', dtype=None, encoding="utf-8")
        data = table[1:,1:]
        row_names = table[0][1:]
        column_names = table[:, 0][1:]

    return data.astype(float), column_names, row_names

def get_highest_weight_loss_trainee(data, column_names, row_names):
    diff_matrix = np.abs(data[:, 0] - data[:, -1])
    return column_names[np.argmax(diff_matrix)]

def get_diff_data(data, column_names, row_names):
    diff_matrix = np.copy(data)
    diff_matrix[:, 0] = 0

    # Used loop here, find another way
    for i in range(1, diff_matrix.shape[1]):
        diff_matrix[:, i] = data[:,i]-data[:,i-1]
    return diff_matrix


def get_highest_loss_month(data, column_names, row_names):
    diff_matrix = get_diff_data(data ,column_names, row_names)
    sum_matrix = sum(diff_matrix[:,:])
    return row_names[np.argmax(np.abs(sum_matrix))]


def get_relative_diff_table(data, column_names, row_names):
    diff_matrix = get_diff_data(data ,column_names, row_names)
    diff_matrix = (diff_matrix[:,1:] - diff_matrix[:,:])/diff_matrix[:,:]
    return diff_matrix



#########################################
# Question 2 - do not delete this comment
#########################################


def read_missions_file(file_name):
    pass


def sum_rewards(bounties):
    pass


def find_best_kingdom(kingdoms, bounties):
    pass


#########################################
# Question 3 - do not delete this comment
#########################################
def compute_entropy(img):
    pixel_map = imageio.imread(img)
    entropy = 0
    bin_cnt = np.bincount(pixel_map.flatten())
    total_cols = sum(bin_cnt)
    print(total_cols)
    for index, value in enumerate(bin_cnt):
        _Pi = bin_cnt[index]/total_cols
        if _Pi != 0:
            entropy += (-_Pi * np.log2(_Pi))


    # for color_value in range(255):
    #     if np.sum(np.bincount(color_value, pixel_map)) != 0:
    #         entropy += np.sum(np.bincount(color_value, pixel_map))
    return entropy

def nearest_enlarge(img, a):
    pass


# Tests for development:
data, col, row = load_training_data("weight_input.csv")
print(get_highest_weight_loss_trainee(data, col, row))
print(get_diff_data(data, col, row))
print(get_highest_loss_month(data, col, row))
# print(get_relative_diff_table(data, col, row))




# ------
print(compute_entropy("cameraman.tif"))