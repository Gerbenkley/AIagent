from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def test():
    # result = get_files_info("calculator", ".")
    # print("Result for current directory:")
    # print(result)
    # print("")

    # result = get_file_content("calculator", "lorem.txt")
    # print("Result for current file:")
    # print(result)
    # print("")

    # result = get_file_content("calculator", "main.py")
    # print("Result for current file:")
    # print(result)
    # print("")

    write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    write_file("calculator", "/tmp/temp.txt", "this should not be allowed")


if __name__ == "__main__":
    test()
