import json
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a6147d888c7079f51e82ee",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a6147d888c7079f51e82ee",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a61497888c7079f51e830d","source_node_id":"69a6148f888c7079f51e8306","source_pin_id":"rear_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a61484888c7079f51e82f9",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a61484888c7079f51e82f9",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a61499888c7079f51e8310","source_node_id":"69a6148f888c7079f51e8306","source_pin_id":"front_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a61488888c7079f51e82ff",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a61488888c7079f51e82ff",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a6149a888c7079f51e8313","source_node_id":"69a6148f888c7079f51e8306","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="motor_controller",
            executable="motor_controller_node",
            name="motor_controller_69a6147f888c7079f51e82f3",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a6147f888c7079f51e82f3",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"motor_id":"motor_0","control_mode":"velocity","max_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd62b3f393789aad70a2:command","name":"command","direction":"input","msg_type":"std_msgs/Float64"},{"pin_id":"69a3cd62b3f393789aad70a2:state","name":"state","direction":"output","msg_type":"polyflow_msgs/MotorState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a61495888c7079f51e830a","source_node_id":"69a6148f888c7079f51e8306","source_pin_id":"front_left_motor","target_pin_id":"command"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="differential_drive",
            executable="differential_drive_node",
            name="differential_drive_69a6148f888c7079f51e8306",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a6148f888c7079f51e8306",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"wheel_radius":0.05,"wheel_separation":0.3,"max_wheel_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c8e4b3f393789aad6f84:cmd_vel","name":"cmd_vel","direction":"input","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a3c8e4b3f393789aad6f84:mode","name":"mode","direction":"input","msg_type":"polyflow_msgs/ModeState"},{"pin_id":"69a3c8e4b3f393789aad6f84:encoder_left","name":"encoder_left","direction":"input","msg_type":"polyflow_msgs/EncoderState"},{"pin_id":"69a3c8e4b3f393789aad6f84:encoder_right","name":"encoder_right","direction":"input","msg_type":"polyflow_msgs/EncoderState"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_left_motor","name":"front_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_left_motor","name":"rear_left_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:front_right_motor","name":"front_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:rear_right_motor","name":"rear_right_motor","direction":"output","msg_type":"std_msgs/Float64"},{"pin_id":"69a3c8e4b3f393789aad6f84:odometry","name":"odometry","direction":"output","msg_type":"nav_msgs/Odometry"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a614ba888c7079f51e833a","source_node_id":"69a614b2888c7079f51e8334","source_pin_id":"encoder_state","target_pin_id":"encoder_right"},{"connection_id":"69a614bc888c7079f51e833d","source_node_id":"69a614b0888c7079f51e832f","source_pin_id":"encoder_state","target_pin_id":"encoder_left"},{"connection_id":"69a614bd888c7079f51e8340","source_node_id":"69a614a9888c7079f51e8324","source_pin_id":"mode","target_pin_id":"mode"},{"connection_id":"69a614bf888c7079f51e8343","source_node_id":"69a614a2888c7079f51e8319","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"},{"connection_id":"69a614c1888c7079f51e8346","source_node_id":"69a614a5888c7079f51e831e","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a61495888c7079f51e830a","target_node_id":"69a6147f888c7079f51e82f3","source_pin_id":"front_left_motor","target_pin_id":"command"},{"connection_id":"69a61497888c7079f51e830d","target_node_id":"69a6147d888c7079f51e82ee","source_pin_id":"rear_left_motor","target_pin_id":"command"},{"connection_id":"69a61499888c7079f51e8310","target_node_id":"69a61484888c7079f51e82f9","source_pin_id":"front_right_motor","target_pin_id":"command"},{"connection_id":"69a6149a888c7079f51e8313","target_node_id":"69a61488888c7079f51e82ff","source_pin_id":"rear_right_motor","target_pin_id":"command"}]')),
            }
        ),
        Node(
            package="mission_runner",
            executable="mission_runner_node",
            name="mission_runner_69a614a2888c7079f51e8319",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a614a2888c7079f51e8319",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"mission":[],"linear_speed":0.5,"angular_speed":1}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":10,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a477bcc85549d8e55e27db:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"},{"pin_id":"69a477bcc85549d8e55e27db:status","name":"status","direction":"output","msg_type":"std_msgs/String"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a614bf888c7079f51e8343","target_node_id":"69a6148f888c7079f51e8306","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
        Node(
            package="gamepad",
            executable="gamepad_node",
            name="gamepad_69a614a5888c7079f51e831e",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a614a5888c7079f51e831e",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"device_index":0,"poll_rate_hz":60,"deadzone":0.05,"max_linear_speed":1,"max_angular_speed":2}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":60,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c77bb3f393789aad6f62:axes","name":"axes","direction":"output","msg_type":"polyflow_msgs/GamepadAxes"},{"pin_id":"69a3c77bb3f393789aad6f62:buttons","name":"buttons","direction":"output","msg_type":"polyflow_msgs/GamepadButtons"},{"pin_id":"69a3c77bb3f393789aad6f62:cmd_vel","name":"cmd_vel","direction":"output","msg_type":"geometry_msgs/Twist"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a614c1888c7079f51e8346","target_node_id":"69a6148f888c7079f51e8306","source_pin_id":"cmd_vel","target_pin_id":"cmd_vel"}]')),
            }
        ),
        Node(
            package="mode_switcher",
            executable="mode_switcher_node",
            name="mode_switcher_69a614a9888c7079f51e8324",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a614a9888c7079f51e8324",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"default_mode":"stopped","allowed_modes":["teleop","automated","stopped"]}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3cd36b3f393789aad7079:set_mode","name":"set_mode","direction":"input","msg_type":"polyflow_msgs/ModeCommand"},{"pin_id":"69a3cd36b3f393789aad7079:mode","name":"mode","direction":"output","msg_type":"polyflow_msgs/ModeState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a614bd888c7079f51e8340","target_node_id":"69a6148f888c7079f51e8306","source_pin_id":"mode","target_pin_id":"mode"}]')),
            }
        ),
        Node(
            package="logger",
            executable="logger_node",
            name="logger_69a614ac888c7079f51e832a",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a614ac888c7079f51e832a",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"log_file":"","log_to_stdout":true}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
            }
        ),
        Node(
            package="optical_encoder",
            executable="optical_encoder_node",
            name="optical_encoder_69a614b0888c7079f51e832f",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a614b0888c7079f51e832f",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"encoder_id":"encoder_0","ticks_per_rev":1024,"publish_rate_hz":50}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c932b3f393789aad6fbc:reset","name":"reset","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3c932b3f393789aad6fbc:encoder_state","name":"encoder_state","direction":"output","msg_type":"polyflow_msgs/EncoderState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a614bc888c7079f51e833d","target_node_id":"69a6148f888c7079f51e8306","source_pin_id":"encoder_state","target_pin_id":"encoder_left"}]')),
            }
        ),
        Node(
            package="optical_encoder",
            executable="optical_encoder_node",
            name="optical_encoder_69a614b2888c7079f51e8334",
            output="screen",
            additional_env={
                "POLYFLOW_NODE_ID": "69a614b2888c7079f51e8334",
                "POLYFLOW_PARAMETERS": json.dumps(json.loads('{"encoder_id":"encoder_0","ticks_per_rev":1024,"publish_rate_hz":50}')),
                "POLYFLOW_CONFIGURATION": json.dumps(json.loads('{"namespace":null,"rate_hz":50,"lifecycle":null}')),
                "POLYFLOW_PINS": json.dumps(json.loads('[{"pin_id":"69a3c932b3f393789aad6fbc:reset","name":"reset","direction":"input","msg_type":"std_msgs/Empty"},{"pin_id":"69a3c932b3f393789aad6fbc:encoder_state","name":"encoder_state","direction":"output","msg_type":"polyflow_msgs/EncoderState"}]')),
                "POLYFLOW_INBOUND_CONNECTIONS": json.dumps(json.loads('[]')),
                "POLYFLOW_OUTBOUND_CONNECTIONS": json.dumps(json.loads('[{"connection_id":"69a614ba888c7079f51e833a","target_node_id":"69a6148f888c7079f51e8306","source_pin_id":"encoder_state","target_pin_id":"encoder_right"}]')),
            }
        ),
    ])