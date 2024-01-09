#LIST
scores = [10,20,30,40,50]
friends = ["w","h","i","l","y"]

#取第1位
print(scores[1])

#取前幾位
print(scores[:4])

#LIST排序
scores.sort()
print(scores)

#LIST串接
scores.extend(friends)
print(scores)

#LIST新增
scores.append(60)
print(scores)

#LIST插入
scores.insert(2,35)
print(scores)

#LIST刪除
scores.remove(50)
print(scores)

#LIST最後一位刪除
scores.pop()
print(scores)

#LIST反轉
scores.reverse()
print(scores)