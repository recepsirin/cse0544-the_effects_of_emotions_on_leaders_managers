import random
import csv

gender = ['Male', 'Female']
manager_level = ['Top', 'Middle', 'Level']
title = ['President', 'Vice-president', 'C-Level', 'Organizational Manager', 'Assistant Manager', 'Supervisor',
         'Board Member']
industry_type = [
    'Aerospace Industry', 'Transport Industry', 'Computer Industry', 'Telecommunication Industry',
    'Agriculture Industry', 'Construction Industry', 'Education Industry', 'Pharmaceutical Industry',
    'Food Industry', 'Health Industry', 'Entertainment Industry', 'Electronics Industry', 'Energy Industry'
]

education_degree = ['Bachelor', 'Master', 'MBA', 'PhD']


def generate_fake_data():
    with open('dataset.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["Gender", "Manager Level", "Title", "Industry Type", "Age", "Education Degree"
                         "Confident", "Capable", "Efficient", "Intelligent", "Friendly",
                         "Trustworthy", "Warm", "Sincere", "Jealous", "Envious", "Admiring", "Proud",
                         "Respectful", "Inspired", "Angry", "Disgusted", "Hateful", "Frustrated", "Ashamed", "Pity",
                         "Sympathy"])
        for l in range(1, 2001):
            if l % 13 == 0:
                continue

            writer.writerow([gender[random.randrange(0, len(gender))],
                             manager_level[random.randrange(0, len(manager_level))],
                             title[random.randrange(0, len(title))],
                             industry_type[random.randrange(0, len(industry_type))],
                             random.randrange(38, 60),  # age
                             education_degree[random.randrange(0, len(education_degree))],  # education degree
                             random.randrange(1, 11),  # Confident
                             random.randrange(1, 11),  # Capable
                             random.randrange(1, 11),  # Efficient
                             random.randrange(1, 11),  # Intelligent
                             random.randrange(1, 11),  # Friendly
                             random.randrange(1, 11),  # Trustworthy
                             random.randrange(1, 11),  # Warm
                             random.randrange(1, 11),  # Sincere
                             random.randrange(1, 11),  # Jealous
                             random.randrange(1, 11),  # Envious
                             random.randrange(1, 11),  # Admiring
                             random.randrange(1, 11),  # Proud
                             random.randrange(1, 11),  # Inspired
                             random.randrange(1, 11),  # Angry
                             random.randrange(1, 11),  # Disgusted
                             random.randrange(1, 11),  # Hateful
                             random.randrange(1, 11),  # Frustrated
                             random.randrange(1, 11),  # Ashamed
                             random.randrange(1, 11),  # Pity
                             random.randrange(1, 11),  # Sympathy
                             ])


if __name__ == "__main__":
    # The effects of emotions on leaders/managers
    generate_fake_data()
