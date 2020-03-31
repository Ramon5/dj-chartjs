class LineNode:
    data = []
    label = ""
    borderColor = "",
    fill = False

    def serialize(self):
        return {
            "data": self.data,
            "label": self.label,
            "borderColor": self.borderColor,
            "fill": self.fill
        }

class Node:
    label = ""
    backgroundColor = []
    data = []

    def serialize(self):
        return {
            "label": self.label,
            "backgroundColor": self.backgroundColor,
            "data": self.data
        }

class RadarNode:
    label = ""
    fill = True
    backgroundColor = ""
    borderColor = ""
    _pointBorderColor = "#fff"
    pointBackgroundColor = ""
    data = []

    def serialize(self):
        return {
            "label": self.label,
            "fill": self.fill,
            "backgroundColor": self.backgroundColor,
            "borderColor": self.borderColor,
            "pointBorderColor": self._pointBorderColor,
            "pointBackgroundColor": self.pointBackgroundColor,
            "data": self.data
        }
