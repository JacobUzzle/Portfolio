using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Item
    {


        public List<int> descriptors;
        public Item()
        {
            descriptors = new List<int>();
                }
        public void Use(Player p)
        {
            /*o	Pre: the player has been instantiated, and has this item in their inventory. The player has a 
             * value representing their current state.
o	Post: executes the item’s passive ability. This will vary depending on the object. 
Something about the player (energy, inventory, location) OR the room they are in OR one of the items in the
user’s inventory may be changed.
*/
        }
        public void Passive(Player p)
        {
            /*o	Pre: the player has been instantiated, and has this item in their inventory. 
             * The player has a value representing their current state.
o	Post: executes the item’s passive ability. This will vary depending on the object. Something about the 
player (energy, inventory, location) OR the room they are in OR one of the items in the user’s inventory may be
changed.
*/
        }
        public List<int> GetDescriptors()
        {
            ///  Pre: this item has a list of descriptors
            ///  Post: returns a list of descriptors describing different aspects of the item
            return descriptors;
        }
        public void AddDescriptor(int desc)
        {
            ///	Pre: this item has a list of descriptors. This does not have to be empty. Desc is a descriptor
            /// Post: adds desc to the list of descriptors
            descriptors.Add(desc);
        }
        public void RemoveDescriptor(int desc)
        {
            /// Pre: this item has a list of descriptors that is not empty, desc is a descriptor.
            /// Post: removes descriptor desc from the list of descriptors for this room\
            descriptors.Remove(desc);
        }
        public void ClearDescriptors()
        {
            ///Pre: this item has a list of descriptors
            ///Post: removes all descriptors from this object
            descriptors.Clear();
        }
    }
}
