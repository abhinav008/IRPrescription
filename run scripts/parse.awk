#!/usr/bin/gawk
BEGIN{
count=0;
}
{
count++;
if(count >5){
	print $2
	}
}
END{
}
