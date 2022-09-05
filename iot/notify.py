import board
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import json


def run(args):
    host = args.host
    rootCAPath = args.rootCAPath
    certificatePath = args.certificatePath
    privateKeyPath = args.privateKeyPath
    port = args.port
    useWebsocket = args.useWebsocket
    clientId = args.clientId
    topic = args.topic

    # Port defaults
    if args.useWebsocket and not args.port:  # When no port override for WebSocket, default to 443
        port = 443
    if not args.useWebsocket and not args.port:  # When no port override for non-WebSocket, default to 8883
        port = 8883

    # Configure logging
    logger = logging.getLogger("AWSIoTPythonSDK.core")
    logger.setLevel(logging.DEBUG)
    streamHandler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)

    # Init AWSIoTMQTTClient
    iotClient = None
    if useWebsocket:
        print("websocket!")
        iotClient = AWSIoTMQTTClient(clientId, useWebsocket=True)
        iotClient.configureEndpoint(host, port)
        iotClient.configureCredentials(rootCAPath)
    else:
        print("NON-websocket!")
        iotClient = AWSIoTMQTTClient(clientId)
        iotClient.configureEndpoint(host, port)
        iotClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

    # AWSIoTMQTTClient connection configuration
    iotClient.configureAutoReconnectBackoffTime(1, 32, 20)
    iotClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    iotClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    iotClient.configureConnectDisconnectTimeout(10)  # 10 sec
    iotClient.configureMQTTOperationTimeout(5)  # 5 sec
    # Connect and subscribe to AWS IoT
    iotClient.connect()
    time.sleep(2)

    message = dict(message=args.message)
    messageJson = json.dumps(message)
    iotClient.publish(topic, messageJson, 1)
    print('Published topic %s: %s\n' % (topic, messageJson))


def main():
    # Read in command-line parameters
    parser = argparse.ArgumentParser()

    parser.add_argument("--endpoint",
                        action="store",
                        required=True,
                        dest="host",
                        help="Your AWS IoT custom endpoint")

    parser.add_argument("--rootCA",
                        action="store",
                        required=True,
                        dest="rootCAPath",
                        help="Root CA file path")

    parser.add_argument("--cert",
                        action="store",
                        dest="certificatePath",
                        help="Certificate file path")

    parser.add_argument("--key",
                        action="store",
                        dest="privateKeyPath",
                        help="Private key file path")

    parser.add_argument("--port",
                        action="store",
                        dest="port",
                        type=int,
                        help="Port number override")

    parser.add_argument("--websocket",
                        action="store_true",
                        dest="useWebsocket",
                        default=False,
                        help="Use MQTT over WebSocket")

    parser.add_argument("--clientId",
                        action="store",
                        dest="clientId",
                        default="basicPubSub",
                        help="Targeted client id")

    parser.add_argument("--topic",
                        action="store",
                        required=True,
                        dest="topic",
                        help="Targeted topic")

    parser.add_argument("--message",
                        action="store",
                        required=True,
                        dest="message",
                        help="Message to publish")

    args = parser.parse_args()

    if args.useWebsocket and args.certificatePath and args.privateKeyPath:
        parser.error("X.509 cert authentication and WebSocket are mutual exclusive. Please pick one.")
        exit(2)

    if not args.useWebsocket and (not args.certificatePath or not args.privateKeyPath):
        parser.error("Missing credentials for authentication.")
        exit(2)

    run(args)


if __name__ == '__main__':
    main()
