class DSU:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1]*size
        
    def find(self,name_idx):
        if self.parent[name_idx] != name_idx:
            self.parent[name_idx] = self.find(self.parent[name_idx])
            
        return self.parent[name_idx]
        
    def union(self,a,b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if self.rank[root_a] < self.rank[root_b]:
            root_a,root_b = root_b,root_a
            
        self.parent[root_b] = root_a
        self.rank[root_a] += self.rank[root_b]
        
        return self.parent[root_a]
        
class Solution:
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        size = len(accounts)
        union_find = DSU(size)
        
        email_to_name_idx = {}
        
        for name_idx in range(size):
            for email in accounts[name_idx][1:]:
                if email in email_to_name_idx:
                    union_find.union(email_to_name_idx[email],name_idx)
                
                email_to_name_idx[email] = union_find.parent[name_idx]
                
        ans = defaultdict(set)
        
        for name_idx in range(size):
            root_name_idx = union_find.find(name_idx)
            
            for account in accounts[name_idx][1:]:
                ans[root_name_idx].add(account)
            
        result = []
        
        for name_idx,emails in ans.items():
            result.append([accounts[name_idx][0]] + sorted(list(emails)))
            
        return result
                
       