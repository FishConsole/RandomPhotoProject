import os
import sqlite3


# 创建或打开sqlite数据库
conn = sqlite3.connect(os.path.join('../数据库', '图片信息资源.db'))
# 创建游标对象
cur = conn.cursor()
# 创建表
cur.execute("CREATE TABLE IF NOT EXISTS users (id, name, age)")
# 插入数据
cur.execute("INSERT INTO users VALUES (1, 'Alice', 20)")
# 查询数据
cur.execute("SELECT * FROM users")
row = cur.fetchone()
print(row)
# 关闭连接
conn.close()
