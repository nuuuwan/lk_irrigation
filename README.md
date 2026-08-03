# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_01:28:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,254 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 01:28:46 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-04 01:26:47 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:19:09 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:16:29 | Panadugama (Nilwala Ganga) | 4.86 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-04 01:16:19 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:12:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | 0.092 | 🔺 Rising |
| 2026-08-04 01:07:11 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.018 |  |
| 2026-08-04 01:06:52 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-08-04 01:06:17 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:05:41 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:04:47 | Badalgama (Maha Oya) | 4.46 | 🟢 Normal | 0.597 | 🔺 Rising |
| 2026-08-04 01:04:44 | Hanwella (Kelani Ganga) | 7.10 | 🟡 Alert | 0.093 | 🔺 Rising |
| 2026-08-04 01:04:44 | Rathnapura (Kalu Ganga) | 7.80 | 🟠 Minor Flood | -0.107 |  |
| 2026-08-04 01:04:27 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-08-04 01:04:00 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.061 |  |
| 2026-08-04 01:03:53 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-08-04 01:03:49 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-04 01:03:21 | Deraniyagala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.138 |  |
| 2026-08-04 01:03:07 | Ellagawa (Kalu Ganga) | 8.31 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-08-04 01:02:55 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-08-04 01:02:52 | Nawalapitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.241 |  |
| 2026-08-04 01:02:46 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:02:38 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-04 01:02:19 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-04 01:02:09 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 01:02:05 | Peradeniya (Mahaweli Ganga) | 7.12 | 🟠 Minor Flood | -0.644 |  |
| 2026-08-04 01:01:46 | Giriulla (Maha Oya) | 4.15 | 🟢 Normal | -0.394 |  |
| 2026-08-04 01:01:27 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:01:17 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:00:38 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 01:04:44 | Rathnapura (Kalu Ganga) | 7.80 | 🟠 Minor Flood | -0.107 |  |
| 2026-08-04 01:02:05 | Peradeniya (Mahaweli Ganga) | 7.12 | 🟠 Minor Flood | -0.644 |  |
| 2026-08-04 01:04:44 | Hanwella (Kelani Ganga) | 7.10 | 🟡 Alert | 0.093 | 🔺 Rising |
| 2026-08-04 01:12:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.04 | 🟡 Alert | 0.092 | 🔺 Rising |
| 2026-08-04 00:06:04 | Kithulgala (Kelani Ganga) | 3.05 | 🟡 Alert | -0.032 |  |
| 2026-08-03 23:11:01 | Glencourse (Kelani Ganga) | 16.38 | 🟡 Alert | -0.045 |  |
| 2026-08-04 01:04:00 | Norwood (Kelani Ganga) | 1.50 | 🟡 Alert | -0.061 |  |
| 2026-08-04 01:04:47 | Badalgama (Maha Oya) | 4.46 | 🟢 Normal | 0.597 | 🔺 Rising |
| 2026-08-04 01:04:27 | Dunamale (Aththanagalu Oya) | 1.46 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-08-04 00:06:57 | Pitabeddara (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-08-04 01:28:46 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-08-04 01:03:07 | Ellagawa (Kalu Ganga) | 8.31 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-08-03 23:08:11 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-08-04 01:02:38 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-04 01:03:49 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-04 01:02:09 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-04 01:16:29 | Panadugama (Nilwala Ganga) | 4.86 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-04 01:06:17 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:01:27 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:02:46 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:19:09 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:01:17 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:16:19 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:26:47 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:04:50 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:05:41 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 01:02:19 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-04 01:02:55 | Moraketiya (Walawe Ganga) | 1.31 | 🟢 Normal | -0.011 |  |
| 2026-08-04 01:07:11 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.018 |  |
| 2026-08-04 01:03:53 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.020 |  |
| 2026-08-04 01:06:52 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-08-03 23:13:30 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.058 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-04 00:02:28 | Thawalama (Gin Ganga) | 3.58 | 🟢 Normal | -0.129 |  |
| 2026-08-04 01:03:21 | Deraniyagala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.138 |  |
| 2026-08-04 01:02:52 | Nawalapitiya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.241 |  |
| 2026-08-04 01:01:46 | Giriulla (Maha Oya) | 4.15 | 🟢 Normal | -0.394 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)