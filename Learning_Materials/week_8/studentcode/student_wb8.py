from approvedimports import *

def make_xor_reliability_plot(train_x, train_y):
    """ Insert code below to  complete this cell according to the instructions in the activity descriptor.
    Finally it should return the fig and axs objects of the plots created.

    Parameters:
    -----------
    train_x: numpy.ndarray
        feature values

    train_y: numpy array
        labels

    Returns:
    --------
    fig: matplotlib.figure.Figure
        figure object
    
    ax: matplotlib.axes.Axes
        axis
    """
    
    # ====> insert your code below here

    hidden_layer_width = list(range(1, 11))
    successes = np.zeros(10)
    epochs = np.zeros((10, 10))

    for h_nodes in hidden_layer_width:
        for repetition in range(10):
            xorMLP = MLPClassifier(hidden_layer_sizes=(h_nodes,), max_iter=2000, random_state=repetition)
            xorMLP.fit(train_x, train_y)
            train_pred = xorMLP.predict(train_x)
            acc = (train_pred == train_y).mean()

            if acc == 1.0:
                successes[h_nodes - 1] += 1
                epochs[h_nodes - 1][repetition] = xorMLP.n_iter_

    efficiency = np.zeros(10)
    for i in range(10):
        if successes[i] == 0:
            efficiency[i] = 1000
        else:
            efficiency[i] = epochs[i].sum() / successes[i]

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    axs[0].plot(hidden_layer_width, successes / 10.0)
    axs[0].set_title("Reliability")
    axs[0].set_xlabel("Hidden Layer Width")
    axs[0].set_ylabel("Success Rate")

    axs[1].plot(hidden_layer_width, efficiency)
    axs[1].set_title("Efficiency")
    axs[1].set_xlabel("Hidden Layer Width")
    axs[1].set_ylabel("Mean Epochs")

    # <==== insert your code above here

    return fig, axs

# make sure you have the packages needed
from approvedimports import *

#this is the class to complete where indicated
class MLComparisonWorkflow:
    """ class to implement a basic comparison of supervised learning algorithms on a dataset """ 
    
    def __init__(self, datafilename:str, labelfilename:str):
        """ Method to load the feature data and labels from files with given names,
        and store them in arrays called data_x and data_y.
        """
        # Define the dictionaries to store the models, and the best performing model/index for each algorithm
        self.stored_models:dict = {"KNN":[], "DecisionTree":[], "MLP":[]}
        self.best_model_index:dict = {"KNN":0, "DecisionTree":0, "MLP":0}
        self.best_accuracy:dict = {"KNN":0, "DecisionTree":0, "MLP":0}

        # Load the data and labels
        # ====> insert your code below here
        self.data_x = np.genfromtxt(datafilename, delimiter=",")
        self.data_y = np.genfromtxt(labelfilename, delimiter=",").astype(int)
        # <==== insert your code above here

    def preprocess(self):
        """ Method to 
           - separate it into train and test splits (using a 70:30 division)
           - apply the preprocessing you think suitable to the data
           - create one-hot versions of the labels for the MLP if there are more than 2 classes
        """
        # ====> insert your code below here
        self.train_x, self.test_x, self.train_y, self.test_y = train_test_split(
            self.data_x, self.data_y, test_size=0.3, stratify=self.data_y, random_state=12345
        )

        self.scaler = StandardScaler()
        self.train_x = self.scaler.fit_transform(self.train_x)
        self.test_x = self.scaler.transform(self.test_x)

        if len(np.unique(self.data_y)) >= 3:
            self.train_y_mlp = to_categorical(self.train_y)
            self.test_y_mlp = to_categorical(self.test_y)
        else:
            self.train_y_mlp = self.train_y
            self.test_y_mlp = self.test_y
        # <==== insert your code above here
    
    def run_comparison(self):
        """ Method to perform a fair comparison of three supervised machine learning algorithms.
        Should be extendable to include more algorithms later.
        """
        # ====> insert your code below here

        # 1. KNN
        for k in [1, 3, 5, 7, 9]:
            model = KNeighborsClassifier(n_neighbors=k)
            model.fit(self.train_x, self.train_y)
            acc = model.score(self.test_x, self.test_y)
            self.stored_models["KNN"].append(model)
            if acc > self.best_accuracy["KNN"]:
                self.best_accuracy["KNN"] = acc
                self.best_model_index["KNN"] = len(self.stored_models["KNN"]) - 1

        # 2. Decision Tree
        for depth in [1, 3, 5]:
            for min_split in [2, 5, 10]:
                for min_leaf in [1, 5, 10]:
                    model = DecisionTreeClassifier(
                        max_depth=depth, min_samples_split=min_split,
                        min_samples_leaf=min_leaf, random_state=12345
                    )
                    model.fit(self.train_x, self.train_y)
                    acc = model.score(self.test_x, self.test_y)
                    self.stored_models["DecisionTree"].append(model)
                    if acc > self.best_accuracy["DecisionTree"]:
                        self.best_accuracy["DecisionTree"] = acc
                        self.best_model_index["DecisionTree"] = len(self.stored_models["DecisionTree"]) - 1

        # 3. MLP
        for h1 in [2, 5, 10]:
            for h2 in [0, 2, 5]:
                for act in ["logistic", "relu"]:
                    if h2 == 0:
                        layers = (h1,)
                    else:
                        layers = (h1, h2)
                    model = MLPClassifier(
                        hidden_layer_sizes=layers,
                        activation=act,
                        max_iter=1000,
                        random_state=12345
                    )
                    model.fit(self.train_x, self.train_y_mlp)
                    acc = model.score(self.test_x, self.test_y_mlp)
                    self.stored_models["MLP"].append(model)
                    if acc > self.best_accuracy["MLP"]:
                        self.best_accuracy["MLP"] = acc
                        self.best_model_index["MLP"] = len(self.stored_models["MLP"]) - 1

        # <==== insert your code above here
    
    def report_best(self) :
        """Method to analyse results.
        Returns
        -------
        accuracy: float
            the accuracy of the best performing model

        algorithm: str
            one of "KNN","DecisionTree" or "MLP"
        
        model: fitted model of relevant type
            the actual fitted model to be interrogated by marking code.
        """
        # ====> insert your code below here
        best_algo = None
        best_acc = -1
        for algo in self.best_accuracy:
            if self.best_accuracy[algo] > best_acc:
                best_acc = self.best_accuracy[algo]
                best_algo = algo
        best_model = self.stored_models[best_algo][self.best_model_index[best_algo]]
        return best_acc, best_algo, best_model
        # <==== insert your code above here

