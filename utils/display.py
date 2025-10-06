"""
Display and formatting utilities
"""

def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("        STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("-" * 50)

def display_students_table(students_list):
    """Display students in a tabular format"""
    if not students_list:
        print("No students to display.")
        return
    
    print("\n" + "=" * 70)
    print(f"{'ID':<10} {'Name':<20} {'Course':<10} {'Marks':<10}")
    print("=" * 70)
    
    for student in students_list:
        print(f"{student['id']:<10} {student['name']:<20} {student['course']:<10} {student['marks']:<10}")
    
    print("=" * 70)
    print(f"Total students: {len(students_list)}")
    print("=" * 70)

def display_message(message, message_type="info"):
    """Display formatted messages"""
    icons = {
        "info": "ℹ️",
        "success": "✅",
        "warning": "⚠️",
        "error": "❌"
    }
    
    icon = icons.get(message_type, "ℹ️")
    print(f"\n{icon} {message}")

def display_student_details(student):
    """Display detailed information about a single student"""
    if not student:
        return
    
    print("\n" + "=" * 40)
    print("        STUDENT DETAILS")
    print("=" * 40)
    print(f"ID:     {student['id']}")
    print(f"Name:   {student['name']}")
    print(f"Course: {student['course']}")
    print(f"Marks:  {student['marks']}")
    print("=" * 40)