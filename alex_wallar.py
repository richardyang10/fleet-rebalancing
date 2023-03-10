import gurobipy as gp
from gurobipy import GRB

def rebalancing_model(T, H, L, cab_id, station_id,R)
    p = 0.1
    # p is a user-defined variable 
    model_r = gp.Model('alex wallar rebalancing model')

    # variable data structure
    rebalancing_decision_set = {(c, j): None for c in cab_id for j in station_id}


    # Decision variables
    x = model_r.addVars(rebalancing_decision_set, vtype=GRB.BINARY, name='x')

    # Model constraints
    model_r.addConstrs((x.sum(c,'*') <=1 for c in cab_id), name='c1' )
    model_r.addConstrs(((x[c,j]*(H-T[c,j])) >= 0), name='c2')
    model_r.addConstrs((gp.quicksum(x[c,j]*(H-T[c,j]) for c in cab_id) <= R[j] * H * p for j in station_id, name='c3')


    # Model objective
    model_r.setObjective(gp.quicksum(x[c,j]*(H-T[c,j])*R[j]/H for c in cab_id for j in station_id))

    model_r.optimize()

    return x
