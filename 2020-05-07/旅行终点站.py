import time
class Solution:
    def destCity(paths):
        """最基础方法"""
        mid_list = []
        while len(mid_list) < len(paths) + 1:
            for destination in paths:
                if mid_list == []:
                    mid_list.extend(destination)
                elif destination[0] == mid_list[len(mid_list) - 1]:
                    mid_list.append(destination[1])
                elif destination[1] == mid_list[0]:
                    mid_list.insert(0, destination[0])
        return mid_list[len(mid_list) - 1]

    def destCity2(paths):
        """转置法"""
        transpost=list(zip(*paths))  #将原paths list 转置，transpost[0]为全部起点，transpost[1]为全部重点
        for destination in transpost[1]: #遍历每个终点，如果终点没有在起点出现过，说明他就是最终的终点
            if destination not in transpost[0]:
                return destination

    def destCity3(paths):
        """集合差集法"""
        begin=set()
        end=set()
        for destination in paths:
            begin.add(destination[0])
            end.add(destination[1])
        where = list(end-begin)
        return where[0]

def main():
    begin=time.perf_counter()
    paths=[["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    print(Solution.destCity(paths=paths))
    end=time.perf_counter()
    print(end-begin)

if __name__ == "__main__":
    main()
