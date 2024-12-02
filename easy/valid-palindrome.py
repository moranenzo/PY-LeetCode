class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Deux pointeurs pour vérifier les extrémités
        left, right = 0, len(s) - 1

        while left < right:
            # Ignorer les caractères non alphanumériques à gauche
            while left < right and not s[left].isalnum():
                left += 1
            # Ignorer les caractères non alphanumériques à droite
            while left < right and not s[right].isalnum():
                right -= 1
            # Comparer les caractères en minuscule
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
