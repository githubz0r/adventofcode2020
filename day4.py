import numpy as np
import re
passports = []
with open('/Users/Deathvoodoo/big_folders_docs/code_advent/day4.txt') as input:
    cur_pw = []
    lines = input.readlines()
    for line in lines:
        if line =='\n':
            passports.append(cur_pw)
            cur_pw = []
        elif line == lines[-1]: # no newline at end
            line = line.strip()
            cur_pw += line.split()
            passports.append(cur_pw)
        else:
            line = line.strip()
            cur_pw += line.split()

def get_dicts(passport):
    pp_dict = {}
    for i in passport:
        i = i.split(':')
        pp_dict[i[0]] = i[1]
    return(pp_dict)

passports = [get_dicts(i) for i in passports]


def is_valid_pp(passport, optional=['cid']):
    valid = None
    n_keys = len(passport.keys())
    optional_in_keys = [i not in passport.keys() for i in optional]
    if n_keys == 8:
        valid = True
    elif all(optional_in_keys) and n_keys == (8-len(optional)):
        valid = True
    else:
        valid = False
    return valid

def check_subset(passport):
    valid = True
    haircl = passport['hcl']

    hgt_re = re.match('((\d+)(in|cm))', passport['hgt'])
    if not bool(hgt_re):
        valid = False
    else:
        #print(passport['hgt'])
        vals = hgt_re.group(2)
        cm_or_in = hgt_re.group(3)
        if cm_or_in == 'cm':
            if int(vals) > 193 or int(vals) < 150:
                valid = False
        elif cm_or_in == 'in':
            if int(vals) > 76 or int(vals) < 59:
                valid = False
    if valid==True:
        print('true', passport['hgt'])
    #print(passport['hgt'])
    for key in passport.keys():
        if passport[key] == None:
            valid = False
    valid_ecl = ['amb','blu','brn','gry','grn','hzl','oth']
    pid_re = re.match('\d{9}', passport['pid'])
    hcl_re = re.match('#([0-9]|[a-f]){6}', haircl)
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        valid = False
    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        valid = False
    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        valid = False
    if len(haircl) != 7:
        valid = False
    if not(bool(hcl_re)):
        valid = False
    if passport['ecl'] not in valid_ecl:
        valid = False
    if len(passport['pid']) != 9:
        valid = False
    if not(bool(pid_re)):
        valid = False
    return valid

passport_validities = np.array([is_valid_pp(i) for i in passports])
valid_inds = np.where(passport_validities)
valid_pp1 = [passports[i] for i in list(valid_inds[0])]
print(len(valid_pp1))

check_subset(valid_pp1[11])
passport_validities2 = np.array([check_subset(i) for i in valid_pp1])
print(np.where(passport_validities2)[0][0:10])
print(valid_pp1[6])
print(np.sum(passport_validities*1))
print(np.sum(passport_validities2*1))
