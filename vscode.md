# vscode

## rust development environment

### toolset
- **linter** - [and] syntax highliting, error detection, code suggestion
  - **chalk** - [and] rustc, clippy
- **formatter** - format the code to the standard specification
- **compiler** - compiles code to binary representation targets
- **package manager** - provides [and] dependency management, additional tooling for development
  - testing tooting
  - etc.

### keybindings
#### navigation
- Hold **Ctrl** and press **Tab** to view a list of all files open in an editor group. To open one of these files, use **Tab** again to pick the file you want to navigate to, then release **Ctrl** to open it.
- quick open a file from the workspace - **Ctrl+P**
- Go to Definition **F12** - Go to the source code of the type definition.
- Peek Definition **Ctrl+Shift+F10** - Bring up a Peek window with the type definition.
- Go to References **Shift+F12** - Show all references for the type.
- Show Call Hierarchy **Shift+Alt+H** - Show all calls from or to a function.
- Go to Symbol in File - **Ctrl+Shift+O**.
- Go to Symbol in Workspace **Ctrl+T**.
#### file edits
- Quick Fixes via the **Ctrl+.**.
- Rename Symbol from the context menu, Command Palette, or via **F2**.
- **format document** Ctrl+Shift+I.

