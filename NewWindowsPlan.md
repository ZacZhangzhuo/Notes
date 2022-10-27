# Windows Reinstallation Plan - 28th Oct

This note is for the first windows reinstallation of the laptop.

---

Content

- [Reasons](#reasons)
- [Before Reinstallation: File Backups](#before-reinstallation-file-backups)
- [After Reinstallation: Uninstall Useless Windows Softwares](#after-reinstallation-uninstall-useless-windows-softwares)
- [After Reinstallation: Basic Logins](#after-reinstallation-basic-logins)
- [After Reinstallation: Applications Installation](#after-reinstallation-applications-installation)
- [After Reinstallation: Set Windows start applications (开机启动的程序)](#after-reinstallation-set-windows-start-applications-开机启动的程序)
- [After Reinstallation: Python Environment](#after-reinstallation-python-environment)
- [After Reinstallation: VSCode Settings](#after-reinstallation-vscode-settings)
- [After Reinstallation: new system backups](#after-reinstallation-new-system-backups)

---

## Reasons

- all the prompts (CMD, PowerShell, Anaconda Shell, Azure Cloud Shell) fails.
  ```
  [已退出进程，代码为 4294967295 (0xffffffff)]
  [已退出进程，代码为 4294967295 (0xffffffff)]
  [已退出进程，代码为 2 (0x00000002)]
  ```
- VSCode overload function fails
  ![](NewWindowsPlan/NewWindowsPlan_2022-10-26-09-39-32.png)
- VSCode ghC# Script Parasite cannot load since lack of .NET4.52. However, .NET4.52 cannot be installed since I have had later versions. The only way is to uninstall all the later versions then install .NET4.52.
- 'Code Smile' appears in my laptop. Code: `0x00000000` something.
  ![](NewWindowsPlan/NewWindowsPlan_2022-10-26-11-33-50.png)\
- File categorization is very important: from now on, `C:\` is only for Windows and software applications, `D:\` is for static files.

## Before Reinstallation: File Backups

- [ ] Backup all static files like `/Zac; /Photography; `
- [ ] Backup office license
- [ ] WIFI passwords
- [ ] VSCode purchased plugins
- [ ] VSCode Markdown template
- [ ] Grasshopper plugins and templates
- [ ] Download OneNote article and abandon OneNote. Every WeChat article comes to ArchZ website
- [ ] Figure out how to reinstall Snagit 13, Bandzip(no advertisement), Pot player
- [ ] Download all installation packages of all softwares needed
  

## After Reinstallation: Uninstall Useless Windows Softwares

- [ ] OneNote
- [ ]

## After Reinstallation: Basic Logins

- [ ] Email
      ![](NewWindowsPlan/NewWindowsPlan_2022-10-26-11-53-16.png)
- [ ] Check terminal (CMD)
- [ ] Microsoft Edge

## After Reinstallation: Applications Installation

- [ ] Office (Official)
- [ ] PowerShell
- [ ] Chinese language package (only download for emergency, no use, Windows will be in English).



- NVIDIA series:

  - [ ] NVIDIA FrameView SDK 1.3.8 (Check necessities)
  - [ ] NVIDIA GeForce Experience 3.26.0.154 (Check necessities)
  - [ ] NVIDIA Control Panel (Check necessities)
  - [ ] NVIDIA HD 音频驱动程序 1.3.39.14 (Check necessities)
  - [ ] NVIDIA PhysX 系统软件 9.21 (Check necessities)
  - [ ] NVIDIA USBC Driver 1.46 (Check necessities)
  - [ ] NVIDIA 图形驱动程序 516.94 (Check necessities)

- .NET series:

  - [ ] Microsoft ASP.NET Core 3.1.3 - Shared FrameView
  - [ ] Microsoft Visual C++ 2005
  - [ ] Microsoft Visual C++ 2015-2022 Redistributable 14.32 x64
  - [ ] Microsoft Visual C++ 2015-2022 Redistributable 14.32 x86
  - [ ] .NET SDK 6.0.2
  - [ ] 

- Lenovo series

  - [ ] Lenovo Hotkeys
  - [ ] Facebook Messenger
  - [ ] Thunderbolt 控制中心 (INTEL CORP)
  - [ ] Dolby Vision
  - [ ]

- Adobe suites

  - [ ] Acrobat DC
  - [ ] Illustrator
  - [ ] Photoshop
  - [ ] Premiere

- Custom applications
  - [ ] Github Desktop
  - [ ] Whats App
  - [ ] Miro
  - [ ] TickTick (滴答清单)
  - [ ] Google drive
  - [ ] VSCode (stable version)
  - [ ] TIM
  - [ ] Slack
  - [ ] Facebook (Edge)
  - [ ] Zoom
  - [ ] PrusaSlicer 2.5.0
  - [ ] City art search
  - [ ] DeepL
  - [ ] HiSuite
  - [ ] instagram (Edge)
  - [ ] YouTube (Edge)
  - [ ] GIT
  - [ ] Grammarly
  - [ ] Blender
  - [ ] Snagit 13
  - [ ] Bandzip(no advertisement)
  - [ ] Pot player
  - [ ] Rhino 7 (setting it well after installation)
  - [ ] Unity (2020.3.20f1c1) (2019.4.36f1c1)

## After Reinstallation: Set Windows start applications (开机启动的程序)

- [ ] Google Drive
- [ ] City art search
- [ ] DeepL

## After Reinstallation: Python Environment

- [ ] No Anaconda?

```
pip install ur-rtde
pip install Rhino-stubs

```

## After Reinstallation: VSCode Settings

- [ ] Path check

```
  "python.autoComplete.extraPaths": [
  "C:\\Zac\\19 Github",
  "C:\\Applications\\Rhino 7\\Plug-ins\\IronPython\\Lib",
  "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib",
  "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\scripts"

],
"python.analysis.extraPaths": [
  "C:\\Zac\\19 Github",
  "C:\\Applications\\Rhino 7\\Plug-ins\\IronPython\\Lib",
  "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib",
  "C:\\Users\\Zac\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\scripts"
],
```

- [ ] Path check of System variables
- [ ]

## After Reinstallation: new system backups

- [ ] Backup the Windows registry (注册表)
- [ ] Create Windows system restore origin (系统还原原点)
- [ ]
