from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)



@app.route("/", methods=["POST", "GET"])
def login():
    try:
        if request.method == "POST":
            deu = request.form["deu"]
            eng = request.form["eng"]
            mat = request.form["mat"]
            nw1 = request.form["nw1"]
            nw2 = request.form["nw2"]
            nw3 = request.form["nw3"]

            my_score = 2 * (int(deu) + int(eng) + int(mat) + int(nw1)) + int(nw2) + int(nw3)

            if my_score > 140:
                result = "1.0"
                satz = "Deine Durchschnittsnote ist"
            elif my_score < 50:
                result = "Nicht Bestanden."
                satz = ""
            else:
                result = None
                for score, result in zip(range(50, 151, 3), range(40, 9, -1)):
                    if my_score <= score:
                        result = str(result / 10)
                        break
                satz = "Deine Durchschnittsnote ist"
            return render_template("main.html", content=result, content2=satz, deu1= deu, eng1= eng, mat1= mat, nw11= nw1, nw21= nw2, nw31= nw3)
    except:
            return render_template("main.html", content="Füll zuerst deine Endnoten aus!", content2="", deu1="")
    else:
        return render_template("base.html")

"""
if __name__ == "__main__":
    app.run(debug=True)
"""