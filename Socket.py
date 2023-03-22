import socket
import pymysql.cursors
import string

# 连接数据库
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='990319',
                             db='data',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # 创建表格
        cursor.execute("CREATE TABLE IF NOT EXISTS gps_gps ("
                       "id INT(11) NOT NULL AUTO_INCREMENT,"
                       "longitude DECIMAL(9,6) NOT NULL,"
                       "latitude DECIMAL(9,6) NOT NULL,"
                       "PRIMARY KEY (id))")

    # 建立socket连接
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(1)

    while True:
        # 等待客户端连接
        print("等待连接....")
        client_socket, address = server_socket.accept()
        print("新连接")
        print("IP is %s" % address[0])
        print("port is %d\n" % address[1])
        # 从客户端接收数据
        data = client_socket.recv(1024).decode('utf-8')
        if data:
            # 解析数据
            lat, lon = data.split(',')
            latitude=lat.translate(str.maketrans('', '','N'))
            longitude=lon.translate(str.maketrans('','','E'))
            print(latitude)
            # 将数据插入到数据库中
            with connection.cursor() as cursor:
                sql = "INSERT INTO `gps_gps` (`longitude`,`latitude`,`data`)"" VALUES (%s,%s,%s)"
                param=(longitude,latitude,"施工地点")    
                cursor.execute(sql,param)
                connection.commit()

finally:
    connection.close()
