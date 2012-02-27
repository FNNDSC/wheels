from wheels import *

class WheelOne( Wheel ):
  _in_ = Enum()
  _out_ = Enum( 'data1' )

  def spin():
    import time; time.sleep(5)
    return 'w1'

class WheelTwo( Wheel ):
  _in_ = Enum()
  _out_ = Enum( 'data2' )

  def spin():
    import time; time.sleep(5)
    return 'w2'

class WheelThree( Wheel ):
  _in_ = Enum( 'data2' )
  _out_ = Enum( 'data3' )

  def spin(data2):
    import time; time.sleep(5)
    return data2 + 'w3'

class WheelFour( Wheel ):
  _in_ = Enum( 'data2' )
  _out_ = Enum( 'data4' )

  def spin(data2):
    import time; time.sleep(7)
    return data2 + 'w4'

class WheelFive( Wheel ):
  _in_ = Enum()
  _out_ = Enum( 'data5' )

  def spin():
    import time; time.sleep(10)
    return 'w5'
    
class WheelSix( Wheel ):
  _in_ = Enum( 'data1', 'data3', 'data4' )
  _out_ = Enum( 'data6' )

  def spin(data1, data3, data4):
    import time; time.sleep(5)
    return data1 + data3 + data4 + 'w6'
    
class WheelSeven( Wheel ):
  _in_ = Enum( 'data5', 'data6' )
  _out_ = Enum( )

  def spin(data5, data6):
    print ('>> PATH: ' + data5 + data6 + 'w7THEEND')


# create the Pype
p = Pype()
p.add( WheelOne )
p.add( WheelTwo )
p.add( WheelThree )
p.add( WheelFour )
p.add( WheelFive )
p.add( WheelSix )
p.add( WheelSeven )
p.run()