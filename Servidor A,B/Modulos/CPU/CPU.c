#include <linux/module.h> 
#include <linux/kernel.h> 
#include <linux/init.h>
#include <linux/list.h>
#include <linux/types.h>
#include <linux/slab.h>
#include <linux/sched.h>
#include <linux/string.h>
#include <linux/fs.h>
#include <linux/seq_file.h>
#include <linux/proc_fs.h>
#include <asm/uaccess.h> 
#include <linux/hugetlb.h>
#include <linux/sched/signal.h>
#include <linux/sched.h>

#define FileProc "CPU"
#define Nombre "RuthLechuga"

struct task_struct *task;
struct task_struct *task_child;
struct list_head *list;
int extra;
int extra2;

static int proc_llenar_archivo(struct seq_file *m, void *v) {

    seq_printf(m, "[\n");
    extra2 = 0;


	for_each_process(task){

		if(extra2 == 0){

			extra2 = 1;

		}else{

			seq_printf(m,",");	
		}



        seq_printf(m, "\n{ \"PID\" : %d, \"Nombre\" : \"%s\", \"Estado\" : %ld , \"uid\" : %i , \"mm\"  : 0,", task->pid, task->comm, task->state, task->cred->uid.val);

		seq_printf(m,"\"sub\": [");

		
		extra = 0;

		list_for_each(list, &task->children){

			if(extra == 0){

				extra = 1;
			}else{

				seq_printf(m,",");	
			}



			task_child = list_entry(list, struct task_struct, sibling);

	    	seq_printf(m, "\n     { \"PID\" : %d, \"Nombre\" : \"%s\" , \"Estado\" : %ld , \"uid\" : %i,  \"mm\"  : 0 }", task_child->pid, task_child->comm, task_child->state,task_child->cred->uid.val);
		}
			
		extra = 0;

		seq_printf(m,"]\n}\n");
		
		}


    seq_printf(m, "\n]\n");
        return 0;
}



static int proc_al_abrir_archivo(struct inode *inode, struct  file *file) {
  return single_open(file, proc_llenar_archivo, NULL);
}

static struct file_operations myops =
{
        .owner = THIS_MODULE,
        .open = proc_al_abrir_archivo,
        .read = seq_read,
        .llseek = seq_lseek,
        .release = single_release,
};



static int simple_init(void){

    proc_create(FileProc,0,NULL,&myops);
    printk(KERN_INFO "Hola mundo, somos el grupo 18 - procesos %s\n", Nombre);
    return 0;
}

static void simple_clean(void){remove_proc_entry(FileProc,NULL);}

module_init(simple_init);
module_exit(simple_clean);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("201602975");
MODULE_DESCRIPTION("");