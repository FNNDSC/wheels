import nipype.pipeline.engine as pe
import time, random, socket, md5, multiprocessing

def uuid( *args ):
  """
    Generates a universally unique ID.
    Any arguments only create more randomness.
  """
  t = long( time.time() * 1000 )
  r = long( random.random() * 100000000000000000L )
  try:
    a = socket.gethostbyname( socket.gethostname() )
  except:
    # if we can't get a network address, just imagine one
    a = random.random() * 100000000000000000L
  data = str( t ) + ' ' + str( r ) + ' ' + str( a ) + ' ' + str( args )
  data = md5.md5( data ).hexdigest()
  return data

class Pype():

  def __init__( self ):
    '''
    '''
    self.__workflow = pe.Workflow( name='nipypeWheels' + str( uuid() ) )
    self.__wheels = []

  def add( self, wheel ):
    '''
    '''
    self.__wheels.append( wheel )

  def run( self, multiThreaded=True ):
    '''
    '''
    print "nipypeWheels v0.2"
    print "-----------------"
    self.__connect()
    print "--"
    print "-- spin tha wheelz.."
    print "-----------------"
    print
    if multiThreaded:
      self.__workflow.run( plugin='MultiProc', plugin_args={'n_procs':multiprocessing.cpu_count()} )
    else:
      # run only single threaded
      self.__workflow.run()

  def __connect( self ):
    '''
    '''
    wheels = self.__wheels

    # this is expensive - but who cares?
    for w in wheels:
      wheel1 = w()
      _ins = w._in_.keys()
      for _i in _ins:
        value = w._in_.get( _i )
        if value != _i:
          # we have a default value set up
          setattr( wheel1.inputs, _i, value )

      outs = w._out_.keys()
      for o in outs:
        for w2 in wheels:
          wheel2 = w2()
          ins = w2._in_.keys()
          for i in ins:
            if i == o:
              print "-- connecting [" + str( w.__name__ ) + "._out_." + str( o ) + "] to [" + str( w2.__name__ ) + "._in_." + str( i ) + "]"
              self.__workflow.connect( wheel1, eval( 'w._out_.' + str( o ) ), wheel2, eval( 'w2._in_.' + str( o ) ) )

