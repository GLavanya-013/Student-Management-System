#!/usr/bin/env python3
"""
Main entry point for Student Management System
"""
from cli.interface import main_menu

def main():
    """Main function to start the application"""
    print("=" * 50)
    print("    Student Management System")
    print("=" * 50)
    main_menu()

if __name__ == "__main__":
    main()