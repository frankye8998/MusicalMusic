

class MuseScoreException(Exception):
  pass

class InvalidFileExtension(MuseScoreException):
  pass

class InvalidScoreID(MuseScoreException):
  pass

class InvalidCredentials(MuseScoreException):
  pass
