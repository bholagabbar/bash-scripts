sudo ntfsfix /dev/sda7
sudo mkdir -p /media/bholagabbar/"LocalDisk"
sudo mount /dev/sda7 /media/bholagabbar/"LocalDisk"

sudo ntfsfix /dev/sda8
sudo mkdir -p /media/bholagabbar/"ExtHDDS"
sudo mount /dev/sda8 /media/bholagabbar/"ExtHDDS"

sudo ntfsfix /dev/sda4/
sudo mkdir -p /media/bholagabbar/"WindowsPartition"
sudo mount /dev/sda4 /media/bholagabbar/"WindowsPartition"
exit 0
