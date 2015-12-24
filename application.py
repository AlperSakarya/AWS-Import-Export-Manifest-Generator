from flask import Flask, render_template, request
from forms import S3ImportForm

# EB looks for an 'application' callable by default.
application = Flask(__name__)
application.secret_key = 'myappseckey'

@application.route('/')
def mainpage():
    return render_template('index.html')

@application.route('/s3im', methods=['GET', 'POST'])
def s3im():
    form = S3ImportForm()
    if request.method == 'GET':
        return render_template('s3im.html', form=form)
    elif request.method == 'POST':
        deviceId = form.deviceId.data
        notificationEmail = form.notificationEmail.data
        acl = form.acl.data
        bucket = form.bucket.data
        logPrefix = form.logPrefix.data
        prefix = form.prefix.data
        logBucket = form.logBucket.data
        trueCryptPassword = form.trueCryptPassword.data
        pinCode = form.pinCode.data
        cacheControl = form.cacheControl.data
        contentDisposition = form.contentDisposition.data
        contentLanguage = form.contentLanguage.data
        contentTypes = form.contentTypes.data
        diskTimestampMetadataKey = form.diskTimestampMetadataKey.data
        expires = form.expires.data
        ignore = form.ignore.data
        setContentEncodingForGzFiles = form.setContentEncodingForGzFiles.data
        staticMetadata = form.staticMetadata.data
        storageClass = form.storageClass.data
        substitutions = form.substitutions.data
        serviceLevel = form.serviceLevel.data
        name = form.name.data
        company = form.company.data
        street1 = form.street1.data
        street2 = form.street2.data
        street3 = form.street3.data
        city = form.city.data
        stateOrProvince = form.stateOrProvince.data
        postalCode = form.postalCode.data
        phoneNumber = form.phoneNumber.data
        country = form.country.data
        dataDescription = form.dataDescription.data
        encryptedData = form.encryptedData.data
        exportCertifierName = form.exportCertifierName.data
        requiresExportLicense = form.requiresExportLicense.data
        deviceValue = form.deviceValue.data
        deviceCountryOfOrigin = form.deviceCountryOfOrigin.data
        deviceType = form.deviceType.data
        typeOfExport = form.typeOfExport.data
        return render_template('s3imresults.html', form=form)


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

