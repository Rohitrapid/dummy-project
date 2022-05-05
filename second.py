from flask import Blueprint
second=Blueprint("second",__name__,static_folder="static", template_folder="templates")

@second.route("/layout")
@second.route("/lay")
def lay():
	return "<h1>Test</h1>"
	