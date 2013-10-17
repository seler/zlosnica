from distutils.core import setup
import py2exe

setup(console=[{"script":"zlosnica.py"}], windows=[{"script":"zlosnica_gui.py"}], options={"py2exe":{"includes":["sip"]}})
