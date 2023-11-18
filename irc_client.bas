server$ = "irc.libera.chat"
nick$ = "quickbasicIRC"
channel$ = "##anime"
client = _OpenClient("TCP/IP:6667:" + server$)
line$ = "nick " + nick$ + Chr$(10) + Chr$(13) + "user a a a a" + Chr$(10) + Chr$(13)
Put #client, , line$: Sleep 2
line$ = "join " + channel$ + Chr$(10) + Chr$(13)
Put #client, , line$: Sleep 2

Do
    _Delay 0.05 ' 50ms delay (20 checks per second)
    Get #client, , buff$
    If buff$ <> "" Then
        Print buff$
        Print ""
        Print user_input$;
        If InStr(1, buff$, "PING") = 1 Then 'handle PING
            s$ = Mid$(buff$, 5, Len(buff$)) 'get orwell.freenode.net
            line$ = "PONG" + s$ + Chr$(10) + Chr$(13)
            Print "pong reached", line$
            Put #client, , line$: Sleep 2
        End If
    End If
    k$ = InKey$
    If k$ <> "" Then
        If k$ = Chr$(8) Then
            user_input$ = Mid$(user_input$, 1, Len(user_input$) - 1)
            Print ""
            Print user_input$;
        Else If k$ = Chr$(13) Then
                line$ = "privmsg " + channel$ + " : " + user_input$ + Chr$(10) + Chr$(13)
                Put #client, , line$: Sleep 2
                user_input$ = ""
                Print ""
            Else
                user_input$ = user_input$ + k$
                Print k$; 'echo user input ; eliminates new lines
            End If
        End If
    End If
Loop
Close client

