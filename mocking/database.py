import db_driver


class DatabaseManager:

  def __init__(self, uri, user, password):
    self.uri = uri
    self.user = user
    self.password = password
    self.conn = None

  def connect(self):
    self.conn = db_driver.connect(uri=self.uri,
                                  user=self.user,
                                  password=self.password)

  def insert(self, table, data):
    values = ', '.join([value for value in data.values()])
    query = "INSERT INTO {} VALUES ({})".format(table, values)
    self.conn.execute(query)
    self.conn.commit()

  def read(self, table, data):
    query = "SELECT * FROM {} WHERE id = {}".format(table, data['id'])
    result = self.conn.execute(query)
    return dict(result)

  def list(self, table):
    query = "SELECT * FROM {}".format(table)
    result = self.conn.execute(query)
    return list(result)

