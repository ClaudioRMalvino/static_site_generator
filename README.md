# Static Site Generator

## Project Objective

This Static Site Generator is a Python-based tool designed to convert Markdown content into a fully functional static HTML website. It aims to simplify the process of creating and maintaining small to medium-sized websites by allowing content to be written in easy-to-use Markdown format. It is a project done for the boot.dev back-end engineering program. 

## Features

- Converts Markdown files to HTML
- Supports basic Markdown syntax including headers, paragraphs, bold, italic, links, and images
- Generates a complete website structure with proper HTML, CSS, and file organization
- Recursive page generation for nested content
- Customizable HTML templates
- Automatic menu generation based on content structure

## Programming Tools and Methods

### Languages
- Python 3.12.2
- HTML
- CSS
- Markdown

### Key Python Libraries
- os
- shutil
- re (regular expressions)
- logging
- unittest

### Development Practices
- Object-Oriented Programming (OOP)
- Test-Driven Development (TDD)
- Modular design

### Version Control
- Git
- GitHub

## Project Structure

├── content
│   ├── index.md
│   └── majesty
│       └── index.md
├── main.sh
├── public
│   ├── images
│   │   └── rivendell.png
│   ├── index.css
│   ├── index.html
│   └── majesty
│       └── index.html
├── src
│   ├── copy_directory.py
│   ├── htmlnode.py
│   ├── main.py
│   ├── markdown_blocks.py
│   ├── markdown_to_html.py
│   ├── markdown_utils.py
│   ├── page_generator.py
│   ├── split_node.py
│   ├── textnode.py
│   └── text_to_node.py
├── static
│   ├── images
│   │   └── rivendell.png
│   └── index.css
├── template.html
├── tests
│   ├── test_block_to_block_type.py
│   ├── test_extract_title.py
│   ├── test_htmlnode.py
│   ├── test_leafnode.py
│   ├── test_markdown_to_blocks.py
│   ├── test_markdown_to_html.py
│   ├── test_markdown_utils.py
│   ├── test_parentnode.py
│   ├── test_split_nodes_delimiter.py
│   ├── test_split_nodes_links_images.py
│   ├── test_textnode.py
│   ├── test_textnode_to_htmlnode.py
│   └── test_text_to_textnodes.py
└── test.sh
