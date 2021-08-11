/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution 
{
    public ListNode partition(ListNode head, int x) 
    {
        
        List<ListNode> minNodes = new ArrayList<ListNode>();
        List<ListNode> maxNodes = new ArrayList<ListNode>();
        
        
        if(head==null){
            return head;
        }
        else
        {
            ListNode currNode = head;
            while(currNode!=null)
            {
                if(currNode.val < x)
                {
                    int size = minNodes.size();
                    if(size > 0)
                    {
                        ListNode temp = minNodes.get(size-1);
                        temp.next = currNode;
                        minNodes.add(currNode);
                    }
                    else
                    {
                        minNodes.add(currNode);
                    }
                }
                else
                {
                    int size = maxNodes.size();
                    if(size > 0)
                    {
                        ListNode temp = maxNodes.get(size-1);
                        temp.next = currNode;
                        maxNodes.add(currNode);
                    }
                    else
                    {
                        maxNodes.add(currNode);
                    }
                }
                currNode = currNode.next;
            }
        
            int minNodeSize = minNodes.size();
            int maxNodeSize = maxNodes.size();
            if(minNodeSize == 0)
            {
                return maxNodes.get(0);
            }
            else if(maxNodeSize == 0)
            {
                return minNodes.get(0);
            }
            else{
                minNodes.get(minNodeSize-1).next = maxNodes.get(0);
                maxNodes.get(maxNodeSize - 1 ).next = null;
                return minNodes.get(0);
            }

    }
}
}