#include <client/linux/handler/exception_handler.h>

#include <iostream>
#include <experimental/filesystem>
namespace fs = std::experimental::filesystem;

static bool dumpCallback(const google_breakpad::MinidumpDescriptor& descriptor, void* context __attribute__ ((unused)), bool succeeded) {
	if (succeeded) {
		std::cerr << "Minidump path: " << descriptor.path() << std::endl;
	} else {
		std::cerr << "CRITICAL: unable to save minidump!" << std::endl;
	}
	return succeeded;
}

void crash() {
	volatile int* wrongAddress = (int*)(NULL);
	*wrongAddress = 1;
}

int main() {
	google_breakpad::MinidumpDescriptor descriptor(fs::current_path());
	google_breakpad::ExceptionHandler eh(descriptor, NULL, dumpCallback, NULL, true, -1);
	crash();
	return 0;
}