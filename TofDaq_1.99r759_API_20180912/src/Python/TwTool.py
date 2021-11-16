import ctypes as ct
from numpy.ctypeslib import ndpointer
import numpy as np
import os
import sys

libname = {'linux':'libtwtool.so', 'linux2':'libtwtool.so', 'darwin':'libtwtool.dylib', 'win32':'TwToolDll.dll'}
toollib = ct.cdll.LoadLibrary(os.path.join(os.path.dirname(os.path.abspath(__file__)), libname[sys.platform]))

tof2mass = toollib.TwTof2Mass if os.name=='posix' else toollib._TwTof2Mass
def TwTof2Mass(tofSample, massCalibMode, p):
    tof2mass.restype = ct.c_double
    if isinstance(p, np.ndarray):
        tof2mass.argtypes = [ct.c_double, ct.c_int, ndpointer(np.float64)]
    else:
        tof2mass.argtypes = [ct.c_double, ct.c_int, ct.POINTER(ct.c_double)]
    return tof2mass(tofSample, massCalibMode, p)

mass2tof = toollib.TwMass2Tof if os.name=='posix' else toollib._TwMass2Tof
def TwMass2Tof(mass, massCalibMode, p):
    mass2tof.restype = ct.c_double
    if isinstance(p, np.ndarray):
        mass2tof.argtypes = [ct.c_double, ct.c_int, ndpointer(np.float64)]
    else:
        mass2tof.argtypes = [ct.c_double, ct.c_int, ct.POINTER(ct.c_double)]
    return mass2tof(mass, massCalibMode, p)

translaterv = toollib.TwTranslateReturnValue if os.name=='posix' else toollib._TwTranslateReturnValue
def TwTranslateReturnValue(ReturnValue):
    translaterv.argtypes = [ct.c_int]
    translaterv.restype = ct.c_char_p
    return translaterv(ReturnValue)

fitsinglepeak = toollib.TwFitSinglePeak if os.name=='posix' else toollib._TwFitSinglePeak
def TwFitSinglePeak(nbrDataPoints, yVals, xVals, peakType, blOffset, blSlope, amplitude, fwhmLo, fwhmHi, peakPos, mu):    
    if isinstance(yVals, np.ndarray):
        fitsinglepeak.argtypes = [ct.c_int, ndpointer(np.float64, shape=nbrDataPoints), ndpointer(np.float64, shape=nbrDataPoints), ct.c_int, ndpointer(np.float64, shape=1), ndpointer(np.float64, shape=1), ndpointer(np.float64, shape=1), ndpointer(np.float64, shape=1), ndpointer(np.float64, shape=1), ndpointer(np.float64, shape=1), ndpointer(np.float64, shape=1)]
    else:
        fitsinglepeak.argtypes = [ct.c_int, ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.c_int, ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.POINTER(ct.c_double)]
    return fitsinglepeak(nbrDataPoints, yVals, xVals, peakType, blOffset, blSlope, amplitude, fwhmLo, fwhmHi, peakPos, mu)

fitsinglepeak2 = toollib.TwFitSinglePeak2 if os.name=='posix' else toollib._TwFitSinglePeak2
def TwFitSinglePeak2(nbrDataPoints, yVals, xVals, peakType, param):
    if isinstance(yVals, np.ndarray):
        fitsinglepeak2.argtypes = [ct.c_int, ndpointer(np.float64, shape=nbrDataPoints), ndpointer(np.float64, shape=nbrDataPoints), ct.c_int,  ndpointer(np.float64, shape=7)]   
    else:
        fitsinglepeak2.argtypes = [ct.c_int, ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.c_int, ct.POINTER(ct.c_double)]   
    return fitsinglepeak2(nbrDataPoints, yVals, xVals, peakType, param)

evalsinglepeak = toollib.TwEvalSinglePeak if os.name=='posix' else toollib._TwEvalSinglePeak
def TwEvalSinglePeak(xVal, param):
    evalsinglepeak.restype = ct.c_double
    if isinstance(param, np.ndarray):
        evalsinglepeak.argtypes = [ct.c_double, ndpointer(np.float64, shape=7)]
    else:
        evalsinglepeak.argtypes = [ct.c_double, ct.POINTER(ct.c_double)]   
    return evalsinglepeak(xVal, param)

getmoleculemass = toollib.TwGetMoleculeMass if os.name=='posix' else toollib._TwGetMoleculeMass
def TwGetMoleculeMass(molecule, mass):
    if isinstance(mass, np.ndarray):
        getmoleculemass.argtypes = [ct.c_char_p, ndpointer(np.float64, shape=1)]
    else:
        getmoleculemass.argtypes = [ct.c_char_p, ct.POINTER(ct.c_double)]   
    return getmoleculemass(molecule, mass)

multipeakfit = toollib.TwMultiPeakFit if os.name=='posix' else toollib._TwMultiPeakFit
def TwMultiPeakFit(nbrDataPoints, dataX, dataY, nbrPeaks, mass, intensity, commonPar, options):
    if isinstance(dataX, np.ndarray):
        multipeakfit.argtypes = [ct.c_int, ndpointer(np.float64, shape=nbrDataPoints), ndpointer(np.float64, shape=nbrDataPoints), ct.c_int, ndpointer(np.float64, shape=nbrPeaks), ndpointer(np.float64, shape=nbrPeaks), ndpointer(np.float64, shape=6), ct.c_int]
    else:
        multipeakfit.argtypes = [ct.c_int, ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.c_int, ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.c_int]
    return multipeakfit(nbrDataPoints, dataX, dataY, nbrPeaks, mass, intensity, commonPar, options)

evalmultipeak = toollib.TwEvalMultiPeak if os.name=='posix' else toollib._TwEvalMultiPeak
def TwEvalMultiPeak(x, nbrPeaks, mass, intensity, commonPar):
    evalmultipeak.restype = ct.c_double
    if isinstance(mass, np.ndarray):
        evalmultipeak.argtypes = [ct.c_double, ct.c_int, ndpointer(np.float64, shape=nbrPeaks), ndpointer(np.float64, shape=nbrPeaks), ndpointer(np.float64, shape=6)]
    else:
        evalmultipeak.argtypes = [ct.c_double, ct.c_int, ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.POINTER(ct.c_double)]   
    return evalmultipeak(x, nbrPeaks, mass, intensity, commonPar)

fitresolution = toollib.TwFitResolution if os.name=='posix' else toollib._TwFitResolution
def TwFitResolution(nbrPoints, mass, resolution, R0, m0, dm):
    if isinstance(mass, np.ndarray):
        fitresolution.argtypes = [ct.c_int, ndpointer(np.float64, shape=nbrPoints), ndpointer(np.float64, shape=nbrPoints), ndpointer(np.float64, shape=1), ndpointer(np.float64, shape=1), ndpointer(np.float64, shape=1)]
    else:
        fitresolution.argtypes = [ct.c_int, ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.POINTER(ct.c_double), ct.POINTER(ct.c_double)]
    return fitresolution(nbrPoints, mass, resolution, R0, m0, dm)

evalresolution = toollib.TwEvalResolution if os.name=='posix' else toollib._TwEvalResolution
def TwEvalResolution(R0, m0, dm, mass):
    evalresolution.restype = ct.c_double
    evalresolution.argtypes = [ct.c_double, ct.c_double, ct.c_double, ct.c_double]
    return evalresolution(R0, m0, dm, mass)
    


