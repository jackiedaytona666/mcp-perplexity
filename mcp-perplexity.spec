# -*- mode: python ; coding: utf-8 -*-
# To build manually use:
# pyinstaller --onefile --name mcp-perplexity src/mcp_perplexity/__init__.py
import os
import sys
from PyInstaller.utils.hooks import collect_data_files

base_path = os.path.dirname(os.path.abspath(SPEC))

a = Analysis(
    ['src/mcp_perplexity/__init__.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src/mcp_perplexity/web/templates', 'mcp_perplexity/web/templates')
    ],
    hiddenimports=[
        'quart.templating',
        'jinja2',
        'jinja2.ext',
        'jinja2.ext.do',
        'jinja2.ext.loopcontrols',
        'jinja2.filters'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='mcp-perplexity',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
