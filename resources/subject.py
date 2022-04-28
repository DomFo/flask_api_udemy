from flask_restful import Resource
from models.subject import SubjectModel


class Subject(Resource):
    def get(self, subject_id):
        subject = SubjectModel.find_by_id(subject_id)
        print(subject)
        if subject:
            return subject.json()
        return {"message": "Item not found."}, 404

    def delete(cls, subject_id):
        subject = SubjectModel.find_by_id(subject_id)
        if not subject:
            return {'message': 'Subject not found'}, 404
        subject.delete_from_db()
        return {'message': 'Subject deleted'}