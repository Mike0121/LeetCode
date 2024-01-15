class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        HashMap = defaultdict(int)

        for email in emails:

            local = email.split("@")[0]
            domain = email.split("@")[1]

            local = local.replace(".", "")
            local = local.split("+")[0]

            HashMap[local + "@" + domain] += 1

        return len(HashMap)