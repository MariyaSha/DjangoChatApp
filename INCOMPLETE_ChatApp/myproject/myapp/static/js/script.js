console.log("this message will be printed in the console");

if (document.getElementById('bottom_of_chat'))
{
	// element is found on the page
	document.getElementById('message_board').scrollTo(0, document.body.scrollHeight + 1000);
}


