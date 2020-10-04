#include <linux/module.h>
#include <linux/fs.h>
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/proc_fs.h>
#include <linux/seq_file.h>
#include <linux/mman.h>
#include <linux/mmzone.h>
#include <linux/swap.h>
#include <linux/vmstat.h>
#include <linux/atomic.h>
#include <linux/vmalloc.h>

void __attribute__((weak)) arch_report_meminfo(struct seq_file *m){}

static int hrrp_proc_show(struct seq_file *m, void *v)
{
	#define K(x) ((x) << (PAGE_SHIFT - 10))
		struct sysinfo i;
		si_meminfo(&i);
		seq_printf(m,"{\n \"FreeRam\" : %8lu , \n  \"TotalRam\" : %8lu \n }",K(i.freeram),K(i.totalram));

		return 0;
	#undef K
}

static int 
hrrp_proc_open(struct inode *inode, struct file *file)
{
	return single_open(file, hrrp_proc_show, NULL);
}

static const struct file_operations hrrp_proc_fops = {
	.owner		= THIS_MODULE,
	.open		= hrrp_proc_open,
	.read		= seq_read,
	.llseek		= seq_lseek,
	.release	= single_release,
};

static int __init 
hrrp_proc_init(void)
{
	printk(KERN_INFO "ModuloRamHR loaded successfully!\n\n");
	proc_create("ModuloRamHR", 0, NULL, &hrrp_proc_fops);
	return 0;
}

static void __exit 
hrrp_proc_exit(void)
{
	printk(KERN_INFO "ModuloRamHR unloaded successfully!\n\n");
	remove_proc_entry("ModuloRamHR", NULL);
}

module_init(hrrp_proc_init);
module_exit(hrrp_proc_exit);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("201602975");
MODULE_DESCRIPTION("");