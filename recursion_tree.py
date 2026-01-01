def main():
    def list_files(parent_directory, current_filepath=""):
        paths = []
        for key, value in parent_directory.items():
            new_file_path = current_filepath + "/" + key
            if value is None:
                paths.append(new_file_path)
            else:
                paths.extend(list_files(value, new_file_path))
        return paths

    test_input = {
        "Documents": {
            "Proposal.docx": None,
            "Receipts": {
                "January": {"receipt1.txt": None, "receipt2.txt": None},
                "February": {"receipt3.txt": None},
            },
        },
    }

    for i in list_files(test_input):
        print(i)


if __name__ == "__main__":
    main()
