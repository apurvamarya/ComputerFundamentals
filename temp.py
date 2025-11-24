def solve():
    import sys
    sys.stdin = open('input.txt', 'r')
    input = sys.stdin.readline

    T = int(input())
    for case_num in range(1, T + 1):
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        impossible = False
        operations = []

        # Quick impossibility check
        for i in range(N):
            if B[i] < A[i]:
                impossible = True
                break
        
        if impossible:
            print(f"Case #{case_num}: -1")
            continue

        maxB = max(B)
        # Find an index in A that already has maxB to use as initial source
        if maxB not in A:
            print(f"Case #{case_num}: -1")
            continue

        # Map from value to indices where B[i] == value and A[i] < B[i]
        from collections import defaultdict
        need_increase = defaultdict(list)
        for i in range(N):
            if A[i] < B[i]:
                need_increase[B[i]].append(i)

        # We will propagate temperatures from largest to smallest
        unique_targets = sorted(set(B), reverse=True)
        # Find any index where A[i] == target (to use as source)
        value_to_source = {}
        for val in unique_targets:
            for i in range(N):
                if A[i] == val:
                    value_to_source[val] = i
                    break

        # Perform operations
        for val in unique_targets:
            if val not in need_increase:
                continue
            source_idx = value_to_source[val]
            for idx in need_increase[val]:
                operations.append((idx + 1, source_idx + 1))  # 1-based indexing
                A[idx] = val  # update temperature
            value_to_source[val] = idx  # now any of these can be source

        print(f"Case #{case_num}: {len(operations)}")
        for op in operations:
            print(op[0], op[1])
solve()

