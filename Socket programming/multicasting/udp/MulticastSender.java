package udp;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;

public class MulticastSender {
    public static void main(String[] args) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        MulticastSocket socket = null;

        try {
            // Create a MulticastSocket
            socket = new MulticastSocket();

            // Read user input for multicast group and message
            System.out.print("Enter multicast group address (e.g., 230.0.0.1): ");
            String groupAddress = reader.readLine();
            InetAddress group = InetAddress.getByName(groupAddress);

            System.out.print("Enter port number: ");
            int port = Integer.parseInt(reader.readLine());

            System.out.print("Enter message to send: ");
            String message = reader.readLine();

            // Create and send the packet
            DatagramPacket packet = new DatagramPacket(
                message.getBytes(),
                message.length(),
                group,
                port
            );

            socket.send(packet);
            System.out.println("Message sent to group " + groupAddress + " on port " + port + ": " + message);
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (socket != null && !socket.isClosed()) {
                socket.close();
            }
        }
    }
}
