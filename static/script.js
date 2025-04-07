const diseaseForms = {
    "Diabetes": ["Number of Pregnancies", "Glucose Level", "Blood Pressure", "Skin Thickness", "Insulin", "BMI", "Diabetes Pedigree Function", "Age"],
    "HeartDisease": ["Age", "Sex : Male(1   ),Female(0)", "Chest Pain Type", "Resting Blood Pressure", "Serum Cholesterol", "Fasting Blood Sugar", "Resting ECG", "Max Heart Rate", "Exercise Induced Angina", "ST Depression", "Slope", "Major Vessels", "Thalassemia"],
    "Parkinsons": ["MDVP: Fo(Hz)", "MDVP: Fhi(Hz)", "MDVP: Flo(Hz)", "MDVP: Jitter(%)", "MDVP: Jitter(Abs)", "MDVP: RAP", "MDVP: PPQ", "Jitter: DDP", "MDVP: Shimmer", "MDVP: Shimmer(dB)", "Shimmer: APQ3", "Shimmer: APQ5", "MDVP: APQ", "Shimmer: DDA", "NHR", "HNR", "RPDE", "DFA", "Spread1", "Spread2", "D2", "PPE"],
    "CKD": ["Bp(Blood Pressure)","Sg(Specific Gravity)","Al( Albumin)","Su(Sugar)","Rbc(Red Blood Cell Count)","Bu(Blood Urea)","Sc(Serum Creatinine)","Sod(Sodium)","Pot(Pottasium)","Hemo(Hemoglobin)","Wbcc(White Blood Cells Count)","Rbcc(Red Blood Cells Count)","Htn(Hypertension)"],
    "Liver": ["Age","Gender:Male(0), Female(1)","BMI","AlcoholConsumption","Smoking:NO(0),YES(1)","GeneticRisk:L(0),M(1),H(2)","PhysicalActivity(0-10 hrs per week)","Diabetes:N0(0),YES(1)","Hypertension:N0(0),YES(1)","LiverFunctionTest:20-100"]
};  

let selectedDisease = "Diabetes";

document.addEventListener("DOMContentLoaded", () => {
    changeContent(selectedDisease);
});

function changeContent(disease) {
    selectedDisease = disease;
    document.getElementById("disease-title").innerText = `${disease} Prediction using ML`;
    
    document.querySelectorAll(".sidebar ul li").forEach(item => item.classList.remove("active"));
    document.querySelector(`.sidebar ul li[onclick="changeContent('${disease}')"]`).classList.add("active");

    let formContainer = document.getElementById("form-container");
    formContainer.innerHTML = "";

    diseaseForms[disease].forEach(placeholder => {
        let input = document.createElement("input");
        input.type = "text";
        input.placeholder = placeholder;
        input.classList.add("input-field");
        formContainer.appendChild(input);
    });

    document.getElementById("result").innerHTML = "";
    document.getElementById("chart-container").style.display = "none";
}



async function submitForm(event, disease) {
    event.preventDefault();
    let inputs = document.querySelectorAll(".input-field");
    let values = Array.from(inputs).map(input => input.value.trim());

    let response = await fetch(`/${disease.toLowerCase()}_predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ values: values })
    });

    let result = await response.json();
    document.getElementById("result").innerHTML = `<p>Prediction: ${result.prediction}</p>`;

    if (result.probability !== undefined) {
        document.getElementById("chart-container").style.display = "block";
        drawChart(disease, result.probability);
    } else {
        document.getElementById("chart-container").style.display = "none";
    }
}

function drawChart(disease, probability) {
    let ctx = document.getElementById("diseaseChart").getContext("2d");
    
    if (window.myDiseaseChart) {
        window.myDiseaseChart.destroy();
    }

    let labels = ["Risk", "No Risk"];
    let colors = ["#FF5733", "#28A745"];

    window.myDiseaseChart = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: labels,
            datasets: [{
                data: [probability, 100 - probability],
                backgroundColor: colors
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: true,
                    position: "bottom"
                }
            }
        }
    });
}
