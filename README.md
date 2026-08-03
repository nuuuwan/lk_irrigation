# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_03:07:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,311 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 03:07:45 | Rathnapura (Kalu Ganga) | 7.65 | 🟠 Minor Flood | -0.083 |  |
| 2026-08-04 03:07:18 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-04 03:06:57 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:06:36 | Badalgama (Maha Oya) | 4.76 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-08-04 03:05:35 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-04 03:05:11 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:04:54 | Nawalapitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.068 |  |
| 2026-08-04 03:04:49 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-08-04 03:04:35 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-04 03:04:26 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-08-04 03:04:25 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-08-04 03:03:47 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:03:19 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.042 |  |
| 2026-08-04 03:03:13 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-04 03:03:03 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:02:55 | Thawalama (Gin Ganga) | 3.06 | 🟢 Normal | -0.170 |  |
| 2026-08-04 03:02:53 | Peradeniya (Mahaweli Ganga) | 6.20 | 🟡 Alert | -0.796 |  |
| 2026-08-04 03:02:51 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:02:44 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:02:43 | Ellagawa (Kalu Ganga) | 8.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 03:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-08-04 03:02:31 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:02:19 | Giriulla (Maha Oya) | 3.20 | 🟢 Normal | -0.446 |  |
| 2026-08-04 03:02:02 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:01:21 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:01:19 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:28:14 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:26:42 | Peradeniya (Mahaweli Ganga) | 6.68 | 🟡 Alert | -0.796 |  |
| 2026-08-04 02:24:24 | Rathnapura (Kalu Ganga) | 7.71 | 🟠 Minor Flood | -0.083 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 03:07:45 | Rathnapura (Kalu Ganga) | 7.65 | 🟠 Minor Flood | -0.083 |  |
| 2026-08-04 02:05:25 | Hanwella (Kelani Ganga) | 7.15 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-08-04 03:02:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.10 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-08-04 02:07:54 | Glencourse (Kelani Ganga) | 16.00 | 🟡 Alert | -0.293 |  |
| 2026-08-04 03:02:53 | Peradeniya (Mahaweli Ganga) | 6.20 | 🟡 Alert | -0.796 |  |
| 2026-08-04 03:04:26 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 180.000 | 🔺 Rising |
| 2026-08-04 00:06:57 | Pitabeddara (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-08-04 03:06:36 | Badalgama (Maha Oya) | 4.76 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-08-04 03:04:35 | Nagalagam Street (Kelani Ganga) | 1.10 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-04 02:02:20 | Dunamale (Aththanagalu Oya) | 1.52 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-04 03:07:18 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-04 03:03:13 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-04 02:16:23 | Putupaula (Kalu Ganga) | 1.78 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-04 03:02:43 | Ellagawa (Kalu Ganga) | 8.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-04 03:05:35 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-04 01:16:29 | Panadugama (Nilwala Ganga) | 4.86 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-04 03:01:19 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:01:21 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:03:47 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:02:02 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:05:11 | Norwood (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:02:44 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:02:31 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:03:03 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:02:51 | Thalgahagoda (Nilwala Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-08-04 03:06:57 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 02:01:45 | Moraketiya (Walawe Ganga) | 1.29 | 🟢 Normal | -0.020 |  |
| 2026-08-04 03:04:49 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-08-04 01:06:52 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | -0.029 |  |
| 2026-08-04 03:03:19 | Urawa (Nilwala Ganga) | 0.81 | 🟢 Normal | -0.042 |  |
| 2026-08-03 23:13:30 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.058 |  |
| 2026-08-04 03:04:54 | Nawalapitiya (Mahaweli Ganga) | 2.78 | 🟢 Normal | -0.068 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-04 02:08:37 | Kithulgala (Kelani Ganga) | 2.82 | 🟢 Normal | -0.113 |  |
| 2026-08-04 01:03:21 | Deraniyagala (Kelani Ganga) | 1.71 | 🟢 Normal | -0.138 |  |
| 2026-08-04 03:02:55 | Thawalama (Gin Ganga) | 3.06 | 🟢 Normal | -0.170 |  |
| 2026-08-04 03:02:19 | Giriulla (Maha Oya) | 3.20 | 🟢 Normal | -0.446 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)