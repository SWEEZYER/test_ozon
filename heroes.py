import requests

API_URL = "https://akabab.github.io/superhero-api/api/all.json"

EMPTY_OCCUPATIONS = ["-", "", "none", "unknown"]


def _get_all_heroes():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка: Не удалось получить данные из API. {e}")
        return None


def _check_occupation(occupation_str, has_occupation):
    normalized_occupation = str(occupation_str).strip().lower()

    is_job_empty = (normalized_occupation in EMPTY_OCCUPATIONS)

    if has_occupation:
        return not is_job_empty
    else:
        return is_job_empty


def _parse_height_cm(height_list):
    if not isinstance(height_list, list) or len(height_list) < 2:
        return 0

    metric_height_str = height_list[1]

    try:
        parts = metric_height_str.split()

        if len(parts) < 2:
            return 0

        value_str = parts[0].replace(',', '.')
        value = float(value_str)
        unit = parts[1]

        if unit == 'cm':
            return int(value)
        elif unit == 'm':
            return int(value * 100)
        else:
            return 0

    except (ValueError, TypeError, IndexError):
        return 0


def find_tallest_hero(gender, has_occupation):
    heroes_list = _get_all_heroes()

    if not heroes_list:
        return None

    tallest_hero_name = None
    max_height_found = 0

    for hero in heroes_list:
        appearance_data = hero.get("appearance", {})
        work_data = hero.get("work", {})

        hero_gender = appearance_data.get("gender")
        hero_occupation = work_data.get("occupation")
        hero_height_list = appearance_data.get("height")

        if hero_gender != gender:
            continue

        if not _check_occupation(hero_occupation, has_occupation):
            continue

        current_height_cm = _parse_height_cm(hero_height_list)

        if current_height_cm > max_height_found:
            max_height_found = current_height_cm
            tallest_hero_name = hero.get("name")

    return tallest_hero_name
