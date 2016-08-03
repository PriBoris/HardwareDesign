function ViaCreation() {
var Board; //IPCB_Board;
var Via;   //IPCB_Via;

    Board = PCBServer.GetCurrentPCBBoard;
    if (Board != Null){

       for(var i=0;i<10;i++){
                        Via           = PCBServer.PCBObjectFactory(eViaObject, eNoDimension, eCreate_Default);
                        Via.X         = MMsToCoord(20+10*i);
                        Via.Y         = MMsToCoord(0);
                        Via.Size      = MMsToCoord(0.9);
                        Via.HoleSize  = MMsToCoord(0.4);
                        Via.LowLayer  = eTopLayer;
                        Via.HighLayer = eBottomLayer;
                        Board.AddPCBObject(Via);

       }

        ShowMessage("info: via created");
    } else {
        ShowMessage("ERROR: board not found");
    }
}
