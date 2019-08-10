#include<bits/stdc++.h>
using namespace std;

class Node{
    public:
    int data;
    Node* next;
    Node(int data){
        this->data = data;
    }
};

Node* head;
void insert(int data){
    Node* temp = new Node(data);
    temp->next = head;
    head = temp;
}

void print(){
    Node* temp = head;
    while(temp != NULL){
        cout<<temp->data;
        temp = temp->next;
    }
}
int main(){
    head = NULL;
    for(int i =0; i<5; i++){
        insert(i+1);
    }

    print();
}