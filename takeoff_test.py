from pymavlink import mavutil
import time

connection = mavutil.mavlink_connection('/dev/ttyUSB0', baud=115200)
connection.wait_heartbeat()
connection.mav.command_long_send(connection.target_system,connection.target_component,mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,1,0)
print(connection.recv_match(type='COMMAND_ACK',blocking=True))

connection.mav.command_long_send(connection.target_system,connection.target_component,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0,0,0,0,0,5)
# lat. and long. zero mean that aircraft will stay in place
# will take off to 5m altitude
print(connection.recv_match(type='COMMAND_ACK',blocking=True))

time.sleep(5)

connection.mav.command_long_send(connection.target_system,connection.target_component,mavutil.mavlink.MAV_CMD_NAV_LAND,0,0,0,0,0,0,0)
print(connection.recv_match(type='COMMAND_ACK',blocking=True))
