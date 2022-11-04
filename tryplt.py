import matplotlib.pyplot as plt
from util import distributions


# plot distributions as square subplots in 4 columns
def plot_distributions(d, cols=4):
    rows = len(d) // cols + 1
    fig, axes = plt.subplots(rows, cols, figsize=(12, 12))
    for i, (name, data) in enumerate(d.items()):
        row = i // cols
        col = i % cols
        ax = axes[row, col]
        ax.hist(data)
        ax.set_title(name)
    plt.tight_layout()
    plt.show()


# main
if __name__ == '__main__':
    # get distributions
    distributions = distributions(100000)
    
    # plot distributions
    plot_distributions(distributions, cols=5)
