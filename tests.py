from functions.get_files_info import get_files_info

print("Results for calculator, .:")
print(get_files_info("calculator", "."))
print("\n")

print("Results for calculator, pkg:")
print(get_files_info("calculator", "pkg"))
print("\n")

print("Results for calculator, /bin:")
print(get_files_info("calculator", "/bin"))
print("\n")

print("Results for calculator, ../:")
print(get_files_info("calculator", "../"))
print("\n")
