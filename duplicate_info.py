import pandas as pd
from pathlib import Path
import os

class duplicate_info:
    def __init__(self, info_path):
        self.info_path = info_path
        self.duplicate_info = self.parse_info()[0]
        self.page_info = self.parse_info()[1]

    def check_line(self, line):
        if ":" in line:
            return True
        else:
            return False

    def check_page_line(self, line):
        if "/" in line:
            return True
        else:
            return False

    def split_line(self, line):
        if self.check_line(line):
            split_line = line.split(":")
            if len(split_line) == 2:
                a, b = split_line
                b = b.replace('\n','')
                return [a, b]
            elif len(split_line) > 2:
                raise Warning("Split line has more than 2 sub-strings.")
                return []
            else:
                raise Warning("Split line has less than 2 sub-strings.")
            return []

    def parse_info(self):
        try:
            info_dict = {}
            info_dict['line_index'] = []
            info_dict['frame'] = []
            info_dict['diff'] = []

            page_dict={}
            page_dict['line_index'] = []
            page_dict['info'] = []
            cnt = 0

            # open file and read lines
            reader = open(self.info_path, 'r')
            lines = reader.readlines()
            for line in lines:
                cnt += 1
                if self.check_line(line):
                    a, b = self.split_line(line)
                    info_dict['line_index'].append(cnt)
                    info_dict['frame'].append(a)
                    info_dict['diff'].append(b)
                else:
                    if self.check_page_line(line):
                        page_dict['line_index'].append(cnt)
                        page_dict['info'].append(line.replace("\n",''))
                    else:
                        print("non information and page info at line: " + cnt)
            return info_dict, page_dict
        except FileNotFoundError as e:
            print(e.strerror + " : " + self.info_path)


    def write_to_csv(self):
        duplicate_df = pd.DataFrame(self.duplicate_info)

        # Detect parent folder of info_file
        parent = Path(self.info_path).parent

        # Write duplicate information to csv
        duplicate_df.to_csv(os.path.join(parent, 'duplicate.csv'), index=False)









