import os
import shutil


def clear_input_folder(input_dir: str = None) -> None:
    """Remove all files and subdirectories under the given input directory.

    If no directory is provided, uses the default path ``data/input`` relative
    to the workspace root. Errors are printed but do not stop the process.
    """

    if input_dir is None:
        # build a path relative to this script's parent directory
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        input_dir = os.path.join(base, "data", "input")

    if not os.path.isdir(input_dir):
        print(f"Input directory does not exist: {input_dir}")
        return

    for entry in os.listdir(input_dir):
        path = os.path.join(input_dir, entry)
        try:
            if os.path.isdir(path) and not os.path.islink(path):
                shutil.rmtree(path)
            else:
                os.unlink(path)
        except Exception as exc:  # pylint: disable=broad-except
            print(f"Failed to delete {path}: {exc}")



