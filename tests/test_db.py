import sqlite3

def test_order_status_in_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE orders (id INT, status TEXT)')
    cursor.execute("INSERT INTO orders VALUES (1, 'pending')")
    cursor.execute('SELECT status FROM orders WHERE id = 1')
    result = cursor.fetchone()[0]
    assert result == 'pending'
    print("数据库校验测试通过！")
    conn.close()