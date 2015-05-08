fimport os
from flask import Flask, url_for, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../data.sqlite')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

db = SQLAlchemy(app)


class ValidationError(ValueError):
    pass


class fallout(db.Model):
    __tablename__ = 'fallout'
    CREATED_UTC = db.Column(db.Integer, index=true)
    SCORE = db.Column(db.Integer, index=True)
    DOMAIN = db.Column(db.String(512), index=True)
    TITLE = db.Column(db.String(512), index =True)
    AUTHOR = db.Column(db.String(512), index = True)
    UPS = db.Column(db.Integer, index = True)
    DOWNS = db.Column(db.Integer, index = True)
    NUM_COMMENTS = db.Column(db.Integer, index = True)
    PERMALINK = db.Column(db.String(512), Index =false)
    THUMBNAIL = db.Column(db.String(512), Index = false)
    URL = db.Column(db.String(512), Index = false)
    
    name = db.Column(db.String(64), index=True)

    def get_url(self):
        return url_for('get_fallout', id=self.id, _external=True)

    def export_data(self):
        return {
            '
            'self_url': self.get_url(),
            'SCORE' : self.SCORE,
            'DOMAIN' : self.DOMAIN,
            'TITLE' : self.TITLE,
            'AUTHOR' : self.AUTHOR,
            'UPS' : self.UPS,
            'DOWNS' : self.DOWNS,
            'NUM_COMMENTS' : self.NUM_COMMENTS,
            'PERMALINK' : self.PERMALINK,
            'THUMBNAIL' : self.THUMBNAIL,
            'URL' :self.URL,
            
            'name': self.name
        }

    def import_data(self, data):
        try:
            self.name = data['name']
        except KeyError as e:
            raise ValidationError('Invalid fallout: missing ' + e.args[0])
        return self


@app.route('/fallout/', methods=['GET'])
def get_fallout():
    return jsonify({'fallout': [fallout.get_url() for fallout in
                                  fallout.query.all()]})

@app.route('/fallout/<int:id>', methods=['GET'])
def get_fallout(id):
    return jsonify(fallout.query.get_or_404(id).export_data())

@app.route('/fallout/', methods=['POST'])
def new_fallout():
    falloutTemp = fallout()
    falloutTemp.import_data(request.json)
    db.session.add(falloutTemp)
    db.session.commit()
    return jsonify({}), 201, {'Location': fallout.get_url()}

@app.route('/fallout/<int:id>', methods=['PUT'])
def edit_fallout(id):
    falloutTemp = fallout.query.get_or_404(id)
    falloutTemp.import_data(request.json)
    db.session.add(falloutTemp)
    db.session.commit()
    return jsonify({})


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
