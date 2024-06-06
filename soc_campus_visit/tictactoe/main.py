from treelib import Tree

X,O,E = 'X','O',''
SYMBOLS = {X,O}
WINNING_POS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
class TicTacToe(object):
  def __init__(self, Si=[ E ] * 9):
    self.Si = Si
    self.winner = E
    self.Si1s = None
    self.value = None
  def actions(self):
    e_cis = [ ci for ci, Si_ci in enumerate(self.Si) if Si_ci == E ]
    return [ (ci, y) for y in SYMBOLS for ci in e_cis ]
  def transit(self, ai):
    ci, y = ai
    Si1 = self.Si.copy()
    Si1[ci] = y
    return TicTacToe(Si1)
  def successors(self, p):
    if self.Si1s == None:
      self.Si1s = [ (a, self.transit(a)) for a in self.actions() if a[1] == p ]
    return self.Si1s
  def is_terminal(self):
    for a,b,c in WINNING_POS:
      if self.Si[a] in SYMBOLS and self.Si[a] == self.Si[b] and self.Si[b] == self.Si[c]:
        self.winner = self.Si[a]
        return True
    return E not in set(self.Si)
  def utility(self, p=X):
    if self.winner == E:
      return 0
    elif self.winner == p:
      return 1
    else:
      return -1
  def __repr__(self) -> str:
    return '\n'.join([''.join(self.Si[i*3:i*3+3]) for i in range(3)])
  def to_latex(self):
    return '\\ttt{'+"}{".join(self.Si)+'}'
s0 = TicTacToe()
a0 = s0.actions()[1]
s1 = s0.transit(a0)
print(s1)

def minimax(state):
  state.value = max_value(state)
  return [ a for a, next_state in state.successors(X) if next_state.value == state.value ]

def max_value(state):
  if state.is_terminal():
    return state.utility()
  v = float('-inf')
  for a, next_state in state.successors(X):
    next_state.value = min_value(next_state)
    v = max(v, next_state.value)
  return v

def min_value(state):
  if state.is_terminal():
    return state.utility()
  v = float('inf')
  for a, next_state in state.successors(O):
    next_state.value = max_value(next_state)
    v = min(v, next_state.value)
  return v

s = TicTacToe([O,X,E,X,X,O,E,O,E])
s = TicTacToe()
print(minimax(s))

def print_tree(tree, s, a_str, depth=0, max_depth=0):

  if max_depth> 0 and depth>=max_depth:
    print(f"[{{$U\\left({s.to_latex()}\\right)={s.value}$}},edge label={{node[midway,left,font=\scriptsize]{{({a_str})}}}}]")
  elif s.Si1s:
    print('[' + f"{{${s.to_latex()}$}},edge label={{node[midway,left,font=\scriptsize]{{({a_str})}}}}")
    for a, next_s in s.Si1s:
        # [$\ttt{O}{X}{X}{X}{X}{O}{O}{O}{X}$,edge label={node[midway,left,font=\scriptsize]{(8,X)}}]
        a_str = ','.join(map(str, a))
        node_tex = f"${next_s.to_latex()}$,edge label={{node[midway,left,font=\scriptsize]{{({a_str})}}}}"
        
        tree.create_node(node_tex, id(next_s), parent=id(s))
        
        # tree.create_node(f"{a} [{next_s.value}] {next_s.to_latex()}", id(next_s), parent=id(s))
        print_tree(tree, next_s, a_str, depth+1, max_depth)
    print(']')
  else:
    print(f"[{{$U\\left({s.to_latex()}\\right)={s.value}$}},edge label={{node[midway,left,font=\scriptsize]{{({a_str})}}}}]")

tree = Tree()
tree.create_node(s.to_latex(), id(s))
print_tree(tree, s, '', max_depth=1)
# print(tree)