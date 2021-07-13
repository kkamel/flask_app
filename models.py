from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.sqlite3'
# Intialize DB
db = SQLAlchemy()
#db.Model.metadata.reflect(db.engine)

class Player(db.Model):
    __tablename__ = 'Player'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    playerID = db.Column(
        db.String,
        index=True,
        unique=True,
        nullable=False
    )
    birthYear = db.Column(
        # TODO use db.Datetime in the future
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    birthYear = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    birthMonth = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    birthDay = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )

    birthCountry = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )

    birthState = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    birthCity = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    deathYear = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    deathMonth = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    deathDay = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    deathCountry = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    deathState = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    deathCity = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    nameFirst = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    nameLast = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    nameGiven = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    weight = db.Column(
        db.Integer,
        index=False,
        unique=False,
        nullable=True
    )
    height = db.Column(
        db.Integer,
        index=False,
        unique=False,
        nullable=True
    )
    bats = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    throws = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    debut = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    finalGame = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=True
    )
    retroID = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )
    bbrefID = db.Column(
        db.String(64),
        index=False,
        unique=False,
        nullable=False
    )


    def __repr__(self):
        return f"Player('{self.id}', '{self.playerID}', '{self.nameFirst}', '{self.nameLast}', '{self.weight}', '{self.height}', '{self.bats}', '{self.throws}', '{self.retroID}', '{self.bbrefID}')"
'''
          def populate(self, row):
        self.player_id = row[0]
        self.birthYear = row[1]
        self.birthMonth = row[2]
        self.birthDay = row[3]
        self.birthCountry = row[4]
        self.birthState = row[5]
        self.birthCity = row[6]
        self.deathYear = row[7]
        self.deathMonth = row[8]
        self.deathDay = row[9]
        self.deathCountry = row[10]
        self.deathState =row[11]
        self.deathCity = row[12]
        self.nameFirst = row[13]
        self.nameLast = row[14]
        self.nameGiven = row[15]
        self.weight = row[16]
        self.height = row[17]
        self.bats = row[18]
        self.throws = row[19]
        self.debut = row[20]
        self.finalGame = row[21]
        self.retroID = row[22]
        self.bbrefID = row[23]

        #print(self.player_id)
'''
'''
playerID,birthYear,birthMonth,birthDay,birthCountry,birthState,birthCity,deathYear,deathMonth,deathDay,deathCountry,deathState,deathCity,nameFirst,nameLast,nameGiven,weight,height,bats,throws,debut,finalGame,retroID,bbrefID

'''