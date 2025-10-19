# 📘 Grade Range Calculator (MicroPython)

A simple MicroPython project that displays grade ranges on an OLED screen.  
Designed to help teachers quickly calculate and visualize student grades using easy button controls.  
**Made with love for my mum ❤️**

---

## 🖼️ Preview

![photo](https://github.com/user-attachments/assets/3ae90c04-0ed2-44e8-a50e-31e62a99ee7f)

*(Replace `photo.jpg` with your actual image filename)*

---

## 🧠 About the Project

This project uses a **MicroPython-compatible microcontroller** (e.g. Raspberry Pi Pico) and a **SH1106 OLED display** to show dynamically calculated grade ranges based on total points.  
Two physical buttons allow adjusting the total points, and the display instantly updates the corresponding grade intervals.

---

## ⚙️ Hardware

- Microcontroller: Raspberry Pi Pico (or similar)
- Display: 1.3" OLED (SH1106, I²C)
- 2 × Buttons (for increasing/decreasing points)
- USB cable for power
- Some electrical tape 😉

---

## 💻 Software

- **Language:** MicroPython  
- **Libraries:** `machine`, `time`, `math`, and `sh1106`  

Upload the `main.py` file to your device using **Thonny** or another MicroPython IDE.

---

## ▶️ How to Use

1. Power the device via USB.  
2. Use the buttons to **increase** or **decrease** the total number of points.  
3. The OLED screen will automatically show updated grade ranges (from grade 1 to 6).  

## 💬 Inspiration

Created as a practical and heartfelt gift for my mum, a teacher who inspires learning every day.  
A small project with a big purpose ❤️

---

## 📄 License

This project is open source under the [MIT License](LICENSE).
