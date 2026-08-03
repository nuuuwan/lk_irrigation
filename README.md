# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_13:10:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,806 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 13:10:13 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | -0.082 |  |
| 2026-08-03 13:08:39 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:07:04 | Kithulgala (Kelani Ganga) | 7.18 | 🔴 Major Flood | -0.308 |  |
| 2026-08-03 13:06:24 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-08-03 13:06:17 | Glencourse (Kelani Ganga) | 13.68 | 🟢 Normal | -0.137 |  |
| 2026-08-03 13:05:58 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:05:07 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-03 13:05:01 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:04:57 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2026-08-03 13:04:49 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:04:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-03 13:04:43 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:04:41 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.147 |  |
| 2026-08-03 13:04:17 | Hanwella (Kelani Ganga) | 5.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-03 13:04:12 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-03 13:04:11 | Deraniyagala (Kelani Ganga) | 5.25 | 🟡 Alert | 1.933 | 🔺 Rising |
| 2026-08-03 13:03:59 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:03:40 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.119 |  |
| 2026-08-03 13:03:13 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-03 13:03:09 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-08-03 13:02:58 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-08-03 13:02:56 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:02:42 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-08-03 13:02:29 | Nawalapitiya (Mahaweli Ganga) | 7.86 | 🔴 Major Flood | 0.207 | 🔺 Rising |
| 2026-08-03 13:02:13 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:02:10 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-08-03 13:02:03 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-03 13:01:51 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:01:50 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:01:46 | Peradeniya (Mahaweli Ganga) | 7.20 | 🟠 Minor Flood | 0.673 | 🔺 Rising |
| 2026-08-03 13:01:31 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:01:26 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:01:22 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:01:16 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.049 |  |
| 2026-08-03 13:00:43 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:00:38 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 13:02:29 | Nawalapitiya (Mahaweli Ganga) | 7.86 | 🔴 Major Flood | 0.207 | 🔺 Rising |
| 2026-08-03 13:07:04 | Kithulgala (Kelani Ganga) | 7.18 | 🔴 Major Flood | -0.308 |  |
| 2026-08-03 13:01:46 | Peradeniya (Mahaweli Ganga) | 7.20 | 🟠 Minor Flood | 0.673 | 🔺 Rising |
| 2026-08-03 12:12:03 | Norwood (Kelani Ganga) | 3.19 | 🟠 Minor Flood | -0.097 |  |
| 2026-08-03 13:04:11 | Deraniyagala (Kelani Ganga) | 5.25 | 🟡 Alert | 1.933 | 🔺 Rising |
| 2026-08-03 12:06:55 | Rathnapura (Kalu Ganga) | 6.52 | 🟡 Alert | 0.142 | 🔺 Rising |
| 2026-08-03 13:04:57 | Holombuwa (Kelani Ganga) | 1.48 | 🟢 Normal | 0.514 | 🔺 Rising |
| 2026-08-03 13:03:09 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-08-03 13:02:42 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-08-03 13:02:03 | Ellagawa (Kalu Ganga) | 7.58 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-03 13:05:07 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-08-03 13:04:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.19 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-03 13:04:12 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-03 13:04:17 | Hanwella (Kelani Ganga) | 5.20 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-03 13:01:26 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:05:58 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:04:43 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:01:22 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:02:13 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:01:51 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:01:50 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:08:39 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:03:59 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:04:49 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:00:43 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:05:01 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:00:38 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 13:01:31 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-03 12:01:37 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | -0.005 |  |
| 2026-08-03 13:06:24 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | -0.010 |  |
| 2026-08-03 13:02:10 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-08-03 13:03:13 | Thaldena (Mahaweli Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-03 13:02:58 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | -0.011 |  |
| 2026-08-03 13:01:16 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.049 |  |
| 2026-08-03 12:04:16 | Magura (Kalu Ganga) | 2.21 | 🟢 Normal | -0.077 |  |
| 2026-08-03 13:10:13 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | -0.082 |  |
| 2026-08-03 13:03:40 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.119 |  |
| 2026-08-03 13:06:17 | Glencourse (Kelani Ganga) | 13.68 | 🟢 Normal | -0.137 |  |
| 2026-08-03 13:04:41 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)