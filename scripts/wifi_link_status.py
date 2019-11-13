#!/usr/bin/env python
# license removed for brevity
import rospy
from subprocess import Popen, PIPE
from warthog_mapping_msgs.msg import Wifi_link_state


encoding = 'utf-8'
wifi_process_name = 'iwconfig'
wifi_interface = 'wlp3s0'
signal_level_string_start = 'Signal level='
signal_level_string_end = ' dBm'
signal_ssid_string_start = 'ESSID:"'
signal_ssid_string_end = '"'


def wifi_link_loop():
    pub = rospy.Publisher('wifi_link_status', Wifi_link_state, queue_size=10)
    rospy.init_node('wifi_link_monitoring_node', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        process = Popen([wifi_process_name, wifi_interface], stdout=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()

        if exit_code != 0:
            rospy.logerr('The system process '+wifi_process_name+ ' returned a error status. Terminating.')
            return

        output_str = output.decode(encoding)

        signal_dbm_ident_index = output_str.find(signal_level_string_start)
        signal_ssid_ident_index = output_str.find(signal_ssid_string_start)

        new_msg = Wifi_link_state()
        new_msg.header.stamp = rospy.Time.now()
        new_msg.header.frame_id = ""

        if signal_dbm_ident_index == -1 or signal_dbm_ident_index == -1:
            new_msg.rssi = -128
            new_msg.ssid = ''

        else:
            try:
                signal_dbm_index_start = signal_dbm_ident_index + len(signal_level_string_start)
                signal_dbm_index_end = output_str.find(signal_level_string_end, signal_dbm_index_start)

                signal_ssid_index_start = signal_ssid_ident_index + len(signal_ssid_string_start)
                signal_ssid_index_end = output_str.find(signal_ssid_string_end, signal_ssid_index_start)

                new_msg.rssi = max(-128, min(int(output_str[signal_dbm_index_start:signal_dbm_index_end]), 127))
                new_msg.ssid = output_str[signal_ssid_index_start:signal_ssid_index_end]
            except Exception as ex:
                rospy.logerr('Parsing output from ' + wifi_process_name + ' failed:' + str(ex) + '. Terminating.')
                rospy.logerr('The string was: \n' + output_str)
                return

        pub.publish(new_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        wifi_link_loop()
    except rospy.ROSInterruptException:
        pass



