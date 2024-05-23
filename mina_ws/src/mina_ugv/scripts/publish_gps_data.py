import rclpy
import serial
from rclpy.node import Node
from ublox_gps import UbloxGps
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix
from rclpy.clock import Clock

class GPSPublisher(Node):

    def __init__(self):
        super().__init__('gps_publisher')
        self.publisher_ = self.create_publisher(NavSatFix, 'gps/fix/ctrl', 10)
        self.port = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)
        self.gps = UbloxGps(self.port)

    def publish(self):
        try: 
            print("Listening for UBX Messages")
            while True:
                try:
                    geo = self.gps.geo_coords()
                    cov = self.gps.geo_cov()

                    time_stamp = Clock().now()

                    msg = NavSatFix()
                    msg.header.stamp = time_stamp.to_msg()
                    msg.header.frame_id = "gps_link"
                    msg.longitude = geo.lon
                    msg.latitude = geo.lat
                    msg.altitude = 0.001 * float(geo.height)
                    NN = cov.posCovNN
                    NE = cov.posCovNE
                    ND = cov.posCovND
                    EE = cov.posCovEE
                    ED = cov.posCovED
                    DD = cov.posCovDD
                    msg.position_covariance = [EE, NE, ED, NE, NN, ND, ED, ND, DD]
                    msg.position_covariance_type = 3
                    self.publisher_.publish(msg)
                except (ValueError, IOError) as err:
                    print(err)
        finally:
            self.port.close()


def main(args=None):
    rclpy.init(args=args)

    gps_publisher = GPSPublisher()
    gps_publisher.publish()

    gps_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

