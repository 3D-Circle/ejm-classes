# coding=utf-8
"""Utility to plot the evolution of equilibrium point of offer and need
REQUIRES python 3.6, matplotlib (pip install matplotlib) 

This script will ask for 2 inputs: (accepted inputs are put in this format: [a / b] expects a or b)
- 'déplacement de la courbe de [demande / offre]'
- 'déplacement de la courbe de {answer to previous question} vers la [gauche / droite]'

if answers to previous questions are both None, 2 additional inputs will be required:
- 'déplacement sur la courbe de demande vers la [gauche / droite]'
- 'déplacement sur la courbe d'offre vers la [gauche / droite]'
"""

import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True


def get_inputs():
    """Get the inputs from user, as specified in the docstring above"""
    courbe = input("déplacement de la courbe de [demande / offre] ")
    déplacement = input(
        f"déplacement de la courbe d{'e ' if courbe == 'demande' else r'''' '''}{courbe} vers la [gauche / droite] "
    )
    if not courbe and not déplacement:
        déplacement_d = input("déplacement de sur la courbe de demande vers la [gauche / droite] ")
        déplacement_o = input("déplacement de sur la courbe d'offre vers la [gauche / droite] ")
        return {'d': déplacement_d, 'o': déplacement_o}
    else:
        return {courbe: déplacement}


def plot(**kwargs):
    """Plot the options specified by the user"""
    fig, ax = plt.subplots()
    frame = plt.gca()

    for side in ('top', 'right', 'bottom', 'left'):
        ax.spines[side].set_visible(False)

    frame.axes.get_xaxis().set_ticks([])
    frame.axes.get_yaxis().set_ticks([])

    ax.annotate("", xy=(10, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(0, 10), xytext=(0, 0), arrowprops=dict(arrowstyle="->"))

    plt.title("Évolution de l'équilibre")
    plt.xlabel("Qté")
    ax.set_ylabel("Prix", rotation=0, ha='right')

    plt.ylim([0, 10])
    plt.xlim([0, 10])

    prix = list(range(1, 10))

    demande = [-x + 10for x in prix]
    offre = [x for x in prix]

    # Courbe d'offre / demande
    d1, = plt.plot(demande, prix, label=r"$D_1$", color='red', zorder=1)
    o1, = plt.plot(offre, prix, label=r"$O_1$", color='green', zorder=1)

    # Courbe d'offre / demande nouvelle
    handler_demande, handler_offre = [d1], [o1]

    # Équilibre d'offre et demande
    équilibres = [(5., 5.)]

    delta = -1 if 'gauche' in kwargs.values() else +1
    if 'demande' in kwargs:
        d2, = plt.plot(
            [i + delta for i in demande],
            prix,
            label=r"$D_2$", color='red', linestyle='dashed', zorder=1
        )
        handler_demande.append(d2)
        équilibres.append((4.5, 4.5) if delta == -1 else (5.5, 5.5))  # nouvel équilibre

    if 'offre' in kwargs:
        o2, = plt.plot(
            [j + delta for j in offre],
            prix,
            label=r"$O_2$", color='green', linestyle='dashed', zorder=1
        )
        handler_offre.append(o2)
        équilibres.append((4.5, 5.5) if delta == -1 else (5.5, 4.5))  # nouvel équilibre

    if 'd' in kwargs and 'o' in kwargs:
        e2_d = (4, 6) if kwargs['d'] == 'gauche' else (6, 4)
        e2_o = (4, 4) if kwargs['o'] == 'gauche' else (6, 6)
        équilibres += [e2_d, e2_o]

    legend_o = plt.legend(handles=handler_offre, loc=1)
    plt.gca().add_artist(legend_o)
    plt.legend(handles=handler_demande, loc=4)

    for index, équilibre in enumerate(équilibres):
        point_color = 'black' if index == 0 else 'red'  # ... we start counting from 0!
        plt.scatter(*équilibre, color=point_color, zorder=2)

        x, y = équilibre
        plt.scatter(x, 0, color='black', s=15, zorder=2)
        plt.scatter(0, y, color='black', s=15, zorder=2)

        plt.plot([0, x], [y, y], linestyle='dotted', color='black', zorder=0)
        plt.plot([x, x], [0, y], linestyle='dotted', color='black', zorder=0)

        if len(équilibres) <= 2 or index == 0:
            plt.annotate(f'$E_{index + 1}$', xy=équilibre, xytext=(-7.5, 15), textcoords='offset points')

            x0, y0 = équilibres[0]
            ax.annotate("", xytext=(x0, 0.1), xy=(x, 0.1), arrowprops=dict(arrowstyle="->", color='blue'))
            ax.annotate("", xytext=(0.1, y0), xy=(0.1, y), arrowprops=dict(arrowstyle="->", color='blue'))

            plt.annotate(f'$Q_{index + 1}$', xy=(x, 0), xytext=(0, 10), textcoords='offset points')
            plt.annotate(f'$P_{index + 1}$', xy=(0, y), xytext=(10, 0), textcoords='offset points')

    plt.show()


if __name__ == '__main__':
    plot(**get_inputs())
