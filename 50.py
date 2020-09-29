def kdiff(l, k):
    ans = []
    for i in range(len(l)):
        for j in range(len(l)):
            if abs(l[i] - l[j]) == k and i != j:
                if l[i] not in ans or l[j] not in ans:
                    ans.append(l[i])
                    ans.append(l[j])
    return len(ans) // 2
list = [1, 2, 3, 4, 5]
print(kdiff(list, 1))
