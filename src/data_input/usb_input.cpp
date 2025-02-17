#include <iostream>
#include <fstream>
#include <fcntl.h>
#include <unistd.h>
#include <termios.h>
#include <string.h>

#define USB_PORT "/dev/ttyUSB0" // Change this to match your system (e.g., COM3 on Windows)
#define OUTPUT_FILE "data.bin"  // Binary file for raw data storage

void configure_serial(int fd) {
    struct termios tty;
    memset(&tty, 0, sizeof tty);
    
    if (tcgetattr(fd, &tty) != 0) {
        std::cerr << "Error getting terminal attributes\n";
        return;
    }

    cfsetospeed(&tty, B115200); // Set baud rate
    cfsetispeed(&tty, B115200);
    
    tty.c_cflag = (tty.c_cflag & ~CSIZE) | CS8; // 8-bit chars
    tty.c_iflag &= ~IGNBRK;                     // Disable break processing
    tty.c_lflag = 0;                            // No signaling chars, no echo
    tty.c_oflag = 0;                            // No remapping, no delays

    tty.c_cc[VMIN] = 1;  // Read at least 1 byte
    tty.c_cc[VTIME] = 1; // Wait time

    if (tcsetattr(fd, TCSANOW, &tty) != 0) {
        std::cerr << "Error setting terminal attributes\n";
    }
}

int main() {
    // Open USB serial port
    int fd = open(USB_PORT, O_RDWR | O_NOCTTY | O_SYNC);
    if (fd == -1) {
        std::cerr << "Error opening " << USB_PORT << "\n";
        return 1;
    }

    configure_serial(fd);
    
    std::ofstream file(OUTPUT_FILE, std::ios::binary); // Open file for binary writing
    if (!file) {
        std::cerr << "Error opening output file\n";
        close(fd);
        return 1;
    }

    char buffer[256];
    int bytes_read;

    std::cout << "Reading data from USB and saving to " << OUTPUT_FILE << "...\n";

    while (true) { // Continuous reading
        bytes_read = read(fd, buffer, sizeof(buffer));
        if (bytes_read > 0) {
            file.write(buffer, bytes_read);
            std::cout << "Received " << bytes_read << " bytes\n";
        }
    }

    file.close();
    close(fd);
    return 0;
}
