# -*- mode: python -*-
a = Analysis(['.\jpylyzer\jpylyzer.py'],
             pathex=['.\jpylyzer'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\jpylyzer', 'jpylyzer.exe'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries +
               [('./license/LICENSE.txt','LICENSE','DATA')],
               [('./doc/jpylyzerUserManual.pdf','./jpylyzer/doc/jpylyzerUserManual.pdf','DATA')],
               [('./example_files/balloon.jp2','./jpylyzer/example_files/balloon.jp2','DATA')],
               [('./example_files/balloon_trunc1.jp2','./jpylyzer/example_files/balloon_trunc1.jp2','DATA')],
               [('./example_files/balloon_trunc2.jp2','./jpylyzer/example_files/balloon_trunc2.jp2','DATA')],
               [('./example_files/balloon_trunc3.jp2','./jpylyzer/example_files/balloon_trunc3.jp2','DATA')],
               [('./example_files/readme.txt','./jpylyzer/example_files/readme.txt','DATA')],
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist_win32', 'jpylyzer'))
