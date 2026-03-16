import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

rules_path = os.path.join(BASE_DIR, "models", "rules.pkl")

rules = pickle.load(open(rules_path, "rb"))


def recommend(product):

    rec = rules[rules["antecedents"].apply(lambda x: product in x)]

    rec = rec.sort_values("confidence", ascending=False)

    recommendations = []

    for items in rec["consequents"].head(5):
        for item in items:
            recommendations.append(item)

    return recommendations