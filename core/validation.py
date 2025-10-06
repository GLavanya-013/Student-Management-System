"""
Validation functions for student data
"""

VALID_COURSES = ["CSE", "ML", "IT", "DS", "AIML"]

def validate_student_data(student_id, name, course, marks):
    """Validate all student data at once"""
    # Check if any field is empty
    if not student_id or not name or not course or not marks:
        return {"valid": False, "message": "All fields are required!"}
    
    # Validate course
    if not validate_course(course):
        return {"valid": False, "message": f"Invalid course! Must be one of: {', '.join(VALID_COURSES)}"}
    
    # Validate marks
    marks_validation = validate_marks(marks)
    if not marks_validation["valid"]:
        return marks_validation
    
    # Validate name (should contain only letters and spaces)
    if not all(c.isalpha() or c.isspace() for c in name):
        return {"valid": False, "message": "Name should contain only letters and spaces!"}
    
    # Validate student ID (should not be empty)
    if not student_id.strip():
        return {"valid": False, "message": "Student ID cannot be empty!"}
    
    return {"valid": True, "message": "All data is valid"}

def validate_course(course):
    """Validate if course is from the allowed list"""
    return course.upper() in VALID_COURSES

def validate_marks(marks):
    """Validate marks input"""
    try:
        marks_int = int(marks)
        if marks_int < 0 or marks_int > 100:
            return {"valid": False, "message": "Marks must be between 0 and 100!"}
        return {"valid": True, "message": "Marks are valid"}
    except ValueError:
        return {"valid": False, "message": "Marks must be a valid number!"}