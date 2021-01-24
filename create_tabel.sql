CREATE TABLE [dbo].[Analyze_Stock](
	[Date] [datetime] NULL,
	[Mã ] [nvarchar](255) NULL,
	[Giá đóng cửa ] [float] NULL,
	[Thay đổi (+/-%) ] [nvarchar](255) NULL,
	[Giá tham chiếu ] [float] NULL,
	[Giá mở cửa ] [float] NULL,
	[Giá cao nhất ] [float] NULL,
	[Giá thấp nhất ] [float] NULL,
	[KLGD khớp lệnh ] [float] NULL,
	[GTGD khớp lệnh ] [float] NULL,
	[KLGD thỏa thuận ] [float] NULL,
	[GTGD thỏa thuận ] [float] NULL,
	[Dif] [float] NULL,
	[Rate_Dif/Tc] [float] NULL,
	[Date text] [nvarchar](255) NULL
) ON [PRIMARY]