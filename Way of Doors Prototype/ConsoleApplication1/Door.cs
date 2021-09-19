using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Runtime.Serialization;


namespace ConsoleApplication1
{
    [Serializable()]
    public class Door
    {
        public int UID;
        public int TypeID;
        public List<int> descriptors;
        public int openEnergy,closeEnergy,passEnergy; 
        public Door()
        {
            descriptors = new List<int>();
            descriptors.Add(0);
            openEnergy = 0;
            closeEnergy = 0;
            passEnergy = 0;
        }
        public List<int> GetDescriptors()
        {
            ///  Pre: this room has a list of descriptors
            ///  Post: returns a list of descriptors describing different aspects of the room
            return descriptors;
        }
        public void AddDescriptor(int desc)
        {
            ///	Pre: this door has a list of descriptors. This does not have to be empty. Desc is a descriptor that
            ///	is not a Open/Close value for Doors
            /// Post: adds desc to the list of descriptors
            if (desc != 0 && desc != 1)
            {
                descriptors.Add(desc);
            }
            
        }
        public void RemoveDescriptor(int desc)
        {
            /// Pre: this door has a list of descriptors that is not empty, desc is a descriptor.Desc is a descriptor that
            ///	is not a Open/Close value for Doors
            /// Post: removes descriptor desc from the list of descriptors for this door. 
            if(desc != 0 && desc != 1)
            {
                descriptors.Remove(desc);
            }

    
        }
        public void ClearDescriptors()
        {
            ///Pre: this room has a list of descriptors
            ///Post: removes all descriptors from this object, then sets the door to closed.
            descriptors.Clear();
            descriptors.Add(0);
        }
        public int GetUniqueId()
        {
            ///Pre: this room has a unique ID
            ///Post: returns this room's unique ID
            return UID;
        }
        public void SetUniqueID(int id)
        {
            ///Pre: this room exists inside a map
            ///Post: sets the unique id to id
            UID = id;
        }
        public int GetTypeId()
        {
            ///Pre: this room has a unique ID
            ///Post: returns this room's unique ID
            return TypeID;
        }
        public void SetTypeID(int id)
        {
            ///Pre: this room exists inside a map
            ///Post: sets the unique id to id
            TypeID = id;
        }
        public void OpenToggle()
        {
            ///Pre: The door has a descriptor value for being open or closed.
            ///Post: Door is open if closed or closed if open
            if (descriptors[0] == 1)
            {
                descriptors[0] = 0;
            }
            else
            {
                descriptors[0] = 1;
            }
            }
        public bool IsOpen()
        {
            ///	Pre: this door exists
            /// Post: returns true if this door is open, false if it is not
            return (descriptors[0] == 1);
        }

    }
}
