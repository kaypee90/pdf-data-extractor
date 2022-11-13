import fitz
filename = "foo.pdf"

FIGURE_KEYWORD = "Figure"
IDLE_KEYWORD = "Idle"

with fitz.open(filename) as doc:
    page = doc[0]
    res = page.get_text("blocks")
    start_capture = False

    header = (
        f"\n========================================================================================================================\n"
        f"                    Table 2-1. Simulated fuel savings from isolated cycle improvements      \n"
        f"========================================================================================================================\n\n"
        f"Cycle         KI          Distance        Improved           Decreased           Eliminate            Decreased\n"
        f"Name        (1/km)         (mi)           Speed              Accel               Stops                Idle\n"
        f"=====      =======       ========        ========          ===========          ============        ==============\n"
    )
    print(header)

    for item in res:
        if FIGURE_KEYWORD in str(item[4]):
            break

        if start_capture:
            records = str(item[4]).split("\n")
            cycle_name = records[0]
            ki = records[1]
            distance = records[2]
            improved_speed = records[3]
            decreased_accl = records[4]
            elimiate_stops = records[5]
            decreased_idle = records[6]
            row = (
                f"{cycle_name}      {ki}         {distance}          {improved_speed}               {decreased_accl}               {elimiate_stops}               {decreased_idle} \n"
                f"=====      =======       ========        ========       ==============       ===============        ==============\n"
            )
            print(row)

        if str(item[4]).startswith(IDLE_KEYWORD):
            start_capture = True