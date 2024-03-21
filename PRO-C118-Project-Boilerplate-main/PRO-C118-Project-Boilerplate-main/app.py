from flask import Flask, request, jsonify
import prediction
app = Flask(__name__)

@app.route('/', methods=['POST'])
def save():
    # extracting date, product name, review, sentiment associated from the JSON data
    data = request.get_json()  # Assuming JSON payload with 'date', 'product', 'review', 'sentiment'
    date = data.get('date')
    product = data.get('product')
    review = data.get('review')
    sentiment = data.get('sentiment')

    # creating a final variable separated by commas
    data_entry = f"{date},{product},{review},{sentiment}\n"

    # open the file in the 'append' mode
    with open('reviews.csv', 'a') as file:
        # Log the data in the file
        file.write(data_entry)

    # return a success message
    return jsonify({'status': 'success', 'message': 'Data Logged'})

if __name__ == "__main__":
    app.run(debug=True)
