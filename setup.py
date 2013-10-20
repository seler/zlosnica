from distutils.core import setup
import py2exe

setup(
    windows=[{"script": "zlosnica.py"}],
    options={"py2exe": {"includes": ["sip"]}},
    data_files=[
	('.', ['msvcp90.dll']),
    ]
)

"""
        ('C:\\Windows\\System32\\', [
		'oleaut32.dll',
		'USER32.dll',
		'IMM32.dll',
		'SHELL32.dll',
		'ole32.dll',
		'WINMM.dll',
		'COMDLG32.dll',
		'ADVAPI32.dll',
		'MSVCP90.dll',
		'WS2_32.dll',
		'WINSPOOL.DRV',
		'GDI32.dll',
		'KERNEL32.dll'
	    ]
	),
"""
