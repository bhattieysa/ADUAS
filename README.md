# Automatic-Door-Unlock-Alert-System
Automatic Door Unlock &amp; Alerts System With The Help Of Raspberry Pi
# Introduction
The Automatic Door Unlock and Alert System (ADUAS) is a cutting-edge security technology specifically developed for home use. The system primarily uses a Raspberry Pi microcontroller to coordinate a sophisticated authentication and threat detection process. The first level of security is achieved by using eye blink detection, which accurately distinguishes between a real person and a photograph. This helps to reduce the possibility of someone using static photos to deceive the system. After confirming the person's live presence, the system uses facial recognition technology to determine if the individual is a registered member of the family. Once the individual is identified, the door unlocks smoothly, ensuring a user-friendly experience while maintaining security. On the other hand, if the face does not correspond to any recognised family member, the system triggers an alarm to indicate the presence of an unfamiliar individual. The system has improved its security measures by integrating object detection algorithms that can accurately identify possible weapons. This functionality is essential for anticipating security breaches and guaranteeing a secure environment. The incorporation of these technologies into the tiny and efficient Raspberry Pi platform showcases the system's adaptability and capacity for extensive acceptance in contemporary households. This summary summarises the core of the project, emphasising its creative utilisation of technology to offer a secure and convenient access control system.



# Hardware Requirement: 

•	Raspberry Pi: The Raspberry Pi [11] is the central component of the ADUAS system, responsible for delivering the computational power required for real-time processing, decision-making, and control. The Raspberry Pi 3 Model B as seen in Figure 1, is chosen for its resilient quad-core ARMv8 CPU, which allows for the efficient execution of intricate algorithms and tasks. This highly adaptable single-board computer provides a wide range of connectivity choices, such as HDMI, USB, Ethernet, and GPIO (General Purpose Input/Output ) ports, which make it ideal for connecting with different hardware components [12] and peripherals.
•	Camera Module: The Pi Camera Module as seen in Figure 2 is essential in the ADUAS system as it captures high-resolution photographs of people entering the entrance. The camera module, which is small and light, may be immediately connected to the Raspberry Pi using the USB port. This allows for a seamless and efficient solution for tasks such as facial recognition and picture processing [8]. The camera module's adaptable focus and expansive lens guarantee ideal coverage of the entry point, taking intricate facial photographs under diverse lighting circumstances.

<br>
<center><img width="300" alt="image" src="https://github.com/bhattieysa/Automatic-Door-Unlock-Alert-System/assets/89656526/e48f37ce-7181-44d8-8df9-9711fe7046cd"></center>
<br>


•	Automatic Door Lock Mechanism/Motor: An automatic door lock mechanism as seen in Figure 3 or DC-Motor as seen in Figure 4 is incorporated into the ADUAS system to safely regulate entry to the premises. The door lock mechanism can include a solenoid-operated deadbolt, an electric strike lock, or a motorised latch, depending on the individual needs and structure of the door and some door locks operate with a DC-Motor so we can use this as well. Through the use of a relay module, the Raspberry Pi may establish a connection and control the door remotely. This control is based on the authentication results acquired from the facial recognition system, allowing for the door to be locked or unlocked as needed.



•	Relay Module: A relay module as seen in Figure 5 acts as the intermediary between the Raspberry Pi and the automated door lock system, enabling safe and dependable management of the door's locking mechanism. The relay module includes several relay channels, each with the ability to switch high-voltage or high-current loads, making it appropriate for managing different types of door locks and access control systems. The system can achieve precise and efficient activation or deactivation of the door lock mechanism by transmitting signals from the Raspberry Pi to the relay module.

 


•	Speaker/Buzzer: The ADUAS system includes a speaker or buzzer as shown in Figure 6 that emits audible warnings or notifications to homeowners in response to security occurrences. The speaker produces auditory signals to signify successful authentication, unauthorised access attempts, or other updates regarding the system's status. In addition, the speaker can be used to transmit speech prompts or instructions to users, thereby improving the user experience and accessibility of the system.



•	Power Supply: The ADUAS system is energised by a steady and dependable power supply as seen in Figure 7, usually a micro USB power adapter linked to the Raspberry Pi. The power supply guarantees continuous operation of the system by delivering ample electrical power to all components and peripherals. In addition, the power supply may include power management capabilities such as overcurrent protection and voltage regulation to prevent electrical risks or system malfunctions.

 


•	Enclosure and Mounting: The ADUAS system can be placed in a robust as seen in Figure 8 to safeguard the hardware components from environmental elements including dust, moisture, and temperature changes. The design of the enclosure should be such that it can fit all the components and ensure adequate ventilation to prevent overheating. In addition, the enclosure design may include mounting features to enable a secure placement near the entry point of the premises. This ensures that the Pi camera and other sensors are positioned and covered optimally.






