obj-m := CPU.o

KERNELDIR ?= /lib/modules/$(shell uname -r)/build

all default: modules
install: modules_install

modules modules_install help clean:
	$(MAKE) -C $(KERNELDIR) M=$(shell pwd) $@
insert:
	sudo insmod CPU.ko
	sudo dmesg
	sudo cat /proc/CPU

desinsert:
	sudo rmmod CPU.ko
	sudo dmesg	

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
