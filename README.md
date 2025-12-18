# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--19_03:16:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **21,818 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 03:16:00 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:13:15 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -54.000 |  |
| 2025-12-19 03:13:13 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -54.000 |  |
| 2025-12-19 03:13:12 | Glencourse (Kelani Ganga) | 8.98 | 🟢 Normal | -54.000 |  |
| 2025-12-19 03:12:43 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.026 |  |
| 2025-12-19 03:12:41 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:12:07 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:10:37 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-19 03:07:56 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2025-12-19 03:07:42 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:06:45 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-19 03:06:31 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:06:07 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-19 03:05:54 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.033 |  |
| 2025-12-19 03:05:52 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.023 |  |
| 2025-12-19 03:05:48 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-19 03:04:44 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.057 |  |
| 2025-12-19 03:04:38 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:04:09 | Nakkala (Kumbukkan Oya) | 1.82 | 🟢 Normal | -0.064 |  |
| 2025-12-19 03:03:26 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:03:22 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:03:18 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | -0.051 |  |
| 2025-12-19 03:03:15 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-19 03:03:14 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2025-12-19 03:03:12 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:02:51 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 03:02:42 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:02:42 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 03:02:29 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -0.070 |  |
| 2025-12-19 03:02:17 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:02:17 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:02:15 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.013 |  |
| 2025-12-19 03:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.078 |  |
| 2025-12-19 03:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:01:50 | Horowpothana (Yan Oya) | 5.73 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-19 03:01:31 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:01:13 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 03:01:11 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:00:32 | Manampitiya (Mahaweli Ganga) | 4.99 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-19 03:00:32 | Manampitiya (Mahaweli Ganga) | 4.99 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-18 18:06:17 | Thanthirimale (Malwathu Oya) | 5.40 | 🟡 Alert | 0.074 | 🔺 Rising |
| 2025-12-19 03:05:48 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2025-12-19 03:01:50 | Horowpothana (Yan Oya) | 5.73 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2025-12-18 18:02:47 | Weraganthota (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2025-12-19 03:06:45 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2025-12-19 03:02:51 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 03:02:42 | Kithulgala (Kelani Ganga) | 1.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2025-12-19 03:10:37 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2025-12-19 03:01:13 | Moragaswewa (Deduru Oya) | 1.50 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-18 18:06:01 | Galgamuwa (Mee Oya) | 1.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2025-12-19 03:02:17 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:02:07 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:02:17 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:03:26 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:01:31 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:03:12 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:04:38 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:03:22 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:16:00 | Panadugama (Nilwala Ganga) | 2.71 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:01:11 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:06:31 | Dunamale (Aththanagalu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:12:41 | Urawa (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:02:42 | Kuda Oya (Kirindi Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2025-12-19 03:03:15 | Magura (Kalu Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2025-12-19 03:06:07 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2025-12-19 03:03:14 | Katharagama (Menik Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2025-12-19 03:07:56 | Rathnapura (Kalu Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2025-12-19 03:02:15 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.013 |  |
| 2025-12-19 03:05:52 | Thawalama (Gin Ganga) | 1.35 | 🟢 Normal | -0.023 |  |
| 2025-12-19 03:12:43 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.026 |  |
| 2025-12-19 02:09:20 | Deraniyagala (Kelani Ganga) | 0.45 | 🟢 Normal | -0.029 |  |
| 2025-12-19 03:05:54 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | -0.033 |  |
| 2025-12-19 03:03:18 | Padiyathalawa (Maduru Oya) | 1.80 | 🟢 Normal | -0.051 |  |
| 2025-12-19 03:04:44 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.057 |  |
| 2025-12-19 03:04:09 | Nakkala (Kumbukkan Oya) | 1.82 | 🟢 Normal | -0.064 |  |
| 2025-12-19 03:02:29 | Siyambalanduwa (Heda Oya) | 1.31 | 🟢 Normal | -0.070 |  |
| 2025-12-19 03:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.34 | 🟢 Normal | -0.078 |  |
| 2025-12-19 03:13:15 | Glencourse (Kelani Ganga) | 8.95 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)