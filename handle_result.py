
def content_parsing(result):
    analyze_str = result.split("#step3_start#")[1]
    analyze_content = analyze_str.split("#step3_end#")[0].strip()

    mes1_str = result.split("#mes1_start#")[1]
    mes1_content = mes1_str.split("#mes1_end#")[0].strip()

    mes2_str = result.split("#mes2_start#")[1]
    mes2_content = mes2_str.split("#mes2_end#")[0].strip()

    mes3_str = result.split("#mes3_start#")[1]
    mes3_content = mes3_str.split("#mes3_end#")[0].strip()

    return analyze_content, mes1_content, mes2_content, mes3_content
