; example2.nsi
;
; This script is based on example1.nsi, but it remember the directory, 
; has uninstall support and (optionally) installs start menu shortcuts.
;
; It will install example2.nsi into a directory that the user selects,

;--------------------------------

; The name of the installer
Name "Zlosnica"

; The file to write
OutFile "zlosnica-setup.exe"

; The default installation directory
InstallDir $PROGRAMFILES\Zlosnica

; Registry key to check for directory (so if you install again, it will 
; overwrite the old one automatically)
InstallDirRegKey HKLM "Software\Zlosnica" "Install_Dir"

; Request application privileges for Windows Vista
RequestExecutionLevel admin

;--------------------------------

; Pages

Page components
Page directory
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles

;--------------------------------

; The stuff to install
Section "Zlosnica (required)"

  SectionIn RO
  
  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  ; Put file there
  File /r "dist\*"
  
  ; Write the installation path into the registry
  WriteRegStr HKLM SOFTWARE\Zlosnica "Install_Dir" "$INSTDIR"
  
  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Zlosnica" "DisplayName" "Zlosnica"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Zlosnica" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Zlosnica" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Zlosnica" "NoRepair" 1
  WriteUninstaller "uninstall.exe"
  
SectionEnd

; Optional section (can be disabled by the user)
Section "Start Menu Shortcuts"

  CreateDirectory "$SMPROGRAMS\Zlosnica"
  CreateShortCut "$SMPROGRAMS\Zlosnica\Uninstall.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0
  CreateShortCut "$SMPROGRAMS\Zlosnica\Zlosnica.lnk" "$INSTDIR\zlosnica.exe" "-g" "$INSTDIR\zlosnica.nsi" 0
  
SectionEnd

;--------------------------------

; Uninstaller

Section "Uninstall"
  
  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Zlosnica"
  DeleteRegKey HKLM SOFTWARE\Zlosnica

  ; Remove files and uninstaller
  Delete $INSTDIR\*
  Delete $INSTDIR\uninstall.exe

  ; Remove shortcuts, if any
  Delete "$SMPROGRAMS\Zlosnica\*.*"

  ; Remove directories used
  RMDir "$SMPROGRAMS\Zlosnica"
  RMDir "$INSTDIR"

SectionEnd
