import os
import sys
import shutil

def main():
    if len(sys.argv) < 3:
        print("Usage: python temp_ops.py <command> [args...]")
        print("Commands:")
        print("  mv <old_path> <new_path>")
        print("  rm <path_to_delete>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "mv" and len(sys.argv) == 4:
        old_path = sys.argv[2]
        new_path = sys.argv[3]
        try:
            shutil.move(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")
        except FileNotFoundError:
            print(f"Error: File not found - {old_path}")
            sys.exit(1)
        except Exception as e:
            print(f"Error renaming {old_path}: {e}")
            sys.exit(1)

    elif command == "rm" and len(sys.argv) == 3:
        path_to_delete = sys.argv[2]
        try:
            if os.path.isdir(path_to_delete):
                shutil.rmtree(path_to_delete)
                print(f"Deleted directory: {path_to_delete}")
            else:
                os.remove(path_to_delete)
                print(f"Deleted file: {path_to_delete}")
        except FileNotFoundError:
            print(f"Error: File not found - {path_to_delete}")
            sys.exit(1)
        except Exception as e:
            print(f"Error deleting {path_to_delete}: {e}")
            sys.exit(1)
    else:
        print(f"Invalid command or arguments for '{command}'.")
        sys.exit(1)

if __name__ == "__main__":
    main()