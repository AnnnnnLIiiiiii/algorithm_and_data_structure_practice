'''
1. Definition area: definding moving function and check/add mehtod of nodes.
'''
def Left(y):
    # Movement takes a node with array type. Check_add does the same,
    x = y.copy()
    i = x.index('0')
    if i%3 != 0:
        x[i], x[i-1] = x[i-1], '0'
    return x

def Right(y):
    x = y.copy()
    i = x.index('0')
    if i%3 != 2:
        x[i], x[i+1] = x[i+1], '0'
    return x

def Up(y):
    x = y.copy()
    i = x.index('0')
    if i > 2:
        x[i], x[i-3] = x[i-3], '0'
    return x

def Down(y):
    x = y.copy()
    i = x.index('0')
    if i < 6:
        x[i], x[i+3] = x[i+3], '0'
    return x

def check_add(node, p_num):
    '''
    node is a string, and p_num is the parent number.
    Once the state is proved to be a new state, the nwe node number will be added as a new key into
    the dictionary with the state as corresponding value.
    '''
    node_str = "".join(node)
    if node_str not in Nodes_set:
        Nodes_set.add(node_str)
        n_num = len(Nodes_set)
        Nodes_dict[node_str] = n_num
        NodesInfo.append([n_num,p_num,0])
        Q_rev.append([node, n_num])

def find_all_states(q_rev):
    while q_rev:
        check_node = q_rev[0][0]
        parent_node_num = q_rev[0][1]
        # Movement takes a node with array type. Check_add does the same,
        # expect it transforms the node into a string and compare that with Nodes_set
        check_add(Left(check_node), parent_node_num)
        check_add(Right(check_node), parent_node_num)
        check_add(Up(check_node), parent_node_num)
        check_add(Down(check_node), parent_node_num)
        Q_rev.pop(0)
        



'''
2. The initializing setting part. Let user input the initial node state and define all needed variables. 
'''
init_str = input('Input the initial state of 8 puzzles in from top left to bottom right (without space): ')
#set node_num be 1, which is the node num of initial state
node_num = 1
parent_node_num = 0
init = [[d for d in init_str], node_num]

# Queue for revolution, pop every time once the first element is used
Q_rev = [init]

# Set for checking, only stores string
Nodes_set = {init_str}

# Dictionary to store all states with node_num as key and string of node state as value
Nodes_dict = {init_str: node_num}
NodesInfo = [[node_num, parent_node_num, 0]]




'''
3. Finding all possible states from initial state.
'''
find_all_states(Q_rev)



'''
4. Print above result in txt file.
'''
# Output all possible nodes in txt 
txt_all_node = open("All Possible Nodes.txt","w+")
all_nodes = list(Nodes_dict.keys())
for i in all_nodes:
    node_list = [int(d) for d in i]
    for j in range(0,3): 
        txt_all_node.write("%d " %node_list[j])   
        txt_all_node.write("%d " %node_list[j+3])  
        txt_all_node.write("%d " %node_list[j+3*2])      
    txt_all_node.write("\n")   




'''
5. Let user input the initial and goal states, and find if the goal state is achievable from the initial state. 
'''
init_str = input('Input the initial state of 8 puzzles in from top left to bottom right (without space): ')
#set node_num be 1, which is the node num of initial state
node_num = 1
parent_node_num = 0
init = [[d for d in init_str], node_num]

# Queue for revolution, pop every time once the first element is used
Q_rev = [init]

# Set for checking, only stores string
Nodes_set = {init_str}

# Dictionary to store all states with node_num as key and string of node state as value
Nodes_dict = {init_str: node_num}
NodesInfo = [[node_num, parent_node_num, 0]]


goal_str = input('Input the goal state of 8 puzzles in from top left to bottom right (without space): ')
goal = [d for d in goal_str]

while Q_rev:
    check_node = Q_rev[0][0]
    parent_node_num = Q_rev[0][1]
    # Movement takes a node with array type. Check_add does the same,
    # expect it transforms the node into a string and compare that with Nodes_set
    check_add(Left(check_node), parent_node_num)
    check_add(Right(check_node), parent_node_num)
    check_add(Up(check_node), parent_node_num)
    check_add(Down(check_node), parent_node_num)
    Q_rev.pop(0)
    if goal_str in Nodes_set:
        break

if len(Nodes_set) != 9*8*7*6*5*4*3:
    n_goal = Nodes_dict[goal_str]
    p_s = NodesInfo[n_goal - 1][1]
    path_nums = [n_goal]
    while p_s != 0:
        n_s = p_s
        path_nums.append(n_s)
        p_s = NodesInfo[n_s - 1][1]
    nodepath = []
    x = list(Nodes_dict.keys())
    for i in path_nums: 
        nodepath.append(x[i-1])
    nodepath = nodepath[::-1]
    path_nums = path_nums[::-1]
    print(path_nums)
    print(nodepath)
else:
    print('The goal state cannot be achieved by the given initial state.')




'''
6. Print out node path in txt file.
'''
txt_path = open("nodePath.txt","w+")
for i in nodepath:
    node_list = [int(d) for d in i]
    for j in range(0,3):
        txt_path.write("%d " %node_list[j])   
        txt_path.write("%d " %node_list[j+3])  
        txt_path.write("%d " %node_list[j+3*2])      
    txt_path.write("\n")   



'''
7. Print out nodes being searched from initial to goal in txt file.
'''
txt_node = open("Nodes_searched.txt","w+")
sereached_nodes = list(Nodes_dict.keys())
for i in sereached_nodes:
    node_list = [int(d) for d in i]
    for j in range(0,3): 
        txt_node.write("%d " %node_list[j])   
        txt_node.write("%d " %node_list[j+3])  
        txt_node.write("%d " %node_list[j+3*2])      
    txt_node.write("\n")   



'''
8. Print out NodesInfo in txt file.
'''
txt_info = open("NodesInfo.txt","w+")
for i in NodesInfo:
    for j in i: 
        txt_info.write("%d " %j)        
    txt_info.write("\n")   

