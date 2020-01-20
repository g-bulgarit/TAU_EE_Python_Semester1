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
    # Copy original just for giggles...
    diff_matrix = np.copy(data)

    # Diff_mat = original - ROR(1) of itself.
    # Then fix the first column to be zeros.
    diff_matrix -= np.roll(diff_matrix,1)
    diff_matrix[:, 0] = 0
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
import pandas as pd

def read_missions_file(file_name):
    try:
        fp = pd.read_csv(file_name, )
        fp.rename(columns={},
                  index={0:"Temaria", 1:"Redania", 2:"Keadwen", 3:"Cintra"},
                  inplace=True)
        fp.drop(["Kingdom"], axis=1, inplace=True)
        return fp
    except IOError:
        raise IOError("Could not open file.")

def sum_rewards(bounties):
    return bounties["Bounty"].sum() - bounties["Expenses"].sum()

def find_best_kingdom(kingdoms, bounties):
    #       ____________
    #      /\  ________ \
    #     /  \ \______/\ \
    #    / /\ \ \  / /\ \ \
    #   / / /\ \ \/ / /\ \ \    Technically,
    #  / / /__\_\/ / /__\_\ \       A one liner.
    # / /_/_______/ /________\
    # \ \ \______ \ \______  /          Actually,
    #  \ \ \  / /\ \ \  / / /               A mess.
    #   \ \ \/ / /\ \ \/ / /
    #    \ \/ / /__\_\/ / /
    #     \  / /______\/ /
    #      \/___________/

    return bounties.apply(lambda x: (bounties.loc[:, "Bounty"]
                                     - bounties.loc[:, "Expenses"])
                                     /bounties.loc[:, ("Duration")]).idxmax()[0]

#########################################
# Question 3 - do not delete this comment
#########################################
def compute_entropy(img):
    pixel_map = imageio.imread(img)
    entropy = 0

    bin_cnt = np.bincount(pixel_map.flatten())
    for index, value in enumerate(bin_cnt):
        _Pi = bin_cnt[index]/sum(bin_cnt)
        if _Pi != 0:
            entropy += (-_Pi * np.log2(_Pi))
    return entropy

def nearest_enlarge(img, a):
    pixel_map = imageio.imread(img)
    size_x, size_y = (pixel_map.shape)
    newSize_x, newSize_y = (size_x*a, size_y*a)
    container = np.zeros(shape=(newSize_x, newSize_y), dtype=int)
    for row_idx, row in enumerate(container):
        for col_idx, col in enumerate(row):
            container[row_idx][col_idx]  = pixel_map[int(np.floor(row_idx*size_y/newSize_y))][int(np.floor(col_idx*size_x/newSize_x))]
    return container

# ---------------------------------------
# Tests for development:
data, col, row = load_training_data("weight_input.csv")
print(get_highest_weight_loss_trainee(data, col, row))
print(get_diff_data(data, col, row))
print(get_highest_loss_month(data, col, row))
# ------
q = read_missions_file("missions.csv")
print(sum_rewards(q))
print(find_best_kingdom(None, q))
# ------
print(compute_entropy("cameraman.tif"))
I = nearest_enlarge('cameraman.tif', 4)
plt.figure()
plt.imshow(I, cmap= plt.cm.gray)
plt.show()