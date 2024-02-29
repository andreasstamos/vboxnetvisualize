# VBoxNetVisualize

A simple tool to visualize VirtualBox Networking topology.

It automatically retrieves the networking information using the VirtualBox CLI tool: `VBoxManage`

As of today, it works only for Internal Networking.

*The tool is still in Alpha, and has been tested to a very limited extent.*  
*(especially in non-Linux platforms there could exist unknown issues)*

## How to run?

1. **Install GraphViz**
    
    In Linux you can usually find it in your Package Manager.  
    (e.g. in Ubuntu to install it: `apt install graphviz`)
    
    In Windows you can follow the instructions here: [https://graphviz.org/download/]  
    *(It is advised that you add it to PATH)*

2. **Install Python dependencies**
 
    ```bash
    pip install -r requirements.txt
    ```

3. **Execute the app**
    ```bash
    python3 main.py
    ```

***

 VBoxNetVisualize
 Copyright (C) 2024  Andreas Stamos
 
 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.

