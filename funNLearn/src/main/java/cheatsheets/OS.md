# Operating System

An Operating system (OS) is a software which acts as an interface between the end user and computer hardware.

## Kernel

The kernel is the central component of a computer operating systems. The only job performed by the kernel is to the manage the communication between the software and the hardware. While the Kernel is the innermost part of an operating system, a shell is the outermost one.

### Features of Kennel

- Low-level scheduling of processes
- Inter-process communication
- Process synchronization
- Context switching

### Types of Kernels

1. Monolithic:
A monolithic kernel is a single code or block of the program. It provides all the required services offered by the operating system. It is a simplistic design which creates a distinct communication layer between the hardware and software.

2. Microkernels:
services are implemented in different address space. The user services are stored in user address space, and kernel services are stored under kernel address space. So, it helps to reduce the size of both the kernel and operating system. In an operating system software performs each of the function:

## Functions of OS (components of OS)

- process management
- Memory management
- File Management
- Device Management
- I/O System Management
- Secondary-storage Management
- Security
- Command interpretation
- Networking
- Job Accounting
- Communication management

## Types of OS

- Batch Operating System
- Multitasking/Time Sharing OS
- Multiprocessing OS
- Real Time OS
- Distributed OS
- Network OS
- Mobile OS

## Firmware vs Operating System

- Firmware is embedded on a chip in the device; OS provides functionality over and above that which is provided by the firmware.

## System Call

A system call is a mechanism that provides the interface between a process and the operating system.
Usage:

- CRUD operations to files/processes
- Network connections sending/receiving packets
- Access to hardware devices like scanner, printer, need a system call.

### Type of System calls

- Process Control
- File Management
- Device Management
- Information Maintenance
- Communications

### Impoortance system calls used in OS

- wait() : wait for another process to complete
- fort() : create a new process
- exec() : execute a process
- kill() : terminate a process
- exit() : terminate program execution

## File System

### File Attributes

name, identifier, location, type, size, protection, time, date and security

### File Type

- Character special file
- ordinary files
- directory files
- special files

### File Access Methods

- Sequential Access: records are accessed in a certain pre-defined sequence
- Random Access (direct random access): Each record has its own address on which
   can be directly accessed for reading and writing.
- Index sequential access: an index is built for every file, with a direct pointer to different memory blocks. the Index is searched sequentially, and its pointer can access the file directly.

## Semaphores And Mutex

- Semaphores
simply a variable that is non-negative and shared between threads.  It uses two atomic operations, 1)wait, and 2) signal for the process synchronization. A semaphore either allows or disallows access to the resource, which depends on how it is set up.

- Mutex
Mutual Exclusion Object. It is a special type of binary semaphore which is used for controlling access to the shared resource.

### Types of Semaphores

- Counting semaphores
- Binary semaphores: (locks, mutex)
   similar to counting semaphores, but their value is restricted to 0 and 1

### Semaphores vs. Mutex

- basically signalling vs locking
- integer vs. an object
- can have multiple threads simultaneously vs. one
- Semaphore value is modified using wait () and signal () operations, on the other hand, Mutex operations are locked or unlocked.

### Characterstics of semaphores

- more than one thread can access
- implemented in the machine-independent of microkernel
- never wastage of process time and resources

## RAM

Random Access Memory / Main memory / Temporary memory / Cache memory / Volatile memory of the computer system

### Main Types

- SRAM : Static RAM : data is stored using the state of a six transistor memory cell. Static RAM is mostly used as a cache memory for the processor (CPU).
- DRAM: Dynamic RAM: allows you to stores each bit of data in a separate capacitor within a specific integrated circuit.

SRAM: Lower access time, costlier, needs constant power supply, in internal cirecuitery, less storage
DRAM: opposite to SRAM

### Other common types

- FPM DRAM: Fast Page Mode Dynamic RAM
- SDR RAM: Synchronous Dynamic Random Access RAM
- RD RAM: Rambus Dynamic RAM
- VRAM : Video
- EDO RAM: Extended Data Output RAM
- Flash Memory: an electrically erasable and programmable permanent type of memory.
- DDR SDRAM: Double Data Rate Synchronous Dynamic RAM

### RAM vs. ROM

ROM

- Contents are not lost when power supply is switched off
- contents written by the manufacturer and can not be overwritten by the user.
- used mainly in the start-up process, stores only several megabytes (MB)
- Slower than RAM
- Types:
  - EPROM: Erasable Programmable
  - PROM: Probrammable
  - EEPROM: Electrically Erasable Programmable
  - Mask ROM: programmable only by manufacturer

## Process vs. Threads

### Process

Process can be defined as an execution unit where a program runs. A process operations can be easily controlled with the help of PCB(Process Control Block). PCB contains all information to processing like process id, priority, state, and contents CPU register, etc.

### Process Architecture

- Stack: The Stack stores temporary data like function parameters, returns addresses, and local variables.
- Heap: Allocates memory, which may be processed during its run time.
- Data: It contains the variable.
- Text: includes the current activity, which is represented by the value of the Program Counter.

### Process States

1. New -> 2, 5, 6
2. Ready -> 3
3. waiting -> 4
4. executing -> 5, 6, 7
5. Blocked -> End state
6. Suspended -> End state
7. Terminated -> End state

### Process Control Block

- Process state
- CPU registers: includes accumulators, index and general-purpose registers, and information of condition code.
- Program counter: the address of the next instruction, which should be executed for that process.
- CPU scheduling information: includes a process priority, pointers for scheduling queues
- Accounting and business information: includes the amount of CPU and time utilities like real time used, job or process numbers, etc.
- Memory-management information: includes the value of the base and limit registers, the page, or segment tables. This depends on the memory system, which is used by the operating system.
- I/O status information: includes a list of open files, the list of I/O devices that are allocated to the process, etc.

### Thread

Thread is an execution unit that is part of a process. A process can have multiple threads, all executing at the same time. It is a unit of execution in concurrent programming. A thread is lightweight and can be managed independently by a scheduler. It helps you to improve the application performance using parallelism. Multiple threads share information like data, code, files, etc. Type of threads:

- Kernel-level threads
- User-level threads
- Hybrid threads

### Inter process communication (IPC)

These are the PCBs of threads. IPC is used for exchanging data between multiple threads in one or more processes or programs.
IPC approaches:

- Pipes
- Message ques
- Message Passing
- Direct Communication: should name each other explicitly.
- Indirect Communication: share a common mailbox
- Shared Memory
- FIFO

### Differences

P: Creation of each process requires separate system calls for each process.
T: Single system call can create more than one thread

P: It is an isolated execution entity and does not share data and information.
T: Threads share data and information.

P: Processes use the IPC(Inter-Process Communication) mechanism for communication that significantly increases the number of system calls.
P: A process has its stack, heap memory with memory, and data map.
T: Threads shares instruction, global, and heap regions. However, it has its register and stack.

P: Process management takes more system calls.
T: Thread management consumes very few, or no system calls because of communication between threads that can be achieved using shared memory.

P: comsume more resources, takes longer in communication/creation and termination, heavier context switching
T: opposite to P

## Process Scheduling

OS task that schedules processes of different states like ready, waiting, and running.

### Process Scheduling Queues

- Job queue
- Ready queue
- Device queue

### Process Scheduling Types

- Long Term (Job scheduler)
- Medium Term (Swapping): enables you to handle the swapped out-processes
- Short Term Scheduler (CPU Scheduler)

## CPU Scheduling

process of determining which process will own CPU for execution while another process is on hold. The main task of CPU scheduling is to make sure that whenever the CPU remains idle, the OS at least select one of the processes available in the ready queue for execution. The selection process will be carried out by the CPU scheduler. It selects one of the processes in memory that are ready for execution.

### Types of CPU Scheduling

- Preemptive Scheduling
the tasks are mostly assigned with their priorities. A running lower priority task holds for some time and resumes when the higher priority task finishes its execution.

- Non-Preemptive Scheduling
the CPU has been allocated to a specific process. The process that keeps the CPU busy will release the CPU either by switching context or terminating.

### Scheduling Terminologies

- Burst Time/Execution Time/running time: time required by the process to complete execution
- Arrival Time: when a process enters in a ready state
- Finish Time: when process complete and exit from a system
- Multiprogramming: A number of programs which can be present in memory at the same time.
- Jobs: a type of program without any kind of user interaction.
- User: a kind of program having user interaction.
- Process: the reference that is used for both job and user.
- CPU/IO burst cycle: Characterizes process execution, which alternates between CPU and I/O activity. CPU times are usually shorter than the time of I/O.

### Dispatcher

Mmodule that provides control of the CPU to the process. The Dispatcher should
be fast so that it can run on every context switch. Dispatch latency is the
amount of time needed by the CPU scheduler to stop one process and start another.
Functions performed by Dispatcher:

- Context Switching
- Switching to user mode
- Moving to the correct location in the newly loaded program.

### Types of CPU scheduling Algorithm

- First Come First Serve (FCFS) : managed with a FIFO queue
  - waiting time = start time - arrival time
  - Average waiting time = (WT1 + WT2 + ....... WTn) / n
  
- Shortest-Job-First (SJF) Scheduling
- Shortest Remaining Time

- Priority Scheduling:
  run based on priority. for processes with equal priority use arrival time. or if a process was partially completed before take that. Types:

  - Preemptive: currently running lower priority task gives up for higher priority tasks.
  - Non-Preemptive: currently running process will release the CPU either by switching context or terminating.

- Round Robin Scheduling: time slice CPU and each process takes CPU for that slice and stand in queue again. Worst Case Latency

   ```bash
   This term is used for the maximum time taken for execution of all the tasks.

   dt = Denote detection time when a task is brought into the list
   st = Denote switching time from one task to another
   et = Denote task execution time
   Formula:

   Tworst = {(dti+ sti + eti ), + (dti+ sti + eti )2 +...+ (dti+ sti + eti )N., + (dti+ sti + eti  + eti) N} + tISR
   tISR = sum of all execution times
   ```

- Multilevel Queue Scheduling :This algorithm separates the ready queue into various separate queues. In this method, processes are assigned to a queue based on a specific property of the process, like the process priority, size of the memory, etc.

## Deadlock, Starvation, Livelock

process enters a waiting state because another waiting process is holding the demanded resource.

- One lane bridge:
- Circular wait: One process is waiting for the resource, which is held by the second process, which is also waiting for the resource held by the third process etc.

### Deadlock Detection

A resource scheduler helps OS to keep track of all the resources which are allocated to different processes. Hence, a deadlock occurrence can be detected by the resource scheduler.

### Deadlock Prevention

prevent a deadlock before it can occur.

1. No preemptive action: No Preemption - A resource can be released only voluntarily by the process holding it after that process has finished its task
2. Mutual Exclusion (Mutex): binary semaphore
3. Hold and Wait:
4. Circular Wait:

### Deadlock Avoidance

Avoidance Algorithms:

- A single instance of a resource type.
  - Use a resource-allocation graph
  - Cycles are necessary which are sufficient for Deadlock

- Multiples instances of a resource type.
  - Cycles are necessary but never sufficient for Deadlock.
  - Uses the banker's algorithm

### Starvation and Deadlock

- D: occurs when one of the processes got blocked.
- S: where all the low priority processes got blocked, and the high priority processes execute.

- D: is an infinite process.
- S: is a long waiting but not an infinite process.

- D: Every Deadlock always has starvation.
- S: Every starvation does n't necessarily have a deadlock.

- D: happens then Mutual exclusion, hold and wait. Here, preemption and circular wait do not occur simultaneously.
- S: It happens due to uncontrolled priority and resource management.

### Livelock

a situation where a request for an exclusive lock is denied repeatedly, as many overlapping shared locks keep on interfering each other. Eg:
Two people meet in a narrow corridoor and both try to move on the side to give space to other one to pass. But then both try to pass, and so on.

Livelock occurs when the total number of allowed processes in a specific system should be defined by the total number of entries in the process table. Therefore, process table slots should be referred to as Finite Resources.

- Livelock vs. deadlock vs. starvation
  - A livelock, is almost similar to a deadlock, except that the states of the processes which are involved in a livelock always keep on changing to one another, none progressing.
  - Livelock is a unique case of resource starvation.

### Process Synchronization

is the task of coordinating the execution of processes in a way that no two processes can have access to the same shared data and resources.

#### Sections of a Program

- Entry Section
- Critical Section: This part allows one process to enter and modify the shared variable.
- Exit Section: Exit section allows the other process that are waiting in the Entry Section, to enter into the Critical Sections. It also checks that a process that finished its execution should be removed through this Section.
- Remainder Section: All other parts of the Code, which is not in Critical, Entry, and Exit Section

#### Critical Section Problem

- The entry to the critical section is handled by the wait() function, and it is represented as P().
- The exit from a critical section is controlled by the signal() function, represented as V().

- Rules for Critical Section
  - Mutual Exclusion
  - Progress: This solution is used when no one is in the critical section, and someone wants in. Then those processes not in their reminder section should decide who should go in, in a finite time.
  - Bound Waiting: When a process makes a request for getting into critical section, there is a specific limit about number of processes can get into their critical section. So, when the limit is reached, the system must allow request to the process to get into its critical section.

- Solutions:
  - Peterson's Solution

      ```c
      PROCESS Pi
      FLAG[i] = true
      while((turn != i) AND (CS is !free)) {
         wait;
      }
      CRITICAL SECTION FLAG[i] = false
      turn = j; //choose another process to go to CS
      ```

  - Synchronization Hardware
  - Mutex locks
  - Semaphore

## Memory Management

### Memory Management Techniques

- Single Contiguous Allocation:
all types of computer's memory except a small portion which is reserved for the OS is available for one application. For example, MS-DOS operating system allocates memory in this way. An embedded system also runs on a single application.

- Partitioned Allocation:
It divides primary memory into various memory partitions, which is mostly contiguous areas of memory. Every partition stores all the information for a specific task or job. This method consists of allotting a partition to a job when it starts & unallocate when it ends.

- Paged Memory Management:
This method divides the computer's main memory into fixed-size units known as page frames. This hardware memory management unit maps pages into frames which should be allocated on a page basis.

- Segmented Memory Management:
Segmented memory is the only memory management method that does not provide the user's program with a linear and contiguous address space. Segments need hardware support in the form of a segment table. It contains the physical address of the section in memory, size, and other data like access protection bits and status.

### Swapping

method in which the process should be swapped temporarily from the main memory to the backing store. It will be later brought back into the memory for continue execution. Backing store is a hard disk or some other secondary storage device that should be big enough inorder to accommodate copies of all memory images for all users. It is also capable of offering direct access to these memory images.

### Memory allocation

Memory allocation is a process by which computer programs are assigned memory or space.

- Low Memory - Operating system resides in this type of memory.
- High Memory- User processes are held in high memory.

### Partition Allocation

Memory is divided into different blocks or partitions. Each process is allocated according to the requirement. Partition allocation is an ideal method to avoid internal fragmentation. Partition allocation schemes :

- First Fit: which is the first sufficient block from the beginning of the main memory.
- Best Fit: the first smallest partition among the free partitions.
- Worst Fit: which is the largest sufficient freely available partition in the main memory.
- Next Fit: searches for the first sufficient partition from the last allocation point.

### Fragmentation

Processes are stored and removed from memory, which creates free memory space, which are too small to use by other processes. After sometimes, that processes not able to allocate to memory blocks because its small size and memory blocks always remain unused is called fragmentation. This type of problem happens during a dynamic memory allocation system when free blocks are quite small, so it is not able to fulfill any request.

- External fragmentation: can be reduced by rearranging memory contents to place all free memory together in a single block.
- Internal fragmentation: can be reduced by assigning the smallest partition, which is still good enough to carry the entire process.

### Paging

a storage mechanism that allows OS to retrieve processes from the secondary storage into the main memory in the form of pages. In the Paging method, the main memory is divided into small fixed-size blocks of physical memory, which is called frames. The size of a frame should be kept the same as that of a page to have maximum utilization of the main memory and to avoid external fragmentation. Paging is used for faster access to data, and it is a logical concept.

### Segmentation

Segmentation method works almost similarly to paging, only difference between the two is that segments are of variable-length whereas, in the paging method, pages are always of fixed size.

### Paging vs. Segmentation

- P is easier to use than S
- P swapping is easier than S, as P has equal sized pages and page frames
- P may cause interval fragmentation while S does not offers internal fragmentation
- S tables use lesser memory than P

### Dynamic Loading

a routine of a program which is not loaded until the program calls it.

### Dynamic Linking

Linking is a method that helps OS to collect and merge various modules of code and data into a single executable file. The file can be loaded into memory and executed. OS can link system-level libraries into a program that combines the libraries at load time. In Dynamic linking method, libraries are linked at execution time, so program code size can remain small.

## Bankers Algorithm

There are X number of account holders of a specific bank, and the total amount of money of their accounts is G.
When the bank processes a car loan, the software system subtracts the amount of loan granted for purchasing a car from the total money ( G + Fixed deposit + Monthly Income Scheme + Gold, etc.) that the bank has. It also checks that the difference is more than or not G. It only processes the car loan when the bank has sufficient money even if all account holders withdraw the money G simultaneously.

### Banker's Algorithm Notations

- X: Indicates the total number of processes of the system.
- Y: Indicates the total number of resources present in the system.
- Available
   [I: Y] indicate which resource is available.
- Max
   [l:X,l: Y]: Expression of the maximum number of resources of type j or process i
- Allocation
   [l:X,l:Y]. Indicate where process you have received a resource of type j
- Need
   Express how many more resources can be allocated in the future

### Resource Request Algorithm

Resource request algorithm enables you to represent the system behavior when a specific process makes a resource request. Steps

- Step 1) When a total requested instance of all resources is lesser than the process, move to step 2.
- Step 2) When a requested instance of each and every resource type is lesser compared to the available resources of each type, it will be processed to the next step. Otherwise, the process requires to wait because of the unavailability of sufficient resources.
- Step 3) Resource is allocated as shown in the below given Pseudocode.

   ```bash
   Available = Available – Request (y)
   Allocation(x) = Allocation(x) + Request(x)
   Need(x) = Need(x) - Request(x)
   ```

## Microprocessor vs. Microcontroller

- MP is the heart of Computer system | MC is the heart of an embedded system
- for MP memory and I/O components need to be connected externally | MC has a processor along with internal memory and I/O components.
- MP can't be used in compact systems | MC can be used in compact systems.
- MP high cost, and power consumption | some MC can also function on batteries.
- MP used in computers | MC used in devices like washing machine, MP3 players, IOTs
- MP uses an external bus to interface to RAM, ROM, and other peripherals | MC uses an internal controlling bus.
- MP has very high speed | MC based systems run up to 200MHz or more depending on the architecture.
