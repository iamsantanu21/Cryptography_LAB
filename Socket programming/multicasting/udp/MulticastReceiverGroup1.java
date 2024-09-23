package udp;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;

public class MulticastReceiverGroup1 {
    @SuppressWarnings("deprecation")
    public static void main(String[] args) {
        MulticastSocket socket = null;
        try {
            InetAddress group = InetAddress.getByName("230.0.0.1");
            socket = new MulticastSocket(4446);
            socket.joinGroup(group);

            byte[] buffer = new byte[256];
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);

            System.out.println("Waiting for messages from Group 1...");

            socket.receive(packet);
            String receivedMessage = new String(packet.getData(), 0, packet.getLength());

            System.out.println("Received message from Group 1: " + receivedMessage);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (socket != null && !socket.isClosed()) {
                socket.close();
            }
        }
    }
}
