#include <stdio.h>
#include <time.h>
#include <unistd.h>

#define ERROR_FILE_OPEN -1
#define SUCCESS 0

int printDatetime(int);


int main(){
    int cnt = 0;
    while(1){
        if(ERROR_FILE_OPEN == printDatetime(cnt)){
            return -1;
        }
        if(cnt > 50){
            return 0;
        }
        cnt ++;

    }
}

int printDatetime(int num){
    FILE* fp;
    char* filename = "./outputNums.log";
    char date[64];
    time_t t;
    if((fp = fopen(filename, "a")) == NULL){
        fprintf(stderr, "[[[ERROR]]] Failed to open FILE\"%s\"\n", filename);
        return ERROR_FILE_OPEN;
    }
    
    t = time(NULL);
    strftime(date, sizeof(date), "%Y/%m/%d %H:%M:%S", localtime(&t));
    fprintf(fp, "%s [%d]\n", date, num);
    fclose(fp);
    sleep(1);
    return SUCCESS;
}