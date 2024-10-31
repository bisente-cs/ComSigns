import os
import base64
from flask import Flask, request, jsonify, render_template, Response
from four_inference_classifier import GestureClassifier
import cv2
import pickle
import mediapipe as mp
import numpy as np
from labels_dict import labels_dict
from gtts import gTTS
from googletrans import Translator

app = Flask(__name__, template_folder='./Template', static_folder='static')
TEMPLATES_AUTO_RELOAD = True
gesture_classifier = GestureClassifier()
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FPS, 60)  # Set frame rate to 60 FPS
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Adjust width
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Adjust height
predicted_character_global = ""



# Text-to-Speech
def detect_language(text):
    translator = Translator()
    detected_lang = translator.detect(text).lang
    return detected_lang


@app.route("/")
def index():
    return render_template("main.html")

@app.route('/detector')
def detector():
    return render_template('detector.html')

@app.route('/texttospeech', methods=['POST'])
def text_to_speech():
    # Get the text from the request body
    data = request.json
    text = data.get('text', '')
    
    # Generate speech
    tts = gTTS(text=text, lang='en', slow=False)  # Set slow to False for normal speed
    tts.save('output.mp3')  # Save to an mp3 file
    
    # Read the temporary file and convert it to base64
    with open('output.mp3', 'rb') as file:
        audio_bytes = file.read()
        audio_base64 = base64.b64encode(audio_bytes).decode()

    # Optionally, delete the temporary file
    os.remove('output.mp3')

    # Return the audio content as base64 encoded string
    return jsonify({'audio_base64': audio_base64})

@app.route('/aboutus')
def aboutus():
    return render_template('about-us.html')

@app.route('/contactus')
def contactus():
    return render_template('contact-us.html')

@app.route('/beginner')
def beginner():
    return render_template('bgnr-category.html')

@app.route('/intermediate')
def intermediate():
    return render_template('inter-category.html')

@app.route('/advanced')
def advanced():
    return render_template('adv-category.html')

#BEGINNER CONTENT

@app.route('/a')
def a():
    return render_template('1_bgnr_a.html')

@app.route('/b')
def b():
    return render_template('1_bgnr_b.html')

@app.route('/c')
def c():
    return render_template('1_bgnr_c.html')

@app.route('/d')
def d():
    return render_template('1_bgnr_d.html')

@app.route('/e')
def e():
    return render_template('1_bgnr_e.html')

@app.route('/f')
def f():
    return render_template('1_bgnr_f.html')

@app.route('/g')
def g():
    return render_template('1_bgnr_g.html')

@app.route('/h')
def h():
    return render_template('1_bgnr_h.html')

@app.route('/i')
def i():
    return render_template('1_bgnr_i.html')

@app.route('/j')
def j():
    return render_template('1_bgnr_j.html')

@app.route('/k')
def k():
    return render_template('1_bgnr_k.html')

@app.route('/l')
def l():
    return render_template('1_bgnr_l.html')

@app.route('/m')
def m():
    return render_template('1_bgnr_m.html')

@app.route('/n')
def n():
    return render_template('1_bgnr_n.html')

@app.route('/o')
def o():
    return render_template('1_bgnr_o.html')

@app.route('/p')
def p():
    return render_template('1_bgnr_p.html')

@app.route('/q')
def q():
    return render_template('1_bgnr_q.html')

@app.route('/r')
def r():
    return render_template('1_bgnr_r.html')

@app.route('/s')
def s():
    return render_template('1_bgnr_s.html')

@app.route('/t')
def t():
    return render_template('1_bgnr_t.html')

@app.route('/u')
def u():
    return render_template('1_bgnr_u.html')

@app.route('/v')
def v():
    return render_template('1_bgnr_v.html')

@app.route('/w')
def w():
    return render_template('1_bgnr_w.html')

@app.route('/x')
def x():
    return render_template('1_bgnr_x.html')

@app.route('/y')
def y():
    return render_template('1_bgnr_y.html')

@app.route('/z')
def z():
    return render_template('1_bgnr_z.html')

@app.route('/1')
def one():
    return render_template('2_bgnr_1.html')

@app.route('/2')
def two():
    return render_template('2_bgnr_2.html')

@app.route('/3')
def three():
    return render_template('2_bgnr_3.html')

@app.route('/4')
def four():
    return render_template('2_bgnr_4.html')

@app.route('/5')
def five():
    return render_template('2_bgnr_5.html')

@app.route('/6')
def six():
    return render_template('2_bgnr_6.html')

@app.route('/7')
def seven():
    return render_template('2_bgnr_7.html')

@app.route('/8')
def eight():
    return render_template('2_bgnr_8.html')

@app.route('/9')
def nine():
    return render_template('2_bgnr_9.html')

@app.route('/10')
def ten():
    return render_template('2_bgnr_10.html')

@app.route('/bp1')
def bp1():
    return render_template('3_bgnr_bp1.html')

@app.route('/bp2')
def bp2():
    return render_template('3_bgnr_bp2.html')

@app.route('/bp3')
def bp3():
    return render_template('3_bgnr_bp3.html')

@app.route('/bp4')
def bp4():
    return render_template('3_bgnr_bp4.html')

@app.route('/bp5')
def bp5():
    return render_template('3_bgnr_bp5.html')

@app.route('/bp6')
def bp6():
    return render_template('3_bgnr_bp6.html')

@app.route('/bp7')
def bp7():
    return render_template('3_bgnr_bp7.html')

@app.route('/bp8')
def bp8():
    return render_template('3_bgnr_bp8.html')

@app.route('/bp9')
def bp9():
    return render_template('3_bgnr_bp9.html')

@app.route('/bp10')
def bp10():
    return render_template('3_bgnr_bp10.html')

@app.route('/bp11')
def bp11():
    return render_template('3_bgnr_bp11.html')

@app.route('/bp12')
def bp12():
    return render_template('3_bgnr_bp12.html')

@app.route('/bp13')
def bp13():
    return render_template('3_bgnr_bp13.html')

@app.route('/bp14')
def bp14():
    return render_template('3_bgnr_bp14.html')

@app.route('/bp15')
def bp15():
    return render_template('3_bgnr_bp15.html')

@app.route('/bp16')
def bp16():
    return render_template('3_bgnr_bp16.html')

@app.route('/bp17')
def bp17():
    return render_template('3_bgnr_bp17.html')

@app.route('/bp18')
def bp18():
    return render_template('3_bgnr_bp18.html')

@app.route('/bp19')
def bp19():
    return render_template('3_bgnr_bp19.html')

@app.route('/bp20')
def bp20():
    return render_template('3_bgnr_bp20.html')

@app.route('/bp21')
def bp21():
    return render_template('3_bgnr_bp21.html')

@app.route('/bp22')
def bp22():
    return render_template('3_bgnr_bp22.html')

@app.route('/bp23')
def bp23():
    return render_template('3_bgnr_bp23.html')

@app.route('/bp24')
def bp24():
    return render_template('3_bgnr_bp24.html')

@app.route('/bp25')
def bp25():
    return render_template('3_bgnr_bp25.html')

@app.route('/bp26')
def bp26():
    return render_template('3_bgnr_bp26.html')

@app.route('/bp27')
def bp27():
    return render_template('3_bgnr_bp27.html')

@app.route('/bp28')
def bp28():
    return render_template('3_bgnr_bp28.html')

@app.route('/bp29')
def bp29():
    return render_template('3_bgnr_bp29.html')

@app.route('/bp30')
def bp30():
    return render_template('3_bgnr_bp30.html')

@app.route('/bp31')
def bp31():
    return render_template('3_bgnr_bp31.html')

@app.route('/bp32')
def bp32():
    return render_template('3_bgnr_bp32.html')

@app.route('/bp33')
def bp33():
    return render_template('3_bgnr_bp33.html')

@app.route('/bp34')
def bp34():
    return render_template('3_bgnr_bp34.html')

@app.route('/bp35')
def bp35():
    return render_template('3_bgnr_bp35.html')

@app.route('/bp36')
def bp36():
    return render_template('3_bgnr_bp36.html')

@app.route('/bp37')
def bp37():
    return render_template('3_bgnr_bp37.html')

@app.route('/bp38')
def bp38():
    return render_template('3_bgnr_bp38.html')

@app.route('/bp39')
def bp39():
    return render_template('3_bgnr_bp39.html')

@app.route('/bp40')
def bp40():
    return render_template('3_bgnr_bp40.html')

@app.route('/bp41')
def bp41():
    return render_template('3_bgnr_bp41.html')

@app.route('/bp42')
def bp42():
    return render_template('3_bgnr_bp42.html')

@app.route('/bp43')
def bp43():
    return render_template('3_bgnr_bp43.html')

@app.route('/bp44')
def bp44():
    return render_template('3_bgnr_bp44.html')

@app.route('/bp45')
def bp45():
    return render_template('3_bgnr_bp45.html')

@app.route('/bp46')
def bp46():
    return render_template('3_bgnr_bp46.html')

@app.route('/bp47')
def bp47():
    return render_template('3_bgnr_bp47.html')

@app.route('/bp48')
def bp48():
    return render_template('3_bgnr_bp48.html')

@app.route('/bp49')
def bp49():
    return render_template('3_bgnr_bp49.html')

@app.route('/bp50')
def bp50():
    return render_template('3_bgnr_bp50.html')

@app.route('/bp51')
def bp51():
    return render_template('3_bgnr_bp51.html')

@app.route('/bp52')
def bp52():
    return render_template('3_bgnr_bp52.html')

@app.route('/bp53')
def bp53():
    return render_template('3_bgnr_bp53.html')

@app.route('/bp54')
def bp54():
    return render_template('3_bgnr_bp54.html')

@app.route('/bp55')
def bp55():
    return render_template('3_bgnr_bp55.html')

@app.route('/bp56')
def bp56():
    return render_template('3_bgnr_bp56.html')

@app.route('/bp57')
def bp57():
    return render_template('3_bgnr_bp57.html')

@app.route('/bp58')
def bp58():
    return render_template('3_bgnr_bp58.html')

@app.route('/bp59')
def bp59():
    return render_template('3_bgnr_bp59.html')

@app.route('/bp60')
def bp60():
    return render_template('3_bgnr_bp60.html')

@app.route('/bp61')
def bp61():
    return render_template('3_bgnr_bp61.html')

@app.route('/bp62')
def bp62():
    return render_template('3_bgnr_bp62.html')

@app.route('/bp63')
def bp63():
    return render_template('3_bgnr_bp63.html')

#INTERMEDIATE

@app.route('/f1')
def f1(): 
    return render_template('1_inter_f1.html')

@app.route('/f2')
def f2(): 
    return render_template('1_inter_f2.html')

@app.route('/f3')
def f3(): 
    return render_template('1_inter_f3.html')

@app.route('/f4')
def f4(): 
    return render_template('1_inter_f4.html')

@app.route('/f5')
def f5(): 
    return render_template('1_inter_f5.html')

@app.route('/f6')
def f6(): 
    return render_template('1_inter_f6.html')

@app.route('/f7')
def f7(): 
    return render_template('1_inter_f7.html')

@app.route('/f8')
def f8(): 
    return render_template('1_inter_f8.html')

@app.route('/f9')
def f9(): 
    return render_template('1_inter_f9.html')

@app.route('/f10')
def f10():
    return render_template('1_inter_f10.html')

@app.route('/f11')
def f11():
    return render_template('1_inter_f11.html')

@app.route('/f12')
def f12():
    return render_template('1_inter_f12.html')

@app.route('/f13')
def f13():
    return render_template('1_inter_f13.html')

@app.route('/f14')
def f14():
    return render_template('1_inter_f14.html')

@app.route('/f15')
def f15():
    return render_template('1_inter_f15.html')

@app.route('/f16')
def f16():
    return render_template('1_inter_f16.html')

@app.route('/f17')
def f17():
    return render_template('1_inter_f17.html')

@app.route('/f18')
def f18():
    return render_template('1_inter_f18.html')

@app.route('/f19')
def f19():
    return render_template('1_inter_f19.html')

@app.route('/f20')
def f20():
    return render_template('1_inter_f20.html')

@app.route('/f21')
def f21():
    return render_template('1_inter_f21.html')

@app.route('/f22')
def f22():
    return render_template('1_inter_f22.html')

@app.route('/e1')
def e1():
    return render_template('2_inter_e1.html')

@app.route('/e2')
def e2():
    return render_template('2_inter_e2.html')

@app.route('/e3')
def e3():
    return render_template('2_inter_e3.html')

@app.route('/e4')
def e4():
    return render_template('2_inter_e4.html')

@app.route('/e5')
def e5():
    return render_template('2_inter_e5.html')

@app.route('/e6')
def e6():
    return render_template('2_inter_e6.html')

@app.route('/e7')
def e7():
    return render_template('2_inter_e7.html')

@app.route('/e8')
def e8():
    return render_template('2_inter_e8.html')

@app.route('/e9')
def e9():
    return render_template('2_inter_e9.html')

@app.route('/e10')
def e10():
    return render_template('2_inter_e10.html')

@app.route('/e11')
def e11():
    return render_template('2_inter_e11.html')

@app.route('/e12')
def e12():
    return render_template('2_inter_e12.html')

@app.route('/e13')
def e13():
    return render_template('2_inter_e13.html')

@app.route('/e14')
def e14():
    return render_template('2_inter_e14.html')

@app.route('/e15')
def e15():
    return render_template('2_inter_e15.html')

@app.route('/dp1')
def dp1():                          
    return render_template('3_inter_dp1.html')

@app.route('/dp2')
def dp2():                          
    return render_template('3_inter_dp2.html')

@app.route('/dp3')
def dp3():                          
    return render_template('3_inter_dp3.html')

@app.route('/dp4')
def dp4():                          
    return render_template('3_inter_dp4.html')

@app.route('/dp5')
def dp5():                          
    return render_template('3_inter_dp5.html')

@app.route('/dp6')
def dp6():                          
    return render_template('3_inter_dp6.html')

@app.route('/dp7')
def dp7():                          
    return render_template('3_inter_dp7.html')

@app.route('/dp8')
def dp8():                          
    return render_template('3_inter_dp8.html')

@app.route('/dp9')
def dp9():                          
    return render_template('3_inter_dp9.html')

@app.route('/dp10')
def dp10():                          
    return render_template('3_inter_dp10.html')

@app.route('/dp11')
def dp11():                          
    return render_template('3_inter_dp11.html')

@app.route('/dp12')
def dp12():                          
    return render_template('3_inter_dp12.html')

@app.route('/dp13')
def dp13():                          
    return render_template('3_inter_dp13.html')

@app.route('/dp14')
def dp14():                          
    return render_template('3_inter_dp14.html')

@app.route('/dp15')
def dp15():                          
    return render_template('3_inter_dp15.html')

@app.route('/dp16')
def dp16():                          
    return render_template('3_inter_dp16.html')

@app.route('/dp17')
def dp17():                          
    return render_template('3_inter_dp17.html')

@app.route('/dp18')
def dp18():                          
    return render_template('3_inter_dp18.html')

@app.route('/dp19')
def dp19():                          
    return render_template('3_inter_dp19.html')

@app.route('/dp20')
def dp20():                          
    return render_template('3_inter_dp20.html')

@app.route('/dp21')
def dp21():                          
    return render_template('3_inter_dp21.html')

@app.route('/dp22')
def dp22():                          
    return render_template('3_inter_dp22.html')

@app.route('/dp23')
def dp23():                          
    return render_template('3_inter_dp23.html')

@app.route('/dp24')
def dp24():                          
    return render_template('3_inter_dp24.html')

@app.route('/dp25')
def dp25():                          
    return render_template('3_inter_dp25.html')

@app.route('/dp26')
def dp26():                          
    return render_template('3_inter_dp26.html')

@app.route('/dp27')
def dp27():                          
    return render_template('3_inter_dp27.html')

@app.route('/dp28')
def dp28():                          
    return render_template('3_inter_dp28.html')

@app.route('/dp29')
def dp29():                          
    return render_template('3_inter_dp29.html')

@app.route('/dp30')
def dp30():                          
    return render_template('3_inter_dp30.html')

@app.route('/dp31')
def dp31():                          
    return render_template('3_inter_dp31.html')

@app.route('/dp32')
def dp32():                          
    return render_template('3_inter_dp32.html')

@app.route('/dp33')
def dp33():                          
    return render_template('3_inter_dp33.html')

@app.route('/dp34')
def dp34():                          
    return render_template('3_inter_dp34.html')

@app.route('/dp35')
def dp35():                          
    return render_template('3_inter_dp35.html')

@app.route('/dp36')
def dp36():                          
    return render_template('3_inter_dp36.html')

#ADVANCE
@app.route('/fpv1')
def fpv1():                         
    return render_template('1_adv_fpv1.html')

@app.route('/fpv2')
def fpv2():                         
    return render_template('1_adv_fpv2.html')

@app.route('/fpv3')
def fpv3():                         
    return render_template('1_adv_fpv3.html')

@app.route('/fpv4')
def fpv4():                         
    return render_template('1_adv_fpv4.html')

@app.route('/fpv5')
def fpv5():                         
    return render_template('1_adv_fpv5.html')

@app.route('/fpv6')
def fpv6():                         
    return render_template('1_adv_fpv6.html')

@app.route('/fpv7')
def fpv7():                         
    return render_template('1_adv_fpv7.html')

@app.route('/fpv8')
def fpv8():                         
    return render_template('1_adv_fpv8.html')

@app.route('/fpv9')
def fpv9():                         
    return render_template('1_adv_fpv9.html')

@app.route('/fpv10')
def fpv10():                         
    return render_template('1_adv_fpv10.html')

@app.route('/fpv11')
def fpv11():                         
    return render_template('1_adv_fpv11.html')

@app.route('/fpv12')
def fpv12():                         
    return render_template('1_adv_fpv12.html')

@app.route('/fpv13')
def fpv13():                         
    return render_template('1_adv_fpv13.html')

@app.route('/fpv14')
def fpv14():                         
    return render_template('1_adv_fpv14.html')

@app.route('/fpv15')
def fpv15():                         
    return render_template('1_adv_fpv15.html')

@app.route('/fpv16')
def fpv16():                         
    return render_template('1_adv_fpv16.html')

@app.route('/fpv17')
def fpv17():                         
    return render_template('1_adv_fpv17.html')

@app.route('/fpv18')
def fpv18():                         
    return render_template('1_adv_fpv18.html')

@app.route('/bs1')
def bs1():                          
    return render_template('2_adv_bs1.html')

@app.route('/bs2')
def bs2():                          
    return render_template('2_adv_bs2.html')

@app.route('/bs3')
def bs3():                          
    return render_template('2_adv_bs3.html')

@app.route('/bs4')
def bs4():                          
    return render_template('2_adv_bs4.html')

@app.route('/bs5')
def bs5():                          
    return render_template('2_adv_bs5.html')

@app.route('/bs6')
def bs6():                          
    return render_template('2_adv_bs6.html')

@app.route('/bs7')
def bs7():                          
    return render_template('2_adv_bs7.html')

@app.route('/bs8')
def bs8():                          
    return render_template('2_adv_bs8.html')

@app.route('/bs9')
def bs9():                          
    return render_template('2_adv_bs9.html')

@app.route('/bs10')
def bs10():                          
    return render_template('2_adv_bs10.html')

@app.route('/bs11')
def bs11():                          
    return render_template('2_adv_bs11.html')

@app.route('/bs12')
def bs12():                          
    return render_template('2_adv_bs12.html')

@app.route('/bs13')
def bs13():                          
    return render_template('2_adv_bs13.html')

@app.route('/bs14')
def bs14():                          
    return render_template('2_adv_bs14.html')

@app.route('/bs15')
def bs15():                          
    return render_template('2_adv_bs15.html')


def generate_frames():
    global predicted_character_global
    while True:

        success, frame = camera.read()
        if not success:
            break

        # Perform gesture classification using your GestureClassifier
        predicted_character, frame = gesture_classifier.predict(frame)
        predicted_character_global = predicted_character 

        # Convert the frame to JPEG format
        ret, jpeg = cv2.imencode(".jpg", frame)
        frame_bytes = jpeg.tobytes()

        # Yield the frame for streaming
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n\r\n"
        )
        
@app.route('/get_predicted_character')
def get_predicted_character():
    global predicted_character_global
    return jsonify({'predicted_character': predicted_character_global})
        

@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
