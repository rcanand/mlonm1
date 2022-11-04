import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme()


penguins = sns.load_dataset("penguins")
f, axs = plt.subplots(2, 2, figsize=(12, 12))

sns.scatterplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species", ax=axs[0][0])
sns.histplot(data=penguins, x="species", hue="species", shrink=.8, alpha=.8, legend=False, ax=axs[0][1])
sns.kdeplot(data=penguins, x="flipper_length_mm", hue="species", multiple="stack", ax=axs[1][0])
f.tight_layout()

sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")
sns.pairplot(data=penguins, hue="species")
sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species", kind="hist")

plt.show()