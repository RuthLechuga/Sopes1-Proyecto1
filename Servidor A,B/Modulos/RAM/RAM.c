#include <linux/module.h>
#include <linux/moduleparam.h>
#include <linux/init.h>
#include <linux/kernel.h>   
#include <linux/proc_fs.h>
#include <linux/uaccess.h>
#include <linux/fs.h>
#include <linux/utsname.h>
#include <linux/mm.h>
#include <linux/swapfile.h>
#include <linux/seq_file.h>
#define BUFSIZE  1000

unsigned long copy_to_user(void __user *to,const void *from, unsigned long n);
unsigned long copy_from_user(void *to,const void __user *from,unsigned long n);
MODULE_LICENSE("RAM G8");
MODULE_AUTHOR("G8");
struct sysinfo i;

static struct proc_dir_entry *ent;

static ssize_t mywrite(struct file *file, const char __user *ubuf,size_t count, loff_t *ppos) 
{
    printk( KERN_DEBUG "write handler\n");
    return -1;
}


static int myread (struct seq_file *buff, void *v){

    printk( KERN_DEBUG "read handler\n");
    si_meminfo(&i);
    seq_printf(buff,"{\"total\":%ld, \"libre\": %ld}", i.totalram, i.freeram);
    
    return 0;
}


static int proc_init (struct inode *inode, struct file *file){
    return single_open(file,myread,NULL);
}
    

static const struct file_operations myops ={
    .owner =THIS_MODULE,
    .read=seq_read,
    .release=single_release,
    .open=proc_init,
    .llseek=seq_lseek
};

static int simple_init(void){

    printk(KERN_INFO "Hola mundo, somos el grupo 18\n");
    ent=proc_create("RAM",0,NULL,&myops);
    return 0;
}

static void simple_cleanup(void)
{
    printk(KERN_INFO "Sayonara mundo, somos el grupo 18\n");
    proc_remove(ent);

}

module_init(simple_init);
module_exit(simple_cleanup);
