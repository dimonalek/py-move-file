import os


def move_file(command: str) -> None:
    try:
        trash, source, destination = command.split()
    except ValueError:
        return
    if trash != "mv" or not source or not destination:
        return
    if source == destination:
        return
    destination_norm = destination.replace("/", "\\")
    if destination_norm.endswith("\\"):
        destination_path_list = destination_norm.split("\\")
        os.makedirs(os.path.join(*destination_path_list), exist_ok=True)
        full_path = os.path.join(destination_norm, source)
        with open(full_path, "w") as file, open(source, "r") as source_file:
            file.write(source_file.read())
        os.remove(source)
    elif "\\" in destination_norm:
        destination_path_list = destination_norm.split("\\")
        os.makedirs(os.path.join(*destination_path_list[:-1]), exist_ok=True)
        full_path = os.path.join(*destination_path_list)
        with open(full_path, "w") as file, open(source, "r") as source_file:
            file.write(source_file.read())
        os.remove(source)
    else:
        with open(destination, "w") as file, open(source, "r") as source_file:
            file.write(source_file.read())
        os.remove(source)
