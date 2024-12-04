from flask import Flask,request,jsonify
import csv

app = Flask(__name__)


MINMAX_FILE_PATH = 'min-maxvalues.csv'
@app.route('/minmax', methods=['POST'])
def minmax():
    # Get the form data
    data = request.get_json()

    # Write data to CSV by overwriting the file
    try:
        with open(MINMAX_FILE_PATH, mode='w', newline='') as file:  # 'w' mode overwrites the file
            writer = csv.DictWriter(file, fieldnames=data.keys())
            # Write header row since we're overwriting the file
            writer.writeheader()
            writer.writerow(data)
        return jsonify({"message": "Data saved successfully!"}), 200
    except Exception as e:
        return jsonify({"message": f"Error saving data: {str(e)}"}), 500

# main driver function
if __name__ == '__main__':
    app.run()