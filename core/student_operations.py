"""
Core operations for student management
"""
from core.validation import validate_student_data, validate_course, validate_marks
from utils.display import display_students_table, display_message

# Global students list (acting as our database)
students = []

def add_student(student_id, name, course, marks):
    """Add a new student to the system"""
    # Validate input data
    validation_result = validate_student_data(student_id, name, course, marks)
    if not validation_result["valid"]:
        return validation_result["message"]
    
    # Check if student ID already exists
    for student in students:
        if student["id"] == student_id:
            return f"Student with ID '{student_id}' already exists!"
    
    # Check maximum limit
    if len(students) >= 9:
        return "Maximum limit of 9 students reached!"
    
    # Add student to list
    student = {
        "id": student_id,
        "name": name,
        "course": course.upper(),
        "marks": int(marks)
    }
    students.append(student)
    return f"Student '{name}' added successfully!"

def view_students():
    """Display all students in tabular format"""
    if not students:
        display_message("No students found in the system.", "warning")
        return
    
    display_students_table(students)

def search_student(search_by_id=None, search_by_name=None, silent=False):
    """Search for students by ID or name"""
    results = []
    
    if search_by_id:
        for student in students:
            if student["id"] == search_by_id:
                results.append(student)
    
    elif search_by_name:
        for student in students:
            if search_by_name.lower() in student["name"].lower():
                results.append(student)
    
    if results:
        if not silent:
            display_students_table(results)
        return results
    else:
        if not silent:
            display_message("No students found matching your criteria.", "warning")
        return None

def update_student(student_id, new_course=None, new_marks=None):
    """Update student course and/or marks"""
    student_found = False
    
    for student in students:
        if student["id"] == student_id:
            student_found = True
            
            if new_course:
                if not validate_course(new_course):
                    return "Invalid course! Must be one of: CSE, ML, IT, DS, AIML"
                student["course"] = new_course.upper()
            
            if new_marks:
                marks_validation = validate_marks(new_marks)
                if not marks_validation["valid"]:
                    return marks_validation["message"]
                student["marks"] = int(new_marks)
            
            break
    
    if student_found:
        return f"Student with ID '{student_id}' updated successfully!"
    else:
        return f"Student with ID '{student_id}' not found!"

def delete_student(student_id):
    """Delete a student by ID"""
    global students
    
    for i, student in enumerate(students):
        if student["id"] == student_id:
            deleted_name = student["name"]
            students.pop(i)
            return f"Student '{deleted_name}' (ID: {student_id}) deleted successfully!"
    
    return f"Student with ID '{student_id}' not found!"

def get_students_count():
    """Get the current number of students"""
    return len(students)

def get_all_students():
    """Get all students (for testing purposes)"""
    return students.copy()

def clear_all_students():
    """Clear all students (for testing purposes)"""
    global students
    students.clear()