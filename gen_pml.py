import numpy as np 
import matplotlib.pyplot as plt
from tspn import MIS

def plot_pml(pml_arr, radius=False, size = 5):
    fig = plt.figure(figsize=(5,5))
    ax = fig.gca()
    ax.set_title('PML points')
    points = plt.scatter(pml_arr[:,0], pml_arr[:,1], s=size, c="k")
    ax.add_artist(points)
    if radius == True:
        for i in range(len(pml_arr)):
            circle = plt.Circle((pml_arr[i,0],pml_arr[i,1]), pml_arr[i,2], color="black", fill=False)   
            ax.add_artist(circle)    
    plt.xlim((0,500))
    plt.ylim((0,500))
    plt.show()
    # plt.hold(True)

    

def generate_pml(num_pml, grid_size, plot=False):
    np.random.seed(4)
    pml_arr_loc = np.random.randint(low = 10, high = grid_size[0]-10, size = (num_pml,2))
    # pml_probs = np.random.randint(low =0.1, high = 0.9) 
    pml_arr_rad = np.random.randint(low = 10, high = 30, size = (num_pml,1))
    pml_arr = np.hstack((pml_arr_loc, pml_arr_rad))
    # print(pml_loc)
    if plot==True:
        plot_pml(pml_arr, radius=True)
    return pml_arr

if __name__=="__main__":
    num_pml = (40)
    grid_size = (500, 500)
    pmls = generate_pml(num_pml, grid_size, plot=True)
    rmax = np.max(pmls[:,2])
    pmls_r = np.hstack((pmls[:,0:2], np.array([ pmls.shape[0]*[rmax] ]).reshape(-1,1)))
    pmls_r = MIS(pmls_r)
    plot_pml(pmls_r, radius = True)