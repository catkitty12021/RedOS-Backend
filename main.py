# Imports
import keep_alive
from scratchclient import ScratchSession
from replit import db
session = ScratchSession("StickRed_Test", "AlanBecker")
connection = session.create_cloud_connection(543069795)

# Definitions
def user(txt):
  o = list(txt)
  out1 = o[0]
  return out1

def pasw(txt):
  o = list(txt)
  out2 = o[2]
  return out2

a = 1
b = 1
c = 0
d = 0

# Main code
while True:
  a = connection.get_cloud_variable("mode")
  if a == '1':
    b = connection.get_cloud_variable("var")
    connection.set_cloud_variable("mode", 11)
    while d != '12':
      d = connection.get_cloud_variable("mode")
    c = connection.get_cloud_variable("var")
    db[b] = b, ",", c
    connection.set_cloud_variable("mode", 0)
  if a == '2':
    b = connection.get_cloud_variable("var")
    connection.set_cloud_variable("mode", 4)
    while c != '5':
      c = connection.get_cloud_variable("mode")
    c = connection.get_cloud_variable("var")
    d = user(b)
    db[b] = d, ",", c
  if a == '3':
    b = connection.get_cloud_variable("var")
    connection.set_cloud_variable("mode", 4)
    while c != '5':
      c = connection.get_cloud_variable("mode")
    c = connection.get_cloud_variable("var")
    d = user(b)
    db[b] = d, ",", c
  if a == '6':
    d = connection.get_cloud_variable("var")
    hhh = db.keys()
    if d in hhh:
      d = db[d]
      c = user(d)
      b = pasw(d)
      connection.set_cloud_variable("var", c)
      connection.set_cloud_variable("var2", b)
      connection.set_cloud_variable("mode", 8)
    else:
      connection.set_cloud_variable("mode", 7)
      connection.set_cloud_variable("var", '00')

keep_alive.keep_alive()
