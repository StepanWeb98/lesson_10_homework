import json


def load_candidates_from_json():

    '''возвращает список всех кандидатов'''

    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        return candidates


def get_candidate(candidate_id):

    '''возвращает одного кандидата по его id'''

    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate_id == candidate['id']:
            return candidate


def get_candidates_by_name(candidate_name):
    '''
    возвращает кандидатов по имени
    '''
    candidates = load_candidates_from_json()
    results = []
    for candidate in candidates:
        if candidate_name in candidate['name'].split():
            results.append(candidate)
    return results

def get_candidates_by_skill(skill_name):
    '''
        возвращает кандидатов по навыку
    '''
    candidates = load_candidates_from_json()
    results = []
    for candidate in candidates:
        if skill_name.title() in candidate['skills'].title().split(', '):
            results.append(candidate)
    return results
