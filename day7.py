import re
inner_bag_re = re.compile('(\d)(.+)')
PATH = '/Users/Deathvoodoo/big_folders_docs/code_advent/'
rules_file = 'day7.txt'

def read_rules(file):
    rules = {}
    with open(file) as input:
        lines = input.readlines()
        for line in lines:
            line = line.strip()
            line = line.strip('.')
            line = line.split('contain')
            outer_bag = line[0].strip()
            if outer_bag[-1] == 's':
                outer_bag = outer_bag[:-1] # remove s from bags
            inner_bags = line[1].split(',')
            inner_bags = [i.strip() for i in inner_bags]
            bag_dict = {}
            for bag in inner_bags:
                match_obj = inner_bag_re.match(bag)
                if not match_obj:
                    bag_dict = bag # no bags str
                else:
                    number = match_obj.group(1)
                    bag = (match_obj.group(2)).strip()
                    if bag[-1] == 's':
                        bag = bag[:-1]
                    bag_dict[bag]=int(number)
            rules[outer_bag]=bag_dict
    return(rules)

rules = read_rules(PATH+rules_file)

def check_key(bag_rules, outer_bag, inner_bag):
    has_bag = 0
    if type(bag_rules[outer_bag]) != str:
        bags_inside = bag_rules[outer_bag].keys()
        if inner_bag in bags_inside:
            #has_bag += bag_rules[outer_bag][inner_bag]
            has_bag += 1
        else:
            for subbag in bags_inside:
                has_bag += check_key(bag_rules=bag_rules, outer_bag=subbag, inner_bag=inner_bag)
    else:
        None
    return has_bag

def count_bags(bag_rules, bag):
    n_bags = 0
    if type(bag_rules[bag]) != str:
        for inner_bag, n in bag_rules[bag].items():
            n_bags += n
            n_bags += n*count_bags(bag_rules=bag_rules, bag=inner_bag)
    return(n_bags)


keys_with_bags = []
for bag in rules.keys():
    if check_key(rules, bag, 'shiny gold bag') > 0:
        keys_with_bags.append(bag)
print(len(keys_with_bags))

#rules_test = read_rules(PATH+'day7_test2.txt')

#print(rules['shiny gold bag'].items())
print(count_bags(rules, 'shiny gold bag'))
#print(count_bags(rules, 'pale beige bag'))
