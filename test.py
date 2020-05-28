from duplicate_info import duplicate_info
from pathlib import Path

if __name__=="__main__":
    file = r"C:\Users\KC Cheng\Desktop\test.csv"
    info_obj = duplicate_info(file)
    info_dict = info_obj.duplicate_info
    page_dict = info_obj.page_info
    print(info_dict)
    print(page_dict)
    info_obj.write_to_csv()
