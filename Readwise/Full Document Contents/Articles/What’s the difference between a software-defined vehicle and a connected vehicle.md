# What’s the difference between a software-defined vehicle and a connected vehicle?

![rw-book-cover](https://blackberry.qnx.com/etc.clientlibs/blackberry/clientlibs/clientlib-core/resources/qnx/og-preview.webp)

## Metadata
- Author: [[qnx.com]]
- Full Title: What’s the difference between a software-defined vehicle and a connected vehicle?
- Category: #articles
- Summary: A software-defined vehicle uses software to manage its operations and features, allowing for continuous updates and improvements. It provides enhanced comfort, performance, and safety compared to traditional hardware-defined vehicles. While similar to connected vehicles, software-defined vehicles focus more on software integration and functionality.
- URL: https://blackberry.qnx.com/en/ultimate-guides/software-defined-vehicle

## Full Document
####  What Is a Software-Defined Vehicle?

A software-defined vehicle is any vehicle that manages its operations, adds functionality, and enables new features primarily or entirely through software.

Software-defined vehicles are the next evolution of the automotive industry. They are the foundation of many other advancements, including self-driving and connected cars. [Deloitte notes](https://www2.deloitte.com/cn/en/pages/consumer-business/articles/software-defined-cars-industrial-revolution-on-the-arrow.html) that they ultimately reflect “the gradual transformation of automobiles from highly electromechanical terminals to intelligent, expandable mobile electronic terminals that can be continuously upgraded”.

####  Benefits of Software-Defined Vehicles

The benefits of software-defined vehicles include:

* Increased comfort through onboard [infotainment systems](https://blackberry.qnx.com/en/ultimate-guides/software-defined-vehicle/infotainment) that integrate connected features such as music and video streaming
* Deeper insights into vehicle performance through [telematics](https://blackberry.qnx.com/en/ultimate-guides/software-defined-vehicle/telematics) and diagnostics, allowing for more effective preventative maintenance
* The capacity for automotive manufacturers to add new features and functionality with over-the-air updates

Software-defined vehicles outperform their hardware-defined predecessors across multiple arenas. In addition to being safer, they provide superior comfort and convenience. Since many Software-defined vehicles are also electric, they could have considerably smaller environmental footprints.

Optimization is another major draw. Manufacturers can continue improving the driver experience and enhance vehicle performance after a car leaves the factory, perpetually improving the driving experience through ongoing development. This represents the most significant paradigm shift the automotive industry has ever experienced, as hardware-defined cars tend to remain generally unchanged throughout their lifecycles.

####  More Benefits of Software-Defined Vehicles

* Increased value of the vehicle over time as new features are added via software updates
* Connectivity between vehicle and smartphone, allowing drivers and passengers to interact with their cars in new ways
* Continuous connectivity, delivering real-time information services to and from the vehicle

    ![Software-Defined Vehicle](https://blackberry.qnx.com/content/dam/blackberry-qnx-com/en/ultimate-guides/02_software-defined-vehicle.webp) 
####  Software-Defined Vehicle Architecture

A software-defined vehicle’s software and hardware architecture tend to be incredibly complex, often comprising multiple interconnected software platforms distributed across as many as one hundred electronic control units (ECUs). Some manufacturers are attempting to rationalize this down to fewer ECUs controlled by a very powerful central computer—but either way, the architecture of Software-Defined Vehicles can be broken down into four distinctive layers:

####  1. User Applications

User applications are software and services that interact or interface directly with drivers and passengers. These may include infotainment systems, vehicle controls, digital cockpits, etc.

####  2. Instrumentation

Systems at the instrumentation layer are generally related to a vehicle’s functionality but don’t typically require direct intervention from a driver. Examples include [Advanced Driver Assistance Systems (ADAS)](https://blackberry.qnx.com/en/ultimate-guides/software-defined-vehicle/advanced-driver-assistance-system) and complex controllers.

####  3. Embedded OS

The core of the software-defined vehicle, the embedded OS manages everything from sandboxing critical functions to facilitating general operations. These are typically built on microkernel architecture, allowing software capabilities and functionality to be added or removed modularly.

####  4. Hardware

The hardware layer includes the engine control unit and the chip on which the embedded operating system is installed. All other physical components of the vehicle also fall under this category, including cameras and other vehicle sensors.

Currently, the most significant obstacle facing Software-Defined Vehicles is that many automotive manufacturers still tightly couple software to hardware. Moving forward, manufacturers will need to adopt more agile, modular development practices and develop applications and ecosystems that operate independently of hardware. More virtualization is likely to be employed to maintain separation between functions and underlying hardware. This will have the added benefit of improved performance, as manufacturers can focus on the best hardware possible without worrying about compatibility.

####  Software-Defined Vehicles vs. Connected Vehicles

There is very little difference between software-defined vehicles and [connected vehicles](https://blackberry.qnx.com/en/ultimate-guides/connected-vehicle-platform).

Both are characterized by extensive safety, convenience, and entertainment features provided and enabled through onboard software. Both integrate multiple software services and platforms through either middleware or APIs. Both incorporate various advanced hardware such as collision detection and ADAS.

The only tangible difference is that, in theory, connected cars have a slightly different use case, explicitly built to interact and interface with their surroundings. Given that many Software-Defined Vehicles now share this functionality, the two are essentially indistinguishable from one another.

####   [Software-Defined Vehicles and Smart Cities](https://blogs.blackberry.com/en/2023/01/sdvs-and-their-role-in-smart-cities)

A [smart city](https://blackberry.qnx.com/en/ultimate-guides/smart-city) is one that’s capable of harnessing the power of today’s most innovative technologies. These cities are defined as urban areas that utilize information and communication technologies (ICT) to improve government services and make them more efficient. Smart cities can also improve the flow and function of how drivers navigate through the urban environment.

As the smart city moves from concept to reality, the SDV will become even more important as a dynamic node in this system. In the smart city, data and information technology are leveraged to improve operational efficiency, share services with public citizens, and provide a better quality of government. This includes helping traffic flow more smoothly, imposing environmental regulations, managing parking more effectively, and reducing energy usage where possible. SDVs will facilitate the integration of vehicles into the smart city.

####  Software Defined Vehicles and Vehicle-to-Everything

Connectivity is central to the concept of the software-defined vehicle. Updating features over the air and providing drivers with live information during their journeys are vital capabilities. The SDV is also integral to realizing [Vehicle-to-Everything (V2X)](https://blackberry.qnx.com/en/ultimate-guides/software-defined-vehicle/vehicle-to-everything) technology. With V2X, the information flow between the car and its surroundings is constant and two-way.

V2X enables vehicles to benefit from urban smart city Internet of Things sensors and data while contributing information from its sensors to central repositories. With SDVs, V2X technology is much easier to implement. The integration of vehicle systems that SDVs provide via software stacks and standards-based communication methods will be a hub for V2X.

Closely linked to smart city developments, V2X leverages high-bandwidth, low-latency wireless connectivity such as 5G to enhance vehicle safety using data supplied by the environment. It can also facilitate driver services, including automatic payment when entering restricted urban areas such as parking or controlled zones, and provide information to other drivers.

####  Software Defined Vehicles and Autonomous Vehicles

[Autonomous vehicles](https://blackberry.qnx.com/en/ultimate-guides/software-defined-vehicle/self-driving-car) are primarily a software challenge. While a self-driving hardware system relies on a suite of different sensors, including cameras, radar, [LiDAR](https://blackberry.qnx.com/en/ultimate-guides/software-defined-vehicle/lidar), and others, what enables autonomy are sophisticated road behavior models developed using intensive Artificial Intelligence and Machine Learning (AI/ML) processed on some of the most powerful supercomputers in the world.

Once implemented, an autonomous driving system requires complete control over core driving functions like acceleration, braking, and steering. This can only be delivered when these functions are interconnected via a central computer running software that integrates them. The SDV provides this with its focus on software as the primary method for delivering functionality.

Full self-driving will also likely require regular software updates as new capabilities and safety improvements become available. The SDV enables this, especially as fewer and fewer features rely on fixed hardware platforms and ECUs that cannot be upgraded dynamically.

####  Software Defined Vehicles and Cybersecurity

To compromise vehicles without connectivity, threat actors need physical access—they need to be near the car when keyless entry is invoked or be in a location with both the car and its keys in the vicinity. For deeper levels of compromise, they would need to enter the vehicle to connect to the diagnostics port.

With an SDV, these functions could be accessed remotely, similar to the malware attacks perpetrated on personal devices and corporate systems. Although there have been no publicized incidents of this occurring (except for controlled demonstrations), the mission-critical nature and safety requirements of road vehicles mean that a breach could be more immediately serious than the theft of even bank details: A moving car suddenly losing its ADAS functions because of a cyberattack could be life-threatening. A compromised self-driving vehicle could be turned into a weapon.

This is why a vehicle software platform with a strong cybersecurity pedigree, such as QNX®, will be essential as SDVs gain popularity. Vehicle software must implement proactive protection systems against cyberattacks like corporate network systems. Cybersecurity solutions can recognize and nullify existing known attacks and detect behavior that could be a previously unseen attempt to compromise systems. With SDVs employing powerful computing hardware, this can be leveraged to run AI-enhanced cybersecurity, keeping vehicles secure and their occupants safe.

#### FAQ

##### What is a software-defined vehicle?

A software-defined vehicle manages operations and enables new features and functionality almost entirely through onboard software.

##### What software is used in the automotive industry?

QNX is a market leader in automotive software, embedded in more than 235 million vehicles worldwide. The platform’s leadership is [expected to persist through 2026](https://www.globalmarketestimates.com/market-report/automotive-infotainment-os-market-3474). Other significant players in the space include Android, Linux, and Windows Embedded Automotive.

In theory, connected cars are built specifically to interact with IoT devices in their surroundings. However, in practice, there is very little difference between the two as SDVs generally provide the same functions and they are used mainly to reference the same concepts.

##### Is Tesla a software-defined vehicle?

Tesla first popularized the concept of software-defined vehicles in 2012. The company remains one of the best-known brands in the space to this day. However, many other manufacturers are now realizing the need for a software-first approach to their vehicle platforms.

##### What’s the connection between software-defined vehicles and self-driving vehicles?

Software-defined vehicles essentially lay the foundation for self-driving cars. Many safety features in software-defined vehicles, such as sensors and LiDAR, are also crucial for autonomous driving.

####   [IVY for Software-Defined Vehicles](https://www.blackberry.com/us/en/products/automotive/blackberry-ivy.html)

As the developer of QNX®, we are one of the leading organizations in the Software-Defined Vehicle space. For more than forty years, we’ve worked tirelessly to build safe, reliable, and secure embedded systems. And we’re not stopping there—in addition to investing heavily in autonomous vehicle research, we’re also working to enable the connected car.

That’s where [IVY®](https://www.blackberry.com/us/en/products/automotive/blackberry-ivy.html) comes in. Leveraging QNX, edge computing, and the cloud, IVY empowers developers and automakers with a secure, reliable way to share vehicle data, deliver new features and functionality, and fuel innovation. IVY is compatible with most platforms and shares close ties with BlackBerry’s broad development community.
