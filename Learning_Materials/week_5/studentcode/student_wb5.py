# DO NOT change anything except within the function
from approvedimports import *

def cluster_and_visualise(datafile_name:str, K:int, feature_names:list):
    """Function to get the data from a file, perform K-means clustering and produce a visualisation of results.

    Parameters
        ----------
        datafile_name: str
            path to data file

        K: int
            number of clusters to use
        
        feature_names: list
            list of feature names

        Returns
        ---------
        fig: matplotlib.figure.Figure
            the figure object for the plot
        
        axs: matplotlib.axes.Axes
            the axes object for the plot
    """
    # ====> insert your code below here

    # 1. get the data from file into a numpy array
    data = np.genfromtxt(datafile_name, delimiter=',', skip_header=1)

    # 2. create a K-Means cluster model with the specified number of clusters
    kmeans = KMeans(n_clusters=K)
    cluster_labels = kmeans.fit_predict(data)

    # 3. create a canvas(fig) and axes to hold your visualisation
    num_features = data.shape[1]
    fig, axs = plt.subplots(nrows=num_features, ncols=num_features, figsize=(10, 10))
    fig.suptitle(f'Visualisation of {K} clusters by your-username', fontsize=16)

    # 4. make the scatter plot matrix with colour-coded clusters
    for i in range(num_features):
        for j in range(num_features):
            ax = axs[i, j]
            if i == j:
                ax.hist(data[:, i], bins=15, color='gray', edgecolor='black')
            else:
                for cluster in range(K):
                    cluster_points = data[cluster_labels == cluster]
                    ax.scatter(cluster_points[:, j], cluster_points[:, i], label=f"Cluster {cluster}", alpha=0.6)

            if i == num_features - 1:
                ax.set_xlabel(feature_names[j])
            if j == 0:
                ax.set_ylabel(feature_names[i])

    # Optional: only add legend to the top-right subplot
    axs[0, -1].legend(loc='upper left', bbox_to_anchor=(1, 1))

    # 5. save it to file as specified
    plt.tight_layout()
    plt.savefig("myVisualisation.jpg", bbox_inches='tight')

    return fig, axs
    # <==== insert your code above here
