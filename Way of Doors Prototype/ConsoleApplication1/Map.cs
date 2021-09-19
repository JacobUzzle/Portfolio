using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;
using System.IO;


namespace ConsoleApplication1
{
    [Serializable()]
    public class Map
    {
        Room root;
        public byte maxdoors, maxlevel, mindoors, minlevel;
        public ushort maxrooms, minrooms;
        public ushort portalchance, maptype;
        //private List<Room> roomtypes;
        // private List<uint> roomchances;
        public List<Room> rooms;

        public Map()
        {
            /*o	Pre: the map doesn’t exist yet.
o	Post: creates a map with a root room of null
o	Variables: Max doors each room may have, max level the map may go to, the minimum number of doors each room may 
have (excluding dead-ends, which must always be able to appear), the minimum number of levels that the map may have,
the maximum number of rooms the map may have, the minimum number of rooms the map may have (supersedes the minimum 
number of levels), hasPortals that represents whether or not the map has portal doors, List with links to all rooms 
in the map
The  maximum number of levels will take precedence over the minimum number of rooms. The minumum
number of levels will take precedence over the maximum number of rooms. If the minimum 
number of rooms is greater than the number of levels that can hold that, it will stop adding rooms.
If the maximum  room number is less than the amount in the minimum number of levels, it will keep adding
rooms until the minimum number of levels is filled out.
Portal chance will be the chance out of 10,000 that a room will have a portal if it does not have the maximum
number of doors.
*/
            root = null;
            maxdoors = 2;
            mindoors = 1;
            maxlevel = 8;
            minlevel = 3;
            maxrooms = 100;
            minrooms = 70;
            portalchance = 25;
            maptype = 0;
            rooms = new List<Room>();
            //rooms.Add(root);
            //Each slot in roomchances corresponds to the TypeID of the corresponding room type
            //roomchances = new List<uint>();

        }
        private Room GetRoomType(string roomfile, string chancefile, int seed)
        {
            /*Pre: roomfile is the file name of a serialized list of rooms without any links to other rooms.
             * chancefile is a file name of a serialized list of nonzero unsigned integers with the frequency of each room 
             * in the corresponding room file being represented at that position in the chance file.
             * Both the chancefile and roomfile must represent lists with an equal count.
             *
             * Seed is an integer.
             Post: returns the room at that based off the seed-created randomly-generated index 
             in the deserialized list. 
             Returns null  if the index is greater than the count of the list itself.*/
            //Load the room and the chances.
            var roompath = Environment.CurrentDirectory + "//" + roomfile;
            var chancepath = Environment.CurrentDirectory + "//" + chancefile;

            XmlSerializer roomreader = new XmlSerializer(typeof(List<Room>));
            StreamReader roomreadfile = new StreamReader(roompath);
            List<Room> roomdata = (List<Room>)roomreader.Deserialize(roomreadfile);
            roomreadfile.Close();
            XmlSerializer chancereader = new XmlSerializer(typeof(List<uint>));
            StreamReader chancereadfile = new StreamReader(chancepath);
            List<uint> chancedata = (List<uint>)roomreader.Deserialize(chancereadfile);
            chancereadfile.Close();
            //Randomly assign the index a value based off the seed
            Random rand = new Random(seed);
            int index = rand.Next();
            //Run through the chance list
            uint sum = 0;
            for (int i = 0; i < chancedata.Count; i++)
            {
                //Compute the sum of this value with all previous chances
                sum = sum + chancedata[i];
                //If the index we are looking for is below or equal to the current sum
                //that means that the index was greater than the previous sum values, and
                //thus outside the range of those values.
                if (index <= sum)
                {
                    return roomdata[i];
                }
            }
            return null;
        }
        private Door GetDoorType(string doorfile, string chancefile, int seed)
        {
            /*Pre: roomfile is the file name of a serialized list of rooms without any links to other rooms.
             * chancefile is a file name of a serialized list of nonzero unsigned integers with the frequency of each room 
             * in the corresponding room file being represented at that position in the chance file.
             * Both the chancefile and roomfile must represent lists with an equal count.
             *
             * Seed is an integer.
             Post: returns the room at that based off the seed-created randomly-generated index 
             in the deserialized list. 
             Returns null  if the index is greater than the count of the list itself.*/
            //Load the room and the chances.
            var roompath = Environment.CurrentDirectory + "//" + doorfile;
            var chancepath = Environment.CurrentDirectory + "//" + chancefile;

            XmlSerializer doorreader = new XmlSerializer(typeof(List<Door>));
            StreamReader doorreadfile = new StreamReader(roompath);
            List<Door> doordata = (List<Door>)doorreader.Deserialize(doorreadfile);
            doorreadfile.Close();
            XmlSerializer chancereader = new XmlSerializer(typeof(List<uint>));
            StreamReader chancereadfile = new StreamReader(chancepath);
            List<uint> chancedata = (List<uint>)doorreader.Deserialize(chancereadfile);
            chancereadfile.Close();
            //Randomly assign the index a value based off the seed
            Random rand = new Random(seed);
            int index = rand.Next();
            //Run through the chance list
            uint sum = 0;
            for (int i = 0; i < chancedata.Count; i++)
            {
                //Compute the sum of this value with all previous chances
                sum = sum + chancedata[i];
                //If the index we are looking for is below or equal to the current sum
                //that means that the index was greater than the previous sum values, and
                //thus outside the range of those values and inside the range of the values above it
                if (index <= sum)
                {
                    return doordata[i];
                }
            }
            return null;
        }
        public void AddRoom(Room r)
        {
            rooms.Add(r);
        }
        public Room GetRoom(int i)
        {
            return rooms[i];
        }
        public void Generate(int seed, byte maxdrs, byte mindrs, byte maxlvl, byte minlvl, ushort maxrms,
            ushort minrms, ushort prtlchnce, string roomfile, string roomchancefile, string doorchancefile,
            string doorfile)
        {
            //	Pre: seed is an integer representing the randomized seed, 
            //o	Post: Makes this map. The map will have a number of random elements using the seed variable. 
            //Each room will have a maximum number of doors equal to maxdoors, a minimum number of doors each 
            //room may have equal to mindoors (dead ends will appear no matter what), the maximum number of levels
            //of the map equal to maxlevel, the minimum number of levels of the map equal to minlevel. Maxrooms will
            //be the maximum number of rooms allowed in the map, and minrooms will be the minimum number of rooms.
            //string maptype 

            /*var roompath = Environment.CurrentDirectory + "//" + roomfile;
            var chancepath = Environment.CurrentDirectory + "//" + chancefile;
            XmlSerializer roomreader = new XmlSerializer(typeof(List<Room>));
            StreamReader roomreadfile = new StreamReader(roompath);
            List<Room> roomdata = (List<Room>)roomreader.Deserialize(roomreadfile);
            roomreadfile.Close();
            XmlSerializer chancereader = new XmlSerializer(typeof(List<uint>));
            StreamReader chancereadfile = new StreamReader(chancepath);
            List<uint> chancedata = (List<uint>)roomreader.Deserialize(chancereadfile);
            chancereadfile.Close();*/
            maxdoors = maxdrs;
            mindoors = mindrs;
            maxlevel = maxlvl;
            minlevel = minlvl;
            maxrooms = maxrms;
            minrooms = minrms;
            portalchance = prtlchnce;
            Random rand = new Random(seed);
            //Duplicate rooms will be added at the indices in temprooms as in rooms
            //in order to keep track of the rooms that haven't been given 'child' rooms
            //(basically rooms that it has doors to that are 1 level below it)
            List<Room> temprooms = new List<Room>();
            //Adding random rooms until the minimum number of rooms is met
            for (int i = 0; i < minrooms; i++)
            {
                Room r = GetRoomType(roomfile, roomchancefile, seed);
                //r.SetUniqueID(i);
                temprooms.Add(r);
            }
            //Add the rest of the rooms between the minimum number of rooms
            //and the maximum number of rooms
            int addamount = rand.Next(0, maxrooms-minrooms);
            for (int i = minrooms; i < minrooms+addamount; i++)
            {
                Room r = GetRoomType(roomfile, roomchancefile, seed);
                //r.SetUniqueID(i);
                temprooms.Add(r);
            }
            //Implementing the map creation using a queue
            List<Room> roomqueue = new List<Room>();
            roomqueue.Add(temprooms[0]);
            rooms.Add(temprooms[0]);
            temprooms.RemoveAt(0);
            //Puts the end location above the index
            //Stops incrementing end location once the current level is 1
            //before the max
            //Stops the loop entirely once the current index is greater than
            //or equal to the end location
            int endlocation = 1;
            int index = 0;
            for (int i = 0; endlocation > index && temprooms != null; i++)
            {

                for (int j = 1; j < mindoors && temprooms != null; j++)
                {
                    int randindex = rand.Next(0, temprooms.Count);
                    temprooms[randindex].SetLevel(i);
                    roomqueue[0].AddRoom(temprooms[randindex]);
                    rooms.Add(temprooms[randindex]);
                    roomqueue.Add(temprooms[randindex]);
                    temprooms.RemoveAt(randindex);
                    if(minlevel > i+1)
                    endlocation++;
                }
                    roomqueue.RemoveAt(0);
                    index++;
            }
            //Implementation adding the rest of the rooms.
            for (int i = 0; temprooms != null; i++)
            {
                //int index = 0;
                //While the queue is not empty
                while (roomqueue != null && temprooms != null)
                {
                    int randdoors = rand.Next(mindoors-1,maxdoors);
                    if (randdoors < mindoors) {
                        //If this has less than the minimum number of doors, 
                        // don't give it any doors
                    }
                    else
                    {
                        //Move the number of next rooms to be added from the temporary room list
                        //to the room queue
                        for (int j = 0; j < randdoors && temprooms != null; j++)
                        {

                            int randindex = rand.Next(0, temprooms.Count);
                            temprooms[randindex].SetLevel(i+1);
                            roomqueue[0].AddRoom(temprooms[randindex]);
                            rooms.Add(temprooms[randindex]);
                            roomqueue.Add(temprooms[randindex]);
                            temprooms.RemoveAt(randindex);
                            endlocation++;


                        }
                    }
                    roomqueue.RemoveAt(0);
                }
            }
            temprooms = null;
            for(int i = 0; i < rooms.Count; i++)
            {
                rooms[i].SetUniqueID(i);
            }

            //Loop through the list of rooms and give them doors equal to the number of rooms
            //they have links to. The door at the corresponding list location will lead to the
            //corresponding room.

        }
    }
}
