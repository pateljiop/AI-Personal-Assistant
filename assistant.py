#!/usr/bin/env python3
"""
AI Personal Assistant - Computer Control & Task Automation
A smart assistant that can execute various tasks on your computer
using natural language commands and AI integration.

Author: Hariom
Version: 1.0.0
"""

import os
import subprocess
import webbrowser
import datetime
import requests
from pathlib import Path


class PersonalAssistant:
    """
    An intelligent personal assistant that automates computer tasks.
    Can perform file operations, open applications, control system settings, etc.
    """
    
    def __init__(self, name="Assistant"):
        self.name = name
        self.commands = {
            'open browser': self.open_browser,
            'open notepad': self.open_notepad,
            'open calculator': self.open_calculator,
            'list files': self.list_files,
            'create file': self.create_file,
            'get time': self.get_time,
            'get date': self.get_date,
            'system info': self.show_system_info,
            'shutdown': self.shutdown_system,
            'help': self.show_help
        }
    
    def open_browser(self, url="https://www.google.com"):
        """Open a web browser with optional URL"""
        try:
            webbrowser.open(url)
            return f"Opening browser with {url}"
        except Exception as e:
            return f"Error opening browser: {str(e)}"
    
    def open_notepad(self):
        """Open notepad application"""
        try:
            if os.name == 'nt':
                subprocess.Popen('notepad.exe')
                return "Notepad opened"
            else:
                subprocess.Popen('gedit')
                return "Text editor opened"
        except Exception as e:
            return f"Error opening notepad: {str(e)}"
    
    def open_calculator(self):
        """Open calculator application"""
        try:
            if os.name == 'nt':
                subprocess.Popen('calc.exe')
                return "Calculator opened"
            else:
                subprocess.Popen('gnome-calculator')
                return "Calculator opened"
        except Exception as e:
            return f"Error opening calculator: {str(e)}"
    
    def list_files(self, directory="."):
        """List files in a directory"""
        try:
            files = os.listdir(directory)
            return f"Files in {directory}: {', '.join(files[:10])}"
        except Exception as e:
            return f"Error listing files: {str(e)}"
    
    def create_file(self, filename, content=""):
        """Create a new file with content"""
        try:
            with open(filename, 'w') as f:
                f.write(content)
            return f"File '{filename}' created successfully"
        except Exception as e:
            return f"Error creating file: {str(e)}"
    
    def get_time(self):
        """Get current time"""
        return f"Current time: {datetime.datetime.now().strftime('%H:%M:%S')}"
    
    def get_date(self):
        """Get current date"""
        return f"Current date: {datetime.date.today().strftime('%Y-%m-%d')}"
    
    def show_system_info(self):
        """Display basic system information"""
        try:
            info = f"System: {os.name}\nPlatform: {os.sys.platform}"
            return info
        except Exception as e:
            return f"Error getting system info: {str(e)}"
    
    def shutdown_system(self):
        """Shutdown the system (requires confirmation)"""
        return "System shutdown requires manual confirmation (security feature)"
    
    def show_help(self):
        """Display all available commands"""
        help_text = "\nAvailable Commands:\n"
        for cmd in self.commands.keys():
            help_text += f"  - {cmd}\n"
        return help_text
    
    def process_command(self, user_input):
        """Process user input and execute corresponding command"""
        user_input = user_input.lower().strip()
        
        # Check for exact command matches
        if user_input in self.commands:
            return self.commands[user_input]()
        
        # Check for URL command
        if user_input.startswith('open browser '):
            url = user_input.replace('open browser ', '')
            return self.open_browser(url)
        
        # Check for file creation command
        if user_input.startswith('create file '):
            filename = user_input.replace('create file ', '')
            return self.create_file(filename)
        
        return "Command not recognized. Type 'help' for available commands."
    
    def start_conversation(self):
        """Start interactive conversation with the assistant"""
        print(f"\n{self.name} initialized. Type 'help' for available commands or 'exit' to quit.\n")
        
        while True:
            try:
                user_input = input(f"{self.name}> ").strip()
                
                if user_input.lower() == 'exit':
                    print(f"{self.name}: Goodbye!")
                    break
                
                if not user_input:
                    continue
                
                response = self.process_command(user_input)
                print(f"{self.name}: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n{self.name}: Shutdown initiated by user.")
                break
            except Exception as e:
                print(f"{self.name}: An error occurred: {str(e)}\n")


def main():
    """Main entry point"""
    assistant = PersonalAssistant("Hariom Assistant")
    assistant.start_conversation()


if __name__ == "__main__":
    main()
