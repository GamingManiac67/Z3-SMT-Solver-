from z3 import *

FACES=6
FACELETS=9

def rotate_FCW(s):
    return [ 
        [ s[0][6], s[0][3], s[0][0], s[0][7], s[0][4], s[0][1], s[0][8], s[0][5], s[0][2], ],  # new F
        [ s[1][0], s[1][1], s[1][2], s[1][3], s[1][4], s[1][5], s[4][8], s[4][5], s[4][2], ],  # new U
        [ s[3][6], s[3][3], s[3][0], s[2][3], s[2][4], s[2][5], s[2][6], s[2][7], s[2][8], ],  # new D
        [ s[1][6], s[3][1], s[3][2], s[1][7], s[3][4], s[3][5], s[1][8], s[3][7], s[3][8], ],  # new R
        [ s[4][0], s[4][1], s[2][0], s[4][3], s[4][4], s[2][1], s[4][6], s[4][7], s[2][2], ],  # new L
        [ s[5][0], s[5][1], s[5][2], s[5][3], s[5][4], s[5][5], s[5][6], s[5][7], s[5][8], ] ] # new B

def rotate_FH(s):
    return [ 
        [ s[0][8], s[0][7], s[0][6], s[0][5], s[0][4], s[0][3], s[0][2], s[0][1], s[0][0], ],
        [ s[1][0], s[1][1], s[1][2], s[1][3], s[1][4], s[1][5], s[2][2], s[2][1], s[2][0], ],
        [ s[1][8], s[1][7], s[1][6], s[2][3], s[2][4], s[2][5], s[2][6], s[2][7], s[2][8], ],
        [ s[4][8], s[3][1], s[3][2], s[4][5], s[3][4], s[3][5], s[4][2], s[3][7], s[3][8], ],
        [ s[4][0], s[4][1], s[3][6], s[4][3], s[4][4], s[3][3], s[4][6], s[4][7], s[3][0], ],
        [ s[5][0], s[5][1], s[5][2], s[5][3], s[5][4], s[5][5], s[5][6], s[5][7], s[5][8], ] ]

def rotate_FCCW(s):
    return [ 
        [ s[0][2], s[0][5], s[0][8], s[0][1], s[0][4], s[0][7], s[0][0], s[0][3], s[0][6], ],
        [ s[1][0], s[1][1], s[1][2], s[1][3], s[1][4], s[1][5], s[3][0], s[3][3], s[3][6], ],
        [ s[4][2], s[4][5], s[4][8], s[2][3], s[2][4], s[2][5], s[2][6], s[2][7], s[2][8], ],
        [ s[2][2], s[3][1], s[3][2], s[2][1], s[3][4], s[3][5], s[2][0], s[3][7], s[3][8], ],
        [ s[4][0], s[4][1], s[1][8], s[4][3], s[4][4], s[1][7], s[4][6], s[4][7], s[1][6], ],
        [ s[5][0], s[5][1], s[5][2], s[5][3], s[5][4], s[5][5], s[5][6], s[5][7], s[5][8], ] ]

def rotate_UCW(s):
    return [ 
        [ s[3][0], s[3][1], s[3][2], s[0][3], s[0][4], s[0][5], s[0][6], s[0][7], s[0][8], ],
        [ s[1][6], s[1][3], s[1][0], s[1][7], s[1][4], s[1][1], s[1][8], s[1][5], s[1][2], ],
        [ s[2][0], s[2][1], s[2][2], s[2][3], s[2][4], s[2][5], s[2][6], s[2][7], s[2][8], ],
        [ s[5][0], s[5][1], s[5][2], s[3][3], s[3][4], s[3][5], s[3][6], s[3][7], s[3][8], ],
        [ s[0][0], s[0][1], s[0][2], s[4][3], s[4][4], s[4][5], s[4][6], s[4][7], s[4][8], ],
        [ s[4][0], s[4][1], s[4][2], s[5][3], s[5][4], s[5][5], s[5][6], s[5][7], s[5][8], ] ]

def rotate_UH(s):
    return [ 
        [ s[5][0], s[5][1], s[5][2], s[0][3], s[0][4], s[0][5], s[0][6], s[0][7], s[0][8], ],
        [ s[1][8], s[1][7], s[1][6], s[1][5], s[1][4], s[1][3], s[1][2], s[1][1], s[1][0], ],
        [ s[2][0], s[2][1], s[2][2], s[2][3], s[2][4], s[2][5], s[2][6], s[2][7], s[2][8], ],
        [ s[4][0], s[4][1], s[4][2], s[3][3], s[3][4], s[3][5], s[3][6], s[3][7], s[3][8], ],
        [ s[3][0], s[3][1], s[3][2], s[4][3], s[4][4], s[4][5], s[4][6], s[4][7], s[4][8], ],
        [ s[0][0], s[0][1], s[0][2], s[5][3], s[5][4], s[5][5], s[5][6], s[5][7], s[5][8], ] ]

def rotate_UCCW(s):
    return [ 
        [ s[4][0], s[4][1], s[4][2], s[0][3], s[0][4], s[0][5], s[0][6], s[0][7], s[0][8], ],
        [ s[1][2], s[1][5], s[1][8], s[1][1], s[1][4], s[1][7], s[1][0], s[1][3], s[1][6], ],
        [ s[2][0], s[2][1], s[2][2], s[2][3], s[2][4], s[2][5], s[2][6], s[2][7], s[2][8], ],
        [ s[0][0], s[0][1], s[0][2], s[3][3], s[3][4], s[3][5], s[3][6], s[3][7], s[3][8], ],
        [ s[5][0], s[5][1], s[5][2], s[4][3], s[4][4], s[4][5], s[4][6], s[4][7], s[4][8], ],
        [ s[3][0], s[3][1], s[3][2], s[5][3], s[5][4], s[5][5], s[5][6], s[5][7], s[5][8], ] ]

def rotate_DCW(s):
    return [ 
        [ s[0][0], s[0][1], s[0][2], s[0][3], s[0][4], s[0][5], s[4][6], s[4][7], s[4][8], ],
        [ s[1][0], s[1][1], s[1][2], s[1][3], s[1][4], s[1][5], s[1][6], s[1][7], s[1][8], ],
        [ s[2][6], s[2][3], s[2][0], s[2][7], s[2][4], s[2][1], s[2][8], s[2][5], s[2][2], ],
        [ s[3][0], s[3][1], s[3][2], s[3][3], s[3][4], s[3][5], s[0][6], s[0][7], s[0][8], ],
        [ s[4][0], s[4][1], s[4][2], s[4][3], s[4][4], s[4][5], s[5][6], s[5][7], s[5][8], ],
        [ s[5][0], s[5][1], s[5][2], s[5][3], s[5][4], s[5][5], s[3][6], s[3][7], s[3][8], ] ]

def rotate_DH(s):
    return [ 
        [ s[0][0], s[0][1], s[0][2], s[0][3], s[0][4], s[0][5], s[5][6], s[5][7], s[5][8], ],
        [ s[1][0], s[1][1], s[1][2], s[1][3], s[1][4], s[1][5], s[1][6], s[1][7], s[1][8], ],
        [ s[2][8], s[2][7], s[2][6], s[2][5], s[2][4], s[2][3], s[2][2], s[2][1], s[2][0], ],
        [ s[3][0], s[3][1], s[3][2], s[3][3], s[3][4], s[3][5], s[4][6], s[4][7], s[4][8], ],
        [ s[4][0], s[4][1], s[4][2], s[4][3], s[4][4], s[4][5], s[3][6], s[3][7], s[3][8], ],
        [ s[5][0], s[5][1], s[5][2], s[5][3], s[5][4], s[5][5], s[0][6], s[0][7], s[0][8], ] ]

def rotate_DCCW(s):
    return [ 
        [ s[0][0], s[0][1], s[0][2], s[0][3], s[0][4], s[0][5], s[3][6], s[3][7], s[3][8], ],
        [ s[1][0], s[1][1], s[1][2], s[1][3], s[1][4], s[1][5], s[1][6], s[1][7], s[1][8], ],
        [ s[2][2], s[2][5], s[2][8], s[2][1], s[2][4], s[2][7], s[2][0], s[2][3], s[2][6], ],
        [ s[3][0], s[3][1], s[3][2], s[3][3], s[3][4], s[3][5], s[5][6], s[5][7], s[5][8], ],
        [ s[4][0], s[4][1], s[4][2], s[4][3], s[4][4], s[4][5], s[0][6], s[0][7], s[0][8], ],
        [ s[5][0], s[5][1], s[5][2], s[5][3], s[5][4], s[5][5], s[4][6], s[4][7], s[4][8], ] ]

def rotate_RCW(s):
    return [ 
        [ s[0][0], s[0][1], s[2][2], s[0][3], s[0][4], s[2][5], s[0][6], s[0][7], s[2][8], ],
        [ s[1][0], s[1][1], s[0][2], s[1][3], s[1][4], s[0][5], s[1][6], s[1][7], s[0][8], ],
        [ s[2][0], s[2][1], s[5][6], s[2][3], s[2][4], s[5][3], s[2][6], s[2][7], s[5][0], ],
        [ s[3][6], s[3][3], s[3][0], s[3][7], s[3][4], s[3][1], s[3][8], s[3][5], s[3][2], ],
        [ s[4][0], s[4][1], s[4][2], s[4][3], s[4][4], s[4][5], s[4][6], s[4][7], s[4][8], ],
        [ s[1][8], s[5][1], s[5][2], s[1][5], s[5][4], s[5][5], s[1][2], s[5][7], s[5][8], ] ]

def rotate_RH(s):
    return [ 
        [ s[0][0], s[0][1], s[5][6], s[0][3], s[0][4], s[5][3], s[0][6], s[0][7], s[5][0], ],
        [ s[1][0], s[1][1], s[2][2], s[1][3], s[1][4], s[2][5], s[1][6], s[1][7], s[2][8], ],
        [ s[2][0], s[2][1], s[1][2], s[2][3], s[2][4], s[1][5], s[2][6], s[2][7], s[1][8], ],
        [ s[3][8], s[3][7], s[3][6], s[3][5], s[3][4], s[3][3], s[3][2], s[3][1], s[3][0], ],
        [ s[4][0], s[4][1], s[4][2], s[4][3], s[4][4], s[4][5], s[4][6], s[4][7], s[4][8], ],
        [ s[0][8], s[5][1], s[5][2], s[0][5], s[5][4], s[5][5], s[0][2], s[5][7], s[5][8], ] ]

def rotate_RCCW(s):
    return [ 
        [ s[0][0], s[0][1], s[1][2], s[0][3], s[0][4], s[1][5], s[0][6], s[0][7], s[1][8], ],
        [ s[1][0], s[1][1], s[5][6], s[1][3], s[1][4], s[5][3], s[1][6], s[1][7], s[5][0], ],
        [ s[2][0], s[2][1], s[0][2], s[2][3], s[2][4], s[0][5], s[2][6], s[2][7], s[0][8], ],
        [ s[3][2], s[3][5], s[3][8], s[3][1], s[3][4], s[3][7], s[3][0], s[3][3], s[3][6], ],
        [ s[4][0], s[4][1], s[4][2], s[4][3], s[4][4], s[4][5], s[4][6], s[4][7], s[4][8], ],
        [ s[2][8], s[5][1], s[5][2], s[2][5], s[5][4], s[5][5], s[2][2], s[5][7], s[5][8], ] ]

def rotate_LCW(s):
    return [ 
        [ s[1][0], s[0][1], s[0][2], s[1][3], s[0][4], s[0][5], s[1][6], s[0][7], s[0][8], ],
        [ s[5][8], s[1][1], s[1][2], s[5][5], s[1][4], s[1][5], s[5][2], s[1][7], s[1][8], ],
        [ s[0][0], s[2][1], s[2][2], s[0][3], s[2][4], s[2][5], s[0][6], s[2][7], s[2][8], ],
        [ s[3][0], s[3][1], s[3][2], s[3][3], s[3][4], s[3][5], s[3][6], s[3][7], s[3][8], ],
        [ s[4][6], s[4][3], s[4][0], s[4][7], s[4][4], s[4][1], s[4][8], s[4][5], s[4][2], ],
        [ s[5][0], s[5][1], s[2][6], s[5][3], s[5][4], s[2][3], s[5][6], s[5][7], s[2][0], ] ]

def rotate_LH(s):
    return [
        [ s[5][8], s[0][1], s[0][2], s[5][5], s[0][4], s[0][5], s[5][2], s[0][7], s[0][8], ],
        [ s[2][0], s[1][1], s[1][2], s[2][3], s[1][4], s[1][5], s[2][6], s[1][7], s[1][8], ],
        [ s[1][0], s[2][1], s[2][2], s[1][3], s[2][4], s[2][5], s[1][6], s[2][7], s[2][8], ],
        [ s[3][0], s[3][1], s[3][2], s[3][3], s[3][4], s[3][5], s[3][6], s[3][7], s[3][8], ],
        [ s[4][8], s[4][7], s[4][6], s[4][5], s[4][4], s[4][3], s[4][2], s[4][1], s[4][0], ],
        [ s[5][0], s[5][1], s[0][6], s[5][3], s[5][4], s[0][3], s[5][6], s[5][7], s[0][0], ] ]

def rotate_LCCW(s):
    return [ 
        [ s[2][0], s[0][1], s[0][2], s[2][3], s[0][4], s[0][5], s[2][6], s[0][7], s[0][8], ],
        [ s[0][0], s[1][1], s[1][2], s[0][3], s[1][4], s[1][5], s[0][6], s[1][7], s[1][8], ],
        [ s[5][8], s[2][1], s[2][2], s[5][5], s[2][4], s[2][5], s[5][2], s[2][7], s[2][8], ],
        [ s[3][0], s[3][1], s[3][2], s[3][3], s[3][4], s[3][5], s[3][6], s[3][7], s[3][8], ],
        [ s[4][2], s[4][5], s[4][8], s[4][1], s[4][4], s[4][7], s[4][0], s[4][3], s[4][6], ],
        [ s[5][0], s[5][1], s[1][6], s[5][3], s[5][4], s[1][3], s[5][6], s[5][7], s[1][0], ] ]

def rotate_BCW(s):
    return [ 
        [ s[0][0], s[0][1], s[0][2], s[0][3], s[0][4], s[0][5], s[0][6], s[0][7], s[0][8], ],
        [ s[3][2], s[3][5], s[3][8], s[1][3], s[1][4], s[1][5], s[1][6], s[1][7], s[1][8], ],
        [ s[2][0], s[2][1], s[2][2], s[2][3], s[2][4], s[2][5], s[4][0], s[4][3], s[4][6], ],
        [ s[3][0], s[3][1], s[2][8], s[3][3], s[3][4], s[2][7], s[3][6], s[3][7], s[2][6], ],
        [ s[1][2], s[4][1], s[4][2], s[1][1], s[4][4], s[4][5], s[1][0], s[4][7], s[4][8], ],
        [ s[5][6], s[5][3], s[5][0], s[5][7], s[5][4], s[5][1], s[5][8], s[5][5], s[5][2], ] ]

def rotate_BH(s):
    return [ 
        [ s[0][0], s[0][1], s[0][2], s[0][3], s[0][4], s[0][5], s[0][6], s[0][7], s[0][8], ],
        [ s[2][8], s[2][7], s[2][6], s[1][3], s[1][4], s[1][5], s[1][6], s[1][7], s[1][8], ],
        [ s[2][0], s[2][1], s[2][2], s[2][3], s[2][4], s[2][5], s[1][2], s[1][1], s[1][0], ],
        [ s[3][0], s[3][1], s[4][6], s[3][3], s[3][4], s[4][3], s[3][6], s[3][7], s[4][0], ],
        [ s[3][8], s[4][1], s[4][2], s[3][5], s[4][4], s[4][5], s[3][2], s[4][7], s[4][8], ],
        [ s[5][8], s[5][7], s[5][6], s[5][5], s[5][4], s[5][3], s[5][2], s[5][1], s[5][0], ] ]

def rotate_BCCW(s):
    return [ 
        [ s[0][0], s[0][1], s[0][2], s[0][3], s[0][4], s[0][5], s[0][6], s[0][7], s[0][8], ],
        [ s[4][6], s[4][3], s[4][0], s[1][3], s[1][4], s[1][5], s[1][6], s[1][7], s[1][8], ],
        [ s[2][0], s[2][1], s[2][2], s[2][3], s[2][4], s[2][5], s[3][8], s[3][5], s[3][2], ],
        [ s[3][0], s[3][1], s[1][0], s[3][3], s[3][4], s[1][1], s[3][6], s[3][7], s[1][2], ],
        [ s[2][6], s[4][1], s[4][2], s[2][7], s[4][4], s[4][5], s[2][8], s[4][7], s[4][8], ],
        [ s[5][2], s[5][5], s[5][8], s[5][1], s[5][4], s[5][7], s[5][0], s[5][3], s[5][6], ] ]

def rotate(op, st, side, j):
    return If(op==0, rotate_FCW(st)[side][j],
        If(op==1, rotate_FCCW(st)[side][j],
        If(op==2, rotate_UCW(st)[side][j],
        If(op==3, rotate_UCCW(st)[side][j],
        If(op==4, rotate_DCW(st)[side][j],
        If(op==5, rotate_DCCW(st)[side][j],
        If(op==6, rotate_RCW(st)[side][j],
        If(op==7, rotate_RCCW(st)[side][j],
        If(op==8, rotate_LCW(st)[side][j],
        If(op==9, rotate_LCCW(st)[side][j],
        If(op==10, rotate_BCW(st)[side][j],
        If(op==11, rotate_BCCW(st)[side][j],
        If(op==12, rotate_FH(st)[side][j],
        If(op==13, rotate_UH(st)[side][j],
        If(op==14, rotate_DH(st)[side][j],
        If(op==15, rotate_RH(st)[side][j],
        If(op==16, rotate_LH(st)[side][j],
        If(op==17, rotate_BH(st)[side][j],
            rotate_BH(st)[side][j], # default
            ))))))))))))))))))

move_names=["FCW", "FCCW", "UCW", "UCCW", "DCW", "DCCW", "RCW", "RCCW", "LCW", "LCCW", "BCW", "BCCW", "FH", "UH", "DH", "RH", "LH", "BH"]

def colors_to_array_of_ints(s):
    rt=[]
    for c in s:
        if c=='W':
            rt.append(True)
        else:
            rt.append(False)
    return rt

def set_current_state (d):
    F=colors_to_array_of_ints(d["F"])
    U=colors_to_array_of_ints(d["U"])
    D=colors_to_array_of_ints(d["D"])
    R=colors_to_array_of_ints(d["R"])
    L=colors_to_array_of_ints(d["L"])
    B=colors_to_array_of_ints(d["B"])
    return F,U,D,R,L,B # return tuple

init_F, init_U, init_D, init_R, init_L, init_B=set_current_state({"F":"....W..W.", "U":"...W...W.", "D":".......W.", "R":"..W...W..", "L":"......W..", "B":"..W......"})

for STEPS in range(1, 20):
    print ("trying %d steps" % STEPS)

    s=Solver()
    state=[[[Bool('state%d_%d_%d' % (n, side, i)) for i in range(FACELETS)] for side in range(FACES)] for n in range(STEPS+1)]

    op=[Int('op%d' % n) for n in range(STEPS+1)]

    # initial state
    for i in range(FACELETS):
        s.add(state[0][0][i]==init_F[i])
        s.add(state[0][1][i]==init_U[i])
        s.add(state[0][2][i]==init_D[i])
        s.add(state[0][3][i]==init_R[i])
        s.add(state[0][4][i]==init_L[i])
        s.add(state[0][5][i]==init_B[i])

    # "must be" state for one (front/white) face
    for j in range(FACELETS):
        s.add(state[STEPS][0][j]==True)

    for n in range(STEPS):
        for side in range(FACES):
            for j in range(FACELETS):
                s.add(state[n+1][side][j]==rotate(op[n], state[n], side, j))

    if s.check()==sat:
        print ("sat")
        m=s.model()
        for n in range(STEPS):
            print (move_names[int(str(m[op[n]]))])
        exit(0)
