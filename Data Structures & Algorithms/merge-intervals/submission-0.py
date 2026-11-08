class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])

        new_ins = []

        for start, end in intervals:
            most_recent = None if len(new_ins) == 0 else new_ins[-1]

            if most_recent is None:
                new_ins.append((start,end))
            else:
                if start <= most_recent[1]:
                    new_interval = (most_recent[0], max(end, most_recent[1]))
                    new_ins[-1] = new_interval
                else:
                    new_ins.append((start,end))
        
        return new_ins
        