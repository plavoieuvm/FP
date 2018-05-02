import constants_pro as c
import math
import random

class ROBOT:

    def __init__(self, sim, wts):

        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim, wts)


        del self.O
        # del self.J
        # del self.S
        del self.SN
        del self.MN

    def send_objects(self, sim):

        # self.light = sim.send_box(x=4, y=0, z=1, length=.25, width=.25, height=.25)
        # sim.send_light_source(body_id=self.light)

        # for i in range(0, 25):
        #
        #     sim.send_box(x=1 + (i/100), y=0, z=.2, length=10, width=.01, height=.01, collision_group='env')
        #


        #self.box = sim.send_box(x=-0.15, y=0, z=c.L2 + c.R2 + .05 + .025, length=0.05, width=.05, height=.05, collision_group='env')


        # RAMP
        self.OR = sim.send_box(x=1.6, y=0, z=.25, length=10.5, width=.01, height=2.7, r1=6, collision_group='env')

        # LOG
        # self.log = sim.send_cylinder(x=1.5, y=0, z=.3, length=10.5, radius=.018, r1=0, r2=1, r3=0, r=1.0, g=0, b=0, collision_group='env')


        # Walker
        self.leg1 = sim.send_cylinder(x=0, y=-c.L2/2, z=(c.L2/2) + c.R2, length=c.L2, radius=c.R2, collision_group='rob')
        self.leg2 = sim.send_cylinder(x=0, y=c.L2/2, z=(c.L2/2) + c.R2, length=c.L2, radius=c.R2, collision_group='rob')

        self.leg3 = sim.send_cylinder(x=-.3, y=-c.L2/2, z=(c.L2/2) + c.R2, length=c.L2, radius=c.R2, collision_group='rob')
        self.leg4 = sim.send_cylinder(x=-.3, y=c.L2/2, z=(c.L2/2) + c.R2, length=c.L2, radius=c.R2, collision_group='rob')


        self.foot1 = sim.send_box(x=.1/2, y=-c.L2/2, z=.05/2, length=.05, width=.1, height=.05, collision_group='rob')
        self.foot2 = sim.send_box(x=.1/2, y=c.L2/2, z=.05/2, length=.05, width=.1, height=.05, collision_group='rob')

        self.foot3 = sim.send_box(x=-.3 - c.R2, y=-c.L2/2, z=.05/2, length=.05, width=.1, height=.05, collision_group='rob')
        self.foot4 = sim.send_box(x=-.3 - c.R2, y=c.L2/2, z=.05/2, length=.05, width=.1, height=.05, collision_group='rob')


        self.body = sim.send_box(x=-.15, y=0, z=c.L2 + c.R2, length=c.L2 + c.R2, width=c.L2+c.R2, height=.1, collision_group='rob')

        self.O = {}

        self.O[0] = self.leg1
        self.O[1] = self.leg2
        self.O[2] = self.foot1
        self.O[3] = self.foot2
        self.O[4] = self.body
        # self.O[5] = self.OR
        self.O[6] = self.leg3
        self.O[7] = self.leg4
        self.O[8] = self.foot3
        self.O[9] = self.foot4

        # self.leg3 = sim.send_cylinder(x=c.L2/2, y=-c.L2/2, z=c.L2 + c.R2, length=c.L2, radius=c.R2, r1=1, r2=0, r3=0, r=0, g=1.0, b=0, collision_group='rob')
        # self.leg4 = sim.send_cylinder(x=c.L2/2, y=c.L2/2, z=c.L2 + c.R2, length=c.L2, radius=c.R2, r1=1, r2=0, r3=0, r=0, g=1.0, b=0, collision_group='rob')
        #
        # self.leg5 = sim.send_cylinder(x=c.L2, y=0, z=c.L2 + c.R2, length=c.L2, radius=c.R2, r1=0, r2=1, r3=0, r=0, g=1.0, b=0, collision_group='rob')

        # self.body = sim.send_box(x=0, y=0, z=0.7, length=.5, width=.5, height=.5)


        #
        # self.O0 = sim.send_box(x=0, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2 * c.R, r=0.5, g=0.5, b=0.5, collision_group='rob')
        # self.O1 = sim.send_cylinder(x=0, y=c.L, z=c.L + c.R, length=c.L, radius=c.R, r1=0, r2=1, r3=0, r=1.0, g=0, b=0, collision_group='rob')
        # self.O2 = sim.send_cylinder(x=c.L, y=0, z=c.L + c.R, length=c.L, radius=c.R, r1=1, r2=0, r3=0, r=0, g=1.0, b=0, collision_group='rob')
        # self.O3 = sim.send_cylinder(x=0, y=0-c.L, z=c.L + c.R, length=c.L, radius=c.R, r1=0, r2=1, r3=0, r=0, g=0, b=1, collision_group='rob')
        # self.O4 = sim.send_cylinder(x=0-c.L, y=0, z=c.L + c.R, length=c.L, radius=c.R, r1=1, r2=0, r3=0, r=1, g=0, b=1, collision_group='rob')
        #
        # self.O5 = sim.send_cylinder(x=0, y=c.L + (c.L/2), z=(c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1,
        #                             r=1, g=0, b=0, collision_group='rob')
        # self.O6 = sim.send_cylinder(x=c.L + (c.L/2), y=0, z=(c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1,
        #                             r=0, g=1, b=0, collision_group='rob')
        # self.O7 = sim.send_cylinder(x=0, y=-(c.L + (c.L/2)), z=(c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1,
        #                             r=0, g=0, b=1, collision_group='rob')
        # self.O8 = sim.send_cylinder(x=-(c.L + (c.L/2)), y=0, z=(c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1,
        #                             r=1, g=0, b=1, collision_group='rob')

        self.CM = sim.assign_collision('env', 'rob')
        self.CM2 = sim.assign_collision('rob', 'rob')
        self.CM1 = sim.assign_collision('env', 'env')


        # self.whiteObject = sim.send_cylinder(x=0, y=0, z=0.6, length=1.0, radius=0.1)
        #
        # self.redObject = sim.send_cylinder(x=0, y=0.5, z=1.1, r1=0, r2=1, r3=0, length=1.0, radius=0.1, r=1, g=0, b=0)

    def send_joints(self, sim):

        self.JW = sim.send_fixed_joint(first_body_id=sim.WORLD, second_body_id=self.OR)


        # self.JW = sim.send_fixed_joint(first_body_id=sim.WORLD, second_body_id=self.light)


        # self.world_joint = sim.send_hinge_joint(first_body_id=sim.WORLD,
        #                                    second_body_id=self.OR,
        #                                    x=1, y=0.0, z=2.5,
        #                                    n1=0, n2=1, n3=0,
        #
        #
        #                             lo=-math.pi, hi=math.pi)

        self.jointfoot1 = sim.send_hinge_joint(first_body_id=self.leg1, second_body_id=self.foot1, x=0, y=-c.L2/2,
                                       z=.05/2, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        self.jointfoot2 = sim.send_hinge_joint(first_body_id=self.leg2, second_body_id=self.foot2, x=0, y=c.L2/2,
                                       z=.05/2, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)




        self.jointfoot3 = sim.send_hinge_joint(first_body_id=self.leg3, second_body_id=self.foot3, x=-.3 - c.R2, y=-c.L2/2,
                                       z=.05/2, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)


        self.jointfoot4 = sim.send_hinge_joint(first_body_id=self.leg4, second_body_id=self.foot4, x=-.3 - c.R2, y=c.L2/2,
                                       z=.05/2, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)


        self.jointbody1 = sim.send_hinge_joint(first_body_id=self.leg1, second_body_id=self.body, x=0, y=-c.L2/2,
                                       z=c.L2 + c.R2, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        self.jointbody2 = sim.send_hinge_joint(first_body_id=self.leg2, second_body_id=self.body, x=0, y=c.L2/2,
                                       z=c.L2 + c.R2, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        self.jointbody3 = sim.send_hinge_joint(first_body_id=self.leg3, second_body_id=self.body, x=-.3 - c.R2, y=-c.L2/2,
                                       z=c.L2 + c.R2, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        self.jointbody4 = sim.send_hinge_joint(first_body_id=self.leg4, second_body_id=self.body, x=-.3 - c.R2, y=c.L2/2,
                                       z=c.L2 + c.R2, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)



        self.J={}
        self.J[0] = self.jointfoot1
        self.J[1] = self.jointfoot2

        self.J[2] = self.jointbody1
        self.J[3] = self.jointbody2
        self.J[4] = self.jointbody3
        self.J[5] = self.jointbody4

        self.J[6] = self.jointfoot3
        self.J[7] = self.jointfoot4





        # self.joint1 = sim.send_hinge_joint(first_body_id=self.leg1, second_body_id=self.leg3, x=0, y=-0.2,
        #                                z=c.L2 + c.R2, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.joint2 = sim.send_hinge_joint(first_body_id=self.leg2, second_body_id=self.leg4, x=0, y=0.2,
        #                                z=c.L2 + c.R2, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        # self.joint3 = sim.send_fixed_joint(first_body_id=self.leg3, second_body_id=self.leg5)
        # self.joint4 = sim.send_fixed_joint(first_body_id=self.leg4, second_body_id=self.leg5)


        # self.J0 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O1, x=0, y=c.L/2,
        #                                z=c.L+c.R, n1=-1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J1 = sim.send_hinge_joint(first_body_id=self.O1, second_body_id=self.O5, x=0, y=c.L + (c.L/2),
        #                                z=c.L + c.R, n1=-1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J2 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O2, x=c.L/2, y=0,
        #                                z=c.L + c.R, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J3 = sim.send_hinge_joint(first_body_id=self.O2, second_body_id=self.O6, x=c.L + (c.L/2), y=0,
        #                                z=c.L + c.R, n1=0, n2=1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J4 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O3, x=0, y=-(c.L/2),
        #                                z=c.L + c.R, n1=1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J5 = sim.send_hinge_joint(first_body_id=self.O3, second_body_id=self.O7, x=0, y=-(c.L + (c.L/2)),
        #                                z=c.L + c.R, n1=1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J6 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O4, x=-(c.L/2), y=0,
        #                                z=c.L + c.R, n1=0, n2=-1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)
        #
        # self.J7 = sim.send_hinge_joint(first_body_id=self.O4, second_body_id=self.O8, x=-(c.L + (c.L/2)), y=0,
        #                                z=c.L + c.R, n1=0, n2=-1, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

        # self.joint = sim.send_hinge_joint(first_body_id=self.whiteObject, second_body_id=self.redObject, x=0, y=0,
        #                                   z=1.1, n1=-1, n2=0, n3=0, lo=-3.14159 / 2, hi=3.14159 / 2)

    def send_sensors(self, sim):

        self.touch1 = sim.send_touch_sensor(body_id=self.foot1)
        self.touch2 = sim.send_touch_sensor(body_id=self.foot2)
        self.touch3 = sim.send_touch_sensor(body_id=self.foot3)
        self.touch4 = sim.send_touch_sensor(body_id=self.foot4)

        self.position = sim.send_position_sensor(body_id=self.body)
        self.veS = sim.send_vestibular_sensor(body_id=self.body)


        self.SN = {}
        self.SN[0] = self.touch1
        self.SN[1] = self.touch2
        self.SN[2] = self.touch3
        self.SN[3] = self.touch4




        # self.T0 = sim.send_touch_sensor(body_id=self.O1)
        # self.T1 = sim.send_touch_sensor(body_id=self.O6)
        # self.T2 = sim.send_touch_sensor(body_id=self.O7)
        # self.T3 = sim.send_touch_sensor(body_id=self.O8)


        # self.L4 = sim.send_light_sensor(body_id=self.L4)


    def send_neurons(self, sim):

        self.cpg = sim.send_function_neuron()
        self.cpg2 = sim.send_function_neuron()

        self.neuron1 = sim.send_sensor_neuron(sensor_id=self.touch1)
        self.neuron2 = sim.send_sensor_neuron(sensor_id=self.touch2)
        self.neuron3 = sim.send_sensor_neuron(sensor_id=self.touch3)
        self.neuron4 = sim.send_sensor_neuron(sensor_id=self.touch4)

        self.SN = {}
        self.SN[0] = self.neuron1
        self.SN[1] = self.neuron2
        self.SN[2] = self.neuron3
        self.SN[3] = self.neuron4


        self.motor1 = sim.send_motor_neuron(joint_id=self.jointbody1, tau=.1)
        self.motor2 = sim.send_motor_neuron(joint_id=self.jointbody2, tau=.1)
        self.motor3 = sim.send_motor_neuron(joint_id=self.jointbody3, tau=.1)
        self.motor4 = sim.send_motor_neuron(joint_id=self.jointbody4, tau=.1)


        # self.ankle1 = sim.send_motor_neuron(joint_id=self.jointfoot1)
        # self.ankle2 = sim.send_motor_neuron(joint_id=self.jointfoot2)
        # self.ankle3 = sim.send_motor_neuron(joint_id=self.jointfoot3)
        # self.ankle4 = sim.send_motor_neuron(joint_id=self.jointfoot4)



        self.MN = {}
        self.MN[0] = self.motor1
        self.MN[1] = self.motor2
        self.MN[2] = self.motor3
        self.MN[3] = self.motor4
        # self.MN[2] = self.ankle1
        # self.MN[3] = self.ankle3
        # self.MN[3] = self.ankle4



        # self.O = {}
        # self.O[0] = self.O0
        # self.O[1] = self.O1
        # self.O[2] = self.O2
        # self.O[3] = self.O3
        # self.O[4] = self.O4
        # self.O[5] = self.O5
        # self.O[6] = self.O6
        # self.O[7] = self.O7
        # self.O[8] = self.O8
        #
        # self.J={}
        # self.J[0] = self.J0
        # self.J[1] = self.J1
        # self.J[2] = self.J2
        # self.J[3] = self.J3
        # self.J[4] = self.J4
        # self.J[5] = self.J5
        # self.J[6] = self.J6
        # self.J[7] = self.J7
        #
        # self.S = {}
        # self.S[0] = self.T0
        # self.S[1] = self.T1
        # self.S[2] = self.T2
        # self.S[3] = self.T3
        # self.S[4] = self.L4

        # self.SN = {}
        # self.MN = {}
        #
        # for s in self.S:
        #
        #     self.SN[s] = sim.send_sensor_neuron(sensor_id=self.S[s])
        #
        # for j in self.J:
        #
        #     self.MN[j] = sim.send_motor_neuron(joint_id=self.J[j], tau=0.3)

    def send_synapses(self, sim, wts):

        # for sn in self.SN:
        #
        #     firstMN = min(self.MN, key=self.MN.get)
        #     sim.send_synapse(source_neuron_id=self.SN[sn], target_neuron_id=self.MN[firstMN],
        #                        weight=random.random() * 2 - 1)

        # sim.send_synapse(source_neuron_id=self.touch1, target_neuron_id=self.motor1, weight=wts[0, i])
        # sim.send_synapse(source_neuron_id=self.touch2, target_neuron_id=self.motor2, weight=wts[j, i])

        sim.send_synapse(source_neuron_id=self.cpg, target_neuron_id=self.motor1, weight=.5)
        sim.send_synapse(source_neuron_id=self.cpg, target_neuron_id=self.motor3, weight=.5)

        sim.send_synapse(source_neuron_id=self.cpg2, target_neuron_id=self.motor2, weight=.5)
        sim.send_synapse(source_neuron_id=self.cpg2, target_neuron_id=self.motor4, weight=.5)


        for j in self.SN:

            for i in self.MN:

                sim.send_synapse(source_neuron_id=self.SN[j], target_neuron_id=self.MN[i], weight=wts[j, i])

