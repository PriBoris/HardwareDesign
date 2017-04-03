
Procedure RunWelcomeForm;
Begin
WelcomeForm1.ShowModal;
End;

Procedure TWelcomeForm1.bDisplayClick(Sender: TObject);
Begin
ShowMessage('welcome to AD scripting system');
End;

Procedure TWelcomeForm1.bCloseClick(Sender: TObject);
Begin
Close;
End;

