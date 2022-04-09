# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['D:/Ministerstwo Kalibracyjne/PyCharm_Projects/Isle_of_Ansur/main.py'],
             pathex=['D:/Ministerstwo Kalibracyjne/PyCharm_Projects/Isle_of_Ansur/system/cache/pyinstaller'],
             binaries=[],
             datas=[('D:/Ministerstwo Kalibracyjne/PyCharm_Projects/Isle_of_Ansur/saves', 'D:/Ministerstwo Kalibracyjne/PyCharm_Projects/builds/saves'), ('D:/Ministerstwo Kalibracyjne/PyCharm_Projects/Isle_of_Ansur/docs', 'D:/Ministerstwo Kalibracyjne/PyCharm_Projects/builds/docs'), ('D:/Ministerstwo Kalibracyjne/PyCharm_Projects/Isle_of_Ansur/stats', 'D:/Ministerstwo Kalibracyjne/PyCharm_Projects/builds/stats'), ('D:/Ministerstwo Kalibracyjne/PyCharm_Projects/Isle_of_Ansur/worlds', 'D:/Ministerstwo Kalibracyjne/PyCharm_Projects/builds/worlds')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Isle of Ansur',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='D:\\Ministerstwo Kalibracyjne\\PyCharm_Projects\\Isle_of_Ansur\\utils\\assets\\icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=False,
               upx_exclude=[],
               name='Isle of Ansur')
