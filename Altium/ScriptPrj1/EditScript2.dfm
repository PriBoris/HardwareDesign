object WelcomeForm1: TWelcomeForm1
  Left = 0
  Top = 0
  Caption = 'Welcome'
  ClientHeight = 213
  ClientWidth = 312
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  OldCreateOrder = False
  PixelsPerInch = 96
  TextHeight = 13
  object bDisplay: TButton
    Left = 24
    Top = 24
    Width = 75
    Height = 25
    Caption = 'Display'
    TabOrder = 0
    OnClick = bDisplayClick
  end
  object bClose: TButton
    Left = 128
    Top = 24
    Width = 75
    Height = 25
    Caption = 'Close'
    TabOrder = 1
    OnClick = bCloseClick
  end
end
