# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Migrationhistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=255)  # Field name made lowercase.
    model = models.BinaryField(db_column='Model')  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__MigrationHistory'


class TBrand(models.Model):
    brandid = models.AutoField(db_column='BrandId', primary_key=True)  # Field name made lowercase.
    brandcode = models.TextField(db_column='BrandCode', blank=True, null=True)  # Field name made lowercase.
    branddesc = models.TextField(db_column='BrandDesc', blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive')  # Field name made lowercase.
    brandlevel = models.IntegerField(db_column='BrandLevel', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    brandpos = models.IntegerField(db_column='BrandPos', blank=True, null=True)  # Field name made lowercase.
    uploadstatus = models.SmallIntegerField(db_column='UploadStatus', blank=True, null=True)  # Field name made lowercase.
    uploaddate = models.DateTimeField(db_column='UploadDate', blank=True, null=True)  # Field name made lowercase.
    downloaddate = models.DateTimeField(db_column='DownloadDate', blank=True, null=True)  # Field name made lowercase.
    rowstatus = models.SmallIntegerField(db_column='RowStatus', blank=True, null=True)  # Field name made lowercase.
    terminal = models.SmallIntegerField(db_column='Terminal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_Brand'


class TCustomer(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', primary_key=True)  # Field name made lowercase.
    customername = models.TextField(db_column='CustomerName', blank=True, null=True)  # Field name made lowercase.
    parentcustomerid = models.IntegerField(db_column='ParentCustomerId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_Customer'


class TDmsconsumer(models.Model):
    consumerid = models.IntegerField(db_column='ConsumerId', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.
    consumercode = models.TextField(db_column='ConsumerCode', blank=True, null=True)  # Field name made lowercase.
    consumername = models.TextField(db_column='ConsumerName')  # Field name made lowercase.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    phoneno = models.TextField(db_column='PhoneNo', blank=True, null=True)  # Field name made lowercase.
    contactno = models.TextField(db_column='ContactNo')  # Field name made lowercase.
    email = models.TextField(db_column='Email')  # Field name made lowercase.
    dateofbirth = models.DateTimeField(db_column='DateofBirth')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSConsumer'


class TDmsdiscounttype(models.Model):
    discounttypeid = models.SmallIntegerField(db_column='DiscountTypeId', primary_key=True)  # Field name made lowercase.
    discounttypename = models.TextField(db_column='DiscountTypeName', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSDiscountType'


class TDmsoutlet(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', primary_key=True)  # Field name made lowercase.
    outletname = models.TextField(db_column='OutletName', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    contactperson = models.TextField(db_column='ContactPerson', blank=True, null=True)  # Field name made lowercase.
    contactno = models.TextField(db_column='ContactNo', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSOutlet'


class TDmsproductstock(models.Model):
    productid = models.IntegerField(db_column='ProductId', primary_key=True)  # Field name made lowercase.
    distributorid = models.IntegerField(db_column='DistributorId')  # Field name made lowercase.
    currentstock = models.IntegerField(db_column='CurrentStock')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSProductStock'
        unique_together = (('productid', 'distributorid'),)


class TDmsproductstockserial(models.Model):
    tranid = models.IntegerField(db_column='TranId', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductId')  # Field name made lowercase.
    productserial = models.CharField(db_column='ProductSerial', max_length=128)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSProductStockSerial'
        unique_together = (('tranid', 'productid', 'productserial'),)


class TDmsproductstocktran(models.Model):
    tranid = models.IntegerField(db_column='TranId', primary_key=True)  # Field name made lowercase.
    tranno = models.TextField(db_column='TranNo', blank=True, null=True)  # Field name made lowercase.
    trandate = models.DateTimeField(db_column='TranDate')  # Field name made lowercase.
    trantype = models.IntegerField(db_column='TranType')  # Field name made lowercase.
    transide = models.IntegerField(db_column='TranSide')  # Field name made lowercase.
    fromcustomerid = models.IntegerField(db_column='FromCustomerId')  # Field name made lowercase.
    tocustomerid = models.IntegerField(db_column='ToCustomerId')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    refinvoiceid = models.IntegerField(db_column='RefInvoiceId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSProductStockTran'


class TDmsproductstocktranitem(models.Model):
    tranid = models.IntegerField(db_column='TranId', primary_key=True)  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductId')  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty')  # Field name made lowercase.
    costprice = models.FloatField(db_column='CostPrice')  # Field name made lowercase.
    salesprice = models.FloatField(db_column='SalesPrice')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSProductStockTranItem'
        unique_together = (('tranid', 'productid'),)


class TDmspromoappliedtoinvoice(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    promotype = models.TextField(db_column='PromoType', blank=True, null=True)  # Field name made lowercase.
    promoid = models.IntegerField(db_column='PromoId')  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductId')  # Field name made lowercase.
    invoiceid = models.IntegerField(db_column='InvoiceId')  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSPromoAppliedToInvoice'


class TDmssalesinvoice(models.Model):
    invoiceid = models.IntegerField(db_column='InvoiceId', primary_key=True)  # Field name made lowercase.
    invoiceno = models.TextField(db_column='InvoiceNo', blank=True, null=True)  # Field name made lowercase.
    invoicedate = models.DateTimeField(db_column='InvoiceDate')  # Field name made lowercase.
    invoicetypeid = models.IntegerField(db_column='InvoiceTypeId')  # Field name made lowercase.
    customerid = models.ForeignKey(TCustomer, models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.
    invoiceamount = models.FloatField(db_column='InvoiceAmount')  # Field name made lowercase.
    discountamount = models.FloatField(db_column='DiscountAmount')  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    consumerid = models.ForeignKey(TDmsconsumer, models.DO_NOTHING, db_column='ConsumerId')  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    reverseapplydate = models.DateTimeField(db_column='ReverseApplyDate', blank=True, null=True)  # Field name made lowercase.
    reversereviseuserid = models.IntegerField(db_column='ReverseReviseUserId', blank=True, null=True)  # Field name made lowercase.
    reverserevisedate = models.DateTimeField(db_column='ReverseReviseDate', blank=True, null=True)  # Field name made lowercase.
    refinvoiceid = models.IntegerField(db_column='RefInvoiceId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSSalesInvoice'


class TDmssalesinvoicedetail(models.Model):
    invoicedetailid = models.IntegerField(db_column='InvoiceDetailId', primary_key=True)  # Field name made lowercase.
    invoiceid = models.IntegerField(db_column='InvoiceId')  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductId')  # Field name made lowercase.
    barcodeserial = models.TextField(db_column='BarcodeSerial', blank=True, null=True)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice')  # Field name made lowercase.
    costprice = models.FloatField(db_column='CostPrice')  # Field name made lowercase.
    isfreeproduct = models.BooleanField(db_column='IsFreeProduct')  # Field name made lowercase.
    freeqty = models.IntegerField(db_column='FreeQty')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSSalesInvoiceDetail'


class TDmssalesinvoicewarrantycardno(models.Model):
    warrantycardid = models.IntegerField(db_column='WarrantyCardId', primary_key=True)  # Field name made lowercase.
    outletid = models.IntegerField(db_column='OutletId')  # Field name made lowercase.
    invoiceid = models.IntegerField(db_column='InvoiceId')  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductId')  # Field name made lowercase.
    warrantycardno = models.TextField(db_column='WarrantyCardNo', blank=True, null=True)  # Field name made lowercase.
    productserialno = models.TextField(db_column='ProductSerialNo', blank=True, null=True)  # Field name made lowercase.
    warrantyparameterid = models.IntegerField(db_column='WarrantyParameterId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSSalesInvoiceWarrantyCardNo'


class TDmssecondarysalesorder(models.Model):
    orderid = models.IntegerField(db_column='OrderId', primary_key=True)  # Field name made lowercase.
    orderno = models.TextField(db_column='OrderNo', blank=True, null=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WarehouseId')  # Field name made lowercase.
    salestype = models.IntegerField(db_column='SalesType')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.
    parentcustomerid = models.IntegerField(db_column='ParentCustomerId')  # Field name made lowercase.
    edd = models.DateTimeField(db_column='Edd')  # Field name made lowercase.
    orderamount = models.FloatField(db_column='OrderAmount')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    refinvoiceno = models.TextField(db_column='RefInvoiceNo', blank=True, null=True)  # Field name made lowercase.
    refinvoicedate = models.DateTimeField(db_column='RefInvoiceDate', blank=True, null=True)  # Field name made lowercase.
    updateuserid = models.IntegerField(db_column='UpdateUserId', blank=True, null=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    authorizedby = models.IntegerField(db_column='AuthorizedBy', blank=True, null=True)  # Field name made lowercase.
    authorizedate = models.DateTimeField(db_column='AuthorizeDate', blank=True, null=True)  # Field name made lowercase.
    authorizeremarks = models.TextField(db_column='AuthorizeRemarks', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSSecondarySalesOrder'


class TDmssecondarysalesorderdetail(models.Model):
    orderid = models.IntegerField(db_column='OrderId', primary_key=True)  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WarehouseId')  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductId')  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice')  # Field name made lowercase.
    orderqty = models.IntegerField(db_column='OrderQty')  # Field name made lowercase.
    confirmedqty = models.IntegerField(db_column='ConfirmedQty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSSecondarySalesOrderDetail'
        unique_together = (('orderid', 'warehouseid', 'productid'),)


class TDmsuser(models.Model):
    userid = models.IntegerField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.
    userfullname = models.TextField(db_column='UserFullName', blank=True, null=True)  # Field name made lowercase.
    username = models.TextField(db_column='UserName')  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    salt = models.TextField(db_column='Salt', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.IntegerField(db_column='CreateUserId')  # Field name made lowercase.
    role = models.TextField(db_column='Role', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DMSUser'


class TDatatransfer(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    tablename = models.TextField(db_column='TableName', blank=True, null=True)  # Field name made lowercase.
    dataid = models.BigIntegerField(db_column='DataId')  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WarehouseId')  # Field name made lowercase.
    transfertype = models.IntegerField(db_column='TransferType')  # Field name made lowercase.
    isdownload = models.IntegerField(db_column='IsDownload')  # Field name made lowercase.
    batchno = models.IntegerField(db_column='BatchNo')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DataTransfer'


class TDmsinvoicediscount(models.Model):
    discountid = models.IntegerField(db_column='DiscountId', primary_key=True)  # Field name made lowercase.
    invoiceid = models.IntegerField(db_column='InvoiceId')  # Field name made lowercase.
    discounttypeid = models.SmallIntegerField(db_column='DiscountTypeId')  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_DmsInvoiceDiscount'


class TProduct(models.Model):
    productid = models.IntegerField(db_column='ProductId', primary_key=True)  # Field name made lowercase.
    productcode = models.TextField(db_column='ProductCode', blank=True, null=True)  # Field name made lowercase.
    productname = models.TextField(db_column='ProductName', blank=True, null=True)  # Field name made lowercase.
    productdesc = models.TextField(db_column='ProductDesc', blank=True, null=True)  # Field name made lowercase.
    productmodel = models.TextField(db_column='ProductModel', blank=True, null=True)  # Field name made lowercase.
    productgroupid = models.ForeignKey('TProductgroup', models.DO_NOTHING, db_column='ProductGroupId')  # Field name made lowercase.
    brandid = models.ForeignKey(TBrand, models.DO_NOTHING, db_column='BrandId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_Product'


class TProductgroup(models.Model):
    pdtgroupid = models.IntegerField(db_column='PdtGroupId', primary_key=True)  # Field name made lowercase.
    pdtgroupname = models.TextField(db_column='PdtGroupName', blank=True, null=True)  # Field name made lowercase.
    groupsort = models.IntegerField(db_column='GroupSort')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ProductGroup'


class TShowroom(models.Model):
    showroomid = models.IntegerField(db_column='ShowroomId', primary_key=True)  # Field name made lowercase.
    showroomcode = models.TextField(db_column='ShowroomCode', blank=True, null=True)  # Field name made lowercase.
    showroomname = models.TextField(db_column='ShowroomName', blank=True, null=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CustomerId')  # Field name made lowercase.
    warehouseid = models.IntegerField(db_column='WarehouseId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_Showroom'


class TWarrantyparam(models.Model):
    warrantyparamid = models.IntegerField(db_column='WarrantyParamId', primary_key=True)  # Field name made lowercase.
    servicewarranty = models.IntegerField(db_column='ServiceWarranty')  # Field name made lowercase.
    partswarranty = models.IntegerField(db_column='PartsWarranty')  # Field name made lowercase.
    specialcomponentwarranty = models.IntegerField(db_column='SpecialComponentWarranty')  # Field name made lowercase.
    iscurrent = models.IntegerField(db_column='IsCurrent')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_WarrantyParam'


class VProductdetails(models.Model):
    productid = models.IntegerField(db_column='ProductId', primary_key=True)  # Field name made lowercase.
    productcode = models.TextField(db_column='ProductCode', blank=True, null=True)  # Field name made lowercase.
    productname = models.TextField(db_column='ProductName', blank=True, null=True)  # Field name made lowercase.
    asgid = models.IntegerField(db_column='AsgId')  # Field name made lowercase.
    asgname = models.TextField(db_column='AsgName', blank=True, null=True)  # Field name made lowercase.
    magid = models.IntegerField(db_column='MagId')  # Field name made lowercase.
    magname = models.TextField(db_column='MagName', blank=True, null=True)  # Field name made lowercase.
    brandid = models.IntegerField(db_column='BrandId')  # Field name made lowercase.
    branddesc = models.TextField(db_column='BrandDesc', blank=True, null=True)  # Field name made lowercase.
    costprice = models.FloatField(db_column='CostPrice')  # Field name made lowercase.
    rsp = models.FloatField(db_column='Rsp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'v_ProductDetails'
