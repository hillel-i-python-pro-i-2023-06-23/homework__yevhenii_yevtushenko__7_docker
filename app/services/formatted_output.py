from app.services.organize_data import organize_data


def get_formatted_output(data) -> organize_data:
    output = ""
    for group_name, members in data.items():
        num_members = len(members)
        output += f"Group: {group_name} (Members: {num_members})\n"
        output += "\n".join([f"  - {name}" for name in members]) + "\n\n"

    return output
