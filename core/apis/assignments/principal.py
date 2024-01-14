from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment,AssignmentStateEnum
from core.models.teachers import Teacher
from.schema import AssignmentSchema,AssignmentGradeSchema,TeacherSchema
from core.libs.exceptions import FyleError


principal_assignment_resources = Blueprint('principal_assignment_resources',__name__)

@principal_assignment_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of Submitted and Graded assignments"""
    submitted_graded_assingments = Assignment.get_submitted_and_graded()
    submitted_graded_assingments_dump = AssignmentSchema().dump(submitted_graded_assingments, many=True)
    return APIResponse.respond(data=submitted_graded_assingments_dump)

@principal_assignment_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def get_all_teachers(p):
    """Returns list All teachers"""
    all_teachers = Teacher.get_all()
    all_teachers_dump = TeacherSchema().dump(all_teachers, many=True)
    return APIResponse.respond(data=all_teachers_dump)

@principal_assignment_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p, incoming_payload):
    """Grade an assignment"""
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)
    cur_assignment  = Assignment.get_by_id(grade_assignment_payload.id)
    
    if cur_assignment.state == AssignmentStateEnum.DRAFT:    
        raise FyleError(400, 'Cannot grade a draft assignment')

    graded_assignment = Assignment.mark_grade(
        _id=grade_assignment_payload.id,
        grade=grade_assignment_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return APIResponse.respond(data=graded_assignment_dump)