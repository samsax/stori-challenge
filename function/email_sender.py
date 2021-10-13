import boto3
from botocore.exceptions import ClientError
class SendMail:
    def __init__(self,summary):
        self.summary = summary
    # Replace sender@example.com with your "From" address.
    # This address must be verified with Amazon SES.
    SENDER = "Stori <samuelarenas@hotmail.es>"

    # Replace recipient@example.com with a "To" address. If your account 
    # is still in the sandbox, this address must be verified.
    RECIPIENT = "samuelsaxofon@gmail.com"

    # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
    AWS_REGION = "us-east-2"

    # The subject line for the email.
    SUBJECT = "Resumen de transacciones"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Resumen de transacciones\r\n")
                
    # The HTML body of the email.
    BODY_HTML = """
                    <!DOCTYPE HTML
                    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
                    xmlns:o="urn:schemas-microsoft-com:office:office">

                    <head>

                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta name="x-apple-disable-message-reformatting">
                    <!--[if !mso]><!-->
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <!--<![endif]-->
                    <title></title>

                    <style type="text/css">
                        table,
                        td {
                        color: #000000;
                        }

                        a {
                        color: #0000ee;
                        text-decoration: underline;
                        }

                        @media (max-width: 480px) {
                        #u_content_image_1 .v-text-align {
                            text-align: center !important;
                        }

                        #u_content_heading_1 .v-font-size {
                            font-size: 24px !important;
                        }

                        #u_content_heading_3 .v-font-size {
                            font-size: 16px !important;
                        }

                        #u_content_button_4 .v-padding {
                            padding: 15px !important;
                        }

                        #u_content_heading_13 .v-font-size {
                            font-size: 16px !important;
                        }

                        #u_column_4 .v-col-padding {
                            padding: 0px !important;
                        }

                        #u_content_heading_4 .v-font-size {
                            font-size: 16px !important;
                        }
                        }

                        @media only screen and (min-width: 620px) {
                        .u-row {
                            width: 600px !important;
                        }

                        .u-row .u-col {
                            vertical-align: top;
                        }

                        .u-row .u-col-50 {
                            width: 300px !important;
                        }

                        .u-row .u-col-100 {
                            width: 600px !important;
                        }

                        }

                        @media (max-width: 620px) {
                        .u-row-container {
                            max-width: 100% !important;
                            padding-left: 0px !important;
                            padding-right: 0px !important;
                        }

                        .u-row .u-col {
                            min-width: 320px !important;
                            max-width: 100% !important;
                            display: block !important;
                        }

                        .u-row {
                            width: calc(100% - 40px) !important;
                        }

                        .u-col {
                            width: 100% !important;
                        }

                        .u-col>div {
                            margin: 0 auto;
                        }
                        }

                        body {
                        margin: 0;
                        padding: 0;
                        }

                        table,
                        tr,
                        td {
                        vertical-align: top;
                        border-collapse: collapse;
                        }

                        .ie-container table,
                        .mso-container table {
                        table-layout: fixed;
                        }

                        * {
                        line-height: inherit;
                        }

                        a[x-apple-data-detectors='true'] {
                        color: inherit !important;
                        text-decoration: none !important;
                        }

                        @media (max-width: 480px) {
                        .hide-mobile {
                            max-height: 0px;
                            overflow: hidden;
                            display: none !important;
                        }

                        }
                    </style>



                    </head>

                    <body class="clean-body u_body"
                    style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #ffffff;color: #000000">

                    <table
                        style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #ffffff;width:100%"
                        cellpadding="0" cellspacing="0">
                        <tbody>
                        <tr style="vertical-align: top">
                            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">

                            <div class="u-row-container" style="padding: 0px;background-color: transparent">
                                <div class="u-row"
                                style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #e4f9f5;">
                                <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
                                    <div class="u-col u-col-50"
                                    style="max-width: 320px;min-width: 300px;display: table-cell;vertical-align: top;">
                                    <div style="width: 100% !important;">

                                        <div class="v-col-padding"
                                        style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">


                                        <table id="u_content_image_1" style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                            cellpadding="0" cellspacing="0" width="100%" border="0">
                                            <tbody>
                                            <tr>
                                                <td
                                                style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 10px 20px;font-family:arial,helvetica,sans-serif;"
                                                align="left">

                                                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                                                    <tr>
                                                    <td class="v-text-align" style="padding-right: 0px;padding-left: 0px;" align="left">

                                                        <img align="left" border="0" src="images/image-1.png" alt="Logo" title="Logo"
                                                        style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: inline-block !important;border: none;height: auto;float: none;width: 55%;max-width: 148.5px;"
                                                        width="148.5" />

                                                    </td>
                                                    </tr>
                                                </table>

                                                </td>
                                            </tr>
                                            </tbody>
                                        </table>


                                        </div>
                                    </div>
                                    <div class="u-col u-col-50"
                                        style="max-width: 320px;min-width: 300px;display: table-cell;vertical-align: top;">
                                        <div style="width: 100% !important;">
                                        <div class="v-col-padding"
                                            style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

                                            <table class="hide-mobile" style="font-family:arial,helvetica,sans-serif;" role="presentation"
                                            cellpadding="0" cellspacing="0" width="100%" border="0">
                                            <tbody>
                                                <tr>
                                                <td
                                                    style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                                                    align="left">

                                                    <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0"
                                                    width="100%"
                                                    style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #e4f9f5;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                    <tbody>
                                                        <tr style="vertical-align: top">
                                                        <td
                                                            style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                            <span>&#160;</span>
                                                        </td>
                                                        </tr>
                                                    </tbody>
                                                    </table>

                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                                </div>
                                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                                <div class="u-row"
                                    style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #0a81ab;">
                                    <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">

                                    <div class="u-col u-col-100"
                                        style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                                        <div style="width: 100% !important;">
                                        <div class="v-col-padding"
                                            style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">


                                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                                            cellspacing="0" width="100%" border="0">
                                            <tbody>
                                                <tr>
                                                <td
                                                    style="overflow-wrap:break-word;word-break:break-word;padding:20px 10px 10px;font-family:arial,helvetica,sans-serif;"
                                                    align="left">

                                                    <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0"
                                                    width="100%"
                                                    style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #0a81ab;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                    <tbody>
                                                        <tr style="vertical-align: top">
                                                        <td
                                                            style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                            <span>&#160;</span>
                                                        </td>
                                                        </tr>
                                                    </tbody>
                                                    </table>

                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>

                                            <table id="u_content_heading_1" style="font-family:arial,helvetica,sans-serif;"
                                            role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                            <tbody>
                                                <tr>
                                                <td
                                                    style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                                                    align="left">

                                                    <h1 class="v-text-align v-font-size"
                                                    style="margin: 0px; color: #e4f9f5; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: arial black,avant garde,arial; font-size: 28px;">
                                                    Resumen de transaciones
                                                    </h1>

                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>

                                            <table id="u_content_heading_3" style="font-family:arial,helvetica,sans-serif;"
                                            role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                            <tbody>
                                                <tr>
                                                <td
                                                    style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                                                    align="left">

                                                    <h4 class="v-text-align v-font-size"
                                                    style="margin: 0px; color: #e4f9f5; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: arial black,avant garde,arial; font-size: 16px;">
                                                    Saldo actual
                                                    </h4>

                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>

                                            <table id="u_content_button_4" style="font-family:arial,helvetica,sans-serif;"
                                            role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                            <tbody>
                                                <tr>
                                                <td
                                                    style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                                                    align="left">

                                                    <div class="v-text-align" align="center">
                                                    <a href="https://unlayer.com/" target="_blank"
                                                        style="box-sizing: border-box;display: inline-block;font-family:arial,helvetica,sans-serif;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #0a81ab; border-radius: 50px;-webkit-border-radius: 50px; -moz-border-radius: 50px; width:auto; max-width:100%; overflow-wrap: break-word; word-break: break-word; word-wrap:break-word; mso-border-alt: none;border-top-color: #e4f9f5; border-top-style: solid; border-top-width: 4px; border-left-color: #e4f9f5; border-left-style: solid; border-left-width: 4px; border-right-color: #e4f9f5; border-right-style: solid; border-right-width: 4px; border-bottom-color: #e4f9f5; border-bottom-style: solid; border-bottom-width: 4px;">
                                                        <span class="v-padding" style="display:block;padding:20px;line-height:120%;"></span>
                                                    </a>

                                                    </div>

                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>

                                            <table id="u_content_heading_13" style="font-family:arial,helvetica,sans-serif;"
                                            role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                            <tbody>
                                                <tr>
                                                <td
                                                    style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                                                    align="left">

                                                    <h4 class="v-text-align v-font-size"
                                                    style="margin: 0px; color: #e4f9f5; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: arial black,avant garde,arial; font-size: 16px;">
                                                    Resumen
                                                    </h4>

                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>

                                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                                            cellspacing="0" width="100%" border="0">
                                            <tbody>
                                                <tr>
                                                <td
                                                    style="overflow-wrap:break-word;word-break:break-word;padding:20px 10px 10px;font-family:arial,helvetica,sans-serif;"
                                                    align="left">

                                                    <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0"
                                                    width="100%"
                                                    style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #0a81ab;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                    <tbody>
                                                        <tr style="vertical-align: top">
                                                        <td
                                                            style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                            <span>&#160;</span>
                                                        </td>
                                                        </tr>
                                                    </tbody>
                                                    </table>

                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                                </div>



                                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                                <div class="u-row"
                                    style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #0c4271;">
                                    <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">

                                    <div class="u-col u-col-100"
                                        style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                                        <div style="width: 100% !important;">
                                        <div class="v-col-padding"
                                            style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">
                                            <!--<![endif]-->

                                            <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0"
                                            cellspacing="0" width="100%" border="0">
                                            <tbody>
                                                <tr>
                                                <td
                                                    style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                                                    align="left">

                                                    <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0"
                                                    width="100%"
                                                    style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #0c4271;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                    <tbody>
                                                        <tr style="vertical-align: top">
                                                        <td
                                                            style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
                                                            <span>&#160;</span>
                                                        </td>
                                                        </tr>
                                                    </tbody>
                                                    </table>

                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                                </div>



                                <div class="u-row-container" style="padding: 0px;background-color: transparent">
                                <div class="u-row"
                                    style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: #0c4271;">
                                    <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">

                                    <div id="u_column_4" class="u-col u-col-100"
                                        style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
                                        <div style="width: 100% !important;">
                                        <div class="v-col-padding"
                                            style="padding: 0px 0px 0px 10px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">
                                            <!--<![endif]-->

                                            <table id="u_content_heading_4" style="font-family:arial,helvetica,sans-serif;"
                                            role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                                            <tbody>
                                                <tr>
                                                <td
                                                    style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;"
                                                    align="left">

                                                    <h3 class="v-text-align v-font-size"
                                                    style="margin: 0px; color: #ffffff; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: arial,helvetica,sans-serif; font-size: 18px;">

                                                    </h3>

                                                </td>
                                                </tr>
                                            </tbody>
                                            </table>
                                        </div>
                                        </div>
                                    </div>
                                    </div>
                                </div>
                                </div>

                            </td>
                        </tr>
                        </tbody>
                    </table>
                    </body>

                    </html>
                """            

    # The character encoding for the email.
    CHARSET = "UTF-8"
    def send(self):
        # Create a new SES resource and specify a region.
        client = boto3.client('ses',region_name=self.AWS_REGION)

        # Try to send the email.
        try:
            #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        self.RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': self.CHARSET,
                            'Data': self.BODY_HTML,
                        },
                        'Text': {
                            'Charset': self.CHARSET,
                            'Data': self.BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': self.CHARSET,
                        'Data': self.SUBJECT,
                    },
                },
                Source=self.SENDER,
            )
        # Display an error if something goes wrong.	
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])