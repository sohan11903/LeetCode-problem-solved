class MyStack {
    public int t;
    public int[] arr;
    public MyStack() {
        t = -1;
        arr = new int[100];
    }

    public void push(int x) {
        t++;
        arr[t] = x;
    }

    public int pop() {
        int temp = arr[t];
        t--;
        return temp;
    }

    public int top() {
        return arr[t];
    }

    public boolean empty() {
        return t == -1;
    }
   
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */