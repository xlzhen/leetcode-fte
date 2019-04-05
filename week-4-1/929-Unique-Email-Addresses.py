class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        set_email = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0]
            local = ('').join(local.split("."))
            email = local + "@" + domain
            set_email.add(email)
        return len(set_email)
