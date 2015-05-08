import os
from flask import Flask, url_for, jsonify, request, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../data.sqlite')

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

db = SQLAlchemy(app)


class ValidationError(ValueError):
    pass


class fallout(db.Model):
    __tablename__ = 'fallout'
    id = db.Column(db.Integer, primary_key = True)
    created_utc = db.Column(db.Float, index=True)
    score = db.Column(db.Integer, index=True)
    domain = db.Column(db.String(512), index=True)
    title = db.Column(db.String(512), index =True)
    author = db.Column(db.String(512), index = True)
    ups = db.Column(db.Integer, index = True)
    downs = db.Column(db.Integer, index = True)
    num_comments = db.Column(db.Integer, index = True)
    permalink = db.Column(db.String(512), index = False)
    thumbnail = db.Column(db.String(512), index = False)
    url = db.Column(db.String(512), index = False)

    def get_url(self):
        return url_for('get_fallout', id=self.id, _external=True)

    def export_data(self):
        return {
            'self_url' : self.get_url(),
            'created_utc' : self.created_utc,
            'score' : self.score,
            'domain' : self.domain,
            'title' : self.title,
            'author' : self.author,
            'ups' : self.ups,
            'downs' : self.downs,
            'num_comments' : self.num_comments,
            'permalink' : self.permalink,
            'thumbnail' : self.thumbnail,
            'url' :self.url,
        
        }

    def import_data(self, data):
        try:
            self.created_utc = data['created_utc']
            self.score = data['score']
            self.domain = data['domain']
            self.title = data['title']
            self.author = data['author']
            self.ups = data['ups']
            self.downs = data['downs']
            self.num_comments = data['num_comments']
            self.permalink = data['permalink']
            self.thumbnail = data['thumbnail']
            self.url = data['url']
                
        except KeyError as e:
            raise ValidationError('Invalid fallout: missing ' + e.args[0])
        return self


@app.route('/fallout/', methods=['GET'])
def get_fallout():
    return jsonify({'fallout': [falloutTemp.get_url() for falloutTemp in
                                  fallout.query.all()]})

@app.route('/fallout/<int:id>', methods=['GET'])
def get_falloutData(id):
    return jsonify(fallout.query.get_or_404(id).export_data())

@app.route('/fallout/', methods=['POST'])
def new_fallout():
    falloutTemp = fallout()
    falloutTemp.import_data(request.json)
    db.session.add(falloutTemp)
    db.session.commit()
    return jsonify({}), 201, {'Location': falloutTemp.get_url()}

@app.route('/fallout/<int:id>', methods=['PUT'])
def edit_fallout(id):
    falloutTemp = fallout.query.get_or_404(id)
    falloutTemp.import_data(request.json)
    db.session.add(falloutTemp)
    db.session.commit()
    return jsonify({})

# todo: implement this template
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.route('/')
def index():
    highlight = {'min': 1, 'max': 2}
    falloutTemp = fallout.query.all()
    return render_template('index.html', falloutTemp=falloutTemp, highlight=highlight)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
