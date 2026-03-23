from wsgiref.simple_server import make_server
from spyne import Application, ServiceBase, rpc, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from temp_soap_service.service import (
    fahrenheit_to_celsius,
    celsius_to_fahrenheit,
)


class TemperatureService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def FahrenheitToCelsius(ctx, Fahrenheit):
        try:
            value = float(Fahrenheit)
            result = fahrenheit_to_celsius(value)
            return f"{result:.2f}"
        except ValueError:
            return "Invalid Fahrenheit value"

    @rpc(Unicode, _returns=Unicode)
    def CelsiusToFahrenheit(ctx, Celsius):
        try:
            value = float(Celsius)
            result = celsius_to_fahrenheit(value)
            return f"{result:.2f}"
        except ValueError:
            return "Invalid Celsius value"


application = Application(
    [TemperatureService],
    tns="http://example.com/temperature/wsdl",
    in_protocol=Soap11(validator="soft"),
    out_protocol=Soap11(),
)

wsgi_app = WsgiApplication(application)


def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    print(f"SOAP service running at http://{host}:{port}")
    print(f"WSDL available at http://{host}:{port}/?wsdl")
    server = make_server(host, port, wsgi_app)
    server.serve_forever()


if __name__ == "__main__":
    run_server()
