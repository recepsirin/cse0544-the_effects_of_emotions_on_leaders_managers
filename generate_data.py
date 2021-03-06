import random
import csv

gender = ['Male', 'Female']
manager_level = ['Top', 'Middle', 'Level']
title = ['President', 'Vice-president', 'C-Level', 'Organizational Manager', 'Assistant Manager', 'Supervisor',
         'Board Member']

education_degree = ['Bachelor', 'Master', 'MBA', 'PhD']
user_response = ['Strongly Agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree']


def generate_fake_data():
    with open('dataset.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["Gender", "Manager Level", "Title", "Age", "Education Degree",
                         "Confident", "Capable", "Efficient", "Intelligent", "Friendly", "Trustworthy", "Warm",
                         "Sincere", "Jealous", "Envious", "Admiring", "Proud", "Inspired", "Angry",
                         "Disgusted", "Hateful", "Frustrated", "Ashamed", "Pity", "Sympathy"])

        for l in range(0, 2000):
            level_of_acceptance = sorted(user_response, key=lambda x: random.random())
            writer.writerow([gender[random.randrange(0, len(gender))],  # Gender
                             manager_level[random.randrange(0, len(manager_level))],  # Manager Level
                             title[random.randrange(0, len(title))],  # Title
                             random.randrange(32, 60),  # age
                             education_degree[random.randrange(0, len(education_degree))],  # education degree
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Confident
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Capable
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Efficient
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Intelligent
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Friendly
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Trustworthy
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Warm
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Sincere
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Jealous
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Envious
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Admiring
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Proud
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Inspired
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Angry
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Disgusted
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Hateful
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Frustrated
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Ashamed
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Pity
                             level_of_acceptance[random.randrange(0, len(level_of_acceptance))],  # Sympathy
                             ])


if __name__ == "__main__":
    # The effects of emotions on leaders/managers
    generate_fake_data()
