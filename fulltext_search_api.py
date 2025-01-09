from flask import Flask, request, jsonify
from sqlalchemy import text

app = Flask(__name__)

@app.route('/teams/search', methods=['GET'])
def search_teams():
    
    regex = request.args.get('regex', '')
    if not regex:
        return jsonify({"error": "Parameter 'regex' is required"}), 400
  
    query = text("""
        SELECT * 
        FROM komanda
        WHERE dop_info::text ~* :regex
    """)
    results = db.session.execute(query, {"regex": regex}).fetchall()
    
    response = [dict(row) for row in results]
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
