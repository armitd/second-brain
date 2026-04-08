# Overcoming ADAS Sensor Challenges with Nexperia: Insights from Nandor Bodo

![rw-book-cover](https://wevolver-project-images.s3.us-west-1.amazonaws.com/0.97wj8tjzzdkunnamed1.jpg)

## Metadata
- Author: [[Ravi Rao]]
- Full Title: Overcoming ADAS Sensor Challenges with Nexperia: Insights from Nandor Bodo
- Category: #articles
- Summary: Advanced Driver Assistance Systems (ADAS) rely on sensors like RADAR, LiDAR, and cameras, but face challenges in power management, communication, and safety. Nexperia, with its expertise in semiconductor applications, provides solutions such as TVS diodes and MOSFETs to enhance the reliability and efficiency of these systems. As vehicles evolve towards greater autonomy, Nexperia continues to support the development of advanced ADAS technology.
- URL: https://www.wevolver.com/article/overcoming-adas-sensor-challenges-with-nexperia-insights-from-nandor-bodo

## Full Document
![Overcoming ADAS Sensor Challenges with Nexperia: Insights from Nandor Bodo](https://images.wevolver.com/eyJidWNrZXQiOiJ3ZXZvbHZlci1wcm9qZWN0LWltYWdlcyIsImtleSI6IjAuOTd3ajh0anp6ZGt1bm5hbWVkMS5qcGciLCJlZGl0cyI6eyJyZXNpemUiOnsid2lkdGgiOjcyMCwiaGVpZ2h0Ijo0NTAsImZpdCI6ImNvdmVyIn19fQ==)
Advanced Driver Assistance Systems (ADAS) are revolutionizing the automotive industry, with sensors like RADAR, LiDAR, and cameras at the heart of this transformation. These sensors enable vehicles to detect their surroundings, support critical safety functions like adaptive cruise control and collision avoidance, and pave the way for autonomous driving. However, integrating and ensuring the reliable operation of these sensors presents significant technical challenges, particularly in power management, communication, and system safety.

To understand and explore these challenges in depth, we spoke with Nandor Bodo, Principal Automotive Application Engineer at Nexperia. With a strong background in automotive research and expertise in semiconductor applications, Nandor has provided a massive contribution in developing solutions for ADAS sensor integration. In this interview, he discusses the key hurdles and how Nexperia’s advanced portfolio, including TVS diodes, MOSFETs, and step-down converters, is driving progress in creating efficient, reliable, and intelligent ADAS sensors for the vehicles of tomorrow.

Connect with [Nandor Bodo on LinkedIn](https://www.linkedin.com/in/nandor-bodo-01a65256) to follow his insights and join the conversation on innovative automotive solutions.

**Q1: Could you share insights into your role at Nexperia and highlight your journey within the automotive industry?**

I started my Automotive journey as a researcher at Liverpool John Moores University focusing on integrated solutions for the propulsion and charging of electric vehicles. The investigated systems were based on topologies incorporating multi-phase motors and as a result, more than ten peer reviewed journal and conference papers were published.

Ever since joining Nexperia I have been focused on identification of product suitability for various applications. Initially, looking at power and small signal MOSFETs and later the complete system offering based on Nexperia automotive product portfolio. The positions held enabled me to gain insights into a variety of automotive applications. I investigated low-voltage applications from high-power electric steering, braking systems, motor control applications to computationally demanding ADAS and related sensors.

**Q2: What are the primary technical challenges in ensuring the reliable operation of ADAS sensors?**

ADAS systems consist of a main controller or central ADAS computer and various sensors. The main ADAS computer controls the vehicle according to the inputs received from these sensors. There are various sensors for the ADAS system, however the most prominent ones are the [radar](https://www.nexperia.com/applications/automotive/adas-radar-sensor-module?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_radar), camera and [lidar](https://www.nexperia.com/applications/automotive/adas-lidar-systems?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_lidar).

To ensure reliable operation of these sensors some basic challenges need to be overcome. Some of these challenges can be grouped according to the subsystems they affect:

* **Power Supply Requirements:**

	+ Unstable battery voltages (12V, 24V, or 48V).
	+ Diverse voltage needs for components like processors and actuators.
* **Power Efficiency Management:**

	+ Need to conserve energy by powering down sub-systems not in use.
* **Communication Architecture and Protocols:**

	+ High-speed data communication risks and need for protection.
	+ Challenges with disturbances from high-voltage connections.
* **Signal Compatibility and Adjustment:**

	+ Mismatched signal formats requiring adjustments for reliable operation.
	+ Signal routing within the application, especially in cameras as they are often on separate PCBs from the motherboard
* Safety and Reliability:

	+ Implementation of external logic functions to provide redundancy, ensuring continuous operation in the event of a processor failure.
	+ Critical for safety-critical ADAS systems to maintain functionality under all conditions.

Depending on the complexity and power of the sensor, these challenges need to be addressed in a different manner.

**Q3: Power management is critical for ADAS sensors to ensure safety and reliability. What are the key challenges in managing and protecting the power supply, and how does Nexperia provide solutions?**

All ADAS components require stable power, but incoming power can cause disturbances that may harm the component or the environment. Nexperia provides solutions for these challenges by offering high-performance and high-reliability products like:

* Transient Voltage Suppressor (TVS) Diodes: Nexperia’s TVS diodes protect against voltage spikes, featuring compact, low-height packages ([PTVS15VS1UR-Q](https://www.nexperia.com/product/PTVS15VS1UR-Q?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_ptvs15vs1ur-q)) that save up to 50% board space, a wide voltage range (3.3V to 64V), and automotive-grade qualification up to 185°C junction temperatures ([PTVS15VS1UTR-Q](https://www.nexperia.com/product/PTVS15VS1UTR-Q?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_ptvs15vs1utr-q)). They are positioned in parallel with the incoming power supply line and their selection depends on supply line impedance and the sensitivity of the other components to voltage spikes. They clamp the voltage at a desired level and protect components against overvoltages, the effects of electrical fast transients, electrostatic discharge, arcs, inductive load switching or even lightning strikes. While TVS diodes are connected in parallel with the supply, other protection devices can be connected in series. They disconnect the supply in case of disturbances. Most of the time this means protection from reverse battery protection and can be realized with various devices according to the ADAS sensor complexity or power level.   
  
**For RADAR sensors Schottky Diodes are sufficient.** They are easy to design and do not require additional control circuits. Schottky diodes are used to decrease the voltage drop across them when they conduct while retaining the current blocking capabilities in reverse polarization. Schottky diodes come in various packages and blocking voltages, however, the recommendation goes to Nexperia’s CFP packaged diodes with improved thermal performance and reduced footprint size (e.g. [PMEG6020AELR-Q](https://www.nexperia.com/product/PMEG6020AELR-Q?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_pmeg6020aelr-q)).

![](https://images.wevolver.com/eyJidWNrZXQiOiJ3ZXZvbHZlci1wcm9qZWN0LWltYWdlcyIsImtleSI6ImZyb2FsYS8xNzQxNjAzODk2Nzk2LTE3NDE2MDM4OTY3OTYucG5nIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjo5NTAsImZpdCI6ImNvdmVyIn19fQ==)
Fig.1: Footprint area comparison SMA versus CFP packages.

* **For cameras, but even more for LiDARs, the increased power consumption and application complexity demands a better solution.** P-channel or N-channel MOSFETs can be used for additional functionality and minimal voltage drop. When combined with an anti-parallel MOSFET and an adequate controller, they act as eFuses, limiting current to enhance safety and reduce wiring costs and weight—critical in EVs. If a single MOSFET is used it can mimic the behavior of the Schottky diode if controlled by an ideal diode controller. The MOSFETs in MLPAK33 and 56 packaging give the right blend of price and performance for ADAS sensor applications.

![A diagram of a computer chip Description automatically generated](https://images.wevolver.com/eyJidWNrZXQiOiJ3ZXZvbHZlci1wcm9qZWN0LWltYWdlcyIsImtleSI6ImZyb2FsYS8xNzQxNjAzODk2ODEwLTE3NDE2MDM4OTY4MTAucG5nIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjo5NTAsImZpdCI6ImNvdmVyIn19fQ==)
*Suggested reading:* [*High-Performance MOSFETs Driving Excellence and Innovations in Automotive Electronics*](https://www.wevolver.com/article/high-performance-mosfets-driving-excellence-and-innovations-in-automotive-electronics)

**Q4: ADAS sensors operate in environments with fluctuating voltage levels. How does Nexperia ensure stable and efficient power delivery for these systems?**

Voltage fluctuations from vehicle batteries (12V, 24V or 48V) are unsuitable for ADAS hardware, which may require much lower voltages (e.g., 1V or 1.8V). To address this, Nexperia provides integrated as well as discrete solutions. Once again recommendations are specific for individual sensor types.

* For the more modest RADAR sensors, integrated step-down converters are the ideal choice. They efficiently reduce and stabilize voltage for ADAS systems. These integrated solutions simplify implementation compared to using discrete components. [Nexperias NEX40400 step-down converter](https://www.nexperia.com/products/analog-logic-ics/power-ics/dc-dc-converters/serie/nex40400?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_nex40400) offers low power consumption and a broad range of functionalities.

![](https://images.wevolver.com/eyJidWNrZXQiOiJ3ZXZvbHZlci1wcm9qZWN0LWltYWdlcyIsImtleSI6ImZyb2FsYS8xNzQxNjAzODk2ODIzLTE3NDE2MDM4OTY4MjMucG5nIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjo5NTAsImZpdCI6ImNvdmVyIn19fQ==)
Fig.3: Integrated Step-Down Converter Example: NEX40400.

* **For more power-hungry sensors like camera and LiDAR, more powerful controllers can be used. These often feature external diodes.** **The recommendation is to use trench technology Schottky diodes.** Due to the innovative trench technology, these devices perform much better in switching applications than their planar counterparts. Due to better switching waveforms and lower reverse recovery charge substantial saving can be achieved especially at high switching frequencies. Also, reduced ringing contributes to reduced emissions, reducing the requirements of the input filtering. Schottky diodes are also available in novel packages like CFP2, CFP3 and CFP5. The [PMEG40T30ER-Q](https://www.nexperia.com/product/PMEG40T30ER-Q?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_pmeg40t30er-q%20) is an automotive qualified trench Maximum Efficiency General Application (MEGA) rectifier in a small, flat CFP3 package.
* Once the voltage levels are adjusted, linear regulators are needed to iron out voltage ripples to suit the requirements of sensitive controllers of the ADAS sensors. Linear regulation can be achieved with BJTs in linear mode or integrated Low Drop-Out (LDO) regulators. Nexperia offers 150mA ([NEX90x15-Q100](https://www.nexperia.com/products/analog-logic-ics/power-ics/linear-and-low-dropout-ldo-regulators-ics/ldo-regulators-greater-than-30-v/serie/nex90515-q100?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_nex90x15-q100)) and 300mA ([NEX90x30-Q100](https://www.nexperia.com/products/analog-logic-ics/power-ics/linear-and-low-dropout-ldo-regulators-ics/ldo-regulators-greater-than-30-v/serie/nex90x30-q100?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_nex90x15-q100)) LDOs that feature low quiescent current (typical 5uA) and a wide input voltage range of up to 40V with up to 45V transient voltage. The LDOs benefit from Nexperia's expertise in package development and can handle excessive heat dissipation. The LDOs also feature an enable pin that can serve to turn a part of the circuit off when it is not needed (such can be a comms port that is not used), and a Power good pin, that can indicate a potential short circuit in the load.

Nexperia has a large portfolio of low Vcesat devices that are suitable for linear mode applications. The below table shows a comparison of some of them.

![Table 1 Comparison of Nexperia’s BJTs for use in voltage regulators](https://images.wevolver.com/eyJidWNrZXQiOiJ3ZXZvbHZlci1wcm9qZWN0LWltYWdlcyIsImtleSI6ImZyb2FsYS8xNzQxNjAzODk2ODM1LTE3NDE2MDM4OTY4MzUucG5nIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjo5NTAsImZpdCI6ImNvdmVyIn19fQ==)
Table 1: Comparison of Nexperia BJTs for use in voltage regulators.

The required reference voltage can be obtained in a few ways. Where lower accuracy voltage regulation and larger output currents (in the double-digit mA range) are required, a Zener diode, with VZ larger or equal to the desired output voltage and the maximum base emitter voltage can be used (Fig. 4). Whereas a more precise LDO uses a shunt voltage regulator like the TL431 or TLVH431 to drive the pass BJT (Fig. 5)

![](https://images.wevolver.com/eyJidWNrZXQiOiJ3ZXZvbHZlci1wcm9qZWN0LWltYWdlcyIsImtleSI6ImZyb2FsYS8xNzQxNjAzODk2ODQ4LTE3NDE2MDM4OTY4NDgucG5nIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjo5NTAsImZpdCI6ImNvdmVyIn19fQ==)
Fig. 4: Linear regulator using a Zener diode.

![](https://images.wevolver.com/eyJidWNrZXQiOiJ3ZXZvbHZlci1wcm9qZWN0LWltYWdlcyIsImtleSI6ImZyb2FsYS8xNzQxNjAzODk2ODgxLTE3NDE2MDM4OTY4ODEucG5nIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjo5NTAsImZpdCI6ImNvdmVyIn19fQ==)
Fig.5: A Circuit schematic showing a 1.8-1.45 C, 3 A voltage regulator with a low-VCEsat BJT and shunt regulator.

**Q5: What strategies does Nexperia employ for load management and ensure energy-efficient performance in these systems?**

**Cameras and LiDARs** can have parts of the design that do not need to be powered all the time. The camera Electronic Control Unit (ECU) can have multiple imagers attached, or the LiDARs can have lasers or motors that don’t have to operate all the time. To conserve energy, these systems can be turned off using integrated or discrete load switches. Another role of load switches can be to manage the power up and down sequence of the controllers. Controlled power sequences prevent surges during operation. Nexperia’s Integrated Load Switch supports efficient load management with a 2.5V–5.5V input range, adjustable current limits (110mA–2.5A), soft start, reverse protection, and 15kV ESD resistance in compact packages.

Load switch realization with NPS4053-Q100 integrated controller and MOSFET

![](https://images.wevolver.com/eyJidWNrZXQiOiJ3ZXZvbHZlci1wcm9qZWN0LWltYWdlcyIsImtleSI6ImZyb2FsYS8xNzQxNjA3ODAxNDcyLTE3NDE2MDc4MDE0NzIucG5nIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjo5NTAsImZpdCI6ImNvdmVyIn19fQ==)
Fig. 6: Load switch realization with [NPS4053-Q100](https://www.nexperia.com/products/analog-logic-ics/power-ics/load-switches/series/NPS4053-Q100.html?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_nps4053-q100) integrated controller and MOSFET

**Q6: High-speed communication between ADAS sensors and central systems poses unique challenges. How does Nexperia ensure communication reliability and signal compatibility?**

* ADAS sensors require a large bandwidth communication with the central ADAS computer. Whether the chosen protocol is CAN, I2C or something else, Nexperia can provide adequate protection for the utilized communication PHYs with Electro-Static Discharge (ESD) protection devices. ESD diodes have lower protection capabilities than TVS diodes, but their low capacitances enable communication of high data rates. To address the increase in battery voltage in commercial, hybrid and electric vehicles Nexperia has an ESD portfolio with a wide-ranging breakdown voltage offering. Suggested devices could be [PESD1IVN27LS-Q](https://www.nexperia.com/product/PESD1IVN27LS-Q?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_pesd1ivn27ls-q%20) or [PESD2CANFD24V-QC](https://www.nexperia.com/product/PESD2CANFD24V-QC?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_pesd2canfd24v-qc). While ESD diodes are available in traditional packages these are embedded in (Dual, Flat, No lead) DFN type packages, providing an increase in component density and side wettable flanks for enabling automatic optical inspection.
* Especially in the **camera and LiDAR** applications the high data rates necessitate faster protocols such as Ethernet. Nexperia is a market leader in this respect, with best-in-class 10/100/1000 Base-T1 Ethernet protection devices that were first to be approved by the OPEN Alliance. The OPEN Alliance proposes two possible external ESD protection devices. As shown in the figure below, one can be placed at the connector (ESD\_1, focus on high surge immunity, e.g. [PESD2ETH1GXT-Q](https://www.nexperia.com/product/PESD2ETH1GXT-Q?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_pesd2eth1gxt-q)) and one at the PHY interface (ESD\_2, focus on low capacitance, can be low standoff voltage, e.g. [PESD5V0C1BLS-Q](https://www.nexperia.com/product/PESD5V0C1BLS-Q?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_pesd5v0c1bls-q)).

![A diagram of a computer Description automatically generated](https://images.wevolver.com/eyJidWNrZXQiOiJ3ZXZvbHZlci1wcm9qZWN0LWltYWdlcyIsImtleSI6ImZyb2FsYS8xNzQxNjAzODk2OTE2LTE3NDE2MDM4OTY5MTYucG5nIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjo5NTAsImZpdCI6ImNvdmVyIn19fQ==)
Fig. 7: Load switch realization with NPS4053-Q100 integrated controller and MOSFET.

After the communication PHYs the signal is often at a voltage level that is not suitable for the controller. For this case Nexperia offers translating transceivers like [NXS0101GW-Q100](https://www.nexperia.com/product/NXS0101GW-Q100?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_nxs0101gw-q100%20) or [NXB0108BQ-Q100](https://www.nexperia.com/product/NXB0108BQ-Q100?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_nxb0108bq-q100%20) that not only change the voltage but also improve signal integrity by employing signal edge accelerators. These devices have automatic direction sensing, which enables easier design in and two directional data flow, sufficient for RADAR applications. However, for particularly high-speed data flow (as found in cameras and LiDARs) and low consumption Nexperias new NXU family (e.g. [NXU0304-Q100](https://www.nexperia.com/product/NXU0304PW-Q100?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_nxu0304-q100), [NXU0104-Q100](https://www.nexperia.com/product/NXU0104PW-Q100?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_nxu0104-q100)) provides a range of solutions with one directional data flow.

|  |  |
| --- | --- |
|  | Download Nexperia’s latest Techbook on Radar SystemsFor a comprehensive understanding of the latest advancements in ADAS Radar Systems, download Nexperia’s new techbook and:* understand the different application trends
* dive into design challenges and learn how to overcome them
* get to know the various Nexperia solutions available for each design challenge
* discover a list of recommended products for power and signal electronics.
 |

**Q7: Safety-critical systems like ADAS require mechanisms to ensure continuous operation even in the event of a component failure. How does Nexperia address this challenge and enhance system reliability?**

In case of failure of some critical component like the main controller, additional layers of logic and safety functions need to be designed. Some logic functions may need to be implemented outside the main controller to achieve redundancy or additional functionality. Nexperia provides compact logic gates and registers. The newest addition in this domain is the MicroPak package, which saves up to 75% PCB area, aligning with the requirement of ADAS sensors design size constraints. The devices in this package are the first and the smallest to support Automated Optical Inspection (AOI) with side-wettable flanks, while meeting automotive-grade standards. Available products include [74AHC1G08GZ-Q100](https://www.nexperia.com/product/74AHC1G08GZ-Q100?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_74ahc1g08gz-q100%20) (AND gate), [74LVC1G14GZ-Q100](https://www.nexperia.com/product/74LVC1G14GZ-Q100?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_74lvc1g14gz-q100%20) (Schmitt trigger buffer) and [74LVC1G80GZ-Q100](https://www.nexperia.com/product/74LVC1G80GZ-Q100?utm_source=wevolver&utm_medium=article&utm_campaign=adas&utm_creative_format=ta_74lvc1g80gz-q100%20) (D-type flip-flop).

![Ein Bild, das Text, Logo, Marke, Flashspeicher enthält. Automatisch generierte Beschreibung](https://images.wevolver.com/eyJidWNrZXQiOiJ3ZXZvbHZlci1wcm9qZWN0LWltYWdlcyIsImtleSI6ImZyb2FsYS8xNzQxNjAzODk2OTUxLTE3NDE2MDM4OTY5NTEucG5nIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjo5NTAsImZpdCI6ImNvdmVyIn19fQ==)
Fig.8: Nexperia's MicroPak (XSON5, SOT8065) Package.

Nexperia’s MicroPak (XSON5, SOT8065) package is designed for efficiency and reliability in compact electronic applications. Key technical specifications are:

* **Dimensions**: 1.1mm x 0.85mm x 0.47mm.
* **Die Compatibility:** Uses the same die as the SOT353.
* **Inspection**: Features side wettable flanks for automated optical inspection.
* **PCB Area Saving**: Offers approximately 75% PCB area saving compared to the SOT353.
* **Reliability**: Zero delamination and rated MSL 1.
* **Solder Layer:** Uniform 7 mm Sn layer on pad sides and bottom.
* **Compliance**: RoHS and dark green compliant.

These specifications highlight the technical advantages of the MicroPak packages, making them suitable for space-constrained and high-reliability applications.

**Q8: The automotive industry is evolving rapidly with advancements like centralised architectures and software-driven innovations. How is Nexperia aligning its solutions to support this shift?**

Centralized architectures and software driven vehicles are enabled by Zone Control Units (ZCU) and Domain Control Units (DCU). These large control units accumulate power and data management from the former small ECUs, that used to be scattered around the vehicle in large numbers, into a much smaller number of strategic placements within the vehicle. This change enables savings in modules like power management and data interface that are now utilized only once in the Zone or Domain units instead of all the ECUs individually, albeit in a more powerful form.

This transformation encompasses an evolution of all the electronic circuit designs in a car and Nexperia is here to support that evolution as a significant supplier and a one-stop-shop for all essential semiconductors needs. The wide range of the Nexperia offering is being reinvented in new, better-performance packaging that enables the necessary miniaturization into the compact ZCUs. This is enabled by the smaller footprint and better thermal properties of the new packages for both power and signal management.

**Q9: What do you envision for the future of ADAS, and how does Nexperia plan to contribute to this evolution?**

Autonomous vehicles are a topic that has been interesting for a long time. Whilst it appears to be difficult to tackle, the prevalence of the topic suggests that it is inevitably the future of the car industry. The transformation is driven by the requirements of new generations of drivers which are redefining the driving experience. Nowadays there is a strong preference for digital content and the need to utilize the time spent in transport focusing on business or leisure activities. Dedicated ADAS Domain Controllers and an increasing number of ADAS sensors are expected to be found in most new vehicles in the near future, as the level of car autonomy increases. The functioning of the ADAS system will be underpinned by the Zonal architecture and the increased power requirement for computation and control of the car will be helped by higher voltage levels of the power distribution system.

Nexperia is actively preparing for the shift and has a range of products in the pipeline to support these changes.

* The rise in computational demands for the ADAS and other controllers is met by developing integrated power management circuits to take over control of parts of the system and relieve the central computers of their control. Such are: ideal diode controllers for reverse battery protection; high side and load switches with integrated protection; integrated converters and controllers for voltage level adjustment, enabling compact, easy-to-design-in solutions; LDOs with protection and enable functions, gate drivers for Si and GaN technology; multichannel LED drivers enabling novel front and back lighting solutions.
* Development of higher voltage MOSFETs is aimed at meeting the incoming 48V revolution, as well as micro-leaded MOSFET packages opening a more affordable option for applications that are not as thermally demanding within the bonnets of electrical vehicles as opposed to combustion engines.
* The CCPAK1212 package is the largest low-voltage package on the market for switches based on Si and GaN technologies. It enables control of explicitly large loads and can act as an isolation switch or main fuse for the 12 or 48V battery of the vehicle.
* Wide-bandgap devices are here to support the propulsion of electric vehicles. However, low-voltage GaN devices can also enable fast switching of converters on the low-voltage side, reducing complete system cost and size by minimizing passives, like capacitances and inductances.
* Last, but certainly not least, Nexperias tradition in providing high-quality, reliable, automotive-graded components with extremely low failure rates, will inevitably support cars in corporate fleets that will require more challenging lifecycles and faster serviceability (possibly with equipment swapped without powering down the vehicle) .

Throughout our conversation with **Nandor Bodo**, we gained valuable insights into the technical challenges of ADAS sensor integration and the strategies used to address them. From managing power supply fluctuations and ensuring reliable communication to enhancing safety and efficiency, tackling these complexities is essential for advancing modern automotive systems.

As vehicles become smarter and safer, ADAS plays a crucial role in this evolution. By addressing these challenges with thoughtful engineering and innovative solutions, Nexperia contributes to the ongoing progress toward a future of more capable and reliable automotive technology.
