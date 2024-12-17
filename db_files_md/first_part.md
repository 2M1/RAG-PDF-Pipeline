Front cover

<!-- image -->


## Summary of changes

This section describes the technical changes that were made in this edition of the paper and in previous editions. This edition might also include minor corrections and editorial changes that are not identified.

Summary of Changes for IBM Power E1050 Technical Overview and Introduction as created or updated on November 20, 2024.

## November 2024, Second Edition

This revision includes the following new and changed information.

## New information

-  Added information about new DDR5 memory support.
-  Added information about the PCIe Gen4 I/O Expansion Drawer.
-  Added information about the NED24 NVMe Expansion Drawer.

## Changed information

-  Noted that the SAS24EX SAS expansion drawer was withdrawn from marketing.
-  Noted that the PCIe Gen3 I/O expansion drawer was withdrawn from marketing.
-  Updated the list of PCIe adapters that are supported.
-  Other minor changes and corrections.

<!-- image -->

Chapter 1.

## IBM Power E1050 overview

This chapter provides a general description of the new IBM Power E1050 (9043-MRX) server, which is a logical follow-on to the IBM Power E950. The IBM Power E1050 server is an enhanced enterprise class four-socket, 4U server that provides massive scalability and flexibility. These systems are agile and deliver extreme density in an energy-efficient design with best in class reliability and resiliency. They provide enterprise clients with a secure environment that balances mission-critical and modernization applications to deliver a frictionless, hybrid cloud experience.

The following topics are covered in this chapter:

-  1.1, 'System overview' on page 2
-  1.2, 'Operating environment' on page 6
-  1.3, 'Physical package' on page 8
-  1.4, 'System features' on page 9
-  1.5, 'Minimum configuration' on page 11
-  1.6, 'PCIe adapter slots' on page 13
-  1.7, 'Operating system support' on page 15
-  1.8, 'Hardware Management Console overview' on page 21
-  1.9, 'IBM Power solutions' on page 29
-  1.10, 'IBM Power platform modernization' on page 33

1

## 1.1  System overview

The Power E1050 server is suited for cloud deployments due to its built-in virtualization capabilities, flexible capacity, and high performance. The model number for this server is 9043-MRX. It features a single enclosure that is four EIA units (4U) and can be configured with two, three, or four dual-chip modules (DCMs). There are three processor options that are available for this server:

-  Twelve cores running at a typical 3.35 - 4.00 GHz (max) frequency range
-  Eighteen cores running at a typical 3.20 - 4.00 GHz (max) frequency range
-  Twenty-four cores running at a typical 2.95 - 3.90 GHz (max) frequency range

A Power E1050 server with four 24-core DCMs offers the maximum of 96 cores and processor cores can run up to eight simultaneous threads to deliver greater throughput. All sockets must be populated with the same processor modules.

Figure 1-1 shows the Power E1050 server.

Figure 1-1   The Power E1050 server

<!-- image -->

Figure 1-2 shows a top view of the Power E1050 server with the top lid removed.

Figure 1-2   Top view of the Power E1050 server with the top lid removed

<!-- image -->

Under the left metal plate are the fans and Non-Volatile Memory Express (NVMe) slots, as depicted in Figure 1-3. Moving right, you next see the memory slots that are associated with the processors to the right of that memory column. Moving further to the right, there is another column of memory slots that are linked to the processors at the right of them. Under the metal plate at the right edge are the four Titanium-class 2300W power supplies and the 11 Peripheral Component Interconnect Express (PCIe) slots, as shown in Figure 1-4. The airflow direction is from the front to the rear of the server, which, in Figure 1-2 on page 2, is from left to right.

Figure 1-3 shows the front view of a Power E1050 server with the front bezel removed.

Figure 1-3   Front view of the Power E1050 server

<!-- image -->

Figure 1-4 shows the rear view of the Power E1050 server. The leftmost slot (P0-C0) is the enterprise Baseboard Management Controller (eBMC) Service Processor Card, and then there are five PCIe slots. On the right side are six more adapter slots.

Figure 1-4   Rear view of the Power E1050 server

<!-- image -->

## System features

Each processor module that is added to the system offers 16 Open Memory Interface (OMI) slots that can be populated with 4U Differential Dual Data Rate DIMMs (DDIMMs). These DDIMMs incorporate either Double Data Rate 4 (DDR4) or Double Data Rate 5 (DDR5) memory chips that deliver a memory bandwidth of up to 409 GBps peak transfer rates per socket for the DDR4-based memory and 819 GBps peak transfer for the DDR5-based memory. With four processor modules, the Power E1050 server provides 64 OMI slots that support up to 16 TB of memory and a maximum peak transfer rate of 3,276 GBps.

Restriction: An IBM Power E1050 can be configured only with DDR4-based memory or DDR5-based memory. Mixing of the two types of memory is not allowed.

The Power E1050 server provides state-of-the-art PCIe Gen5 connectivity. Up to 11 PCIe slots are provided in the system unit with different characteristics:

-  Six PCIe Gen4 x16 or PCIe Gen5 x8 slots
-  Two PCIe Gen5 x8 slots
-  Three PCIe Gen4 x8 slots

The number of available slots depends on the number of available processor modules. For more information about the system diagram, see Figure 2-1 on page 36.

Note: Although some slots are x8 capable only, all connectors in the system have x16 connectors.

If more slots are needed, up to four I/O expansion drawers, either Gen4 or Gen3, 1 with two fanout modules each can be added to the system. Each fanout module provides six slots. With eight fanout modules in four I/O drawers, the maximum number of available slots is 51. It is possible to mix Gen3 and Gne4 drawers within a system.

The PCIe slots can be populated with a range of adapters covering local area network (LAN), Fibre Channel (FC), serial-attached SCSI (SAS), Universal Serial Bus (USB), and cryptographic accelerators. At least one network adapter must be included in each system.

The Power E1050 server offers up to 10 internal NVMe U.2 flash bays that can be equipped with 800 GB U.2 Mainstream NVMe drives or U.2 Enterprise class NVMe drives in different sizes up to 6.4 TB. Each NVMe device is connected as a separate PCIe endpoint and can be assigned individually to VMs for best flexibility. The 10 NVMe bays offer a maximum of 64 TB internal storage. For all 10 NVMe bays to b available, the server must be populated with all four processor cards. With two or three processor cards, the server can be populated with six NVMe devices.

The Power E1050 server does not have internal spinning SAS drives. However, it is possible to attach 19-inch disk expansion drawers that offer SFF Gen2-carrier bays for SAS disks. For more information, see 2.4, 'Internal I/O subsystem' on page 66.

## Dynamic configuration capabilities and virtualization

In addition to extensive hardware configuration flexibility, the Power E1050 server offers Elastic Capacity on Demand (Elastic CoD) to temporarily activate processor cores and memory. Also included is IBM Active Memory Expansion, which uses data compression to expand the available memory for AIX partitions; and Active Memory Mirroring (AMM), which mirrors critical memory segments that are used by the hypervisor.

For optimal flexibility, the Power E1050 server can be integrated into an IBM Power Private Cloud with Shared Utility Capacity pool, also known as IBM Power Enterprise Pool 2.0. This pool can include Power E1050 servers, Power E950 servers, or a combination of both. Within the pool, a base capacity (of processor cores, memory, and OS licenses or subscriptions) is purchased and available for usage across any servers in the pool.

All additional resources that are installed on the servers in the pool are activated as available for usage. If the total usage of resources in the pool (metered on a per-minute basis) exceeds the sum of the purchased Base Capacity within the pool, the excess usage is billed to the customer. Billing can be either prepaid by purchasing credits in advance or post-paid, with IBM generating a monthly invoice in the latter case. For more information about IBM Power Enterprise Pools see IBM Power Systems Private Cloud with Shared Utility Capacity: Featuring Power Enterprise Pools 2.0 , SG24-8478,

The Power E1050 server includes IBM PowerVM® Enterprise Edition to deliver virtualized environments and support a frictionless hybrid cloud experience. Workloads can run the AIX, and Linux operating systems (OSs), including the Red Hat OpenShift Container Platform. IBM i is not a supported OS on the Power E1050 server.

The Power E1050 server also provides strong resiliency characteristics, which include Power10 chip capabilities and memory protection. The new 4U DDIMMS that are used in the Power E1050 server offer an enhanced buffer, N+1 voltage regulation, and spare dynamic RAM (DRAM) technology. Also, technologies like Chipkill with advanced error correction code (ECC) protection are included, and transparent Power10 memory encryption with no performance impact. This technology is the same enterprise class technology that is used in the Power E1080 server.

Other resiliency features that are available in the Power E1050 server are hot-plug NVMe bays, hot-plug PCIe slots, redundant and hot-plug power supplies, hot-plug redundant cooling fans, hot-plug Time of Day battery, and even highly resilient architecture for power regulators.

Table 1-1 shows a summary of features of the Power E1050 server.

Table 1-1   Power E1050 server feature summary

| Feature                  | Comments                                                                                                                                                                                            |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Processors               | 12, 18, or 24 CPU cores per socket.                                                                                                                                                                 |
| Sockets                  | Four sockets are available. 2, 3, or 4 sockets may  be populated.                                                                                                                                   |
| Memory                   |  Up to 64 OMI slots that can be equipped with  4U DDIMMs.  DDIMM sizes are 32, 64, 128, and 256 GB.  8 TB 16 TB maximum memory.                                                                  |
| Integrated PCIe          |  Six PCIe Gen4 16-lane or PCIe Gen5 8-lane  slots.  Two PCIe Gen5 8-lane slots.  Three PCIe Gen4 8-lane slots.  PCIe slots are full-high and half-length, and  use blind-swap cassettes (BSCs). |
| Internal NVMe Flash bays | Up to 10 U.2 NVMe bays for 15-mm NVMe drives  or 7-mm NVMe drives in a 15-mm carrier.                                                                                                               |
| Internal USB ports       | USB 3.0. Two front and two rear.                                                                                                                                                                    |
| Media bays               | DVD through an external USB DVD.                                                                                                                                                                    |
| Maximum I/O drawers      | Four PCIe Gen3 I/O drawers (#EMX0).                                                                                                                                                                 |
| External storage drawers | Up to 64 EXP12SX or ESP24SX drawers.                                                                                                                                                                |

Table 1-2 shows the major differences between the Power E950 and Power E1050 servers.

Table 1-2    Comparing the Power E950 and Power E1050 servers

| Features                        | Power E950 server                                           | Power E1050 server                                             |
|---------------------------------|-------------------------------------------------------------|----------------------------------------------------------------|
| Processor                       | IBM Power9® (single-chip  module (SCM))                     | Power10 (DCM)                                                  |
| Sockets                         | 2 - 4                                                       | 2 - 4                                                          |
| Maximum cores                   | 32, 40, 44, or 48                                           | 48, 72, or 96                                                  |
| Maximum memory                  | 16 TB                                                       | 16 TB                                                          |
| DIMM type and DIMM slots  count | Up to 128 industry-standard  DIMMs                          | Up to 64 DDIMMs                                                |
| L4 cache                        | Yes                                                         | Yes                                                            |
| Memory bandwidth                | 920 GBps                                                    | 3.276 GBps                                                     |
| Memory DRAM spare               | Yes                                                         | Yes                                                            |
| I/O expansion slots             | Yes                                                         | Yes                                                            |
| PCIe slots                      | 11 (eight Gen4 16-lane + two  Gen4 8-lane + one Gen3 slots) | 11 (six Gen5 x8/Gen4 x16 + two  Gen5 x8 + three Gen4 x8 slots) |
| Acceleration ports              | Eight (CAPI 2.0 +  IBM OpenCAPI)                            | Six (IBM OpenCAPI)                                             |
| PCIe hot-plug support           | Yes + blind swap                                            | Yes + blind swap                                               |
| IO bandwidth                    | 630 GBps                                                    | 756 GBps                                                       |
| Internal storage bays           | 12 (eight SAS + four NVMe  drives)                          | 10 (10 NVMe drives)                                            |
| Internal storage controllers    | Optional Concurrently maintainable                          | Optional Concurrently maintainable                             |

## 1.2  Operating environment

Table 1-3 details the operating environment for the Power E1050 server.

## Power E1050 operating environment

Table 1-3 Operating environment for the Power E1050 server

| System Power E1050 server                                                       | System Power E1050 server   | System Power E1050 server         |
|---------------------------------------------------------------------------------|-----------------------------|-----------------------------------|
| Item                                                                            | Operating                   | Non-operating                     |
| Recommended: 18 - 27 °C (64.4 - 80.6 °F) Allowable: 5 - 40 °C (41.0 - 140.0 °F) | 5 - 45 °C (41.0 - 113.0 °F) | Temperature                       |
| Relative humidity                                                               | 5 - 85%                     | 8 - 80%                           |
|                                                                                 | 27 °C (80.6 °F)             | Maximum dew point 24 °C (75.2 °F) |
| Operating voltage                                                               |                             | 200 - 240 V AC N/A                |

| Power E1050 operating environment   | Power E1050 operating environment                                                                          | Power E1050 operating environment   |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|-------------------------------------|
| System                              | Power E1050 server                                                                                         | Power E1050 server                  |
| Operating frequency                 | 50 - 60 Hz +/- 3 Hz AC                                                                                     | N/A                                 |
| Maximum power consumption           | 5,200 W maximum                                                                                            | N/A                                 |
| Maximum power source  loading       | 5.36 kVA maximum                                                                                           | N/A                                 |
| Maximum thermal output              | 17,742 BTU per hour                                                                                        | N/A                                 |
| Maximum altitude                    | 3,050 m (10,000 ft.)                                                                                       | N/A                                 |
| Maximum noise level                 | 8.2 bels LwAm (heavy workload  on one maximally configured  4-socket enclosure, 2 TB  memory, 25°C, 500 m) | N/A                                 |

Note: IBM does not recommend operation above 27 °C, but you can expect full performance up to 35 °C for these systems. Above 35 °C, the system is capable of operating, but possible reductions in performance might occur to preserve the integrity of the system components. Above 40 °C, there might be reliability concerns for components within the system.

Environmental assessment: The IBM Systems Energy Estimator tool can provide more accurate information about the power consumption and thermal output of systems that are based on a specific configuration, including adapters and I/O expansion drawers.

Note: The derate maximum allowable dry-bulb temperature is 1°C (1.8°F) per 175 m (574 ft) above 900 m (2,953 ft), with up to a maximum allowable elevation of 3050 m (10,000 ft).

Government regulations, such as those prescribed by the Occupational Safety and Health Administration (OSHA) or European Community Directives, may govern noise level exposure in the workplace, which might apply to you and your server installation. The Power E1050 is available with an optional acoustical door feature that can help reduce the noise that is emitted from this system.

The actual sound pressure levels in your installation depend upon various factors, including the number of racks in the installation, the size, materials, and configuration of the room where you designate the racks to be installed, the noise levels from other equipment, the ambient room temperature, and employees' location in relation to the equipment.

Compliance with such government regulations also depends on many more factors, including the duration of employees' exposure and whether employees wear hearing protection. As a best practice, consult with qualified experts in this field to determine whether you are in compliance with the applicable regulations.

## 1.3  Physical package

The system node requires 4U and the PCIe I/O expansion drawer requires 4U. Thus, a single-enclosure system with one PCIe I/O expansion drawer requires 8U.

Table 1-4 lists the physical dimensions of the system node and the PCIe I/O Expansion Drawer.

Table 1-4   Physical dimensions of the system node and the PCIe Gen3 I/O Expansion Drawer

| Dimension   | Power E1050 system node         | PCIe I/O expansion drawer         |
|-------------|---------------------------------|-----------------------------------|
| Width       | 448 mm (17.6 in.)               | 448 mm (17.6 in.)                 |
| Depth       | 902 mm (35.5 in.)               | 736.6 mm (29.0 in.)               |
| Height      | 175 mm (6.9 in.) four EIA units | 177.8 mm (7.0 in.) four EIA units |
| Weight      | 69 kg (153 lb)                  | 54.4 kg (120 lb)                  |

To help ensure installability and serviceability in non-IBM industry-standard racks, review the installation planning information for any product-specific installation requirements.

Note: The EMX0 remote I/O drawer connection in the T42 and S42 racks stops the rear door from closing, so you must have the 8-inch rack extensions.

Figure 1-5 shows the front view of the Power E1050 server.

Figure 1-5   Front view of the Power E1050 server

<!-- image -->

## 1.4  System features

This section covers the standard system features that are included in the Power E1050 server.

## 1.4.1  Power E1050 server features

This summary describes the standard features that are available on the Power E1050 (9043-MRX) server model:

-  The Power E1050 supports 24 - 96 processor cores with 2 - 4 Power10 processor modules.
-  The Power E1050 delivers 256 GB to 16 TB high-performance DDR4 or DDR5 memory with an L4 cache.
-  A Power E1050 server supports up to 10 NVMe drives.
-  Up to 11 hot-swap PCIe slots may be in the system unit:
- - Six PCIe Gen5 x8 or Gen4 x16 slots.
- - Three PCIe Gen4 x8 slots.
- - Two PCIe Gen5 x 8 slots.
- - With two processor modules, there are seven PCIe slots; with three modules and four modules, there are 11 PCIe slots.
-  The PCIe I/O Expansion Drawer (#EMX0 or #EMZ0) expands the number of full-high, hot-swap slots:
- - Up to two PCIe drawers with two processor modules (a maximum of 31 slots on the server).
- - Up to four PCIe drawers with four processor modules (a maximum of 51 slots on the server).
-  The IBM Power E1050 can support up to 64 EXP24SX SFF Drawers, providing a total of 1,536 SAS bays for disks or SSDs. Although the EXP24SX is no longer actively marketed, it remains a supported option.
- For a more cost-effective and higher-performing solution, consider the NED24 NVMe Expansion Drawer. Each NED24 drawer can accommodate up to 24 NVMe drives, offering up to 154 TB of storage capacity. The Power E1050 can support a maximum of two NED24 drawers. Each drive in the NED24 is individually addressable and can be assigned to an AIX, Linux, or a Virtual I/O Server (VIOS) partition.
-  System unit I/O (integrated I/O):
- - USB 3.0 ports: four 3.0 ports, two front and two rear.
- - USB 2.0 ports: two rear 2.0 ports for limited use.
- - HMC ports: two 1 GbE RJ45.
-  Four hot-plug and redundant power supplies 2300 W (200 - 240 V AC) (#EB39).
-  System unit only 4U in a 19 inch rack-mounted hardware.
-  Primary OS:
- - AIX (#2146): small-tier licensing.
- - Linux (#2147): Red Hat Enterprise Linux (RHEL) and SUSE Linux Enterprise Server.

## Processor modules

-  The Power E1050 supports 24 - 96 processor cores:
- - Twelve-core typical 3.35 - 4.0 GHz (max) #EPEU Power10 processor.
- - Eighteen-core typical 3.20 - 4.0 GHz (max) #EPEV Power10 processor.
-  Twenty-four-core typical 2.95 - 3.90 GHz (max) #EPGW Power10 processor.
-  A minimum of two and a maximum of four processor modules are required for each system. The modules can be added to a system later through a Miscellaneous Equipment Specification (MES) upgrade, but the system requires scheduled downtime to install. All processor modules in one server must be of the same frequency (same processor module feature number), that is, you cannot mix processor modules of different frequencies.
-  Permanent CoD processor core activations are required for the first processor module in the configuration and are optional for any additional modules. Specifically:
- - Two, three, or four 12-core typical 3.35 - 4.0 GHz (max) processor modules (#EPEU) require 12 processor core activations (#EPUR) at a minimum.
- - Two, three, or four 18-core typical 3.20 - 4.0 GHz (max) processor modules (#EPEV) require 18 processor core activations (#EPUS) at a minimum.
-  Two, three, or four 24-core typical 2.95 - 3.90 GHz (max) processor modules (#EPGW) require 24 processor core activations (#EPYT) at a minimum.
-  Temporary CoD capabilities are optionally available for processor cores that are not permanently activated. An HMC is required for temporary CoD.

## System memory

-  256 GB - 16 TB high-performance memory up to 3200 MHz DDR4 or DDR5 OMI:
- - DDR5 options:
- · 64 GB DDIMM Memory (#EMFH)
- · 128 GB DDIMM Memory (#EMFJ)
- · 256 GB DDIMM Memory (#EMFK)
- · 512 GB DDIMM Memory (#EMFL)
- - DDR4 options:
- · 64 GB DDIMM Memory (#EM75)
- · 128 GB DDIMM Memory (#EM76)
- · 256 GB DDIMM Memory (#EM77)
- · 512 GB DDIMM Memory (#EM7J)
- - Optional Active Memory Expansion (#EMBM).
- - Mixed DIMM size support (#EMCM). 2
-  As your memory requirements increase, the system capabilities increase as follows:
- - With two processor modules installed, 32 DDIMM slots are available. The minimum memory is 256 GB.
- - With three processor modules installed, 48 DDIMM slots are available. The minimum memory is 384 GB.
- - With four processor modules installed, 64 DDIMM slots are available. The minimum memory is 512 GB. Sixteen DDIMMs are available per socket.
- - The more DDIMM slots that are filled, the larger the bandwidth that is available to the server.

Permanent CoD memory activations are required for at least 50% of the physically installed memory or 256 GB of activations, whichever is larger. Use 1 GB activation (#EMCP) and 100 GB activation (#EMCQ) features to order permanent memory activations.

Temporary CoD for memory is available for memory capacity that is not permanently activated. Temporary CoD activations are delivered through Virtual Capacity machine type and model (4586-COD) by using the IBM Entitled Systems Support process. An HMC is required for temporary CoD.

Notes: Memory is ordered in a quantity of eight of the same memory feature.

-  The minimum memory that is supported per two Power10 processors that are installed is 256 GB.
-  The minimum memory that is supported per three Power10 processors that are installed is 384 GB.
-  The minimum memory that is supported per four Power10 processors that are installed is 512 GB.

## Storage options

The Power E1050 supports up to 10 NVMe 7 mm or 15-mm drives:

-  Six NVMe drives within a two or three-socket configuration
-  Ten NVMe drives within a four-socket configuration

All NVMe drives are driven directly from the system backplane with no PCIe card or cables required.

The 7-mm NVMe drives from the IBM Power E950 are also supported on the Power E1050 with a carrier conversion feature that is offered to hold these drives.

## 1.5 Minimum configuration

Minimum configuration describes the most basic parts of the Power E1050 server in an initial order that are required to have a fully working environment. This configuration was tested, validated, and certified by an IBM development team. The Power E1050 server model belongs to the mid-range category, and it can scale up vertically through physical add-on upgrades and resource activations of inactive processors and memory capacity, otherwise known as Capacity Upgrade on Demand (CUoD).

The Power E1050 server is a 4-socket based processor where the first two sockets at a minimum must be populated. As for the memory DIMM slots, four out of 16 per socket must be inserted. The smallest set is 256 GB.

Table 1-5 lists the minimum features of a Power E1050 server configuration.

Table 1-5   Selecting the minimum configuration for the Power E1050 server

| Feature                                              | Feature  Code                                                                            | Feature Code description                                                                                                                                                                                                                                                                                          | Minimum  quantity                                                 |
|------------------------------------------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Primary OS  Feature Code                             |  #2146  #2147                                                                          |  Primary OS Indicator-AIX  Primary OS Indicator-Linux                                                                                                                                                                                                                                                           | 1                                                                 |
| Heat sink +  thermal  interface  material (TIM)  pad |  #EPLU  #EPLV                                                                          |  Front Heat Sink + TIM PAD (For MRX)  Rear Heat Sink + TIM PAD (For MRX)                                                                                                                                                                                                                                        |  1  1 Note: Applies  to base two  sockets  populated.           |
| Processor card                                       |  #EPEU  #EPEV  #EPGW                                                                  |  12-core typical 3.35 - 4.0 GHZ (max)  processor  18-core typical 3.20 - 4.0 GHZ (max)  processor  24-core typical 2.95 - 3.90 GHZ (max)  processor                                                                                                                                                            | Two of any  processor  Feature Code,  and they must  be the same. |
| Processor  activation                                | AIX or  Virtual I/O  Server  (VIOS):  #EPUR  #EPUS  #EPYT Linux only:  #EPUN  #EPUP | AIX or VIOS:  One core Processor Activation for #EPEU  One core Processor Activation for #EPEV  One core Processor Activation for #EPGW Linux only:  One core Processor Activation for #EPEU  Linux only  One core Processor Activation for #EPEV  Linux only  One core Processor Activation for #EPGW      | AIX or VIOS:  12  18  24 Linux only:  12  18  24            |
| Memory DIMM                                          |  #EM75  #EM76  #EM77  #EM7J  #EMFH  #EMFJ  #EMFK  #EMFL                          |  64 GB (2 x 32 GB) DDR4 Memory DIMM  128 GB (2 x 64 GB) DDR4 Memory DIMM  256 GB (2 x 128 GB) DDR4 Memory DIMM  512 GB (2 x 256 GB) DDR4 Memory DIMM  64 GB (2 x 32 GB) DDR5 Memory DIMM  128 GB (2 x 64 GB) DDR5 Memory DIMM  256 GB (2 x 128 GB) DDR5 Memory DIMM  512 GB (2 x 256 GB) DDR5 Memory DIMM | Four of the  Feature Code  for a base  2-socket. a                |
| Memory  activation                                   | #EMCP                                                                                    | 1 GB Memory Activation for MRX                                                                                                                                                                                                                                                                                    | 256 GB or 50%  memory that is  installed,  whichever is  higher.  |
| NVMe  backplane                                      | #EJ0Q                                                                                    | 10 NVMe U.2 Flash Drive bays                                                                                                                                                                                                                                                                                      | 1                                                                 |

| Feature          | Feature  Code                           | Feature Code description                                                                                                                                                                                                                             | Minimum  quantity                                                                               |
|------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| NVMe device      |  #EC5X  #EC7T  #ES1E  #ES1G  #ES3E |  Mainstream 800 GB SSD PCIe3 NVMe U.2  module for AIX or Linux  800 GB Mainstream NVMe U.2 SSD 4k for  AIX or Linux  Enterprise 1.6 TB SSD PCIe4 NVMe U.2  module for AIX or Linux  Enterprise 3.2 TB SSD PCIe4 NVMe U.2 module for AIX or Linux | One of any of  these Feature  Codes.  Note: As a best  practice, use  two for a  mirrored copy. |
| Network  adapter |  #EC2U  #EC66  #EN0W                 |  PCIe3 2-Port 25/10Gb NIC&ROCE SR/Cu  Adapter  PCIe4 2-port 100 Gb ROCE EN adapter  PCIe2 2-port 10/1GbE BaseT RJ45 Adapter                                                                                                                       | Choose one of  any of these  Feature  Codes.                                                    |
| Power supplies   | EB39                                    | Power Supply - 2300W for Server (200 - 240  VAC)                                                                                                                                                                                                     | 4                                                                                               |
| Power cord       | 4558                                    | Power cord To PDU/UPS (100 - 240V/16A)                                                                                                                                                                                                               | 4                                                                                               |
| Language  group  | 9300                                    | Language Group Specify - US English                                                                                                                                                                                                                  | One of any  language                                                                            |

- a. IBM now offers a mixed DIMM memory feature (#EMCM) for the Power E1050, which enables the mixing of 128 GB and 256 GB DIMMs in a 50:50 ratio.

