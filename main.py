import numpy as np
import itertools as it

from exp.exp import ExperimentGUI


def generate(ncontext, ntrial):
    """
    defines prob, rewards, contexts, trials etc...
    :param ncontext:
    :param ntrial:
    :return:
    """
    # ------------------------------------------------------------------------------- # 
    context = np.repeat([range(ncontext//2)], ntrial//(ncontext//2), axis=0)
    # context = np.repeat(range(ncontext), ntrial)
    # shuffle
    for t in range(len(context)):
        np.random.shuffle(context[t])
    # replace by new contexts
    context = context.flatten()
    for i, j in zip(range(4), range(4, 8)):
        context[(np.arange(len(context)) >= ntrial/2) * (context == i)] = j

    # prepare arrays
    reward = np.zeros(ncontext, dtype=object)
    prob = np.zeros(ncontext, dtype=object)
    r = np.zeros(ntrial, dtype=object)
    p = np.zeros(ntrial, dtype=object)
    options = [0, 1]
    idx_options = np.repeat([[0, 1]], ntrial, axis=0)

    # Define probs and rewards for each pair
    # ------------------------------------------------------------------------------- # 
    # AB and IJ
    for i in [0, 0 + 4]:
        reward[i] = [[0, 0], [-0.5, 0.5]]
        prob[i] = [[0.5, 0.5], [0.5, 0.5]]

    # CD and KL
    for i in [1, 1 + 4]:
        reward[i] = [[0, 0], [-0.5, 0.5]]
        prob[i] = [[0.5, 0.5], [0.5, 0.5]]

    #  EF and MN
    for i in [2, 2 + 4]:
        reward[i] = [[-0.5, 0.5], [-0.5, 0.5]]
        prob[i] = [[0.25, 0.75], [0.75, 0.25]]

    #  GH and OP
    for i in [3, 3 + 4]:
        reward[i] = [[0, 0.5], [0, -0.5]]
        prob[i] = [[0.5, 0.5], [0.5, 0.5]]
    # ------------------------------------------------------------------------------- # 

    for t in range(ntrial):
        r[t] = np.array(reward[context[t]])
        p[t] = np.array(prob[context[t]])
        np.random.shuffle(idx_options[t])

    return context, r, p, ntrial, idx_options, options, ntrial//2


def main():
    ncontext = 8
    context, r, p, ntrial, idx_options, options, pause = generate(ncontext=8, ntrial=16)

    img_list = ['a', 'b',
                'c', 'd',
                'e', 'f',
                'g', 'h',
                'i', 'j',
                'k', 'l',
                'm', 'n',
                'o', 'p']

    np.random.shuffle(img_list)

    context_map = {k: tuple(v) for k, v in enumerate(np.random.choice(
        img_list, size=(len(img_list)//2, 2), replace=False
    ))}

    exp = ExperimentGUI(
        ntrial=ntrial,
        name="Positivity",
        context=context,
        reward=r,
        prob=p,
        context_map=context_map,
        idx_options=idx_options,
        options=options,
        pause=pause
    )
    exp.run()


if __name__ == "__main__":
    main()
