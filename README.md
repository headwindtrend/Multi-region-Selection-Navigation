# Hover Region Navigator

*A Sublime Text 3 plugin that gives you instant awareness of all your selections — no matter how far apart they are.*

---

## 🌟 Overview

When you have multiple selections scattered across a large file, it’s hard to know where they all are or what they contain.  
**Hover Region Navigator** solves that by turning your selections into a navigable map.

Simply hover your mouse over any selected region, and a popup will appear listing the *other* selected regions — including:

- Their **line number** and **character range**
- The **leading portion** of their text content  
- Clickable entries that **scroll instantly** to that region

It’s like having a “selection overview” panel that lives right under your cursor.

---

## 🧠 Why It’s Useful

- **Spatial Awareness:** Know exactly where all your selections are at a glance.  
- **Quick Navigation:** Jump directly to any region without cycling or scrolling.  
- **Context Preservation:** Peek at other selections while staying focused on the current one.  
- **Verification Tool:** Double-check what you’ve selected before batch editing or running macros.  
- **Pattern Exploration:** Skim what your regular expression has matched by `Find All` and hover a selected region.  
- **Plugin Debugging Aid:** Developers can inspect region positions and contents quickly.

---

## ⚙️ Installation

1. Open Sublime Text’s **Packages** folder:
   - `Preferences → Browse Packages…`
2. Go into the **User** subfolder.
3. Save the file as `hover_region_navigator.py` or whatever you preferred as far as it's ending with `.py`.

---

## 🕹️ How to Use

1. Make **multiple selections** (e.g., use the `Find` panel to find something with multiple occurrences and hit the button `Find All`).  
2. **Hover your mouse** over any of the selected regions.  
3. A popup will appear listing all *other* selections, each showing:
   - The line number and character positions  
   - A short preview of the selected text  
4. **Click** on any item in the popup to:
   - Scroll that region into view  

If you hover outside any selection, the popup automatically hides.

---

# If you appreciate my work, i will be very grateful if you can support my work by making small sum donation thru PayPal with `Send payment to` entered as `headwindtrend@gmail.com`. Thank you very much for your support.
