class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i] == "C":
                record.pop()
            elif operations[i] == "+" and len(record) >= 2:
                sum_ = 0
                sum_ = int(record[-1]) + int(record[-2])
                record.append(sum_)
            elif operations[i] == "D" and len(record) >= 1:
                double = 1
                double = int(record[-1])*2
                record.append(double)
            else:
                record.append(int(operations[i]))
        sum_ = sum(record)
        return sum_


