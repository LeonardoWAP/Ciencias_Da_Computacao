#include <iostream>
#include <cstdlib>
#include <ctime>
#define tamanho 10
using namespace std;
typedef struct{
      int topo;
      int item[tamanho] ;
      int qtnd;
}PILHA;

void iniciaPilha (PILHA &p) { 
    p.topo = -1;
    p.qtnd = 0;
}

bool pilhaVazia(PILHA &p){
    if(p.topo == -1 )
        return true;
    else
        return false;
}

bool pilhaCheia(PILHA &p){
    if (p.topo == tamanho-1)
        return true;
    else
        return false;
}

void empilha(PILHA &p, int x){
    p.item[++p.topo]=x;
    p.qtnd++;
   

}

int desempilha(PILHA &p){
    p.qtnd--;
    return (p.item[p.topo--]) ;
    
}

int numeroAleatorio(int menor, int maior) {
       return rand()%(maior-menor+1) + menor;
}

void enchervetor(PILHA &pilha){
    srand((unsigned)time(0)); 
    //para gerar números aleatórios reais.
    for(int n = 1;n <= 10;n++){
       ;
        int aleatorio = numeroAleatorio(1, 100);
        empilha(pilha,aleatorio);
    }
}

void imprimir(PILHA p){
    for(int i=0; i< p.qtnd; i++){
        cout<<p.item[i]<<endl;
    }
}


void vencer(PILHA p){
    int cont=0;
    for(int i=0;i<tamanho-1;i++){
        if (p.item[i] <p.item[i+1]) {
            cont=cont+1;
        }
    }
    if (cont == tamanho-1){
        cout<<"!!!O senhor(a) Venceu ParaBens!!!";

    }

}


int main ()
{
int opc;
int esc;
int rec;
int des1;
int des2;
int des3;
/*incia as pilhas*/
PILHA pilha1;

iniciaPilha (pilha1);

PILHA pilha2;

iniciaPilha (pilha2);

PILHA pilha3;

iniciaPilha (pilha3);

enchervetor(pilha1);

imprimir(pilha1);

cout<< "\n0 - sair do jogo.\n1 - movimentar.\n";
cin>>opc;
while (true){
    if (opc==0){
    cout<<"finalizado!!";
    break;
    }
    if (opc==1){
        cout<<"De qual pilha deseja movimentar:  ";
        cin>>esc;
        while (esc != 1 && esc != 2 && esc != 3){
            cout<<"VALOR INVALIDO!! De qual pilha deseja movimentar:  ";
            cin>>esc;
        }

        cout<<"qual pilha irá receber:  ";
        cin>>rec;
        while ((rec != 1 && rec != 2 && rec != 3) || (esc == rec)){
            cout<<"VALOR INVALIDO!! Qual pilha irá receber:  ";
            cin>>rec;
        }
    

        if (esc == 1){
            des1=desempilha(pilha1);
            if (rec == 2){
                empilha(pilha2,des1);
            }
            if (rec == 3){
                empilha(pilha3,des1);
            }
        }
        if (esc == 2){
            des2=desempilha(pilha2);
            if (rec == 1){
                empilha(pilha1,des2);
            }
            if (rec == 3){
                empilha(pilha3,des2);
            }

        }
        if (esc == 3){
            des3=desempilha(pilha3);
             if (rec == 1){
                empilha(pilha1,des3);
            }
            if (rec == 2){
                empilha(pilha2,des3);
            }

        }
    

    }
    cout<< "PILHA 1:"<<endl;
    imprimir(pilha1);
    cout<< "PILHA 2:"<<endl;
    imprimir(pilha2);
    cout<< "PILHA 3:"<<endl;
    imprimir(pilha3);
    vencer(pilha1);
    vencer(pilha1);
    vencer(pilha1);
}
return 0;
}
