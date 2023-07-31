# class for handling mapping rules
# 2023/6/1, Tadashi masuda
# Amagasa Laboratory, University of Tsukuba

import json
import os.path


class Mapping:
    def __init__(self, path):
        mapping_uri = path  # './data_set2/mapping/mapping_gav.json'
        # マッピングデータの取り込み
        json_open_file = open(mapping_uri, 'r')
        self.mapping_dict = json.load(json_open_file)
        json_open_file.close()

        self.var_prefix_map = {}  # a dictionary of variables and their corresponding URI transformation tables
        for mapping in self.mapping_dict['rules']:
            subj = mapping['subject']
            if subj['type'] == 'Variable' and subj['uri'] != 'plain':
                self.var_prefix_map[subj['variable']] = subj['uri']
            obje = mapping['object']
            if obje['type'] == 'Variable' and obje['uri'] != 'plain':
                self.var_prefix_map[obje['variable']] = obje['uri']
            pass
        pass

        self.mapping_func = {}
        uri_path = os.path.dirname(path)
        uri_path = os.path.dirname(uri_path)
        uri_path = uri_path + '/uri/'
        for file in os.listdir(uri_path):  # read *.py
            if file.endswith(".py"):
                with open(uri_path+file, 'r') as input_file:
                    uri_genre_code = input_file.read()
                    self.mapping_func[file] = uri_genre_code
                    pass
        pass
