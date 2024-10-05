The error message `'uvicorn' is not recognized as an internal or external command` usually means that either Uvicorn is not installed or it's not available in your system's `PATH`.

### To resolve this issue, follow these steps:

#### Step 1: Verify Uvicorn Installation

First, make sure Uvicorn is installed. In your terminal (Command Prompt or PowerShell), run:

``` bash
pip show uvicorn
```

If Uvicorn is not installed, you will not see any output, or it will mention that the package is not found. In that case, install it with:

```bash
pip install uvicorn[standard]
```

#### Step 2: Add Python to Environment Variables (if needed)

If Uvicorn is installed but still shows the error, it's possible that the Python `Scripts` folder (where Uvicorn is installed) is not in your system's PATH.

To add Python and its scripts to your PATH on Windows:

1. **Find the Python Path**: 
   - Open the terminal (Command Prompt or PowerShell) and run:
   
   ```bash
   where python
   where pip
   ```

   This will show you the locations of your Python installation and the `Scripts` folder. Example output might look like this:
   
   ```
   C:\Users\YourUsername\AppData\Local\Programs\Python\Python39\python.exe
   C:\Users\YourUsername\AppData\Local\Programs\Python\Python39\Scripts\pip.exe
   ```

2. **Add Paths to Environment Variables**:
   - Copy the folder paths for both the Python executable and the `Scripts` directory (e.g., `C:\Users\YourUsername\AppData\Local\Programs\Python\Python39\Scripts\`).
   - Right-click on **This PC** or **My Computer**, select **Properties**, and then click **Advanced system settings**.
   - In the **System Properties** window, click the **Environment Variables** button.
   - Under **System variables**, find the **Path** variable and click **Edit**.
   - Add the paths you copied earlier (one for Python and one for the `Scripts` folder) by clicking **New** and pasting each one.

3. **Apply Changes**:
   - Click **OK** to apply changes and close all windows.

#### Step 3: Test Uvicorn

After adding Python to your `PATH`, restart your terminal and try running Uvicorn again:

```bash
uvicorn main:app --reload
```

This should now work. Let me know if you face any other issues!