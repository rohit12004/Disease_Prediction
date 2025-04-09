# from flask import Flask, request, jsonify, render_template
# import numpy as np
# import pandas as pd
# import pickle

# app = Flask(__name__)

# # Load models
# diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
# heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
# parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
# CKD_model = pickle.load(open('CKD_model_final.sav', 'rb'))
# liver_model = pickle.load(open('Liver_disease_model.sav','rb'))

# symptoms_model = pickle.load(open('symptoms_model1.sav', 'rb'))
# label_encoder = pickle.load(open('label_encoder.sav', 'rb'))
# symptoms_list = pickle.load(open('symptoms_list.sav', 'rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/symp')
# def symp():
#     sorted_symptoms = sorted(symptoms_list)
#     return render_template('symptoms.html',symptoms_list=sorted_symptoms)

# @app.route('/predictfromsymptoms', methods=['POST'])
# def predictfromsymptoms():
#     data = request.json
#     selected_symptoms = data['symptoms']

#     # Initialize input vector with zeros
#     input_vector = [0] * len(symptoms_list)

#     for symptom in selected_symptoms:
#         if symptom != "0" and symptom in symptoms_list: 
#              index = symptoms_list.get_loc(symptom)
#              input_vector[index] = 1

#     # input_df = pd.DataFrame([input_vector], columns=symptoms_list)

#     # Make prediction
#     predicted_label = symptoms_model.predict([input_vector])
#     predicted_disease = label_encoder.inverse_transform([predicted_label])[0]

#     probabilities = symptoms_model.predict_proba([input_vector])[0]  
   
#     predicted_label = symptoms_model.predict([input_vector])[0]
#     predicted_class_index = predicted_label 
  
#     predicted_disease_probability = probabilities[predicted_class_index]
   
#     # print(f"Probability of predicted disease: {predicted_disease_probability}")

#     return jsonify({
#         'predicted_disease': predicted_disease,
#         'Probability': round(predicted_disease_probability * 100, 2)
#         })



# def validate_input(data, expected_length):
#     if not data or len(data) != expected_length:
#         return f"Invalid input: Expected {expected_length} values, but got {len(data) if data else 0}."
#     try:
#         data = np.array(data, dtype=float).reshape(1, -1)
#     except ValueError:
#         return "Invalid input: Please enter numeric values."
#     return data

# @app.route('/diabetes_predict', methods=['POST'])
# def diabetes_predict():
#     try:
#         data = request.json.get('values')
#         validated_data = validate_input(data, 8)
        
#         if isinstance(validated_data, str):
#             return jsonify({'error': validated_data}), 400

#         prediction = diabetes_model.predict(validated_data)[0]
#         probability = diabetes_model.predict_proba(validated_data)[0][1] * 100

#         return jsonify({
#             'prediction': "THE PERSON HAS DIABETES" if prediction == 1 else "THE PERSON DOES NOT HAVE DIABETES",
#             'probability': round(probability, 2)
#         })
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @app.route('/heartdisease_predict', methods=['POST'])
# def heartdisease_predict():
#     try:
#         data = request.json.get('values')
#         validated_data = validate_input(data, 13)
        
#         if isinstance(validated_data, str):
#             return jsonify({'error': validated_data}), 400
        
#         prediction = heart_disease_model.predict(validated_data)[0]
#         probability = heart_disease_model.predict_proba(validated_data)[0][1] * 100

#         return jsonify({
#             'prediction': "THE PERSON HAS HEART DISEASE" if prediction == 1 else "THE PERSON DOES NOT HAVE HEART DISEASE",
#             'probability': round(probability, 2)
#         })
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @app.route('/ckd_predict', methods=['POST'])
# def CKD_predict():
#     try:
#         data = request.json.get('values')
#         validated_data = validate_input(data, 13)
        
#         if isinstance(validated_data, str):
#             return jsonify({'error': validated_data}), 400
        
#         prediction = CKD_model.predict(validated_data)[0]
#         probability = CKD_model.predict_proba(validated_data)[0][1] * 100

#         return jsonify({
#             'prediction': "THE PERSON HAS CKD" if prediction == 1 else "THE PERSON DOES NOT HAVE CKD",
#             'probability': round(probability, 2)
#         })
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
    

# @app.route('/liver_predict', methods=['POST'])
# def liver_predict():
#     try:
#         data = request.json.get('values')
#         validated_data = validate_input(data, 10)
        
#         if isinstance(validated_data, str):
#             return jsonify({'error': validated_data}), 400
        
#         prediction = liver_model.predict(validated_data)[0]
#         probability = liver_model.predict_proba(validated_data)[0][1] * 100

#         return jsonify({
#             'prediction': "THE PERSON HAS LIVER DISEASE" if prediction == 1 else "THE PERSON DOES NOT HAVE LIVER DISEASE",
#             'probability': round(probability, 2)
#         })
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500


# @app.route('/parkinsons_predict', methods=['POST'])
# def parkinsons_predict():
#     try:
#         data = request.json.get('values')
#         validated_data = validate_input(data, 22)
        
#         if isinstance(validated_data, str):
#             return jsonify({'error': validated_data}), 400
        
#         prediction = parkinsons_model.predict(validated_data)[0]
#         probability = parkinsons_model.predict_proba(validated_data)[0][1] * 100

#         return jsonify({
#             'prediction': "THE PERSON HAS PARKINSONS DISEASE" if prediction == 1 else "THE PERSON DOES NOT HAVE PARKINSONS DISEASE",
#             'probability': round(probability, 2)
#         })
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
    



# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
CKD_model = pickle.load(open('CKD_model_final.sav', 'rb'))
liver_model = pickle.load(open('Liver_disease_model.sav','rb'))

symptoms_model = pickle.load(open('symptoms_model1.sav', 'rb'))
label_encoder = pickle.load(open('label_encoder.sav', 'rb'))
symptoms_list = pickle.load(open('symptoms_list.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/symp')
def symp():
    sorted_symptoms = sorted(symptoms_list)
    return render_template('symptoms.html', symptoms_list=sorted_symptoms)

@app.route('/predictfromsymptoms', methods=['POST'])
def predictfromsymptoms():
    data = request.json
    selected_symptoms = data['symptoms']

    # Initialize input vector with zeros
    input_vector = [0] * len(symptoms_list)

    for symptom in selected_symptoms:
        if symptom != "0" and symptom in symptoms_list:
            index = symptoms_list.get_loc(symptom)
            input_vector[index] = 1

    probabilities = symptoms_model.predict_proba([input_vector])[0]

    # Get indices of top 3 probabilities
    top3_indices = np.argsort(probabilities)[-3:][::-1]

    # Map indices to disease names and probabilities
    top3_diseases = []
    for idx in top3_indices:
        disease = label_encoder.inverse_transform([idx])[0]
        prob = round(probabilities[idx] * 100, 2)
        top3_diseases.append({'disease': disease, 'probability': prob})

    return jsonify({'top_3_diseases': top3_diseases})


def validate_input(data, expected_length):
    if not data or len(data) != expected_length:
        return f"Invalid input: Expected {expected_length} values, but got {len(data) if data else 0}."
    try:
        data = np.array(data, dtype=float).reshape(1, -1)
    except ValueError:
        return "Invalid input: Please enter numeric values."
    return data

@app.route('/diabetes_predict', methods=['POST'])
def diabetes_predict():
    try:
        data = request.json.get('values')
        validated_data = validate_input(data, 8)

        if isinstance(validated_data, str):
            return jsonify({'error': validated_data}), 400

        prediction = diabetes_model.predict(validated_data)[0]
        probability = diabetes_model.predict_proba(validated_data)[0][1] * 100

        return jsonify({
            'prediction': "THE PERSON HAS DIABETES" if prediction == 1 else "THE PERSON DOES NOT HAVE DIABETES",
            'probability': round(probability, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/heartdisease_predict', methods=['POST'])
def heartdisease_predict():
    try:
        data = request.json.get('values')
        validated_data = validate_input(data, 13)

        if isinstance(validated_data, str):
            return jsonify({'error': validated_data}), 400

        prediction = heart_disease_model.predict(validated_data)[0]
        probability = heart_disease_model.predict_proba(validated_data)[0][1] * 100

        return jsonify({
            'prediction': "THE PERSON HAS HEART DISEASE" if prediction == 1 else "THE PERSON DOES NOT HAVE HEART DISEASE",
            'probability': round(probability, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/ckd_predict', methods=['POST'])
def CKD_predict():
    try:
        data = request.json.get('values')
        validated_data = validate_input(data, 13)

        if isinstance(validated_data, str):
            return jsonify({'error': validated_data}), 400

        prediction = CKD_model.predict(validated_data)[0]
        probability = CKD_model.predict_proba(validated_data)[0][1] * 100

        return jsonify({
            'prediction': "THE PERSON HAS CKD" if prediction == 1 else "THE PERSON DOES NOT HAVE CKD",
            'probability': round(probability, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/liver_predict', methods=['POST'])
def liver_predict():
    try:
        data = request.json.get('values')
        validated_data = validate_input(data, 10)

        if isinstance(validated_data, str):
            return jsonify({'error': validated_data}), 400

        prediction = liver_model.predict(validated_data)[0]
        probability = liver_model.predict_proba(validated_data)[0][1] * 100

        return jsonify({
            'prediction': "THE PERSON HAS LIVER DISEASE" if prediction == 1 else "THE PERSON DOES NOT HAVE LIVER DISEASE",
            'probability': round(probability, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/parkinsons_predict', methods=['POST'])
def parkinsons_predict():
    try:
        data = request.json.get('values')
        validated_data = validate_input(data, 22)

        if isinstance(validated_data, str):
            return jsonify({'error': validated_data}), 400

        prediction = parkinsons_model.predict(validated_data)[0]
        probability = parkinsons_model.predict_proba(validated_data)[0][1] * 100

        return jsonify({
            'prediction': "THE PERSON HAS PARKINSONS DISEASE" if prediction == 1 else "THE PERSON DOES NOT HAVE PARKINSONS DISEASE",
            'probability': round(probability, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
