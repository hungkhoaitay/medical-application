from TofDaq import *


if TwTofDaqRunning() == False:
    print 'TofDaq recorder application is not running'
else:
    print 'TofDaq recorder application is running'
    if TwDaqActive() == False:
        print 'No active acquisition'
    else:
        print 'Acquisition active'
    
    print 'NbrSamples:', TwGetDaqParameter('NbrSamples')
    print 'BlockPeriod:', TwGetDaqParameter('BlockPeriod')
    print 'a:', TwGetDaqParameter('a')
    print 'BaseFileName:', TwGetDaqParameter('BaseFileName')

    Rv = TwSetDaqParameter('NbrSamples', '25000')
        
    if Rv==TwSuccess:
        print 'NbrSamples changed to 25000'

    if Rv==TwValueAdjusted:
        print 'NbrSamples changed to', TwGetDaqParameter('NbrSamples')

    someInt = TwGetDaqParameterInt('NbrSamples')
    print 'someInt valid:', someInt

    someInt = TwGetDaqParameterInt('a')
    print 'someInt invalid type:', someInt

    someInt = TwGetDaqParameterInt(None)
    print 'someInt None:', someInt

    someBool = TwGetDaqParameterBool('AutoSaveCombined')
    print 'someBool valid:', someBool

    someBool = TwGetDaqParameterBool('NbrSamples')
    print 'someBool invalid type:', someBool

    someBool = TwGetDaqParameterBool(None)
    print 'someBool None:', someBool

    someFloat = TwGetDaqParameterFloat('a')
    print 'someFloat valid:', someFloat

    someFloat = TwGetDaqParameterFloat('DataPath')
    print 'someFloat invalid type:', someFloat

    someFloat = TwGetDaqParameterFloat(None)
    print 'someFloat None:', someFloat

    someInt64 = TwGetDaqParameterInt64('BlockPeriod')
    print 'someInt64 valid:', someInt64

    someInt64 = TwGetDaqParameterInt64('a')
    print 'someInt64 invalid type:', someInt64

    someInt64 = TwGetDaqParameterInt64(None)
    print 'someInt64 None:', someInt64

    pInt = ctypes.c_int(12345)
    print TwTranslateReturnValue(TwGetDaqParameterIntRef('NbrSamples', pInt))
    print pInt.value

    pFloat = ctypes.c_float(12345.6)
    print TwTranslateReturnValue(TwGetDaqParameterFloatRef('a', pFloat))
    print pFloat.value

    pInt64 = ctypes.c_int64(123456789)
    print TwTranslateReturnValue(TwGetDaqParameterInt64Ref('BlockPeriod', pInt64))
    print pInt64.value


    S = range(1,100)
    M = range(1,100)
    print TwTranslateReturnValue(TwConfigVarNbrMemories(True, S, M))
    
    
             
raw_input('Press Enter...')
