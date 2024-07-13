import json
import random

def generate_test_data():
    ip_app_dict = {}
    app_words = [
        "alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "iota", "kappa",
        "lambda", "mu", "nu", "xi", "omicron", "pi", "rho", "sigma", "tau", "upsilon", "phi", "chi",
        "psi", "omega", "apollo", "zeus"
    ]

    app_names = [f'app_{word}' for word in app_words]

    for i in range(1, 201):
        ip = f'1.1.1.{i}'
        num_apps = random.randint(1, 5)
        apps = random.sample(app_names, num_apps)
        ip_app_dict[ip] = apps

    with open('ip_app_data.json', 'w') as file:
        json.dump(ip_app_dict, file, indent=4)

generate_test_data()