from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QAction, QFileDialog
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.uic import *
import plotui
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive







class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('mainwindow.ui', self)

        self.mlpObcPck1Header.clicked.connect(self.mlpObcPck1HeaderClicked)
        self.mlpObcCmdsInBitPattern.clicked.connect(self.mlpObcCmdsInBitPatternClicked)
        self.mlpState.clicked.connect(self.mlpStateClicked)
        self.mlpNogoId.clicked.connect(self.mlpNogoIdClicked)
        self.mlpCmdSentCount.clicked.connect(self.mlpCmdSentCountClicked)
        self.issueDopCmds.clicked.connect(self.issueDopCmdsClicked)
        self.mlpDipStatus.clicked.connect(self.mlpDipStatusClicked)
        self.missileSupplyInVolts.clicked.connect(self.missileSupplyInVoltsClicked)
        self.launcherSupplyInvolts.clicked.connect(self.launcherSupplyInvoltsClicked)

        self.mlpObcTelMsg1Header.clicked.connect(self.mlpObcTelMsg1HeaderClicked)
        self.mlpState_2.clicked.connect(self.mlpState_2Clicked)
        self.mlpStateBitPattern.clicked.connect(self.mlpStateBitPatternClicked)
        self.mlpNogoId_2.clicked.connect(self.mlpNogoId_2Clicked)
        self.obcNogoId.clicked.connect(self.obcNogoIdClicked)
        self.NavigationStatus.clicked.connect(self.NavigationStatusClicked)
        self.insStatusWord.clicked.connect(self.insStatusWordClicked)
        self.syncForwardCount.clicked.connect(self.syncForwardCountClicked)
        self.swInu03.clicked.connect(self.swInu03Clicked)
        self.launcherSupplyInVolts.clicked.connect(self.launcherSupplyInVoltsClicked)
        self.missileSupplyInVolts_2.clicked.connect(self.missileSupplyInVolts_2Clicked)
        self.umbilicalMatingStatus.clicked.connect(self.umbilicalMatingStatusClicked)
        self.triggerPressbyPilot.clicked.connect(self.triggerPressbyPilotClicked)
        self.mlpObcCmd.clicked.connect(self.mlpObcCmdClicked)
        self.mlpDipStatus_2.clicked.connect(self.mlpDipStatus_2Clicked)
        self.mlpMode.clicked.connect(self.mlpModeClicked)
        self.minsAltitude.clicked.connect(self.minsAltitudeClicked)

        self.minsAltitudeatTakeoff.clicked.connect(self.minsAltitudeatTakeoffClicked)
        self.minsAltitudeDiff.clicked.connect(self.minsAltitudeDiffClicked)
        self.obcHealth.clicked.connect(self.obcHealthClicked)
        self.insHealth.clicked.connect(self.insHealthClicked)
        self.autoLaunchState.clicked.connect(self.autoLaunchStateClicked)
        self.autoLaunchStatePattern.clicked.connect(self.autoLaunchStatePatternClicked)
        self.autoLaunchT0.clicked.connect(self.autoLaunchT0Clicked)
        self.timeAtBuildupVoltage.clicked.connect(self.timeAtBuildupVoltageClicked)
        self.atbVoltage.clicked.connect(self.atbVoltageClicked)

        self.mlpObcCmdHeader.clicked.connect(self.mlpObcCmdHeaderClicked)
        self.sequenceNumber.clicked.connect(self.sequenceNumberClicked)
        self.CmdId.clicked.connect(self.CmdIdClicked)

        self.obcMlpSurvHeader.clicked.connect(self.obcMlpSurvHeaderClicked)
        self.obcState.clicked.connect(self.obcStateClicked)
        self.obcNogoId_2.clicked.connect(self.obcNogoId_2Clicked)
        self.obcAck.clicked.connect(self.obcAckClicked)
        self.insStatusWord_2.clicked.connect(self.insStatusWord_2Clicked)
        self.sensorStatusWord.clicked.connect(self.sensorStatusWordClicked)
        self.gpsstatusWord.clicked.connect(self.gpsstatusWordClicked)
        self.obcHealth_2.clicked.connect(self.obcHealth_2Clicked)
        self.insHealth_2.clicked.connect(self.insHealth_2Clicked)
        self.batteryVoltage.clicked.connect(self.batteryVoltageClicked)
        self.dipStatus.clicked.connect(self.dipStatusClicked)

        self.pb_browse.clicked.connect(self.pb_browseClicked)


        self.show()




    def pb_browseClicked(self):
        path = QFileDialog.getExistingDirectory()
        self.le_path.setText(path)
        dir_path= self.le_path.text()

        data_mlp_obc_packet1_msg = pd.read_csv(dir_path + '/0820_Engg.txt', header=None, usecols=range(0, 32),
                                               sep=' ')
        data_mlp_obc_packet1_msg = pd.DataFrame(data_mlp_obc_packet1_msg)
        self.a = data_mlp_obc_packet1_msg[0]
        self.b = data_mlp_obc_packet1_msg[1]
        self.c = data_mlp_obc_packet1_msg[3]
        self.d = data_mlp_obc_packet1_msg[4]
        self.e = data_mlp_obc_packet1_msg[5]
        self.f = data_mlp_obc_packet1_msg[6]
        self.g = data_mlp_obc_packet1_msg[16]
        self.h = data_mlp_obc_packet1_msg[17]
        self.i = data_mlp_obc_packet1_msg[18]
        self.j = data_mlp_obc_packet1_msg[19]

        data_mlp_obc_tel_msg = pd.read_csv(dir_path + '/0840_Engg.txt', header=None, usecols=range(0, 32), sep=' ')
        data_mlp_obc_tel_msg = pd.DataFrame(data_mlp_obc_tel_msg)
        self.a1 = data_mlp_obc_tel_msg[0]
        self.b1 = data_mlp_obc_tel_msg[1]
        self.c1 = data_mlp_obc_tel_msg[3]
        self.d1 = data_mlp_obc_tel_msg[4]
        self.e1 = data_mlp_obc_tel_msg[5]
        self.f1 = data_mlp_obc_tel_msg[6]
        self.g1 = data_mlp_obc_tel_msg[7]
        self.h1 = data_mlp_obc_tel_msg[8]
        self.i1 = data_mlp_obc_tel_msg[9]
        self.j1 = data_mlp_obc_tel_msg[10]
        self.k1 = data_mlp_obc_tel_msg[11]
        self.l1 = data_mlp_obc_tel_msg[12]
        self.m1 = data_mlp_obc_tel_msg[13]
        self.n1 = data_mlp_obc_tel_msg[14]
        self.o1 = data_mlp_obc_tel_msg[15]
        self.p1 = data_mlp_obc_tel_msg[16]
        self.q1 = data_mlp_obc_tel_msg[17]
        self.r1 = data_mlp_obc_tel_msg[18]
        self.s1 = data_mlp_obc_tel_msg[19]
        self.t1 = data_mlp_obc_tel_msg[20]
        self.u1 = data_mlp_obc_tel_msg[21]
        self.v1 = data_mlp_obc_tel_msg[22]
        self.w1 = data_mlp_obc_tel_msg[23]
        self.x1 = data_mlp_obc_tel_msg[24]
        self.y1 = data_mlp_obc_tel_msg[25]
        self.z1 = data_mlp_obc_tel_msg[26]
        self.A1 = data_mlp_obc_tel_msg[27]

        data_mlp_obc_cmd_msg = pd.read_csv(dir_path + '/0940_Engg.txt', header=None, usecols=range(0, 32), sep=' ')
        data_mlp_obc_cmd_msg = pd.DataFrame(data_mlp_obc_cmd_msg)
        self.a2 = data_mlp_obc_cmd_msg[0]
        self.b2 = data_mlp_obc_cmd_msg[1]
        self.c2 = data_mlp_obc_cmd_msg[2]
        self.d2 = data_mlp_obc_cmd_msg[3]

        data_mlp_obc_surv_msg = pd.read_csv(dir_path + '/0C60_Engg.txt', header=None, usecols=range(0, 32), sep=' ')
        data_mlp_obc_surv_msg = pd.DataFrame(data_mlp_obc_surv_msg)
        self.a3 = data_mlp_obc_surv_msg[0]
        self.b3 = data_mlp_obc_surv_msg[1]
        self.c3 = data_mlp_obc_surv_msg[3]
        self.d3 = data_mlp_obc_surv_msg[4]
        self.e3 = data_mlp_obc_surv_msg[5]
        self.f3 = data_mlp_obc_surv_msg[6]
        self.g3 = data_mlp_obc_surv_msg[7]
        self.h3 = data_mlp_obc_surv_msg[8]
        self.i3 = data_mlp_obc_surv_msg[10]
        self.j3 = data_mlp_obc_surv_msg[11]
        self.k3 = data_mlp_obc_surv_msg[12]
        self.l3 = data_mlp_obc_surv_msg[13]




    def plot_data(self, x, y, title, x_label, y_label, legend):
        fig, plot1 = plt.subplots(1, 1)

        plot1.plot(x, y, 'r.-')
        plot1.set_title(title)
        plot1.set_xlabel(x_label)
        plot1.set_ylabel(y_label)
        plot1.grid(color='black', ls='-.', lw=0.25)
        plot1.legend(labels=[legend], loc='best')
        plt.show()

    def int_hex(self, x):
        y = []
        for i in x:
            y.append(hex(i))
        return y

    #plot_data(x, y, 'Mlp State', 'time(sec)-->', 'Mlp State-->', ' ')'''


    def mlpObcPck1HeaderClicked(self):
        # This is executed when the button is pressed
        self.plot_data(self.a, self.int_hex(self.b), 'Mlp Obc Packet1 Header', 'time(sec)-->', 'Mlp Obc Packet1 Header-->', '')

    def mlpStateClicked(self):
        self.plot_data(self.a, self.c, 'Mlp State', 'time(sec)-->', 'Mlp State-->', '0 - INITIAL_STATE\n1 - CHK_AC_ID_STATE\n'
                                                                          '2 - CHK_INTERLOCKS_STATE\n3 - CHECK_MISSILE_POWERON_DIP_STATE\n'
                                                                          '4 - ISSUE_PBIT_STATE\n5 - COMM_CHECK\n6 - ISSUE_START_MISSION_TO_OBC\n'
                                                                          '7 - ISSUE_START_FA_STATE\n8 - WAIT_FOR_FA_CMD_ACK\n9 - WAIT_FOR_FA_COMPLETION_STATE\n'
                                                                          '10 - WAIT_FOR_NAV_READY\n11 - WAIT_FOR_TRIGGER_STATE\n12 - WAIT_FOR_ENTER_NAV_CMD_ACK\n'
                                                                          '13 - CHK_NAV_STATUS\n14 - AUTOLAUNCH_STATE\n15 - PRELAUNCH_MLP_ISSUED_NOGO_STATE\n'
                                                                          '16 - PRELAUNCH_DO_NOTHING_STATE\n17 - PRELAUNCH_DO_NOTHING_STATE_2')

    def mlpNogoIdClicked(self):
        self.plot_data(self.a, self.d, 'Mlp Nogo Id', 'time(sec)-->', 'Mlp Nogo Id-->', '1 - MLP_POST_FAILURE\n2 - EXTERNAL_SUPPLY_FAILURE\n'
                                                                              '3 - MISSILE_PRESENCE_FAILED\n4 - MISSILE_POWERON_DIP_FAILED\n'
                                                                              '5 - OBC_HEALTH_FAILURE\n6 - INS_HEALTH_FAILURE\n7 - MLP_COMM_CHK_A_FAILURE\n'
                                                                              '8 - MLP_COMM_CHK_B_FAILURE\n9 - MLP_COMM_CHK_A_B_FAILURE\n'
                                                                              '10 - OBC_REALTIME_COUNT_FAILURE\n11 - OBC_ISSUED_NOGO\n12 - ENTER_NAV_FAILED\n'
                                                                              '13 - FAILED_TO_TAKE_SET_MM_CMD\n14 - FAILED_TO_TAKE_START_FA\n'
                                                                              '15 - FAILED_TO_TAKE_ENTER_NAV\n16 - AL_ENTER_NAV_CMD_ACK_FAILURE\n'
                                                                              '17 - AL_ENTER_NAV_FAILURE\n18 - AL_TB_PYRO_ARM_STATUS_FAILURE\n'
                                                                              '19 - AL_TB_FIRING_STATUS_FAILURE\n20 - AL_BATTARY_VOLTAGE_BUILDUP_FAILURE\n'
                                                                              '21 - AL_INTERNAL_SWITCHOVER_STATUS_FAILURE\n22 - AL_SOLENOID_FIRING_STATUS_FAILURE\n'
                                                                              '23 - AL_UMBILICAL_MATING_STATUS_FAILURE\n24 - AL_FIRE_TB_CMD_ACK_FAILURE')

    def mlpObcCmdsInBitPatternClicked(self):
        self.plot_data(self.a, self.int_hex(self.e), 'Mlp Obc Cmds In Bit Pattern', 'time(sec)-->', 'Mlp Obc Cmds In Bit Pattern-->', '')

    def mlpCmdSentCountClicked(self):
        # This is executed when the button is pressed
        self.plot_data(self.a, self.f, 'Mlp Command Sent Count', 'time(sec)-->', 'Mlp Cmd Sent Count-->', '')

    def issueDopCmdsClicked(self):
        self.plot_data(self.a, self.int_hex(self.g), 'Issue Dop Commands', 'time(sec)-->', 'Issue Dop Cmds-->', '')

    def mlpDipStatusClicked(self):
        self.plot_data(self.a, self.int_hex(self.h), 'Mlp Dip Status', 'time(sec)-->', 'Mlp Dip Status-->', 'B16-MISSILE_POWER_RELAY_STATUS\nB17-TWDL_POWER_RELAY_STATUS\n'
                                                                                                  'B18-TB_ARM_RELAY_STATUS\nB19-MISSILE_READY_STATUS\nB20-ITLR_STATUS\n'
                                                                                                  'B21-TACTICAL_RELEASE_STATUS\nB22-UMBLICAL_MATING_STATUS\n'
                                                                                                  'B29-RELEASE_CONSENT\nB30-TRIGGER_PRESS')

    def launcherSupplyInvoltsClicked(self):
        self.plot_data(self.a, self.i, 'Launcher Supply In Volts', 'time(sec)-->', 'Launcher Supply In Volts-->', '')

    def missileSupplyInVoltsClicked(self):
        self.plot_data(self.a, self.j, 'Missile Supply In Volts', 'time(sec)-->', 'Missile Supply In Volts-->', '')




    def mlpObcTelMsg1HeaderClicked(self):
        self.plot_data(self.a1, self.int_hex(self.b1), 'Mlp Obc Telemetry Message1 Header', 'time(sec)-->', 'Mlp Obc TelMsg1 Header-->', '')

    def mlpState_2Clicked(self):
        self.plot_data(self.a1, self.c1, 'Mlp State', 'time(sec)-->', 'Mlp State-->', '0 - INITIAL_STATE\n1 - CHK_AC_ID_STATE\n'
                                                                            '2 - CHK_INTERLOCKS_STATE\n3 - CHECK_MISSILE_POWERON_DIP_STATE\n'
                                                                            '4 - ISSUE_PBIT_STATE\n5 - COMM_CHECK\n6 - ISSUE_START_MISSION_TO_OBC\n'
                                                                            '7 - ISSUE_START_FA_STATE\n8 - WAIT_FOR_FA_CMD_ACK\n'
                                                                            '9 - WAIT_FOR_FA_COMPLETION_STATE\n10 - WAIT_FOR_NAV_READY\n'
                                                                            '11 - WAIT_FOR_TRIGGER_STATE\n12 - WAIT_FOR_ENTER_NAV_CMD_ACK\n'
                                                                            '13 - CHK_NAV_STATUS\n14 - AUTOLAUNCH_STATE\n'
                                                                            '15 - PRELAUNCH_MLP_ISSUED_NOGO_STATE\n16 - PRELAUNCH_DO_NOTHING_STATE\n'
                                                                            '17 - PRELAUNCH_DO_NOTHING_STATE_2')

    def mlpStateBitPatternClicked(self):
        self.plot_data(self.a1, self.int_hex(self.d1), 'Mlp State Bit Pattern', 'time(sec)-->', 'Mlp State Bit Pattern-->', '')

    def mlpNogoId_2Clicked(self):
        self.plot_data(self.a1, self.e1, 'Mlp NogoId', 'time(sec)-->', 'Mlp NogoId-->', '1 - MLP_POST_FAILURE\n2 - EXTERNAL_SUPPLY_FAILURE\n'
                                                                              '3 - MISSILE_PRESENCE_FAILED\n4 - MISSILE_POWERON_DIP_FAILED\n'
                                                                              '5 - OBC_HEALTH_FAILURE\n6 - INS_HEALTH_FAILURE\n'
                                                                              '7 - MLP_COMM_CHK_A_FAILURE\n8 - MLP_COMM_CHK_B_FAILURE\n'
                                                                              '9 - MLP_COMM_CHK_A_B_FAILURE\n10 - OBC_REALTIME_COUNT_FAILURE\n'
                                                                              '11 - OBC_ISSUED_NOGO\n12 - ENTER_NAV_FAILED\n13 - FAILED_TO_TAKE_SET_MM_CMD\n'
                                                                              '14 - FAILED_TO_TAKE_START_FA\n15 - FAILED_TO_TAKE_ENTER_NAV\n'
                                                                              '16 - AL_ENTER_NAV_CMD_ACK_FAILURE\n17 - AL_ENTER_NAV_FAILURE\n'
                                                                              '18 - AL_TB_PYRO_ARM_STATUS_FAILURE\n19 - AL_TB_FIRING_STATUS_FAILURE\n'
                                                                              '20 - AL_BATTARY_VOLTAGE_BUILDUP_FAILURE\n21 - AL_INTERNAL_SWITCHOVER_STATUS_FAILURE\n'
                                                                              '22 - AL_SOLENOID_FIRING_STATUS_FAILURE\n23 - AL_UMBILICAL_MATING_STATUS_FAILURE\n'
                                                                              '24 - AL_FIRE_TB_CMD_ACK_FAILURE')

    def obcNogoIdClicked(self):
        self.plot_data(self.a1, self.f1, 'Obc Nogo Id', 'time(sec)-->', 'Obc Nogo Id-->', '1 - MLP_PBIT_FAILURE\n2 - WEAPON1_POWER_ON_FAILURE\n'
                                                                                '3 -  WEAPON2_POWER_ON_FAILURE\n4 - WEAPON1_COMM_CHECK_FAILURE\n'
                                                                                '5 - WEAPON2_COMM_CHECK_FAILURE\n6 - WEAPON1_RELEASE_PRESSURE_FAILURE\n'
                                                                                '7 - WEAPON2_RELEASE_PRESSURE_FAILURE\n8 - LRS_STATUS_FAILURE\n'
                                                                                '9 - RRS_STATUS_FAILURE\n10 - WEAPON1_RELEASE_FAILURE\n'
                                                                                '11 - WEAPON2_RELEASE_FAILURE\n12 - WEAPON2_ISSUED_NOGO\n13 - UNKNOWN_REASON')

    def NavigationStatusClicked(self):
        self.plot_data(self.a1, self.int_hex(self.g1), 'Navigation Status', 'time(sec)-->', 'Navigation Status-->', '0x1 - MASTER_DATA_AVAILABLE\n0x3 - MASTER_ALIGNMENT_COMPLETED\n'
                                                                                                          '0x7 - MASTER_DATA_VALID\n0xf - MASTER_DATA_FORWARDING_STARTED\n0x1f - START_FA_ISSUED\n'
                                                                                                          '0x3f - GC_COMPLETED\n0x7f - NAV_READY_SET\n'
                                                                                                          '0xff - ENTER_NAV_ISSUED\n0x1ff - NAV_STARTED')

    def insStatusWordClicked(self):
        self.plot_data(self.a1, self.int_hex(self.h1), 'Ins Status Word', 'time(sec)-->', 'Ins Status Word-->', '0x0 - \n0x40 - INU-03-OK\n'
                                                                                                      '0x1cc - FA-MODE,INU-03_OK,STATIC NAV-MODE\n'
                                                                                                      '0xdcc - DRIFT VALUES POSTED,GCC_COMPLETE,FA-MODE,INU-03_OK,STATIC NAV-MODE\n'
                                                                                                      '0x4dcc - FA operation with MINS,DRIFT VALUES POSTED, GCC_COMPLETE,FA-MODE,INU-03_OK, STATIC NAV-MODE\n'
                                                                                                      '0x4fcc - NAV_READY,FA-MODE,INU-03_OK, STATIC NAV-MODE\n0x4fec - NAVIGATION')

    def syncForwardCountClicked(self):
        self.plot_data(self.a1, self.i1, 'Sync Forward Count', 'time(sec)-->', 'Sync Forward Count-->', '')

    def swInu03Clicked(self):
        self.plot_data(self.a1, self.int_hex(self.j1), 'SwInu03', 'time(sec)-->', 'SwInu03-->', '')

    def launcherSupplyInVoltsClicked(self):
        self.plot_data(self.a1, self.k1, 'Launcher Supply In Volts', 'time(sec)-->', 'Launcher Supply In Volts-->', '')

    def missileSupplyInVolts_2Clicked(self):
        self.plot_data(self.a1, self.l1, 'Missile Supply In Volts', 'time(sec)-->', 'Missile Supply In Volts-->', '')

    def umbilicalMatingStatusClicked(self):
        self.plot_data(self.a1, self.m1, 'Umbilical Mating Status', 'time(sec)-->', 'Umbilical Mating Status-->', '')

    def triggerPressbyPilotClicked(self):
        self.plot_data(self.a1, self.n1, 'Trigger Press by Pilot', 'time(sec)-->', 'Trigger Press by Pilot-->', '')

    def mlpObcCmdClicked(self):
        self.plot_data(self.a1, self.int_hex(self.o1), 'Mlp Obc Cmd', 'time(sec)-->', 'Mlp Obc Cmd-->', '0x0208 - SET_MISSION_MODE_FLAG\n'
                                                                                              '0x0307 - START_FA\n0x0350-ENTER_NAV')

    def mlpDipStatus_2Clicked(self):
        self.plot_data(self.a1, self.int_hex(self.p1), 'Mlp Dip Status', 'time(sec)-->', 'Mlp Dip Status-->', 'B16 - MISSILE_POWER_RELAY_STATUS\nB17 - TWDL_POWER_RELAY_STATUS\n'
                                                                                                    'B18 - TB_ARM_RELAY_STATUS\nB19 - MISSILE_READY_STATUS\n'
                                                                                                    'B20 - ITLR_STATUS\nB21 - TACTICAL_RELEASE_STATUS\n'
                                                                                                    'B22 - UMBLICAL_MATING_STATUS\nB29 - RELEASE_CONSENT\nB30 - TRIGGER_PRESS')

    def mlpModeClicked(self):
        self.plot_data(self.a1, self.int_hex(self.q1), 'Mlp Mode', 'time(sec)-->', 'Mlp Mode-->', '0x5501-RFT\n0x5502-CFT\n0x5503-DUMMY_DROP\n,'
                                                                                        '0x5504-DUMMY_DROP_WITHOUT_ALT_TIME\n0x5505-CFT_WITHOUT_INS\n'
                                                                                        '0x5506-RFT_WITHOUT_INS\n0x5507-CFT_ON_GROUND\n0x5508-RFT_ON_GROUND')

    def minsAltitudeClicked(self):
        self.plot_data(self.a1, self.r1, 'Mins Altitude', 'time(sec)-->', 'Mins Altitude-->', '')

    def minsAltitudeatTakeoffClicked(self):
        self.plot_data(self.a1, self.s1, 'Mins Altitude at Takeoff', 'time(sec)-->', 'Mins Altitude at Takeoff-->', '')

    def minsAltitudeDiffClicked(self):
        self.plot_data(self.a1, self.t1, 'Mins Altitude Diff', 'time(sec)-->', 'Mins Altitude Diff-->', '')

    def obcHealthClicked(self):
        self.plot_data(self.a1, self.u1, 'Obc Health', 'time(sec)-->', 'Obc Health-->', '')

    def insHealthClicked(self):
        self.plot_data(self.a1, self.v1, 'Ins Health', 'time(sec)-->', 'Ins Health-->', '')

    def autoLaunchStateClicked(self):
        self.plot_data(self.a1, self.w1, 'AutoLaunch State', 'time(sec)-->', 'AutoLaunch State-->', '0 - AUTOLAUNCH_STATE_1\n1 - AUTOLAUNCH_STATE_2\n'
                                                                                          '2-  AUTOLAUNCH_STATE_3\n3 - AUTOLAUNCH_STATE_4\n'
                                                                                          '4 - AUTOLAUNCH_STATE_5\n5 - AUTOLAUNCH_STATE_\n'
                                                                                          '6 - AUTOLAUNCH_STATE_7\n7 - AUTOLAUNCH_LAUNCH_SUCCESSFUL\n'
                                                                                          '10 - AUTOLAUNCH_STATE_WAIT_STATE_1\n11 - AUTOLAUNCH_STATE_WAIT_STATE_2\n'
                                                                                          '12 - AUTOLAUNCH_STATE_WAIT_STATE_3\n13 - AUTOLAUNCH_STATE_WAIT_STATE_4\n'
                                                                                          '14 - AUTOLAUNCH_STATE_WAIT_STATE_5\n15 - AUTOLAUNCH_STATE_WAIT_STATE_6')

    def autoLaunchStatePatternClicked(self):
        self.plot_data(self.a1, self.int_hex(self.x1), 'AutoLaunch State Pattern', 'time(sec)-->', 'AutoLaunch State Pattern-->', '')

    def autoLaunchT0Clicked(self):
        self.plot_data(self.a1, self.y1, 'AutoLaunch T0', 'time(sec)-->', 'AutoLaunch T0-->', '')

    def timeAtBuildupVoltageClicked(self):
        self.plot_data(self.a1, self.z1, 'Time At Buildup Voltage', 'time(sec)-->', 'Time At Buildup Voltage-->', '')

    def atbVoltageClicked(self):
        self.plot_data(self.a1, self.A1, 'Atb Voltage', 'time(sec)-->', 'Atb Voltage-->', '')



    def mlpObcCmdHeaderClicked(self):
        self.plot_data(self.a2, self.int_hex(self.b2), 'Mlp Obc Command Header', 'time(sec)-->', 'Mlp Obc Cmd Header', '')

    def sequenceNumberClicked(self):
        self.plot_data(self.a2, self.c2, 'Sequence Number', 'time(sec)-->', 'Sequence Number-->', '')

    def CmdIdClicked(self):
        self.plot_data(self.a2, self.int_hex(self.d2), 'Command ID', 'time(sec)-->', 'Cmd ID-->', '0x0208 - SET_MISSION_MODE_FLAG\n'
                                                                                              '0x0307 - START_FA\n0x0350-ENTER_NAV')



    def obcMlpSurvHeaderClicked(self):
        self.plot_data(self.a3, self.int_hex(self.b3), 'Obc Mlp Surveillance Header', 'time(sec)-->', 'Obc Mlp Surv Header-->', '')

    def obcStateClicked(self):
        self.plot_data(self.a3, self.c3, 'Obc State', 'time(sec)-->', 'Obc State-->', '')

    def obcNogoId_2Clicked(self):
        self.plot_data(self.a3, self.d3, 'Obc NogoId', 'time(sec)-->', 'Obc NogoId-->', '1 - MLP_PBIT_FAILURE\n2 - WEAPON1_POWER_ON_FAILURE\n'
                                                                              '3 - WEAPON2_POWER_ON_FAILURE\n4 - WEAPON1_COMM_CHECK_FAILURE\n'
                                                                              '5 - WEAPON2_COMM_CHECK_FAILURE\n6 - WEAPON1_RELEASE_PRESSURE_FAILURE\n'
                                                                              '7 - WEAPON2_RELEASE_PRESSURE_FAILURE\n8 - LRS_STATUS_FAILURE\n'
                                                                              '9 - RRS_STATUS_FAILURE\n10 - WEAPON1_RELEASE_FAILURE\n'
                                                                              '11 - WEAPON2_RELEASE_FAILURE\n12 - WEAPON2_ISSUED_NOGO\n'
                                                                              '13 - UNKNOWN_REASON')

    def obcAckClicked(self):
        self.plot_data(self.a3, self.e3, 'Obc Ack', 'time(sec)-->', 'Obc Ack-->', '')

    def insStatusWord_2Clicked(self):
        self.plot_data(self.a3, self.int_hex(self.f3), 'Ins Status Word', 'time(sec)-->', 'Ins Status Word-->', '0x0 - \n0x40 - INU-03-OK\n'
                                                                                                      '0x1cc - FA-MODE, INU-03_OK, STATIC NAV-MODE\n'
                                                                                                      '0xdcc - DRIFT VALUES POSTED, GCC_COMPLETE,FA-MODE, INU-03_OK, STATIC NAV-MODE\n'
                                                                                                      '0x4dcc - FA operation with MINS,DRIFT VALUES POSTED, GCC_COMPLETE,FA-MODE,INU-03_OK, STATIC NAV-MODE\n'
                                                                                                      '0x4fcc - NAV_READY,FA-MODE,INU-03_OK, STATIC NAV-MODE\n0x4fec-NAVIGATION')

    def sensorStatusWordClicked(self):
        self.plot_data(self.a3, self.int_hex(self.g3), 'Sensor Status Word', 'time(sec)-->', 'Sensor Status Word-->', '')

    def gpsstatusWordClicked(self):
        self.plot_data(self.a3, self.int_hex(self.h3), 'Gps Status Word', 'time(sec)-->', 'Gps status Word-->', '')

    def obcHealth_2Clicked(self):
        self.plot_data(self.a3, self.i3, 'Obc Health', 'time(sec)-->', 'Obc Health-->', '')

    def insHealth_2Clicked(self):
        self.plot_data(self.a3, self.j3, 'Ins Health', 'time(sec)-->', 'Ins Health-->', '')

    def batteryVoltageClicked(self):
        self.plot_data(self.a3, self.k3, 'Battery Voltage', 'time(sec)-->', 'Battery Voltage-->', '')

    def dipStatusClicked(self):
        self.plot_data(self.a3, self.int_hex(self.l3), 'Dip Status', 'time(sec)-->', 'Dip Status-->', 'B16 - MISSILE_POWER_RELAY_STATUS\nB17 - TWDL_POWER_RELAY_STATUS\n'
                                                                                            'B18 - TB_ARM_RELAY_STATUS\nB19 - MISSILE_READY_STATUS\n'
                                                                                            'B20 - ITLR_STATUS\nB21 - TACTICAL_RELEASE_STATUS\n'
                                                                                            'B22 - UMBLICAL_MATING_STATUS\nB29 - RELEASE_CONSENT\nB30 - TRIGGER_PRESS')

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()


