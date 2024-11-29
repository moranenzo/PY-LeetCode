class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices or len(prices) < 2:
            return 0

        # Initialiser le prix minimum rencontré et le profit maximum
        min_price = float('inf')  # Très grand nombre
        max_profit = 0  # Profit maximum initialisé à 0

        # Parcours des prix
        for price in prices:
            # Mettre à jour le prix minimum
            min_price = min(min_price, price)
            # Calculer le profit si on vend aujourd'hui
            current_profit = price - min_price
            # Mettre à jour le profit maximum
            max_profit = max(max_profit, current_profit)

        return max_profit


sol = Solution()

assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5

assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
