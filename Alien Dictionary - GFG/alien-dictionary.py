#User function Template for python3
from collections import defaultdict

class Solution:
    def findOrder(self,alien_dict, N, K):
        
        def dfs(node):
            if node in visited:
                return
            
            for neighbour in graph[node]:
                dfs(neighbour)
                
            alphabet_order_rev.append(node)
            visited.add(node)
            return
                    
            
            
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for idx in range(N-1):
            size = min(len(alien_dict[idx]),len(alien_dict[idx+1]))
            for i in range(size):
                if alien_dict[idx][i] != alien_dict[idx+1][i]:
                    graph[alien_dict[idx][i]].append(alien_dict[idx+1][i])
                    indegree[alien_dict[idx+1][i]] += 1
                    break
        
        todo = []
        
        for ascii in range(ord('a'),ord('a')+k):
            letter = chr(ascii)
            if indegree[letter] == 0:
                todo.append(letter)
        
        alphabet_order_rev = []
        visited = set()
        
        for node in todo:
            dfs(node)
            
        return alphabet_order_rev[::-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends