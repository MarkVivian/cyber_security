# <center> MARKDOWN FORMATTING GUIDE </center>
---

This guide is designed to be your complete instruction book for writing and formatting Markdown files.

## Table of Contents
1.  [Headers](#headers-from-largest-to-smallest)
2.  [Text Styling](#text-styling)
3.  [Paragraphs and Line Breaks](#paragraphs)
4.  [Indentation and Blockquotes](#blockquotes)
5.  [Lists](#lists)
    - [Unordered Lists](#unordered-lists)
    - [Ordered Lists](#ordered-lists)
    - [Task Lists](#task-lists)
    - [Nested Lists](#nested-lists)
6.  [Code Formatting](#code-formatting)
    - [Inline Code](#inline-code)
    - [Code Blocks](#code-blocks)
7.  [Links](#links)
8.  [Images](#images)
9.  [Tables](#tables)
10. [Horizontal Rules](#horizontal-rules)
11. [Advanced Formatting & GitHub-Specific Features](#advanced)
    - [Collapsible Sections](#collapsible-sections)
    - [Keyboard Keys](#keyboard-keys)
    - [Emojis](#emojis)
    - [Badges](#badges)
    - [Anchors](#anchors)
    - [Footnotes](#footnotes)
    - [Highlighting](#highlighting)
    - [Strikethrough](#strikethrough)
    - [GitHub Mentions, Issues, and Commits](#github-specifics)
12. [Using HTML in Markdown](#html)
13. [Escaping Characters](#escaping)
14. [Best Practices for READMEs](#best-practices)

---

## Headers (from largest to smallest):
- # Title (H1)# 
- ## Section (H2)##`
- ### Subsection (H3)###
- #### Sub-subsection (H4)####
- ##### Small header (H5)#####
- ###### Smallest header (H6)######   


## Text Styling:
- **bold text**
- *italics*
- ***bold and italics*** 
- ~~strikethrough~~
- `inline code`  
    ### Example:  
    * This is **bold**, this is *italic*, this is ***both***, and this is ~~struck through~~.  
    * Use `code` for inline commands.




## Lists
- Unordered list item* Alternative unordered list1. Ordered list2. Second item    - Nested item    - Another nested item  
Example:  
1. First step
    - Sub-step one
    - Sub-step two
2. Second step


## Links
[Link text](URL)[Link with title](URL "hover text")<https://direct.link>  
Example:  
[Visit GitHub](https://github.com)  
[Documentation](./docs/README.md "Read more")


## Images
![Alt text](image.jpg)![Alt text](image.jpg "Image title")  
Example:  
![Script Logo](./images/logo.png "Our Script Collection")


## Code Blocks
:```language code here ```  
Example:  
```bash
#!/bin/bash
echo "Hello World"
```



## Tables
:| Header 1 | Header 2 ||----------|----------|| Cell 1   | Cell 2   |  
Example:  
| Script Name | Description |
|-------------|-------------|
| backup.sh   | Daily backup|


## Blockquotes
:> This is a quote>> Nested quote  
Example:  
> Important note:  
> This script requires root privileges


## Horizontal Rules
:---***___  

## Task Lists
:- [x] Completed task- [ ] Pending task  
Example:  
- [x] Write documentation  
- [ ] Add examples


## Collapsible sections
:<details><summary>Click to expand</summary>Content here</details>  
Example:  
<details>  
<summary>Advanced Configuration</summary>  
Additional settings and options here...  
</details>


## Keyboard Keys
:<kbd>Ctrl</kbd> + <kbd>C</kbd>  
Example:  
Press <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd> to open terminal


## Emojis:  
Emojis can be used to make your README more engaging and visually appealing.  
Use colon syntax to insert emojis, e.g., :smile: for 😄.  
GitHub supports a wide range of emojis. See the emoji cheat sheet for a full list.

Example:  
Welcome to my project! 🎉  
- :rocket: Fast and efficient  
- :star: Feature-rich


Badges:  

Badges are small images that display information like build status, license, or version.  
They can be added to your README to provide quick insights.  
Use services like Shields.io to create custom badges.

Example:  
![GitHub license](https://img.shields.io/github/license/username/repo)  
![Build Status](https://img.shields.io/travis/username/repo)


Anchors:  

Anchors allow you to create internal links within your README, making navigation easier for large documents.  
To create an anchor, use <a name="section-name"></a> before the section.  
Link to it using [Link text](#section-name).

Example:  
<a name="installation"></a>  
## Installation  
...  
[Go to Installation](#installation)


Tables of Contents:  

A table of contents (TOC) helps readers navigate your README, especially if it's long.  
You can manually create a TOC by listing sections with anchor links.

Example:  
- [Installation](#installation)  
- [Usage](#usage)  
- [Contributing](#contributing)


GitHub-Specific Features:  

GitHub offers additional Markdown features:  
Mention users with @username.  
Link to issues with #issue-number.  
Reference commits with SHA hashes.



Example:  
Thanks to @octocat for the contribution!  
See issue #42 for more details.  
Fixed in commit abc123.


Best Practices for READMEs:  

Keep your README concise and focused on essential information.  
Use clear, simple language to ensure accessibility.  
Include key sections like installation, usage, and contribution guidelines.  
Update your README regularly to reflect changes in your project.  
Use visuals like images or badges to enhance readability.



