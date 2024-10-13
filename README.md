
# Syringe Detection Research Project

## Project Overview

Adverse events associated with injectable medications significantly impact patient safety, with drug administration errors being among the most frequently reported incidents in anesthesia. This project aims to develop a real-time auditory or visual feedback system that detects syringe handling by anesthesia providers using computer vision algorithms. By identifying syringes and vials in real-time from head-mounted cameras, we seek to enhance patient safety and reduce medication errors.

I had the unique experience of aiding the engineering side, and helped develop part of the machine vision algorithm. I was responsible for image preprocessing and bounding box annotation. The code is a small example similar to my work performed.

## Implementation Considerations

Wearable devices are limited by space and processing power. The code written focused on efficiency and speed to limit the lag between administration and error detection for patient safety and efficacy of the system. This is a constant issue in the wearable space. As an engineer who has hardware experience, some possible recommendations include:

* **Wireless Communication** - Bluetooth Low Energy (BLE) to wirelessly update physician records.
* **Processing Power** - For efficient processing of video feed.
* **Battery Life and Rechargeability** - For ease of use by the Anesthesiologist, and usability for a whole day (considerations in software and hardware).
* **Form Factor** - For comfort and usability.
* **Cost** - For accessibility across hospitals.

## Potential Microcontrollers

- **STM32F4 Series**: Known for high-speed processing capabilities, making it suitable for real-time applications.
- **STM32WB Series**: Offers wireless communication features, which are beneficial for updating physician records wirelessly.

  
## Objectives

1. **Determine reliability of drug label identification** using machine learning tools.
2. **Assess accuracy of automated drug delivery dose calculations**.
3. **Design and test the feasibility of a power-efficient real-time wearable camera system**.

## References

1. National Institutes of Health. (n.d.). *Project Details: 10782884*. Retrieved from [https://reporter.nih.gov/project-details/10782884](https://reporter.nih.gov/project-details/10782884)

2. Kelly, E. M. (n.d.). *Research Projects*. Retrieved from [https://sites.google.com/uw.edu/kellyem/research-projects?authuser=0](https://sites.google.com/uw.edu/kellyem/research-projects?authuser=0)
