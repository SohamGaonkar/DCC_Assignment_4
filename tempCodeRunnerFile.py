    # else:
    #     page = request.args.get('page', 1, type=int)
    #     offset = (page - 1) * per_page
        
    #     try:
    #         cursor = mysql.connection.cursor()
    #         cursor.execute("SELECT COUNT(*) FROM purchase_details ")
    #         total_records = cursor.fetchone()[0]
    #         total_pages = total_records // per_page
    #         if total_records % per_page != 0:
    #             total_pages += 1
            
    #         cursor.execute("SELECT DISTINCT `Name of the Purchaser` FROM purchase_details")
    #         company_names = [row[0] for row in cursor.fetchall()]
            
    #         cursor.execute("SELECT * FROM purchase_details LIMIT %s OFFSET %s", (per_page, offset))
    #         entire_table = cursor.fetchall()
    #         column_headers = [i[0] for i in cursor.description]
    #         cursor.close()
            
    #         return render_template("home.html", static_data=entire_table, responsive_data=None, headers=column_headers, total_pages=total_pages, current_page=page, company_names=company_names)
    #     except SQLAlchemyError as e:
    #         return render_template("error.html", error=str(e))
    #     except Exception as e:
    #         return render_template("error.html", error=str(e))