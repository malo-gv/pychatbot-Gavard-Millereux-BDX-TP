from functions import *


directory = 'ressources/speeches-20231110/'
files_names = (list_of_files(directory, "txt"))
print(list(files_names))


print(donner_nom2(files_names[4]))
