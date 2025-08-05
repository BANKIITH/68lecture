from collections import Counter

survey_results = [
    ["Python", "JavaScript", "C++"],        # Participant 1
    ["Python", "JavaScript", "C#"],         # Participant 2
    ["Python", "Java"],                     # Participant 3
    ["Python", "C++", "JavaScript"],        # Participant 4
    ["Python", "JavaScript", "C++", "Java"] # Participant 5
]


common_languages = set(survey_results[0])
for participant in survey_results[1:]:
    common_languages &= set(participant)


all_languages = [lang for participant in survey_results for lang in participant]
language_counts = Counter(all_languages)
languages_chosen_once = [lang for lang, count in language_counts.items() if count == 1]


unique_languages = set(all_languages)
num_unique_languages = len(unique_languages)


languages_chosen_by_2 = [lang for lang, count in language_counts.items() if count == 2]


participant_sets = [set(p) for p in survey_results]
duplicates = []
for i in range(len(participant_sets)):
    for j in range(i + 1, len(participant_sets)):
        if participant_sets[i] == participant_sets[j]:
            duplicates.append((i + 1, j + 1))  


print("1. Languages chosen by all participants:", common_languages)
print("2. Languages chosen by only one participant:", languages_chosen_once)
print("3. Number of unique languages:", num_unique_languages)
print("4. Languages chosen by exactly two participants:", languages_chosen_by_2)
print("5. Participants with the same favorite languages:", duplicates)
