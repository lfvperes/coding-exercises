class Solution(object):
    def decToBinary(self, dec):
        binary = []
        while dec > 0:
            binary.append(dec % 2)
            dec //= 2
        return binary

    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        times = []
        for h in range(12):
            for m in range(60):
                if sum(self.decToBinary(h)) + sum(self.decToBinary(m)) == turnedOn:
                    times.append(f'{h}:{m:02.0f}')
        return times
