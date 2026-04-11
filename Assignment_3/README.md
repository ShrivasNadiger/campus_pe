# NexusChat — AI Chat UI

A modern, responsive chat interface inspired by Claude and ChatGPT, built with **HTML, CSS, JavaScript, jQuery & Bootstrap 5**.

---

## 📁 Project Structure

```
YourName_ChatUI/
├── index.html          # Main HTML file
├── css/
│   └── style.css       # All custom styles with CSS variables
├── js/
│   └── chat.js         # All chat functionality (jQuery + vanilla JS)
├── screenshots/
│   ├── desktop.png     # Desktop screenshot
│   ├── tablet.png      # Tablet screenshot
│   └── mobile.png      # Mobile screenshot
└── README.md           # This file
```

---

## 🚀 How to Run

1. **Unzip** the project folder.
2. Open `index.html` in any modern browser (Chrome, Firefox, Safari, Edge).
3. No server or build step required — it's pure HTML/CSS/JS.

> **Tip:** Use VS Code with the "Live Server" extension for the best development experience.

---

## ✅ Features Implemented

### Core Features

- ✅ Welcome screen with 4 suggestion cards (clickable)
- ✅ Message display with **user** and **AI** bubbles (left/right aligned)
- ✅ Animated typing indicator (bouncing dots)
- ✅ Auto-resizing textarea input
- ✅ Send button with enabled/disabled state
- ✅ Enter to send, Shift+Enter for new line
- ✅ Empty message prevention
- ✅ Mock AI responses with 1–2 second delay
- ✅ Auto-scroll on new messages
- ✅ Timestamps on every message
- ✅ Sidebar with 260px fixed width
- ✅ New Chat button with history saving
- ✅ Mobile hamburger menu + sidebar slide-in
- ✅ Sidebar overlay on mobile
- ✅ Responsive from 320px to 1920px

### Bonus Features

- ✅ **Dark mode toggle** with smooth CSS variable transition (4 pts)
- ✅ **Message formatting** — bold `**text**`, italic `*text*`, inline code `` `code` ``, code blocks ` ``` ``` ` (3 pts)
- ✅ **Export chat** as `.txt` file using JavaScript Blob API (3 pts)
- ✅ **Custom scrollbar styling** across all scroll areas (2 pts)

---

## 🎨 Design Highlights

- **Typography:** `Syne` (display/headings) + `DM Sans` (body text)
- **Color system:** CSS custom properties for both light and dark themes
- **Accent color:** Burnt orange `#e8622a` — warm, distinctive, memorable
- **Animations:** Fade-in for messages, bouncing dots for typing, float animation for welcome icon
- **Responsive:** Mobile-first, tested from 320px to 1920px

---

## 🛠 Technologies Used

| Technology   | Version | Purpose                        |
| ------------ | ------- | ------------------------------ |
| HTML5        | —       | Semantic structure             |
| CSS3         | —       | Custom styles, variables, anim |
| JavaScript   | ES6+    | DOM manipulation, Blob API     |
| jQuery       | 3.7.1   | Event handling, DOM updates    |
| Bootstrap 5  | 5.3.3   | Grid system, responsive base   |
| Font Awesome | 6.5.0   | Icons                          |
| Google Fonts | —       | Syne + DM Sans typography      |

---

## 📋 Assignment Checklist

- [x] Messages appear correctly when sent
- [x] User and AI messages are visually different
- [x] Send button disabled when input empty
- [x] Send button enabled when text present
- [x] Enter sends; Shift+Enter = new line
- [x] Typing indicator shows/hides correctly
- [x] Auto-scroll on new messages
- [x] Textarea auto-resizes
- [x] Suggestion cards are clickable
- [x] Welcome screen hides after first message
- [x] Sidebar appears/hides on mobile
- [x] Responsive on all screen sizes
- [x] No console errors

---
