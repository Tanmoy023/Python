import os

for i in range (0, 10):
    os.rename(f"dataF/subData_{i+1}", f"dataF/tutorial_{i+1}") # it find the subData_n in the path of dataF and rename it into tutorial_n