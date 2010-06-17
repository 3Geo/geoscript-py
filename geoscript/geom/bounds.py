from org.geotools.geometry.jts import ReferencedEnvelope
from geoscript.util import deprecated
from geoscript import proj

class Bounds(ReferencedEnvelope):
  """
  A two dimensional bounding box.
  """
  def __init__(self, west=None, south=None, east=None, north=None, prj=None, env=None):
    if prj:
      prj = proj.Projection(prj)

    if env:
      if prj:
        ReferencedEnvelope.__init__(self, env, prj._crs)
      else:
        ReferencedEnvelope.__init__(self, env)
    else:
      ReferencedEnvelope.__init__(self, west, east, south, north, 
         prj._crs if prj else None)

  def getwest(self):
    return self.minX()
  west = property(getwest)
  """
  The leftmost/westmost oordinate of the bounds.
  """

  @deprecated
  def get_l(self):
    return self.west
  l = property(get_l, None, None, "Use west.")

  def getsouth(self):
    return self.minY()
  south = property(getsouth)
  """
  The bottomtmost/southmost oordinate of the bounds.
  """

  @deprecated
  def get_b(self):
    return self.south
  b = property(get_b, None, None, "Use south.")

  def geteast(self):
    return self.maxX()
  east = property(geteast)
  """
  The rightmost/eastmost oordinate of the bounds.
  """

  @deprecated
  def get_r(self):
    return self.east
  r = property(get_r, None, None, 'Use east.')

  def getnorth(self):
    return self.maxY()
  north = property(getnorth)
  """
  The topmost/northmost oordinate of the bounds.
  """

  @deprecated
  def get_t(self):
    return self.north
  t = property(get_t, None, None, 'Use north.')

  def getproj(self):
    crs = self.coordinateReferenceSystem
    if crs:
      return proj.Projection(crs)
  proj = property(getproj)
  """
  The :class:`Projection <geoscript.proj.Projection>` of the bounds. ``None`` if the projection is unknown.
  """

  def reproject(self, prj):
    """
    Reprojects the bounding box.
    
    *prj* is the destination :class:`Projection <geoscript.proj.Projection>` 

    """
    if not self.proj:
      raise Exception('No projection set on bounds, unable to reproject')

    prj = proj.Projection(prj)
    return Bounds(env=self.transform(prj._crs, True))
   
  def __repr__(self):
    s = '(%s, %s, %s, %s' % (self.west, self.south, self.east, self.north)
    if self.proj:
      s = '%s, %s' % (s, self.proj.id)

    return '%s)' % s

