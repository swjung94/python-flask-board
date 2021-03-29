from sboard import db

class MainContents(db.Model):
    __tablename__='main_contents'
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # foreignkey 설정에서 테이블 이름은 MainContents일 경우 기본은 main_contents이다.
    question_id = db.Column(db.Integer, db.ForeignKey('main_contents.id', ondelete='CASCADE'))
    question = db.relationship('MainContents', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
