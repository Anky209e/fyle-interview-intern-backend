from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment
from.schema import AssignmentSchema,AssignmentGradeSchema


principal_assignment_resources = Blueprint('principal_assignment_resources',__name__)

@principal_assignment_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    """Returns list of Submitted and Graded assignments"""
    submitted_graded_assingments = Assignment.get_submitted_and_graded()
    submitted_graded_assingments_dump = AssignmentSchema().dump(submitted_graded_assingments, many=True)
    return APIResponse.respond(data=submitted_graded_assingments_dump)