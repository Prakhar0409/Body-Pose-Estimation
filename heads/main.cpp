/* 

 DETECT DIFFERENT BODY PARTS USING HAAR-LIKE FEATURES

 AUTHOR: PRATEEK JOSHI

*/

#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

#include <iostream>
#include <stdio.h>

#include "detectBodyParts.h"

using namespace std;
using namespace cv;

#define ENABLE_FACE_DETECTION 1
#define ENABLE_EYE_DETECTION 0
#define ENABLE_EAR_DETECTION 0
#define ENABLE_MOUTH_DETECTION 0
#define ENABLE_NOSE_DETECTION 0
#define ENABLE_SMILE_DETECTION 0
#define ENABLE_LOWERBODY_DETECTION 0
#define ENABLE_UPPERBODY_DETECTION 0
#define ENABLE_FULLBODY_DETECTION 0
#define ENABLE_HAND_DETECTION 1

int main( int argc, const char** argv ){
    VideoCapture capture(0); // capture video from webcam
    Mat frame, prevFrame;
    
    string RAW_PATH = "./raw";
    int save_img_cnt = 0;
    while( true ){
        // Capture the current frame from the input video stream
        capture >> frame;
        
        // Downsample the input frame for faster processing
        float downsampleFactor = 1.0;
        resize(frame, frame, Size(), downsampleFactor, downsampleFactor, INTER_NEAREST);
        
        // Apply the classifier to the frame depending on the enabled macros
        if( !frame.empty() )
        {
            if(ENABLE_FACE_DETECTION) detectFace(frame);
            if(ENABLE_EYE_DETECTION) detectEyes(frame);
            if(ENABLE_EAR_DETECTION) detectEars(frame);
            if(ENABLE_MOUTH_DETECTION) detectMouth(frame);
            if(ENABLE_NOSE_DETECTION) detectNose(frame);
            if(ENABLE_SMILE_DETECTION) detectSmile(frame);
            if(ENABLE_LOWERBODY_DETECTION) detectLowerBody(frame);
            if(ENABLE_UPPERBODY_DETECTION) detectUpperBody(frame);
            if(ENABLE_FULLBODY_DETECTION) detectFullBody(frame);
            if(ENABLE_HAND_DETECTION) detectHand(frame);
        }
        
        else
        {
            cout << "No captured frame. Stopping!" << endl;
            break;
        }
      


    
        char buf[128];
        switch(cv::waitKey(10) & 255){
            case 27:    //exit
                // running = false;
                break;
            case 's':   //save
                sprintf(buf, "%d.jpg", save_img_cnt++);
                string filename = buf;
                filename = RAW_PATH + "/" + filename;
                cout << "saving: " << filename << endl;
                cv::imwrite(filename, frame);      
                break;
        }

        // int c = waitKey(10);
        // if( (char)c == 27 ) { break; }
    }
    
    capture.release();
    
    return 0;
}

