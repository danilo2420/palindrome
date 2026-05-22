from flask import Blueprint

palindrome_bp = Blueprint("palindrome", __name__, url_prefix="/palindrome")

@palindrome_bp.route("/isit/<word>")
def is_palindrome(word):
    try:
        for i in range(int(len(word)/2)):
            if word[i] != word[len(word) - 1 - i]:
                return "Not a palindrome"
        return "I'ts a palindrome!", 200
    except:
        return "Error", 500