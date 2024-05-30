import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import style


def main(argv=None) -> int:
    iris_data = sns.load_dataset('iris')

    style.use('ggplot')
    sns.swarmplot(x="species", y="petal_length", data=iris_data, \
                  palette="muted")
    plt.ylabel("petal length, cm")
    plt.xlabel("species")
    plt.title("Species vs. Petal Length")
    plt.show()

    sns.catplot(data=iris_data, x="species", y="petal_length", \
                kind="bar", palette="muted", legend=False)
    plt.ylabel("petal length, cm")
    plt.xlabel("species")
    plt.title("Species vs. Petal Length")
    plt.show()

    sns.boxplot(data=iris_data, x="species", y="petal_length", \
                palette="muted")
    plt.ylabel("petal length, cm")
    plt.xlabel("species")
    plt.title("Species vs. Petal Length")
    plt.show()

    sns.pairplot(data=iris_data, hue="species", size=2)
    plt.ylabel("petal length, cm")
    plt.xlabel("species")
    plt.show()

    return 0


if __name__ == '__main__':
    raise SystemExit(main())