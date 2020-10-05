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

static int generar(struct seq_file *m, void *v)
{
	#define K(x) ((x) << (PAGE_SHIFT - 10))
		struct sysinfo i;
		si_meminfo(&i);
		seq_printf(m,"{\n \"Free\" : %8lu , \n  \"Total\" : %8lu \n }",K(i.freeram),K(i.totalram));

		return 0;
	#undef K
}

static int 
abrir(struct inode *inode, struct file *file)
{
	return single_open(file, generar, NULL);
}

static const struct file_operations var_entorno = {
	.owner		= THIS_MODULE,
	.open		= abrir,
	.read		= seq_read,
	.llseek		= seq_lseek,
	.release	= single_release,
};

static int __init 
crear(void)
{
	printk(KERN_INFO ">>Se creo el modulo RAM\n\n");
	proc_create("RAM", 0, NULL, &var_entorno);
	return 0;
}

static void __exit 
salir(void)
{
	printk(KERN_INFO ">>Modulo RAM cargado\n\n");
	remove_proc_entry("RAM", NULL);
}

module_init(crear);
module_exit(salir);

MODULE_AUTHOR("201602975 Ruth Nohemy Ardón Lechuga");
MODULE_DESCRIPTION("--RAM---");
MODULE_LICENSE("GPL");