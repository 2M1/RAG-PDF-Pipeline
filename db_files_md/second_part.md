## 1.6 PCIe adapter slots

The Power E1050 server has up to 11 PCIe slots in the systems drawer. A mix of PCIe Gen5 and Gen4 general-purpose hot-plug slots can deliver configuration flexibility and expandability. Two adapter slots are PCIe Gen5 8-lane, three adapter slots are PCIe Gen4 8-lane, and six adapter slots are Gen4 16-lane or Gen5 8-lane. All adapter slots are full-height, half-length in size. BSCs are used to house the adapter in the system unit for installation, removal, and service from the rear of the system. All the PCIe slots are single-root I/O virtualization (SR-IOV) capable.

The 16-lane slots can provide up to twice the bandwidth of the 8-lane slots because they offer twice as many PCIe lanes. PCIe Gen5 slots can support up to twice the bandwidth of PCIe Gen4 slots and up to four times the bandwidth of a PCI Gen3 slot, assuming an equivalent number of PCIe lanes. PCIe Gen1, PCIe Gen2, PCIe Gen3, PCIe Gen4, and PCIe Gen5 adapters can be plugged into a PCIe Gen5 slot, if that adapter is supported. The 16-lane slots can be used to attach PCIe Gen3 or PCIe Gen4 I/O expansion drawers.

Table 1-6 shows the number of slots that is supported by the number of processor modules.

Table 1-6   Available PCIe slots

|   Processor modules |   2-socket | 3-socket or 4-socket                   |
|---------------------|------------|----------------------------------------|
|                   2 |          6 | x16 Gen5 or four slots  (CAPI-capable) |
|                   3 |          3 | x8 Gen4 slots                          |
|                   2 |          2 | x8 Gen5 slots                          |

## Notes:

-  The PCIe Genx8 slot, C1, is reserved for an Ethernet adapter to help ensure proper manufacture and test of the server.
-  Each NVMe SSD interface is a Gen4 x4 PCIe bus. The NVMe drives can be in an OS-controlled RAID 0, RAID 1 array. Hardware RAID is not supported on the NVMe drives.
-  This server has an energy-efficient design for cooling the PCIe adapter environment. The server can sense which IBM PCIe adapters are installed in their PCIe slots. If an adapter is known to require higher levels of cooling, the server automatically speeds up fans to increase airflow across the PCIe adapters.
-  The terms '16-lane' and 'x16' and '8-lane' and 'x8' are interchangeably used in this case with the same meaning.

Figure 1-6 shows the 11 PCIe adapter slots location with labels for the Power E1050 server model.

Figure 1-6   PCIe adapter slot locations on the Power E1050 server

<!-- image -->

Slot C0 is not included in the list. It is meant for only the eBMC service processor card. The total number of PCIe adapter slots that is available can be increased by adding one or more PCIe Gen3 I/O expansion drawers (#EMX0). The maximum number depends on the number of processor modules physically installed. The maximum is independent of the number of processor core activations.

Table 1-7 list the number of maximum number of I/O drawers per populated socket.

Table 1-7   I/O drawers per populated processor socket

|   Number of processor sockets |   Maximum number of PCI I/O  drawers | Number of fan-out modules   |
|-------------------------------|--------------------------------------|-----------------------------|
|                             2 |                                    2 | Up to 4                     |
|                             3 |                                    3 | Up to 6                     |
|                             4 |                                    4 | Up to 8                     |

The connection of each fanout module in a PCIe Gen3 or PCIe Gen4 expansion drawer requires the installation of one (#EJ08) PCIe cable adapter that is placed in one of the PCIe x16 adapter slots of the system unit. For more information about I/O expansion drawers, see 2.4.4, 'Attachment of I/O-drawers' on page 72 and 3.9, 'External IO subsystems' on page 101.

## 1.7  Operating system support

The Power E1050 server supports AIX and Linux OSs, and includes support for Red Hat OpenShift. In addition, VIOS can be installed in a special logical partition (LPAR) where its primary function is to host physical I/O adapters, such as network and storage connectivity, and provide virtualized I/O devices for client LPARs.

For more information about the software that is available on IBM Power, see IBM Power.

The minimum supported levels of IBM AIX and Linux at the time of announcement are described in the following sections. For more information about hardware features, see the Power E1050 sales manual page.

IBM Power Systems Prerequisites helps to plan a successful system upgrade by providing the prerequisite information for features in use or that you plan to add to a system. It is possible to choose an MTM (9043-MRX for Power E1050) and discover all the prerequisites, the OS levels that are supported, and other pertinent information.

## 1.7.1  AIX operating system

At the time of announcement, Power E1050 supports the following minimum levels of AIX when installed with direct I/O connectivity:

-  AIX 7.3 with the 7300-00 Technology Level and Service Pack 2 or later
-  AIX 7.2 with the 7200-05 Technology Level and Service Pack 4 or later

At the time of announcement, Power E1050 supports the following minimum level of AIX when installed with virtual I/O:

-  AIX 7.3 with the 7300-00 Technology Level and Service Pack 1 or later
-  AIX 7.2 with the 7200-05 Technology Level and Service Pack 1 or later
-  AIX 7.2 with the 7200-04 Technology Level and Service Pack 2 or later
-  AIX 7.1 with the 7100-05 Technology Level and Service Pack 6 or later

Notes: AIX 7.1 has been withdrawn from marketing since November 2021. AIX 7.2 is the minimum available version for a new software order.

AIX 7.1 instances must run in an LPAR in IBM Power8® compatibility mode with a VIOS-based virtual storage and network.

AIX 7.2 instances can use both physical and virtual I/O adapters, but must run in an LPAR in IBM Power9 compatibility mode.

AIX 7.3 instances can use both physical and virtual I/O adapters, and can run in an LPAR in native Power10 mode.

IBM periodically releases maintenance packages (service packs (SPs) or technology levels (TLs)) for the AIX OS. For more information about these packages, and downloading and obtaining the installation packages, see Fix Central.

The Service Update Management Assistant (SUMA), which can help you automate the task of checking and downloading OS downloads, is part of the base OS. For more information about the suma command, see IBM Documentation.

The AIX OS software is available to order in the following editions:

-  AIX Standard Edition: Stand-alone AIX OS only.
-  AIX Enterprise Edition: The AIX OS plus the bundled Power software stack.
-  IBM Private Cloud Edition with AIX7: An enhanced set from the AIX Enterprise Edition of the bundled software stack intended for private cloud usage. For the list of offered software that is included, see 1.9, 'IBM Power solutions' on page 29.

## Subscription licensing model

AIX Standard Edition, AIX Enterprise Edition, and IBM Private Cloud Edition with AIX are also available under a subscription licensing model that provides access to an IBM software maintenance for a specified subscription term (1 or 3 years). The subscription term begins on the start date and ends on the expiration date, which is reflected at the IBM ESS website.

Customers are licensed to run the product through the expiration date of the 1- or 3-year subscription term, and then can renew the subscription at the end of it to continue using the product. This model provides flexible and predictable pricing over a specific term, with lower upfront costs of acquisition.

Another benefit of this model is that the licenses are customer number entitled, which means that they are not tied to a specific hardware serial number as with a standard license grant. Therefore, the licenses can be moved between on-premises and cloud if needed, something that is becoming more of a requirement with hybrid workloads.

The product IDs for the subscription licenses are listed in Table 1-8.

Table 1-8   Subscription license product IDs (1- or 3-year terms)

| Product ID   | Description                                              |
|--------------|----------------------------------------------------------|
| 5765-2B1     | IBM AIX 7 Standard Edition Subscription 7.3.0            |
| 5765-2E1     | IBM AIX Enterprise Edition Subscription 1.8.0            |
| 5765-2C1     | IBM Private Cloud Edition with AIX 7 Subscription 1.8.0  |
| 5765-6C1     | IBM Private Cloud Edition Subscription 8.0 (without AIX) |

The subscription licenses are orderable through an IBM configurator. The standard AIX license grant and monthly term licenses for standard edition are still available.

## 1.7.2 Linux operating system distributions

Linux is an open-source, cross-platform OS that runs on numerous platforms from embedded systems to mainframe computers. It provides an UNIX like implementation across many computer architectures.

The following Linux distributions are supported on the Power E1050 server model.

## Red Hat Enterprise Linux

The latest version of the RHEL distribution from Red Hat is supported in native Power10 mode, allowing it to access all the features of the Power10 processor and platform.

At the time of announcement, the Power E1050 server supports the following minimum levels of the RHEL OS:

-  Red Hat Enterprise Linux 8.4 for Power Little Endian (LE) or later
-  Red Hat Enterprise Linux 9.0 for Power LE or later
-  Red Hat Enterprise Linux for SAP with Red Hat Enterprise Linux 8.4 for Power LE or later

Note: RHEL 9.0 for Power LE or later is supported to run once it is announced.

RHEL is sold on a subscription basis, with initial subscriptions and support that are available for 1 year, 3 years, or 5 years. Support is available either directly from Red Hat or from IBM Technical Support Services. An RHEL 8 for Power LE unit subscription covers up to four cores and up to four LPARs, and the subscription can be stacked to cover more cores and LPARs.

When a client orders RHEL from IBM, a subscription activation code is published at the IBM ESS website. After you retrieve this code from IBM ESS, use it to establish proof of entitlement and download the software from Red Hat.

## SUSE Linux Enterprise Server

The latest version of the SUSE Linux Enterprise Server distribution of Linux from SUSE is supported in native Power10 mode, allowing it to access all the features of the Power10 processor and platform.

At the time of announcement, the Power E1050 server supports the following minimum levels of SUSE Linux Enterprise Server OS:

-  SUSE Linux Enterprise Server 15 Service Pack 3 or later
-  SUSE Linux Enterprise Server for SAP with SUSE Linux Enterprise Server 15 Service Pack 3 or later

SUSE Linux Enterprise Server is sold on a subscription basis, with initial subscriptions and support that are available for 1 year, 3 years, or 5 years. Support is available either directly from SUSE or from IBM Technical Support Services. A SUSE Linux Enterprise Server 15 unit subscription covers 1 - 2 sockets or 1 - 2 LPARs, and they subscriptions can be stacked to cover more sockets and LPARs.

When a client orders SUSE Linux Enterprise Server from IBM, a subscription activation code is published at the IBM ESS website. After you retrieve this code from IBM ESS, use it to establish proof of entitlement and download the software from SUSE.

## Linux and Power10 technology

The Power10 specific toolchain is available in Advance Toolchain 15.0, which allows clients and developers to use all new Power10 processor-based technology instructions when programming. The cross-module function call impact was reduced because of a new PC-relative addressing mode.

One specific benefit of Power10 technology is a 10 times - 20 times advantage over Power9 processor-based technology for artificial intelligence (AI) inferencing workloads because of increased memory bandwidth and new instructions. One example is the new special purpose-built Matrix Math Accelerator (MMA) that was tailored for the demands of machine learning and deep learning inference. The MMA also supports many AI data types.

Network virtualization is an area with significant evolution and improvements, which benefit virtual and containerized environments. The following recent improvements were made for Linux networking features on Power10 processor-based servers:

-  SR-IOV allows virtualization of network cards at the controller level without needing to create virtual Shared Ethernet Adapters (SEAs) in the VIOS partition. It is enhanced with a virtual Network Interface Controller (vNIC), which allows data to be transferred directly from the partitions to or from the SR-IOV physical adapter without transiting through a VIOS partition.
-  Hybrid Network Virtualization (HNV) allows Linux partitions to use the efficiency and performance benefits of SR-IOV logical ports and participate in mobility operations, such as active and inactive Live Partition Mobility (LPM) and Simplified Remote Restart (SRR). HNV is enabled by selecting Migratable when an SR-IOV logical port is configured.

## Security

Security is a top priority for IBM and our distribution partners. Linux security on IBM Power is a vast topic that can be the subject of detailed separate material. However, improvements in the areas of hardening, integrity protection, performance, platform security, and certifications are introduced in this section.

Hardening and integrity protection deal with protecting the Linux kernel from unauthorized tampering while allowing upgrading and servicing of the kernel. These topics become even more important when running in a containerized environment with an immutable OS, such as CoreOS in Red Hat OpenShift.

Performance is a security topic because specific hardening mitigation strategies (for example, against side-channel attacks) can have a significant performance effect. In addition, cryptography can use significant compute cycles.

The Power E1050 features transparent memory encryption at the level of the controller, which prevents an attacker from retrieving data from physical memory or storage-class devices that are attached to the processor bus.

## 1.7.3  Red Hat OpenShift Container Platform

The Red Hat OpenShift Container Platform is supported to run on IBM Power servers, including the IBM Power E1050 server. Red Hat OpenShift Container Platform is a container orchestration and management platform that provides a resilient and flexible environment to develop and deploy applications. It extends the open source Kubernetes project to provide an enterprise-grade platform to run and manage workloads by using Linux container technology.

A Red Hat OpenShift Container Platform cluster is built from several nodes, which can run on either physical or virtual machines (VMs). A minimum of three control plane nodes are required to support the cluster management function, and at least two compute nodes are required to provide the capacity to run workloads. During installation, an extra bootstrap node is required to host the files that are required for the installation and initial setup.

The bootstrap and control plane nodes are all based on RHEL CoreOS, which is a minimal immutable container host version of the RHEL distribution that inherits the associated hardware support statements. The compute nodes can run on either RHEL or RHEL CoreOS.

Red Hat OpenShift Container Platform is available on a subscription basis, with initial subscriptions and support that are available for 1 year, 3 years, or 5 years. Support is available either directly from Red Hat or from IBM Technical Support Services. Red Hat OpenShift Container Platform subscriptions cover two processor cores each, and they can be stacked to cover more cores. At the time of announcement, the Power E1050 server supports Red Hat OpenShift Container Platform 4.10 or later.

When a client orders Red Hat OpenShift Container Platform for Power from IBM, a subscription activation code is published at the IBM ESS website. After you retrieve this code from IBM ESS, use it to establish proof of entitlement and download the software from Red Hat.

For more information about running Red Hat OpenShift Container Platform on IBM Power, see the Red Hat OpenShift documentation.

## 1.7.4  Virtual I/O Server

VIOS is part of the IBM PowerVM Enterprise edition feature. VIOS is software that is installed in a special LPAR, which facilitates the sharing of physical I/O resources between client LPARs within the server. VIOS provides a virtual Small Computer System Interface (SCSI) target, virtual Fibre Channel, SEA, and PowerVM Active Memory Sharing capabilities to client LPARs within the system.

The minimum required level of VIOS for the Power E1050 server model is VIOS 3.1.3.21 or later. IBM regularly updates the VIOS code. For more information, see IBM Fix Central.

## 1.7.5  Entitled Systems Support

The IBM ESS website is the IBM goto place to view and manage IBM Power and IBM Storage software and hardware. In general, most products that are offered by IBM Systems that are purchased through IBM Digital Sales representatives or IBM Business Partners are accessed at this website when IBM e-config on Cloud is used.

The website features the following three main sections:

-  My Entitled Software: Activities that are related to IBM Power and IBM Storage software, such as downloading licensed, no-charge, and trial software media; placing software update orders; and managing software keys.
-  My Entitled Hardware: Activities that are related to IBM Power and IBM Storage hardware, such as renewing Update Access Keys (UAKs); buying and using Elastic CoD; assigning or buying credits for new and existing pools in Enterprise Pools 2.0; downloading Storage CoD codes; and managing Hybrid Capacity credits.
-  My Inventory: Activities that are related to IBM Power and IBM Storage inventory, such as browsing software licenses, software maintenance, and hardware inventory; or managing inventory retrievals by using Base Composer or generating several types of reports.

For initial access and to get more information, see IBM ESS.

Note: A valid registered IBMid is required before a user can sign in to IBM ESS.

## 1.7.6  Update Access Keys

UAKs are a technology that was introduced with Power8 servers and adapted by the IBM Power9 and Power10 servers. An UAK is an important parameter that is first validated by the system before an update can proceed.

UAKs have two types:

-  System firmware UAK: This UAK is checked when system firmware updates are applied to the system. The UAK includes an expiration date. System firmware updates contain a release date. When attempting to apply a system firmware update, if the release date for the firmware updates has passed the expiration date for the UAK, the updates are not processed. As UAKs expire, they must be replaced by using either the HMC or the Advanced System Management Interface (ASMI) on the service processor.
-  AIX UAK: This UAK checks for an active Software Maintenance Agreement (SWMA) when updating the AIX OS. The server uses an AIX update that includes the expiration date for the associated SWMA agreement. The server periodically checks and informs the administrator about AIX UAKs that are about to expire, that have expired, or that are missing. The AIX UAK is a CoD code. There is a single AIX UAK per server (not one per LPAR). As the AIX UAK expires, it must be replaced by using either the HMC or ASMI GUI.

By default, newly delivered systems include an UAK that often expires after 3 years. Thereafter, the UAK can be extended every 6 months, but only if an IBM maintenance contract exists. The contract can be verified at the IBM ESS website (see 1.7.5, 'Entitled Systems Support' on page 19).

Figure 1-7 shows an example of viewing the system firmware UAK in the HMC.

Figure 1-7   UAK view from the HMC

<!-- image -->

Figure 1-8 shows another example of viewing the access key in ASMI.

Figure 1-8   Access key view from the ASMI

<!-- image -->

## 1.8  Hardware Management Console overview

The HMC can be a hardware appliance or virtual appliance that can be used to configure and manage your systems. The HMC connects to one or more managed systems and provides capabilities for the following primary functions:

-  Systems Management functions, such as power off, power on, system settings, CoD, enterprise pools, shared processor pools (SPPs), Performance and Capacity Monitoring, and starting ASMI for managed systems.
-  Delivers virtualization management through support for creating, managing, and deleting LPARs, LPM, and Remote Restart; configuring SRIOV; and managing VIOSs, dynamic resource allocation, and OS terminals.
-  Acts as the Service Focal Point (SFP) for systems and supports service functions, including Call Home, dump management, guided repair and verify, concurrent firmware updates for managed systems, and around-the-clock error reporting with Electronic Service Agent (ESA) for faster support.
-  Provides appliance management capabilities for configuring the network and users on the HMC, and updating and upgrading the HMC.

## 1.8.1 HMC 7063-CR2

The 7063-CR2 IBM Power HMC (see Figure 1-9) is a second-generation IBM Power processor-based HMC.

Figure 1-9   HMC 7063-CR2

<!-- image -->

The CR2 model includes the following features:

-  Six-core Power9 130 W processor chip
-  64 GB (4x16 GB) or 128 GB (4x32 GB) of memory RAM
-  1.8 TB with RAID 1 protection of internal disk capacity
-  Four-port 1 Gb Ethernet (RH-45), 2-port 10 Gb Ethernet (RJ-45), two USB 3.0 ports (front side) and two USB 3.0 ports (rear side), and 1 Gb Intelligent Platform Management Interface (IPMI) Ethernet (RJ-45)
-  Two 900 W power supply units (PSUs)
-  Remote Management Service: IPMI port (OpenBMC) and Redfish application programming interface (API)
-  The Base Warranty is 1 year 9x5 with available optional upgrades

A USB Smart Drive is not included.

Note: The recovery media for V10R1 is the same for 7063-CR2 and 7063-CR1.

The 7063-CR2 is compatible with flat panel console kits 7316-TF3, TF4, and TF5.

Note: The 7316-TF3 and TF4 were withdrawn from marketing.

## 1.8.2 Virtual HMC

Initially, the HMC was sold only as a hardware appliance, including the HMC firmware. However, IBM extended this offering to allow the purchase of the hardware appliance and a virtual appliance that can be deployed on ppc64le architectures and deployed on x86 platforms.

Any customer with a valid contract can download this offering from the IBM ESS website, or this offering can be included with an initial Power E1050 order.

The virtual HMC supports the following hypervisors:

-  On x86 processor-based servers:
- - Kernel-based Virtual Machine
- - Xen
- - VMware
-  On Power processor-based servers: PowerVM

The following minimum requirements must be met to install the virtual HMC:

-  16 GB of memory
-  Four virtual processors
-  Two network interfaces (a maximum of four is allowed)
-  One disk drive (500 GB available disk drive)

For an initial Power E1050 order with the IBM configurator (e-config), you can find the HMC virtual appliance by selecting Add software → Other System Offering s (as product selections) and then select either of the following items:

-  5765-VHP for IBM HMC Virtual Appliance for Power V10
-  5765-VHX for IBM HMC Virtual Appliance x86 V10

For more information about an overview of the Virtual HMC, see this web page.

For more information about how to install the virtual HMC appliance and all requirements, see IBM Documentation.

## 1.8.3 BMC network connectivity rules for the 7063-CR2

The 7063-CR2 HMC features a baseboard management controller (BMC), which is a specialized service processor that monitors the physical state of the system by using sensors. The OpenBMC that is used on 7063-CR2 provides a GUI that can be accessed from a workstation that has network connectivity to the BMC. This connection requires an Ethernet port to be configured for use by the BMC.

Note: This section describes the BMC of the hardware HMC 7063-CR2. The Power E1050 also uses an eBMC for the systems management, as described in 2.6, 'The enterprise Baseboard Management Controller' on page 74.

The 7063-CR2 provides two network interfaces (eth0 and eth1) for configuring network connectivity for BMC on the appliance.

Each interface maps to a different physical port on the system. Different management tools name the interfaces differently. The HMC task Console Management → Console Settings → Change BMC/IPMI Network Settings modifies only the Dedicated interface.

The BMC ports are listed in Table 1-9.

Table 1-9   BMC ports

| Management tool                                 | Logical port   | Shared or dedicated   | CR2 physical port    |
|-------------------------------------------------|----------------|-----------------------|----------------------|
| OpenBMC UI                                      | eth0           | Shared                | eth0                 |
| OpenBMC UI                                      | eth1           | Dedicated             | Management port only |
| ipmitool                                        | lan1           | Shared                | eth0                 |
| ipmitool                                        | lan2           | Dedicated             | Management port only |
| HMC task (change  BMC or IMPI Network  settings | lan2           | Dedicated             | Management port only |

Figure 1-10 shows the BMC interfaces of the HMC.

Figure 1-10   BMC interfaces

<!-- image -->

The main difference is that the shared and dedicated interface to the BMC can coexist. Each one has its own LAN number and physical port. Ideally, the customer configures one port, but both can be configured. The rules to connecting IBM Power servers to the HMC remain the same as previous versions.

## 1.8.4  High availability HMC configuration

For the best manageability and redundancy, a dual HMC configuration is suggested. This configuration can be two hardware appliances, but also one hardware appliance and one virtual appliance or two virtual appliances.

The following requirements must be met:

-  Two HMCs are at the same version.
-  The HMCs use different subnets to connect to the Flexible Service Processors (FSPs).
-  The HMCs can communicate with the servers' partitions over a public network to allow for full synchronization and function.

## 1.8.5 HMC code level requirements for Power E1050

The minimum required HMC version for Power E1050 is V10R1 M1020. V10R1 is supported only on 7063-CR1, 7063-CR2, and Virtual HMC appliances. It is not supported on 7042 machine types. HMC with V10R1 cannot manage Power7 processor-based systems.

An HMC that is running V10R1 M1020 includes the following features:

-  HMC OS Secure Boot support for the 7063-CR2 appliance.
-  Ability to configure login retries and suspended time and support for inactivity expiration in the password policy.
-  Ability to specify the HMC location and data replication for groups.
-  VIOS Management Enhancements:
- - Prepare for VIOS maintenance:
- · Validate for redundancy for the storage and network that is provided by VIOS to customer partitions.
- · Switch path of redundant storage and network to start failover.
- · Roll back to original configuration on failure of preparation.
- · Audit the various validation and preparation steps that are performed.
- · Report any failure that is seen during preparation.
- - CLI and scheduled operations support for VIOS backup or restore VIOS configurations and SSP configurations
- - Option to back up or restore a Shared Storage Pool configuration in HMC
- - Options to import or export the backup files to external storage
- - Option to fail over all vNICs from one VIOS to another one
-  Supports 128 MB and 256 MB local memory bus (LMB) sizes.
-  Automatically chooses the fastest network for LPM memory transfer.
-  HMC user experience enhancements:
- - Usability and performance improvements
- - Enhancements to help connect global search
- - Quick view of serviceable events
- - More progress information for UI wizards
-  Allows LPM/Remote Restart when a virtual optical device is assigned to a partition.
-  UAK support.
-  Configures the Virtualization Management Interface (VMI) connection to the Power Hypervisor for the Power E1050 and for the Power10 scale-out servers.

-  Scheduled operation function: In the ESA, there is a new feature that allows customers to receive message alerts only if scheduled operations fail (see Figure 1-11).

Figure 1-11   HMC alert feature

<!-- image -->

Log retention of the HMC audit trail is also increased.

## 1.8.6  Configuring the VMI

Starting with the Power10 scale-out servers and the Power E1050 server, IBM Power servers are migrating to an industry-standard service processor chipset that is known as eBMC. As part of the eBMC transition, the virtualization management communication path was removed from the service processor.

This path is something specific to PowerVM with the HMC. eBMC is based on of the OpenBMC code base, which is platform-neutral. Developers wanted to minimize the number of PowerVM specific functions in eBMC.

The industry-standard service processor communication protocols and the performance of the service processor do not lend themselves well to supporting the virtualization management traffic pass-through like with the FSP in the past. VMI was invented to satisfy the need for a new network connection point for the HMC.

The VMI design is a combination of HMC and Power Hypervisor support for a new VMI network endpoint for handling virtualization management. The service processor now has two IP addresses for each system management network port: one for system management (eBMC), and one for virtualization management (VMI).

Note: Each port also has two MAC addresses, that is, BMC and VMI each have one.

The eBMC IP address is the equivalent of the FSP IP address in previous generations of IBM Power servers. The WebUI, Representational State Transfer (REST) interfaces, and others, all use the eBMC IP address. This IP address is the only one that users interact with directly.

The VMI IP address is used for virtualization management. This IP address is the one that the HMC used to communicate with Power Hypervisor for partition management and consoles. Users do not interact directly with this IP address. From a customer perspective, other than having two IP addresses on the service network instead of one, there is no difference from an HMC user perspective.

All traffic between the HMC and VMI is encrypted with TLS by using a system unique certificate.

Figure 1-12 shows a dual HMC connection to the eBMC of an Power E1050 server.

Figure 1-12   Dual HMC connection to a Power E1050 server

<!-- image -->

VMI supports both DHCP and static IP address configurations. After the server is connected to the HMC and configured by setting the access passwords, you may configure the VMI. To configure the VMI, click VMI Configuration in the HMC GUI, as shown in Figure 1-13. In the configuration dialog box, you may switch between DHCP or a static IP address. The default VMI connection setting (not the eBMC connection) for a new Power E1050 server is static, so if you want to use DHCP, you must change the configuration from static to DHCP before you power on the server.

Figure 1-13   VMI configuration of a Power E1050 server

<!-- image -->

Here is a summary for configuring a new server that has factory settings:

- 1. Connect the Ethernet cable from the eBMC port to the internal HMC network.
- 2. Plug in the power cables. The eBMC starts and obtains the IP address configuration from the DHCP server on the HMCs.
- 3. Enter the access password or, if HMC auto-discovers, the default credentials are used.
- 4. The server shows as Power Off, but it is now in a manageable state.
- 5. Configure the VMI to change from static to DHCP, as shown in Figure 1-13.
- 6. Power on the server. The VMI obtains its IP address, and the HMC to VMI connection is established automatically.

## 1.8.7  HMC currency

In recent years, cybersecurity emerged as a national security issue and an increasingly critical concern for CIOs and enterprise IT managers.

The IBM Power processor-based architecture has always ranked highly in terms of end-to-end security, which is why it remains a platform of choice for mission-critical enterprise workloads.

A key aspect of maintaining a secure IBM Power environment is helping ensure that the HMC (or virtual HMC) is current and fully supported (including hardware, software, and IBM Power firmware updates).

Outdated or unsupported HMCs represent a technology risk that can quickly and easily be mitigated by upgrading to a current release.

## 1.9  IBM Power solutions

The Power E1050 server comes cloud-enabled with integrated PowerVM Enterprise capabilities.

## 1.9.1  IBM Power Private Cloud Solution with Dynamic Capacity

The IBM Power Private Cloud Solution with Dynamic Capacity is an infrastructure offering that you can use to leverage cloud agility and economics while getting the same business continuity and flexibility that you already enjoy from IBM Power servers.

The IBM Power Private Cloud Solution offers:

-  Cost optimization with pay-for-use pricing
-  Automated and consistent IT management with Red Hat Ansible for IBM Power
-  IBM Proactive Support for IBM Power services
-  IBM Systems Lab Services Assessment and implementation assistance

Both Elastic and Shared Utility Capacity options are available on all Power E1050 servers through the Virtual Capacity (4586-COD) MTM and the IBM ESS website.

Elastic Capacity on the Power E1050 server enables you to deploy pay-for-use consumption of processor, memory, and supported OSs.

Shared Utility Capacity on Power E1050 servers provides enhanced multi-system resource sharing and by-the-minute tracking and consumption of compute resources across a collection of systems within a Power Enterprise Pools 2.0 (PEP2). Shared Utility Capacity delivers a complete range of flexibility to tailor initial system configurations with the right mix of purchased and pay-for-use consumption of processor, memory, and software across a collection of Power E1050 and Power E950 servers.

Metered Capacity is the extra installed processor and memory resource above each system's Base Capacity. It is activated and made available for immediate use when a pool is started, and then it is monitored by the minute by an IBM Cloud Management Console (IBM CMC).

For more information, see IBM Power Enterprise Pools 2.0.

Metered resource usage is charged only for minutes that exceed the pool's aggregate base resources, and usage charges are debited in real time against your purchased Capacity Credits (5819-CRD) on account.

IBM offers a Private Cloud Capacity Assessment and Implementation Service that is performed by IBM Systems Lab Services professionals, which can be preselected at time of purchase or requested for qualifying Power E1050 servers.

## 1.9.2 IBM Private Cloud Edition 1.8

IBM Private Cloud Edition is a complete package that adds flexible licensing models in the cloud. It helps you to rapidly deploy multi-cloud infrastructures with a compelling set of cloud-enabled capabilities. The IBM Power Enterprise Cloud Edition primarily provides value for clients that use both AIX and Linux on Power, with simplified licensing models and advanced features.

The IBM Private Cloud Edition (5765-ECB) includes:

-  IBM PowerSC 2.1
-  IBM PowerSC Multi-Factor Authentication (MFA)
-  IBM Cloud PowerVC for Private Cloud
-  IBM VM Recovery Manager DR
-  IBM Tivoli® Monitoring

If you use IBM AIX as the primary OS, there is a specific offering for it: IBM Private Cloud Edition with AIX 7 1.8.0 (5765-CBA). The offering includes:

-  IBM AIX 7.3 or IBM AIX 7.2
-  IBM PowerSC 2.1
-  IBM PowerSC MFA
-  IBM Cloud PowerVC for Private Cloud
-  IBM VM Recovery Manager DR
-  IBM Tivoli Monitoring

## IBM PowerSC 2.1

IBM PowerSC 2.1 (5765-SC2) provides a security and compliance solution that is optimized for virtualized environments on IBM Power running IBM PowerVM and IBM AIX, or Linux on Power. Security control and compliance are some of the key components that are needed to defend virtualized data centers and a cloud infrastructure against evolving threats.

The PowerSC 2.1 product contains the following enhancements:

-  A blacklisting anti-virus feature to allow selective, on-demand hash searches across endpoints that are managed through PowerSC
-  Linux on Intel support for PowerSC endpoints, including MFA on IBM Power
-  Single sign-on (SSO) support
- Users can log in to PowerSC through SSO with their OpenID Connect (OIDC) Enterprise identity provider and MFA, enabling integration with any application user interface (UI).
-  MFA support for Rivest-Shamir-Adleman (RSA) web API
- User MFA includes RSA through the web API, and it no longer employs the access control entry (ACE) protocol.
-  User-defined alt-disk for TL and SP updates
- Users can specify alt-disk through Trusted Network Connect (TNC) for TL and SP updates on AIX endpoints.

For more information, see the PowerSC 2.1 sales manual.

## IBM PowerSC Multi-Factor Authentication

IBM PowerSC MFA provides alternative authentication mechanisms for systems that are used with RSA SecurID-based authentication systems, and certificate authentication options such as Common Access Card (CAC) and Personal Identification Verification (PIV) cards. IBM PowerSC MFA allows the use of alternative authentication mechanisms instead of the standard password.

You can use IBM PowerSC MFA with many applications, such as Remote Shell (rsh), Telnet, and Secure Shell (SSH).

IBM PowerSC MFA raises the level of assurance of your mission-critical systems with a flexible and tightly integrated MFA solution for IBM AIX and Linux on Power virtual workloads running on IBM Power servers.

For more information, see the PowerSC MFA sales manual.

## IBM PowerVC for Private Cloud

IBM PowerVC for Private Cloud works with IBM Power Virtualization Center to provide an end-to-end cloud solution. You can use PowerVC for Private Cloud to provision workloads and manage virtual images.

With PowerVC for Private Cloud, you can perform several operations, depending on your role within a project.

Administrators can perform the following tasks:

-  Creating projects and assigning images to projects to give team-specific access to images
-  Setting policies on projects to specify default virtual machine (VM) expiration
-  Authorizing users to projects
-  Creating expiration policies to reduce abandoned VMs
-  Specifying which actions require approvals and approving requests
-  Creating, editing, and deleting deployment templates
-  Deploying an image from a deployment template
-  Dispositioning requests
-  Performing lifecycle operations on VMs, such as capture, start, stop, delete, resume, and resize
-  Monitoring usage (metering) data across the project or per user

Users can perform the following tasks on resources to which they are authorized. Some actions might require administrator approval. When a user tries to perform a task for which approval is required, the task moves to the request queue before it is performed (or rejected).

-  Performing lifecycle operations on VMs, such as capture, start, stop, delete, resume, and resize
-  Deploying an image from a deployment template
-  Viewing and withdrawing outstanding requests
-  Requesting VM expiration extension
-  Viewing their usage data

## PowerVC 2.0 UI

IBM Power Virtualization Center 2.0 introduces a new UI that is based on the Carbon framework. Carbon is the IBM open-source design system for products and digital experiences. With the IBM Design Language as its foundation, the system consists of working code, design tools and resources, human interface guidelines, and a vibrant community of contributors.

IBM Power Virtualization Center 2.0 comes with a new UI, and many new features and enhancements.

Because IBM Power Virtualization Center is built on the OpenStack technology, you might see some terminology in messages or other text that is not the same as what you see elsewhere in PowerVC. There is also some terminology that might be different from what you are used to seeing in other IBM Power products.

## Feature support for PowerVC editions

PowerVC offers different functions depending on the edition that you installed and the hypervisor that are you are using to manage your systems.

IBM Cloud PowerVC Manager includes all the functions of the PowerVC Standard Edition plus the following features:

-  A self-service portal that allows the provisioning of new VMs without direct system administrator intervention. An option is for policy approvals for the requests that are received from the self-service portal.
-  Deploy templates that simplify cloud deployments.
-  Cloud management policies that simplify management of cloud deployments.
-  Metering data that can be used for chargeback.

For more information, see the PowerVC 2.0 sales manual.

## IBM VM Recovery Manager DR

IBM VM Recovery Manager DR (5765-DRG) is an automated DR solution that enables IBM Power users to achieve low recovery times for both planned and unplanned outages. It introduces support for more storage replication solutions and support for an extra guest OS, which broadens the offering's applicability to a wider range of client requirements.

IBM VM Recovery Manager DR offers support for the following features:

-  IBM DS8000® Global Mirror
-  IBM SAN Volume Controller (SVC), and IBM Storwize® Metro and Global Mirror
-  Extended Memory Controller Symmetrix Remote Data Facility (SRDF) synchronous replication
-  Boot device selection for IBM Power8 processor-based systems

For more information, see the VMRM-DR sales manual.

## IBM Tivoli Monitoring

IBM Tivoli Monitoring products monitor the performance and availability of distributed OSs and applications. These products are based on a set of common service components that are collectively known as IBM Tivoli Management Services. Tivoli Management Services components provide security, data transfer and storage, notification mechanisms, UI presentation, and communication services in an agent-server-client architecture.

## 1.10  IBM Power platform modernization

Cloud capabilities are a prerequisite for using enterprise-level IT resources. There is a rich infrastructure around IBM Power to help modernize services with the strategic initiatives of your business.

The most important products are:

-  IBM Power Virtual Servers
-  Red Hat OpenShift Container Platform for Power

