# Windows Reinstallation Plan - 28th Oct 

This note is for the first windows reinstallation of the laptop.

---

Content

- [Reasons](#reasons)
- [Before Reinstallation: File Backups](#before-reinstallation-file-backups)
- [After Reinstallation: Uninstall Useless Windows Softwares](#after-reinstallation-uninstall-useless-windows-softwares)
- [After Reinstallation: Basic Logins](#after-reinstallation-basic-logins)
- [After Reinstallation: Applications Installation](#after-reinstallation-applications-installation)
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

## After Reinstallation: Uninstall Useless Windows Softwares

- [ ]

## After Reinstallation: Basic Logins

- [ ] Email
  ![](NewWindowsPlan/NewWindowsPlan_2022-10-26-11-53-16.png)
- [ ]

## After Reinstallation: Applications Installation
- [ ] Office (Official)


- NVIDIA series:
  - [ ] NVIDIA FrameView SDK 1.3.8 (Check necessities)
  - [ ] NVIDIA GeForce Experience 3.26.0.154 (Check necessities)

- .NET series:

  - [ ]

- Adobe suites


- Custom applications
  - [ ] Github Desktop
  - [ ] 


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