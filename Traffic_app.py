# from flask import *
# import os
# from werkzeug.utils import secure_filename
# from keras.models import load_model
# import numpy as np
# from PIL import Image

# app = Flask(__name__)

# # Classes of trafic signs
# classes = { 0:'Speed limit (20km/h)',
#             1:'Speed limit (30km/h)',
#             2:'Speed limit (50km/h)',
#             3:'Speed limit (60km/h)',
#             4:'Speed limit (70km/h)',
#             5:'Speed limit (80km/h)',
#             6:'End of speed limit (80km/h)',
#             7:'Speed limit (100km/h)',
#             8:'Speed limit (120km/h)',
#             9:'No passing',
#             10:'No passing veh over 3.5 tons',
#             11:'Right-of-way at intersection',
#             12:'Priority road',
#             13:'Yield',
#             14:'Stop',
#             15:'No vehicles',
#             16:'Vehicle > 3.5 tons prohibited',
#             17:'No entry',
#             18:'General caution',
#             19:'Dangerous curve left',
#             20:'Dangerous curve right',
#             21:'Double curve',
#             22:'Bumpy road',
#             23:'Slippery road',
#             24:'Road narrows on the right',
#             25:'Road work',
#             26:'Traffic signals',
#             27:'Pedestrians',
#             28:'Children crossing',
#             29:'Bicycles crossing',
#             30:'Beware of ice/snow',
#             31:'Wild animals crossing',
#             32:'End speed + passing limits',
#             33:'Turn right ahead',
#             34:'Turn left ahead',
#             35:'Ahead only',
#             36:'Go straight or right',
#             37:'Go straight or left',
#             38:'Keep right',
#             39:'Keep left',
#             40:'Roundabout mandatory',
#             41:'End of no passing',
#             42:'End no passing vehicle > 3.5 tons' }

# def test_on_img(img):
#     data=[]
#     image = Image.open(img)
#     image = image.resize((30,30))
#     data.append(np.array(image))
#     X_test=np.array(data)
#     Y_pred = model.predict(X_test)
#     Y_pred_classes = np.argmax(Y_pred, axis=-1)
#     return image,Y_pred_classes

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         # Get the file from post request
#         f = request.files['file']
#         file_path = secure_filename(f.filename)
#         f.save(file_path)
#         # Make prediction
#         result = test_on_img(file_path)
#         s = [str(i) for i in result]
#         a = int("".join(s))
#         result = "Predicted Traffic🚦Sign is: " +classes[a]
#         os.remove(file_path)
#         return result
#     return None

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import *
import os
from werkzeug.utils import secure_filename
from keras.models import load_model
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the saved model
# Load the saved model
model_path = 'D:\Traffic_Sign_Recognition\Web_App\Traffic_Signs_WebApp\model/TSR.h5'
model = load_model(model_path)

# Classes of trafic signs
classes = { 0:'Speed limit (20km/h) This traffic sign indicates that the speed limit for vehicles is restricted to 20 kilometers per hour (km/h).It imposes a controlled speed limit in the area, typically for safety purposes, requiring vehicles to travel at a reduced pace.',
            1:'Speed limit (30km/h) This traffic sign signifies a maximum speed limit of 30 kilometers per hour (km/h) for vehicles. It mandates a controlled speed within the specified area, usually for safety reasons, necessitating vehicles to adhere to a slower pace.',
            2:'Speed limit (50km/h) This traffic sign denotes a speed limit of 50 kilometers per hour (km/h) for vehicles. It mandates a controlled speed within the designated area, typically prioritizing safety, and requires vehicles to maintain a moderate pace.',
            3:'Speed limit (60km/h) This traffic sign indicates a maximum speed limit of 60 kilometers per hour (km/h) for vehicles. It enforces a controlled speed within the specified area, often emphasizing safety concerns, and necessitates vehicles to maintain a restrained pace.',
            4:'Speed limit (70km/h) This is a speed limit sign indicating the maximum speed on this road is 70kph, as long as the conditions are safe and your vehicle is allowed to drive that fast.',
            5:'Speed limit (80km/h) This traffic sign communicates a speed limit of 80 kilometers per hour (km/h) for vehicles. It mandates a controlled speed within the designated area, typically emphasizing safety, and requires vehicles to maintain a moderate pace within this limit.',
            6:'End of speed limit (80km/h)',
            7:'Speed limit (100km/h)',
            8:'Speed limit (120km/h)',
            9:'No passing The "No Passing" sign signifies that overtaking or passing other vehicles is prohibited in the indicated area. This restriction is usually enforced in areas where visibility is limited, such as curves or hills, or where there is insufficient space for safe passing.',
            10:'No passing veh over 3.5 tons',
            11:'Right-of-way at intersection The "Right-of-Way at Intersection" sign indicates which vehicle has priority when multiple vehicles approach an intersection simultaneously. Typically, it informs drivers about yielding rules, helping to prevent accidents and maintain smooth traffic flow.',
            12:'Priority road The "Priority Road" sign indicates that the road ahead has priority over intersecting roads. It means that vehicles on the priority road have the right of way over vehicles approaching from side roads or junctions. Drivers on intersecting roads must yield to traffic on the priority road, ensuring smooth traffic flow and safety.',
            13:'Yield The "Yield" sign instructs drivers to give the right of way to vehicles approaching from another direction, typically at intersections or merge points. When encountering this sign, motorists must slow down, be prepared to stop if necessary, and yield to oncoming traffic or pedestrians before proceeding. It ensures safe and orderly movement of vehicles through intersections or merging lanes.',
            14:'Stop The "Stop" sign mandates that all vehicles must come to a complete halt at the designated intersection. Drivers must yield the right-of-way to all other vehicles and pedestrians before proceeding. This sign ensures safety at intersections and regulates traffic flow.',
            15:'No vehicles The "No Vehicles" sign indicates that motor vehicles are prohibited from entering the designated area. It usually applies to specific types of vehicles or all motor vehicles and may be accompanied by exceptions or additional signage specifying which types of vehicles are excluded. This sign helps regulate traffic flow, prevent congestion, or safeguard pedestrian zones.',
            16:'Vehicle > 3.5 tons prohibited The "Vehicle > 3.5 tons prohibited" sign indicates that vehicles weighing more than 3.5 tons are not allowed to enter the specified area or use the indicated road. This restriction helps in managing traffic, preventing heavy vehicles from accessing roads not suitable for their weight, and ensuring road safety.',
            17:'No entry The "No Entry" sign prohibits vehicles from entering the designated area or roadway. It indicates that the specified route is off-limits, usually for reasons such as safety, traffic management, or restricted access. Drivers must obey this sign to prevent unauthorized entry and maintain order on the road.',
            18:'General caution',
            19:'Dangerous curve left',
            20:'Dangerous curve right',
            21:'Double curve',
            22:'Bumpy road The "Bumpy Road" sign warns drivers of an uneven or rough road surface ahead. It alerts motorists to reduce speed and exercise caution to safely navigate through the area, minimizing the risk of accidents or damage to vehicles.',
            23:'Slippery road',
            24:'Road narrows on the right The "Road Narrows on the Right" sign indicates that the width of the road will decrease on the right side ahead. Drivers should be prepared for a narrower roadway and potentially adjust their position accordingly to ensure safe passage, especially when encountering oncoming traffic or obstacles.',
            25:'Road work The "Road Work" sign alerts drivers to ongoing construction or maintenance activities on the road ahead. It warns motorists to be prepared for potential changes in road conditions, such as lane closures, reduced speed limits, or temporary detours. Drivers should exercise caution, follow any posted instructions, and be mindful of construction workers and equipment in the area.',
            26:'Traffic signals The term "Traffic Signals" refers to the system of lights (red, yellow, green) and sometimes arrows, installed at intersections or roadways to regulate the flow of traffic. These signals dictate when vehicles should stop, yield, or proceed, helping to manage traffic efficiently and prevent accidents. Drivers must obey traffic signals to ensure safe and orderly movement on the road.',
            27:'Pedestrians The term "Pedestrians" refers to individuals who are traveling on foot, such as walking or running, along sidewalks, crosswalks, or other designated pedestrian areas. Pedestrians have the right of way at crosswalks and intersections, and drivers are required to yield to them to ensure their safety. Pedestrian crossings and signs are used to indicate where pedestrians can safely cross roads and where drivers should be particularly cautious.',
            28:'Children crossing The "Children Crossing" sign alerts drivers to the presence of a designated area where children are likely to cross the road, such as near schools, parks, or residential areas. It serves as a warning for motorists to be extra cautious and vigilant, especially regarding the safety of young pedestrians who may be less predictable or visible on the road. Drivers should reduce their speed, be prepared to stop, and watch for children crossing the street when they see this sign.',
            29:'Bicycles crossing The "Bicycles Crossing" sign alerts drivers to the presence of a designated area where bicyclists are likely to cross the road. It serves as a warning for motorists to be cautious and watch out for cyclists who may be crossing the street. Drivers should reduce their speed, be prepared to stop, and give cyclists the right of way when they see this sign to ensure their safety and prevent accidents.',
            30:'Beware of ice/snow The "Beware of Ice/Snow" sign warns drivers of hazardous road conditions caused by ice or snow. It serves as an alert for motorists to exercise caution and adjust their driving behavior accordingly when encountering slippery or icy road surfaces due to freezing temperatures or snowfall. Drivers should reduce their speed, increase their following distance, and avoid sudden maneuvers to prevent accidents and maintain control of their vehicle in these conditions.',
            31:'Wild animals crossing',
            32:'End speed + passing limits The "End of Speed Limit and Passing Restrictions" sign indicates the termination of any previously posted speed limit or passing restrictions. It informs drivers that they are no longer bound by the speed limit or passing rules that were in effect in the preceding area. Motorists should resume driving according to the standard speed limits and passing regulations applicable to the road they are entering.',
            33:'Turn right ahead The "Turn Right Ahead" sign indicates to drivers that they will encounter a right turn shortly ahead. It serves as an advance warning, prompting motorists to prepare for the upcoming maneuver by signaling appropriately and positioning their vehicle correctly to make a safe and timely turn.',
            34:'Turn left ahead The "Turn Left Ahead" sign informs drivers that there is a left turn coming up shortly ahead. It serves as an advance notice, allowing motorists to prepare for the upcoming turn by signaling appropriately and positioning their vehicle correctly to safely navigate the leftward maneuver.',
            35:'Ahead only The "Ahead Only" sign indicates that the road ahead leads straight and does not offer any other options such as turns or diverging paths. It directs drivers to continue traveling straight ahead without making any turns or deviations from the current roadway. Motorists should follow this sign to stay on the designated route and maintain safe navigation through the area.',
            36:'Go straight or right The "Go Straight or Right" sign indicates to drivers that they have the option to either continue straight ahead or make a right turn at the upcoming intersection or junction. It allows motorists to choose their desired direction based on their intended route. Drivers should pay attention to road markings and other signs to ensure they choose the appropriate lane for their chosen direction.',
            37:'Go straight or left The "Go Straight or Left" sign indicates to drivers that they have the option to either continue straight ahead or make a left turn at the upcoming intersection or junction. It offers motorists the choice to proceed in either direction, depending on their intended route. Drivers should pay attention to road markings and other signs to ensure they choose the appropriate lane for their desired direction.',
            38:'Keep right The "Keep Right" sign instructs drivers to stay to the right side of the road or roadway. It typically indicates that there is an obstruction or hazard ahead, such as road work, a narrowed lane, or a merging lane on the left. Motorists should obey this sign by maintaining their position on the right side of the road, ensuring smooth traffic flow and safe passage through the designated area.',
            39:'Keep left The "Keep Left" sign instructs drivers to stay to the left side of the road or roadway. It typically indicates that there is an obstruction or hazard ahead, such as road work, a narrowed lane, or a merging lane on the right. Motorists should obey this sign by maintaining their position on the left side of the road, ensuring smooth traffic flow and safe passage through the designated area.',
            40:'Roundabout mandatory',
            41:'End of no passing',
            42:'End no passing vehicle > 3.5 tons' }

def test_on_img(img, model):
    data=[]
    image = Image.open(img)
    image = image.resize((30,30))
    data.append(np.array(image))
    X_test=np.array(data)
    Y_pred = model.predict(X_test)
    Y_pred_classes = np.argmax(Y_pred, axis=-1)
    return image,Y_pred_classes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)
        # Make prediction
        result = test_on_img(file_path, model)
        s = [str(i) for i in result[1]]
        a = int("".join(s))
        result = "Predicted Traffic🚦Sign is: " +classes[a]
        os.remove(file_path)
        return result
    return None

if __name__ == '__main__':
    app.run(debug=True)