def main():
    def count_nested_levels(nested_documents, target_document_id, level=1):
        for id in nested_documents:
            if id == target_document_id:
                return level
            else:
                doc_id = count_nested_levels(
                    nested_documents[id], target_document_id, level=level + 1
                )
                if doc_id != -1:
                    return doc_id
        return -1

    test1_input = {1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}
    test2_input = {1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}

    print(count_nested_levels(test1_input, 2))  # Expected output: 2
    print(count_nested_levels(test2_input, 9))  # Expected output: 4


if __name__ == "__main__":
    main()
