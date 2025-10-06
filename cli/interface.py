"""
CLI interface for Student Management System
"""
from core.student_operations import (
    add_student, view_students, search_student, 
    update_student, delete_student, get_students_count
)
from utils.display import display_menu, display_message

def main_menu():
    """Display main menu and handle user choices"""
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_student_interface()
        elif choice == '2':
            view_students_interface()
        elif choice == '3':
            search_student_interface()
        elif choice == '4':
            update_student_interface()
        elif choice == '5':
            delete_student_interface()
        elif choice == '6':
            display_message("Thank you for using Student Management System!", "info")
            break
        else:
            display_message("Invalid choice! Please enter a number between 1-6.", "error")

def add_student_interface():
    """Interface for adding a new student"""
    print("\n" + "="*40)
    print("          ADD STUDENT")
    print("="*40)
    
    if get_students_count() >= 9:
        display_message("Maximum limit reached! Cannot add more than 9 students.", "error")
        return
    
    try:
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Student Name: ").strip()
        course = input("Enter Course (CSE, ML, IT, DS, AIML): ").strip().upper()
        marks = input("Enter Marks: ").strip()
        
        result = add_student(student_id, name, course, marks)
        display_message(result, "success" if "successfully" in result else "error")
        
    except KeyboardInterrupt:
        display_message("\nOperation cancelled by user.", "warning")
    except Exception as e:
        display_message(f"An error occurred: {str(e)}", "error")

def view_students_interface():
    """Interface for viewing all students"""
    print("\n" + "="*40)
    print("          ALL STUDENTS")
    print("="*40)
    view_students()

def search_student_interface():
    """Interface for searching students"""
    print("\n" + "="*40)
    print("          SEARCH STUDENT")
    print("="*40)
    
    search_by = input("Search by (1) ID or (2) Name? Enter 1 or 2: ").strip()
    
    if search_by == '1':
        student_id = input("Enter Student ID to search: ").strip()
        result = search_student(search_by_id=student_id)
    elif search_by == '2':
        name = input("Enter Student Name to search: ").strip()
        result = search_student(search_by_name=name)
    else:
        display_message("Invalid choice! Please enter 1 or 2.", "error")
        return
    
    if not result:
        display_message("No students found matching your criteria.", "warning")

def update_student_interface():
    """Interface for updating student details"""
    print("\n" + "="*40)
    print("          UPDATE STUDENT")
    print("="*40)
    
    student_id = input("Enter Student ID to update: ").strip()
    
    # First check if student exists
    existing_student = search_student(search_by_id=student_id, silent=True)
    if not existing_student:
        display_message(f"Student with ID '{student_id}' not found!", "error")
        return
    
    print("\nWhat would you like to update?")
    print("1. Course")
    print("2. Marks")
    print("3. Both Course and Marks")
    
    choice = input("Enter your choice (1-3): ").strip()
    
    new_course = None
    new_marks = None
    
    if choice in ['1', '3']:
        new_course = input("Enter new Course (CSE, ML, IT, DS, AIML): ").strip().upper()
    
    if choice in ['2', '3']:
        new_marks = input("Enter new Marks: ").strip()
    
    result = update_student(student_id, new_course, new_marks)
    display_message(result, "success" if "successfully" in result else "error")

def delete_student_interface():
    """Interface for deleting a student"""
    print("\n" + "="*40)
    print("          DELETE STUDENT")
    print("="*40)
    
    student_id = input("Enter Student ID to delete: ").strip()
    
    # Confirm deletion
    confirm = input(f"Are you sure you want to delete student with ID '{student_id}'? (y/n): ").strip().lower()
    
    if confirm in ['y', 'yes']:
        result = delete_student(student_id)
        display_message(result, "success" if "successfully" in result else "error")
    else:
        display_message("Deletion cancelled.", "info")