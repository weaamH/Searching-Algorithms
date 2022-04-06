class Node:

    def __init__(self, cityname, city_id, parent, visited, dis):
        self.parent = parent
        self.visited = visited
        self.city_id = city_id
        self.cityname = cityname
        self.dis = dis

    def set_cityname(self, cityname):
        self.cityname = cityname

    def get_cityname(self):
        return self.cityname

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def set_city_id(self, city_id):
        self.city_id = city_id

    def get_city_id(self):
        return self.city_id

    def set_visited(self, visited):
        self.visited = visited

    def get_visited(self):
        return self.visited

    def set_dis(self, dis):
        self.dis = dis

    def get_dis(self):
        return self.dis



