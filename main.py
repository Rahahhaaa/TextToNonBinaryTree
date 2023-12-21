import re
import collections

class Node:
    def __init__(self, item,type_):
        self.item = item
        self.type = type_
        self.children = []
        
    def preorder(self):
        print(self.item)
        for i in self.children:
            i.preorder()
        
class NBT:
    def __init__(self, r):
        self.root = r
        
    def preorder(self):
        if self.root: self.root.preorder()

def tokenizer(input_expression):
    current = 0
    tokens = []
    topic = re.compile('topic\s*:\s*"(?P<item>[^\"]*)"', re.I);
    sentence = re.compile('sentence\s*:\s*"(?P<item>[^\"]*)"', re.I);
    whiteSpace = re.compile(r"\s");
    while current < len(input_expression):
        char = input_expression[current]
        if re.match(whiteSpace, char):
            current = current+1
            continue
        if char == '{':
            tokens.append({
                'type': 'left_paren',
                'value': '{'
            })
            current = current+1
            continue
        if char == '}':
            tokens.append({
                'type':'right_paren',
                'value':'}'
            })
            current = current + 1
            continue
        if topic.match(input_expression[current:]):
            tokens.append({
                'type':'topic',
                'value':topic.match(input_expression[current:]).group('item')
            })
            current = current+topic.match(input_expression[current:]).end()
            continue
        if sentence.match(input_expression[current:]):
            tokens.append({
                'type':'sentence',
                'value': sentence.match(input_expression[current:]).group('item')
            })
            current = current+sentence.match(input_expression[current:]).end()
            continue
        current = current + 1
    return tokens
        
def parser(tokens):
    global current
    current = 0
    global parents
    parents = []
    def walk(aarg):
        global current
        stack = collections.deque()
        while True:
            token = tokens[current]
            if token.get('type') == 'topic':
                parg = Node(token.get('value'), token.get('type'))
                aarg.children.append(parg)
                current = current + 1
                walk(parg)
            elif token.get('type') == 'sentence':
                aarg.children.append(Node(token.get('value'),token.get('type')))
                current = current + 1
            elif token.get('type') == 'left_paren':
                stack.append('{')
                current = current + 1
            elif token.get('type') == 'right_paren':
                stack.pop()
                current = current + 1
            if stack:
                continue
            else:
                return
                
    while current < len(tokens):
        parg = Node(tokens[current].get('value'),tokens[current].get('type'))
        if tokens[current].get('type') == 'topic':
            parents.append(parg)
            current = current + 1
            walk(parg)
    
    return parents
       
# 
def print_tree(current_node, indent="", last='updown'):
    nb_children = lambda node: sum(nb_children(child) for child in node.children) + 1
    size_branch = {child: nb_children(child) for child in current_node.children}
    """ Creation of balanced lists for "up" branch and "down" branch. """
    up = sorted(current_node.children, key=lambda node: nb_children(node))
    down = []
    while up and sum(size_branch[node] for node in down) < sum(size_branch[node] for node in up):
        down.append(up.pop())
    """ Printing of "up" branch. """
    for child in up:     
        next_last = 'up' if up.index(child) is 0 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '│', " " * len(current_node.item))
        print_tree(child, indent=next_indent, last=next_last)
    """ Printing of current node. """
    if last == 'up': start_shape = '┌'
    elif last == 'down': start_shape = '└'
    elif last == 'updown': start_shape = ' '
    else: start_shape = '├'
    if up: end_shape = '┤'
    elif down: end_shape = '┐'
    else: end_shape = ''
    print('{0}{1}{2}{3}'.format(indent, start_shape, current_node.item, end_shape))
    """ Printing of "down" branch. """
    for child in down:
        next_last = 'down' if down.index(child) is len(down) - 1 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '│', " " * len(current_node.item))
        print_tree(child, indent=next_indent, last=next_last)

def main():
    input = '''
              topic:"food"{
	sentence:"I love food",
	sentence:"my favorite food is mola😁",
	topic:"korean food"{
		sentence:"kimchi",
		topic:"tang"{
			sentence:"budaejjigae",
			sentence:"kimchijjigae",
			topic:"seafoodtang"{
				sentence:"haemuljjambbongtang",
			},
			topic:"sogogitang"{
				sentence:"galbijjim",
			}
		},
	},
	topic:"chinese food"{
		sentence:"tanghulu",
		sentence:"tangsuyuk",
		sentence:"jjambbong",
	}
}

topic:"programming"{
    sentence:"not coding",
    topic:"c++"{
        sentence:"adlfkjlsfkgj"
    }
    topic:"java"{
        sentence:"akfjgslfjg"
    }
    topic:"python"{
        sentence:"aldkfjs;lkfgj;sklf",
        sentence:"askfdjg;slkfj;"
    }
}
              '''
    tokens = tokenizer(input)
    maps = []
    roots = parser(tokens)
    for root in roots:
        maps.append(NBT(root))
    
    for map_ in maps:
        print_tree(map_.root)

if __name__ == "__main__":
    main()

