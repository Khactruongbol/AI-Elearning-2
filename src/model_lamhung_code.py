#  Nhiem vu:
#    1. Tao danh sach canh ke (adjacency list) dang vong tron
#    2. Ham not_both_eating(Pi, Pj)
#    3. Trace kiem tra rang buoc
#  Interface voi cac cap khac:
#   Nhan: philosophers, domain tu build_problem(n)
#   Cung cap: adj_list, not_both_eating()         

# PHAN 1 - ADJACENCY LIST
# Pi ke voi P(i-1) va P(i+1), vong tron: Pn ke voi P1
def build_adjacency_list(philosophers):
    n   = len(philosophers)
    adj = {}
    for i in range(n):
        left  = philosophers[(i - 1) % n]
        right = philosophers[(i + 1) % n]
        adj[philosophers[i]] = [left, right]
    return adj

# PHAN 2 - HAM not_both_eating(Pi, Pj)
# Ma hoa rang buoc CSP: not (Pi = Eating and Pj = Eating)
def not_both_eating(val_i, val_j):
    return not (val_i == "Eating" and val_j == "Eating")

# PHAN 3 - TRACE KIEM TRA RANG BUOC
# Duyet tung cap ke, goi not_both_eating(), in ket qua chi tiet
def trace_constraints(assignment, adj):
    print("  TRACE KIEM TRA RANG BUOC - Dining Philosophers CSP")

    print("\nAssignment:")
    for p, state in assignment.items():
        print(f"   {p} = {state}")

    print("\nKiem tra tung rang buoc:")

    checked  = set()
    all_ok   = True
    violated = []

    for pi, neighbors in adj.items():
        for pj in neighbors:
            pair = tuple(sorted([pi, pj]))
            if pair in checked:
                continue
            checked.add(pair)

            vi = assignment.get(pi)
            vj = assignment.get(pj)

            if vi is None or vj is None:
                print(f"   {pi}--{pj}: chua gan du, bo qua")
                continue

            ok     = not_both_eating(vi, vj)
            status = "THOA" if ok else "VI PHAM"
            print(f"   {pi}={vi:<8}  |  {pj}={vj:<8}  ->  {status}")

            if not ok:
                all_ok = False
                violated.append(f"{pi}-{pj}")

    if all_ok:
        print("\nKET LUAN: Assignment HOP LE\n")
    else:
        print(f"\nKET LUAN: VI PHAM tai cap: {', '.join(violated)}\n")

    return all_ok
