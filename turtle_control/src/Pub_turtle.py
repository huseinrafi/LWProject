#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('/chatter', String, queue_size=10)  # Membuat publisher ke topic 'chatter'
    rospy.init_node('talker', anonymous=True)  # Inisialisasi node dengan nama 'talker'

    while not rospy.is_shutdown():
        input_message = input("Masukkan Perintah untuk menggerakkan Turtle (Maju, Mundur, Kiri, Kanan)")  # Meminta input pesan dari user  
        rospy.loginfo(f"Sending: {input_message}")
        pub.publish(input_message)

if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
