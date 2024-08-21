def KMP(pat):
    R=256
    m=len(pat)
    dfa=[[0]*m for r in range(R)]
    dfa[ord(pat[0])][0]=1
    x=0
    for j in range(1, m):
        for c in range(R):
            dfa[c][j] = dfa[c][x]
        dfa[ord(pat[j])][j] = j+1
        x = dfa[ord(pat[j])][x]
    return dfa

def all_elements_in_list_are_zeros (l):
    return all(v==0 for v in l)
def export_dfa_to_graphviz(dfa, fname):
    m=len(dfa[0]) # len of pattern
    f=open(fname,"w")
    f.write("digraph finite_state_machine {\n")
    f.write("rankdir=LR;\n")
    f.write("\n")
    f.write("size=\"8,5\"\n")
    f.write(f"node [shape = doublecircle]; S_0 S_{m};\n")
    f.write("node [shape = circle];\n")
    for state in range(m):
        exits=[]
        for R in range(256):
            next=dfa[R][state]
            if next!=0:
                exits.append((R,next))
        for exit in exits:
            next_state=exit[1]
            label="'"+chr(exit[0])+"'"
            s=f"S_{state}-> S_{next_state} [ label = \"{label}\" ];\n"
            f.write (s)
        s=f"S_{state}-> S_0 [ label = \"other\" ];\n"
        f.write (s)
    f.write("}\n")
    f.close()
    print (f"{fname} written")
def search(dfa, txt):
# simulate operation of DFA on text
    m=len(dfa[0]) # len of pattern
    n=len(txt)
    j=0 # FA state
    i=0
    while i<n and j<m:
        j = dfa[ord(txt[i])][j]
        i=i+1
    if j == m:
        return i- m # found
    return n
# not found



def search_eel(txt):
 # simulate operation of DFA on text
    m=3 # len of pattern
    n=len(txt)
    j=0 # FA state
    i=0 # iterator for txt[]
    while i<n and j<m:
        ch=txt[i]
        if j==0 and ch=='e':
            j=1
        elif j==1 and ch=='e':
            j=2 
        elif j==2 and ch=='e':
            j=2
        elif j==2 and ch=='l':
            j=3
        else:
            j=0 # reset
            i=i+1
    if j == m:
        return i- m # found
    return n
    # not found