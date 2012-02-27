<img src="http://fnndsc.github.com/wheels/artwork/logo.png">

### What is it?

<b>nipypeWheels</b> is an interface for <b>easy pipelining</b> using Nipype (http://nipy.sourceforge.net/nipype/). 
It comes with a <b>Pype and Wheels</b>. The <b>Pype</b> automatically connects <b>Wheels</b> and runs them in a <i>multi-threaded</i> fashion.
Each <b>Wheel</b> is a completely configurable unit. It can execute any python code and attaches to other <b>Wheels</b> using inputs and outputs.

### Get it! ###
<a href="https://github.com/FNNDSC/wheels/zipball/master"><img border="0" width="60" src="https://github.com/images/modules/download/zip.png"></a><a href="https://github.com/FNNDSC/wheels/tarball/master"><img border="0" width="60" src="https://github.com/images/modules/download/tar.png"></a>
<br>Download + Unzip! Then execute <b>python example.py</b> to run the example. Nipype required!

### Example ###
Let's realize a simple workflow. The following image shows how seven different wheels interact and get executed in respect to time. The Wheels get linked automatically by analyzing the inputs and outputs.

<img src="http://fnndsc.github.com/wheels/artwork/example.png">

Here is <b>the code</b>:

    from wheels import *
    
    #
    # (1) Create the seven wheels.
    #
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
    
    #
    # (2) Add them to a Pype
    #
    p = Pype()
    p.add( WheelOne )
    p.add( WheelTwo )
    p.add( WheelThree )
    p.add( WheelFour )
    p.add( WheelFive )
    p.add( WheelSix )
    p.add( WheelSeven )
    #
    # (3) .. now SPIN THA WHEELZ!!
    #
    p.run()

### License ###
Copyright (c) 2012 Fetal Neonatal Neuroimaging and Developmental Science Center, Children's Hospital Boston

This code is licensed under the MIT License: http://www.opensource.org/licenses/mit-license.php

<a href="http://childrenshospital.org/FNNDSC"><img src="http://xtk.github.com/chb_logo.jpg" alt="Children's Hospital Boston" title="Children's Hospital Boston"></a>
<a href="http://hms.harvard.edu"><img src="http://xtk.github.com/hms_logo.jpg" alt="Harvard Medical School" title="Harvard Medical School"></a>