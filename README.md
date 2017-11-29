# Estimating (Upper) Body Pose using Kinematic Tree

Goal is to be able to estimate 3D configuration of human body from a video. 

## Methodolody 

Using inverse kinematics, we want to estimate the joints, given the position and velocity of the end effectors. Since detecting and tracking feet is not straightforward, we only stick to try and estimate the upper body pose. 

heads contains detection of head and palms/fists from any video. These output the position of the end effector. To fit the kinematic model, we use [KDL](http://www.orocos.org/wiki/orocos/kdl-wiki)

To make a tree, simply make chains and attach them as below:
```
KDL::Chain torso_chain;
torso_chain.addSegment(KDL::Segment(KDL::Joint(KDL::Joint::None),
KDL::Frame(Rotation::Rotation(0,0,-1, 1,0,0, 0,-1,0))));
torso_chain.addSegment(KDL::Segment(KDL::Joint(KDL::Joint::RotZ),
KDL::Frame().DH( 0.0320   ,  M_PI/2.0,  0.0   ,  0.0    )));
torso_chain.addSegment(KDL::Segment(KDL::Joint(KDL::Joint::RotZ),
KDL::Frame().DH( 0.0    ,  M_PI/2.0,  0.0   , -M_PI/2.0)));
torso_chain.addSegment(KDL::Segment(KDL::Joint(KDL::Joint::RotZ)));


KDL::Chain right_arm_chain;
right_arm_chain.addSegment(KDL::Segment(KDL::Joint(KDL::Joint::None),
KDL::Frame().DH(-0.0233647,  M_PI/2.0, -0.1433 , -(105.0/180.0)*M_PI)));
right_arm_chain.addSegment(KDL::Segment(KDL::Joint(KDL::Joint::RotZ),
KDL::Frame().DH( 0.0, M_PI/2.0, -0.10774, -M_PI/2.0)));
right_arm_chain.addSegment(KDL::Segment(KDL::Joint(KDL::Joint::RotZ),
KDL::Frame().DH( 0.0, -M_PI/2.0,  0.0   , -M_PI/2.0)));

```
The joint constraints assumed by me are as the ones given in the presentation

## Results

While trying this method on simple kinematics chain, the results were to bizzare to be any hopeful. A simple experiment that I conducted with the chain can be found in experiments folder.



