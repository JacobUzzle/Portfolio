using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
namespace ConsoleApplication1
{
    public partial class Form1 : Form
    {
        Player poo;
        Room root;
        public Form1()
        {
            InitializeComponent();
            FormBorderStyle = FormBorderStyle.None;
            WindowState = FormWindowState.Maximized;
            poo = new Player();
            poo.ChangeEnergy(100);
            root = new Room();
            Room r1 = new Room(); Room r2 = new Room(); Room r3 = new Room();
            Room r4 = new Room(); Room end = new Room();
            Door d1 = new Door();
            Door d2 = new Door(); Door d3 = new Door(); Door d4 = new Door(); Door d5 = new Door();
            Door exit = new Door();
            root.AddRoom(r1);
            r1.AddRoom(r2);
            r1.AddRoom(r3);
            root.AddRoom(r4);
            r4.AddRoom(end);
            root.AddDoor(d1);
            r1.AddDoor(d2);
            r1.AddDoor(d3);
            root.AddDoor(d4);
            r4.AddDoor(d5);
            end.AddDoor(exit);

            d1.AddDescriptor(3);

            d2.AddDescriptor(5);

            d3.AddDescriptor(4);

            d4.AddDescriptor(5);
            d5.AddDescriptor(3);
            exit.AddDescriptor(2);
            button1.Text = DoorName(root.GetDoor(0));
            button2.Text = DoorName(root.GetDoor(1));
            poo.SetRoom(root);
            pictureBox2.Hide();
            button3.Hide();
            pictureBox3.Hide();
            label1.Text = "Energy: " + poo.GetEnergy().ToString();
        }
        private string DoorName(Door d) {
            string openclose = " (open)";
            if (d.GetDescriptors()[0] == 0)
            {
                openclose = " (closed)";
            }
            if (d.GetDescriptors()[1] == 2)
            {
                return "Exit"+openclose;
            }
            if(d.GetDescriptors()[1] == 3)
            {
                return "Exceptionally Normal Door" + openclose;
            }
            if (d.GetDescriptors()[1] == 4)
            {
                return "Normal Door" + openclose;
            }
            if (d.GetDescriptors()[1] == 5)
            {
                return "Magical Door" + openclose;
            }
            return "Door lol" + openclose;
        }
        private void button1_Click(object sender, EventArgs e)
        {
            
            if (poo.GetRoom().GetDoor(0).GetDescriptors()[1] == 2)
            {
                pictureBox2.Location = pictureBox1.Location;
                pictureBox2.Show();
            }
            else
            {
                poo.ChangeEnergy(-1);
                label1.Text = "Energy: " + poo.GetEnergy().ToString();
                if (!(poo.GetRoom().GetDoor(0).IsOpen())) { poo.GetRoom().GetDoor(0).OpenToggle(); }
                poo.SetRoom(poo.GetRoom().GetRoom(0));
                if (poo.GetRoom().GetDoor(0) != null)
                {
                    button1.Show();
                    button1.Text = DoorName(poo.GetRoom().GetDoor(0));
                }
                else
                { button1.Hide(); }
                if (poo.GetRoom().GetDoor(1) != null)
                {
                    button2.Show();
                    button2.Text = DoorName(poo.GetRoom().GetDoor(1));
                }
                else
                { button2.Hide(); }
                if (poo.GetRoom().GetDoor(0) == null && poo.GetRoom().GetDoor(1) == null)
                {
                    button3.Show();
                }
            }
            if (poo.GetEnergy() < 0)
            {
                button1.Hide();
                button2.Hide();
                pictureBox3.Location = new Point(150,0);
                pictureBox3.Show();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            
            if (poo.GetRoom().GetDoor(1).GetDescriptors()[1] == 2)
            {
                pictureBox2.Location = pictureBox1.Location;
                pictureBox2.Show();
            }
            else
            {
                poo.ChangeEnergy(-1);
                if (!(poo.GetRoom().GetDoor(1).IsOpen())){ poo.GetRoom().GetDoor(1).OpenToggle(); }
                label1.Text = "Energy: " + poo.GetEnergy().ToString();
                poo.SetRoom(poo.GetRoom().GetRoom(1));
                if (poo.GetRoom().GetDoor(0) != null)
                {
                    button1.Show();
                    button1.Text = DoorName(poo.GetRoom().GetDoor(0));
                }
                else
                { button1.Hide(); }
                if (poo.GetRoom().GetDoor(1) != null)
                {
                    button2.Show();
                    button2.Text = DoorName(poo.GetRoom().GetDoor(1));
                }
                else
                { button2.Hide(); }
                if (poo.GetRoom().GetDoor(0) == null && poo.GetRoom().GetDoor(1) == null)
                {
                    button3.Show();
                }
            }
            if (poo.GetEnergy() < 0)
            {
                button1.Hide();
                button2.Hide();
                pictureBox3.Location = new Point(150, 0);
                pictureBox3.Show();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            button1.Text = DoorName(root.GetDoor(0));
            button2.Text = DoorName(root.GetDoor(1));
            button3.Hide();
            button1.Show();
            button2.Show();
            poo.ChangeEnergy(-10);
            label1.Text = "Energy: " + poo.GetEnergy().ToString();
            poo.SetRoom(root);
        }

        private void exitbutton_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
