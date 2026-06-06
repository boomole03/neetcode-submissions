class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        """
        create a map from an email to another

        "neet@gmail.com" -> "neet_dsa@gmail.com"
        """

        account_map = defaultdict(set)
        owner_map = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                account_map[email].add(first_email)
                account_map[first_email].add(email)
                owner_map[email] = name

        shared_accounts = []
        seen = set()

        def dfs(email, c):
            seen.add(email)
            c.append(email)
            for e in account_map[email]:
                if e not in seen:
                    dfs(e, c)
        
        for email in account_map:
            if email not in seen: 
                connects = []
                dfs(email, connects)
                shared_accounts.append(connects)

        res = []

        for shared in shared_accounts:
            res.append([owner_map[shared[0]]] + sorted(shared))

        return res

