import math

from flask import Flask, abort, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


def _form_number(name):
    try:
        value = float(request.form[name])
    except (KeyError, ValueError):
        abort(400, description=f"El campo '{name}' debe ser numérico.")

    if not math.isfinite(value):
        abort(400, description=f"El campo '{name}' debe ser un número finito.")
    return value


@app.route("/compra", methods=["GET", "POST"])
def compra():
    cantidad = precio = subtotal = descuento = total = None

    if request.method == "POST":
        try:
            cantidad = int(request.form["cantidad"])
        except (KeyError, ValueError):
            abort(400, description="La cantidad debe ser un número entero.")
        precio = _form_number("precio")

        if cantidad < 1 or precio < 0:
            abort(400, description="La cantidad debe ser positiva y el precio no puede ser negativo.")

        subtotal = cantidad * precio
        descuento = subtotal * 0.10 if subtotal > 1000 else 0
        total = subtotal - descuento

    return render_template(
        "compra.html",
        cantidad=cantidad,
        precio=precio,
        subtotal=subtotal,
        descuento=descuento,
        total=total,
    )


@app.route("/salario", methods=["GET", "POST"])
def salario():
    horas = pago_hora = salario_total = None

    if request.method == "POST":
        horas = _form_number("horas")
        pago_hora = _form_number("pago_hora")

        if horas < 0 or pago_hora < 0:
            abort(400, description="Las horas y el pago por hora no pueden ser negativos.")

        horas_normales = min(horas, 40)
        horas_extra = max(horas - 40, 0)
        salario_total = (horas_normales * pago_hora) + (horas_extra * pago_hora * 2)

    return render_template(
        "salario.html",
        horas=horas,
        pago_hora=pago_hora,
        salario_total=salario_total,
    )


@app.route("/temperatura", methods=["GET", "POST"])
def temperatura():
    celsius = fahrenheit = kelvin = None

    if request.method == "POST":
        celsius = _form_number("celsius")
        fahrenheit = (celsius * 9 / 5) + 32
        kelvin = celsius + 273.15

    return render_template(
        "temperatura.html",
        celsius=celsius,
        fahrenheit=fahrenheit,
        kelvin=kelvin,
    )


@app.route("/empresa")
def empresa():
    return render_template("empresa.html")


@app.route("/servicios")
def servicios():
    return render_template("servicios.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True) 