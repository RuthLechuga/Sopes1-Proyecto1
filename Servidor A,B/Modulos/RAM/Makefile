obj-m := RAM.o

KERNELDIR ?= /lib/modules/$(shell uname -r)/build

all default: modules
install: modules_install

modules modules_install help clean:
	$(MAKE) -C $(KERNELDIR) M=$(shell pwd) $@


clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
	
test_uno:
	sudo dmesg -C
	sudo insmod RAM.ko
	sudo cat /proc/RAM
	sudo rmmod RAM.ko
	sudo dmesg