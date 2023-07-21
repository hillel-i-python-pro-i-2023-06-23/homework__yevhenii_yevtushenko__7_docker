from app.services.generate_users import T_HUMANS


def organize_data(humans: T_HUMANS):
    organized_data = {}
    for human in humans:
        group_name = human["group"]
        if group_name not in organized_data:
            organized_data[group_name] = []
        organized_data[group_name].append(human["name"])

    return organized_data
