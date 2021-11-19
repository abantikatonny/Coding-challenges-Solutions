class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        Total_count = 0
        for types, unit in boxTypes:
            if truckSize <= types:
                Total_count += truckSize * unit
                break

            Total_count += types * unit
            truckSize -= types

        return Total_count


