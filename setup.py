from cx_Freeze import setup, Executable
import os
script = 'main.py'
include_files = [
    ('file', 'file'),
    ('server', 'server'),
    ('utils', 'utils'),
    ('requirements.txt', '.'),
    ('.env', '.'),
    (os.path.join(os.getenv('VIRTUAL_ENV'), 'Lib', 'site-packages', 'wcferry', 'sdk.dll'), 'wcferry')
]
build_exe_options = {
    'packages': ['os', 'sys', 'threading', 'logging', 'wcferry'],
    'include_files': include_files
}
setup(
    name='YourAppName',
    version='1.0',
    description='Your application description',
    options={'build_exe': build_exe_options},
    executables=[Executable(script, base=None)]
) 