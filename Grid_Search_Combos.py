import pickle
combinations_grid_search = []
l2_norm_clip = [0.5, 1.0, 2.5, 5.0, 10.0, 20.0]
noise_multiplier = [0.0001, 0.2, 0.4, 0.6, 0.8, 1.0, 2.0]
learning_rate = [0.001, 0.05, 0.1, 0.15, 0.25]

# 6 * 7 * 5
# l2_norm_clip = [0.5*i for i in range(1, 3)]
# noise_multiplier = [0.2*j for j in range(1,3)]
# learning_rate = [0.005*x for x in range(3)]

for norm in l2_norm_clip:
    for noise in noise_multiplier:
        for rate in learning_rate:
            combinations_grid_search.append((norm, noise, rate))

# Open a file and use dump()
with open('combos.pkl', 'wb') as file:
    # A new file will be created
    pickle.dump(combinations_grid_search, file)