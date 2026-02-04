# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--04_08:05:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **63,854 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **82** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-04 08:05:41 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-04 08:05:13 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-04 08:05:10 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.014 |  |
| 2026-02-04 08:05:00 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-04 08:04:37 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:04:18 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-02-04 08:04:16 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.114 |  |
| 2026-02-04 08:02:38 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-04 08:02:36 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:34 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-02-04 08:02:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:11 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:10 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:09 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:05 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:04 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:01 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:59 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:58 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:55 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:54 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:53 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:52 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:51 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:49 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.031 |  |
| 2026-02-04 08:01:49 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:46 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:45 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:43 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 08:01:43 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.075 |  |
| 2026-02-04 08:01:29 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:21 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.020 |  |
| 2026-02-04 08:01:19 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:00:49 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-02-04 08:00:09 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-04 07:24:26 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-04 07:22:03 | Baddegama (Gin Ganga) | 0.97 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:22:02 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:22:00 | Baddegama (Gin Ganga) | 0.95 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:59 | Baddegama (Gin Ganga) | 0.10 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:57 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:56 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:55 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:53 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:52 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:51 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:49 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:47 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:46 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:44 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:42 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:41 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:39 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:37 | Baddegama (Gin Ganga) | 1.08 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:35 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:34 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:32 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:30 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:28 | Baddegama (Gin Ganga) | 1.22 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:26 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:24 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:22 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:20 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:18 | Baddegama (Gin Ganga) | 1.45 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:17 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:15 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:11 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | -0.014 |  |
| 2026-02-04 07:21:01 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-04 07:18:39 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-04 07:16:02 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-04 07:15:47 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-04 07:13:52 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-04 07:13:07 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.012 |  |
| 2026-02-04 07:11:46 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-04 07:09:35 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.061 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-03 05:18:55⌛ | Magura (Kalu Ganga) | 0.88 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-02-04 08:05:00 | Hanwella (Kelani Ganga) | 0.64 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-04 07:03:19 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-04 08:02:38 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-02-04 07:13:52 | Holombuwa (Kelani Ganga) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-04 08:05:13 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-04 08:01:43 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 07:08:21 | Thaldena (Mahaweli Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-04 08:02:36 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:29 | Moragaswewa (Deduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:13 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-04 07:15:47 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:04:37 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:40:09⌛ | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-02-03 06:07:19⌛ | Ellagawa (Kalu Ganga) | 4.23 | 🟢 Normal | 0.000 |  |
| 2026-02-04 07:01:29 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:00:09 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:17 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:01:19 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.000 |  |
| 2026-02-04 07:18:39 | Urawa (Nilwala Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-04 08:02:10 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-02-04 07:06:42 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-03 07:13:11⌛ | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-02-04 08:04:18 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-02-04 08:05:41 | Dunamale (Aththanagalu Oya) | 0.31 | 🟢 Normal | -0.010 |  |
| 2026-02-04 08:02:34 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.012 |  |
| 2026-02-04 08:05:10 | Baddegama (Gin Ganga) | 0.96 | 🟢 Normal | -0.014 |  |
| 2026-02-04 08:01:21 | Weraganthota (Mahaweli Ganga) | -2.41 | 🟢 Normal | -0.020 |  |
| 2026-02-04 06:02:42 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-02-04 08:00:49 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-02-02 18:03:26⌛ | Thanthirimale (Malwathu Oya) | 2.37 | 🟢 Normal | -0.021 |  |
| 2026-02-03 09:01:34 | Galgamuwa (Mee Oya) | 0.34 | 🟢 Normal | -0.022 |  |
| 2026-02-04 08:01:49 | Panadugama (Nilwala Ganga) | 2.43 | 🟢 Normal | -0.031 |  |
| 2026-02-04 07:09:35 | Peradeniya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.061 |  |
| 2026-02-03 05:02:29⌛ | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.069 |  |
| 2026-02-04 08:01:43 | Glencourse (Kelani Ganga) | 8.63 | 🟢 Normal | -0.075 |  |
| 2026-02-04 06:02:42 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.095 |  |
| 2026-02-03 22:06:20 | Putupaula (Kalu Ganga) | 0.39 | 🟢 Normal | -0.110 |  |
| 2026-02-04 08:04:16 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.114 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)