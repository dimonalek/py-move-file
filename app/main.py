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
    if "/" not in destination:
        os.rename(source, destination)
    else:
        destination_dir = destination.split("/")
        destination_file = destination_dir[-1]
        destination_dir.pop()
        destination_dir = "/".join(destination_dir)
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        with open(
            source, "r"
        ) as source_file, open(
            destination, "w"
        ) as destination_file:
            for line in source_file:
                destination_file.write(line)
        os.remove(source)
