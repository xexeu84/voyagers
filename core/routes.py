class RouteManager:
    def __init__(self):
        self.routes = []
    def add_route(self, origin, destination, space_available):
        route = {"from": origin, "to": destination, "kg": space_available}
        self.routes.append(route)
        return f"Ruta {origin} -> {destination} registrada."
