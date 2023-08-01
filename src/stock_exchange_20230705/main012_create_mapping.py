# stock_exchange_20230705 / main012_create_mapping.py
# create mapping file from ForBackBench files
# 2023/8/1, by Tadashi Masuda
# Amagasa Laboratory, University of Tsukuba

import json
import re

with open('/media/masuda/HDS2-UT/PycharmProjects/PyForBackBench20230629/scenarios/StockExchange/ontop-files/gav-mapping.obda', 'r') as input_file:
    mode = None
    prefixes = {}
    json_list = []
    json_element = {}
    var_number = 10000  # used to create VAR10000, etc.
    gav_data = input_file.readlines()
    for line in gav_data:
        if line.find('PrefixDeclaration') >= 0:
            mode = 'PrefixDeclaration'  # set the mode and go to the next line
            continue
        elif line.find('MappingDeclaration') >= 0:
            mode = 'MappingDeclaration'  # set the mode and go to the next line
            continue
        else:  # actual execution
            if mode == 'PrefixDeclaration':
                input_line = line.replace('\n', '').replace(' ', '').replace('\t', '').replace('http:', 'http$').replace('https:', 'https$')
                if input_line:
                    input_split = input_line.split(':')
                    prefixes[input_split[0]] = input_split[1].replace('http$', 'http:').replace('https$', 'https:')  # set the prefixes
                pass
            if mode == 'MappingDeclaration':
                input_line = line.replace('\t', ' ').replace('\n', '').replace('  ', ' ')
                if input_line:  # if input_line contains something
                    for prefix_key, prefix_value in prefixes.items():
                        input_line = input_line.replace(prefix_key+':', prefix_value)  # replace all the prefixes
                    # input_line is mappingID / target / source
                    if input_line.find('mappingId ') >= 0:  # mappingID line
                        json_element = {}  # initialize the json element for this mapping
                        json_element['mappingId'] = input_line.replace('mappingId ', '')  # set the mapping ID
                    if input_line.find('target ') >= 0:  # target line
                        target_line = input_line.replace('target ', '')  # remove the target key word
                        target_split = target_line.split(' ')  # subj/pred/obje is separated with spaces
                        subject_term = target_split[0]
                        predicate_term = target_split[1]
                        object_term = target_split[2]

                        json_term = {}  # create json element for 'subject'
                        subject_replaced_name = 'VAR'+str(var_number)  # ex. VAR10000
                        if subject_term.find('{') >= 0:
                            matches_subject = re.findall(r'[{]var\d+[}]', subject_term)  # extract variables
                            subject_var_name = matches_subject[0].replace('{', '').replace('}', '')  # ex. var1
                            json_term['type'] = 'Variable'
                            json_term['uri'] = 'plain'
                            json_term['content'] = ''
                            json_term['variable'] = subject_replaced_name
                            json_element['subject'] = json_term
                        else:
                            print('Invalid subject term: ', subject_term)  # something is wrong for 'subject'

                        json_term = {}  # create json element for 'predicate'
                        predicate_var_name = 'VAR'+str(var_number+1)  # ex. VAR10001
                        json_term['type'] = 'NamedNode'
                        if predicate_term == 'a':  # handling 'a'
                            predicate_term = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type'
                        json_term['content'] = predicate_term
                        json_term['variable'] = predicate_var_name
                        json_element['predicate'] = json_term

                        json_term = {}  # create json element for 'object'
                        object_replaced_name = 'VAR'+str(var_number+2)  # ex. VAR10002
                        object_is_variable = False  # first assume the object is not a variable
                        if object_term.find('{') >= 0:
                            matches_subject = re.findall(r'[{]var\d+[}]', object_term)
                            object_var_name = matches_subject[0].replace('{', '').replace('}', '')
                            json_term['type'] = 'Variable'
                            json_term['uri'] = 'plain'
                            json_term['content'] = ''
                            object_is_variable = True  # variable is found in the object
                        else:  # object is a literal
                            json_term['type'] = 'NamedNode'
                            json_term['uri'] = '-'
                            json_term['content'] = object_term
                        json_term['variable'] = object_replaced_name
                        json_element['object'] = json_term

                        var_number += 100  # VAR10000 -> VAR10100

                        pass
                    if input_line.find('source ') >= 0:  # source line
                        matches_subject = re.findall(r'(A\.\"c0\" as var\d+)|(\"c0\" as var\d+)', input_line)
                        sql = input_line.replace('source ', '')  # remove 'source' key word
                        matched_string = str(matches_subject[0][0]).replace(' as ', ') as ')
                        sql = sql.replace(str(matches_subject[0][0]),
                                          f"CONCAT('http://www.owl-ontologies.com/Ontology1207768242.owl#ns/', {matched_string}")\
                            .replace(subject_var_name, subject_replaced_name)  # subject replaced name is defined in 'target'

                        if object_is_variable:
                            matches_object = re.findall(r'([A-Z]\.\"c\d\" as var\d+)', sql)
                            matched_string = str(matches_object[0]).replace(' as ', ') as ')
                            sql = sql.replace(str(matches_object[0]),
                                              f"CONCAT('http://www.owl-ontologies.com/Ontology1207768242.owl#ns/', {matched_string}")\
                                .replace(object_var_name, object_replaced_name)
                        else:
                            sql = sql.replace(' FROM ', f", CONCAT('{object_term}') AS {object_replaced_name} FROM ")

                        sql = sql.replace('"', '\"')
                        json_element['SQL'] = sql  # 'SQL' element in the mapping file
                        json_list.append(json_element)
                        pass

    with open('../../data/stock_exchange_20230705/mapping/mapping.json', 'w') as output_file:  # write the created mapping file
        json.dump(json_list, output_file, indent=2)  # in JSON format
