# SkyVision Team Project

## University Information

**University:** Inha University 

## Course Information

**Course:** Vertically Integrated Projects [202402-ISE3140-001]

**Professors of course:**

- Kakani Vijay
- Mehdi Pirahandeh
- Serrao Pruthvi Loy Rozario

## Team Info

---

**Team Leader:** 12225261 Meliboev Shukurullo @Shukurullo Meliboyev

**Team Member:** 12225264 Kiyomov Asadbek @Asadbey Kiyamov

**Team Member:** 12214754 Shabonov Abdulloh @Abdulloh Shabonov

**Team Member:** 12235648 G’ofurjonov Kozimjon

## Project Name

**Project Name:** SkyVision Library Assistant Robot
- link for presentation video - https://drive.google.com/file/d/174igEtJkvZ2wcBD3kgvugEDOZsQWnZ02/view?usp=sharing
## System Overview

The system comprises multiple interconnected software modules running on the TurtleBot 🤖, which interact with the library's database 📂 and the user. The primary goal is to provide an intuitive and automated way for users to locate books 📚.

## How It Works

### User Input

- A user provides a voice command 🎤, such as "Find the book Introduction to Algorithms."

### Speech-to-Text Conversion

- The Speech Recognition Module 🎤 processes the user's voice and converts it into text.

### Natural Language Processing (NLP)

- The NLP Module 🧠 analyzes the text, extracts the intent, and identifies key details like the book title or author.

### Database Query

- The Database Query Module 🔄 sends the extracted information to the Library Books Location Database 📂, retrieving the location of the specified book.

### Pathfinding and Navigation

- The Pathfinding Module 🔎 calculates the optimal route from the robot’s current position to the book’s location.
- The Obstacle Detection Module 🚶 ensures safe navigation, avoiding obstacles along the way.

### Robot Movement

- The Robot Movement Controller sends commands to the TurtleBot 🤖, enabling it to lead the user to the book’s location.

### User Guidance and Feedback

- The TurtleBot provides real-time feedback to the user through a Feedback Module using audio cues or visual indicators, ensuring the user is aware of the process and progress.

## Core Features

- **Voice Command Interface:**  Allows users to interact with the system naturally, without needing technical knowledge.
- **Efficient Pathfinding:** 🔎 Utilizes advanced algorithms to calculate the shortest and safest path to the book’s location.
- **Obstacle Avoidance:** 🚶 Equipped with sensors to detect and avoid obstacles during navigation.
- **Seamless Database Integration:** 📂 Integrates with the library’s book database to retrieve real-time book location information.
- **User-Friendly Feedback:** 🎧 Provides audio or visual cues to ensure the user can follow the TurtleBot easily.

## Target Audience

- **Students and Researchers:** 📚 Quickly locate books in large libraries without assistance from library staff.
- **Libraries:** Improve user experience and optimize resource management by reducing reliance on staff for book location assistance.

## Technical Details

### Hardware

- **TurtleBot:** 🤖 A versatile robot platform equipped with sensors (e.g., lidar, cameras) and actuators.

### Software Modules

- **Speech-to-Text Module:** 🎤 Converts user voice to text.
- **NLP Module:** 🧠 Extracts commands and book information.
- **Database Query Module:** 🔄 Interfaces with the library’s book database.
- **Pathfinding and Navigation Module:** 🔎 Calculates routes and commands movement.
- **Obstacle Detection Module:** 🚶 Ensures safe movement by avoiding obstacles.
- **Robot Movement Controller:**  Executes navigation and movement tasks.
- **Feedback Module:** Provides real-time guidance to the user.

### Programming

- **Python-based implementation** 💻 for module development.
- **ROS (Robot Operating System)** 🔧 for hardware control and integration.

## Benefits

- **Time-Saving:** ⏳ Reduces the time required to locate books.
- **Accessibility:** 🌐 Makes it easier for users unfamiliar with the library layout to find resources.
- **Scalability:** 🌐 Can be adapted for different libraries with minimal customization.
- **Innovation:** 💡 Demonstrates the application of robotics in everyday environments.
