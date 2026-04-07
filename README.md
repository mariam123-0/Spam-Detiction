# 📩 Spam Detection System

A lightweight, keyword-based spam detection application built with Streamlit that instantly identifies spam messages and returns a clear **SPAM** or **NOT SPAM** verdict to protect users from unwanted and potentially harmful content.

## 🎯 Project Goal

The primary goal of this project is to provide users with a **simple, fast, and accurate** way to determine whether a message is spam or legitimate (ham). The system analyzes text input and returns only one of two possible results:

| Result | Meaning |
|--------|---------|
| 🚨 **SPAM** | The message contains spam indicators and is potentially harmful |
| ✅ **NOT SPAM** | The message appears legitimate and safe |

No complex metrics, no confusing scores - just a clear **SPAM** or **NOT SPAM** answer.

## ✨ Key Features

- **Binary Result Output**: Returns only SPAM or NOT SPAM - simple and clear
- **Instant Detection**: Real-time analysis with immediate feedback
- **Clean Interface**: Minimalist design focused on core functionality
- **Comprehensive Keyword Database**: Detects 30+ common spam indicators
- **Visual Feedback**: Color-coded results with animations
  - 🔴 Red box with "SPAM" for detected spam
    ![image alt](https://github.com/mariam123-0/Spam-Detiction/blob/babce41fbe9e20d1dac37946f61e9acbe4a95b60/SpamExample.png)
  - 🟢 Green box with "NOT SPAM" for legitimate messages
    ![image alt](https://github.com/mariam123-0/Spam-Detiction/blob/babce41fbe9e20d1dac37946f61e9acbe4a95b60/NotSpamExample.png)
- **Zero Dependencies**: Only requires Streamlit and basic Python
- **Responsive Design**: Works seamlessly on all devices

