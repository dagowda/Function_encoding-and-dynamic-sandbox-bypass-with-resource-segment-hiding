#include <windows.h>
#include <iostream>
#include <string>

int main() {
    // Get the full path of the executable
    char fullPath[MAX_PATH];
    if (GetModuleFileNameA(NULL, fullPath, MAX_PATH) == 0) {
        std::cerr << "Failed to get the executable path! Error: " << GetLastError() << std::endl;
        return 1;
    }

    // Command to launch a helper process
    std::string command = "cmd.exe /C timeout 5 && del \"" + std::string(fullPath) + "\"";

    // Launch the helper process
    STARTUPINFOA si = { sizeof(STARTUPINFOA) };
    PROCESS_INFORMATION pi = {};

    if (!CreateProcessA(NULL, command.data(), NULL, NULL, FALSE, CREATE_NO_WINDOW, NULL, NULL, &si, &pi)) {
        std::cerr << "Failed to launch deletion process! Error: " << GetLastError() << std::endl;
        return 1;
    }

    // Close process and thread handles
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    std::cout << "Executable will self-delete in 5 seconds." << std::endl;

    return 0;
}
