# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_10:32:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,693 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 10:32:50 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:22:23 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:20:50 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-08-03 10:17:54 | Norwood (Kelani Ganga) | 3.06 | 🟠 Minor Flood | 0.772 | 🔺 Rising |
| 2026-08-03 10:17:09 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:14:35 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:13:46 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.038 |  |
| 2026-08-03 10:12:12 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.084 |  |
| 2026-08-03 10:09:58 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-03 10:09:38 | Peradeniya (Mahaweli Ganga) | 6.78 | 🟡 Alert | -0.331 |  |
| 2026-08-03 10:09:10 | Kithulgala (Kelani Ganga) | 2.99 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-08-03 10:07:28 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:06:43 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-08-03 10:06:25 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-03 10:06:20 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-03 10:06:02 | Rathnapura (Kalu Ganga) | 6.46 | 🟡 Alert | -0.094 |  |
| 2026-08-03 10:05:36 | Hanwella (Kelani Ganga) | 4.97 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-08-03 10:05:30 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-03 10:04:40 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:04:19 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-03 10:04:10 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-03 10:04:09 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-08-03 10:04:00 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.068 |  |
| 2026-08-03 10:03:47 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.033 |  |
| 2026-08-03 10:03:32 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-08-03 10:03:30 | Pitabeddara (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.168 |  |
| 2026-08-03 10:03:20 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.05 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-03 10:02:45 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 10:02:17 | Nawalapitiya (Mahaweli Ganga) | 4.60 | 🟡 Alert | 0.520 | 🔺 Rising |
| 2026-08-03 10:02:16 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:02:16 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:02:08 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.020 |  |
| 2026-08-03 10:01:59 | Glencourse (Kelani Ganga) | 14.21 | 🟢 Normal | -0.172 |  |
| 2026-08-03 10:01:23 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:00:41 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:00:40 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:00:37 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:00:17 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-03 10:00:08 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 10:17:54 | Norwood (Kelani Ganga) | 3.06 | 🟠 Minor Flood | 0.772 | 🔺 Rising |
| 2026-08-03 10:02:17 | Nawalapitiya (Mahaweli Ganga) | 4.60 | 🟡 Alert | 0.520 | 🔺 Rising |
| 2026-08-03 10:06:02 | Rathnapura (Kalu Ganga) | 6.46 | 🟡 Alert | -0.094 |  |
| 2026-08-03 10:09:38 | Peradeniya (Mahaweli Ganga) | 6.78 | 🟡 Alert | -0.331 |  |
| 2026-08-03 10:09:10 | Kithulgala (Kelani Ganga) | 2.99 | 🟢 Normal | 0.286 | 🔺 Rising |
| 2026-08-03 10:03:32 | Giriulla (Maha Oya) | 1.31 | 🟢 Normal | 0.247 | 🔺 Rising |
| 2026-08-03 10:05:36 | Hanwella (Kelani Ganga) | 4.97 | 🟢 Normal | 0.197 | 🔺 Rising |
| 2026-08-03 10:04:09 | Ellagawa (Kalu Ganga) | 7.30 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-08-03 10:04:10 | Deraniyagala (Kelani Ganga) | 1.95 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-08-03 10:09:58 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-03 10:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.05 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-03 10:06:20 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-08-03 10:04:19 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-03 10:06:25 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-03 10:00:17 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-03 10:00:08 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 10:02:45 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 10:00:37 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:17:09 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:01:23 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:22:23 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:02:16 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:32:50 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:00:41 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:03:20 | Dunamale (Aththanagalu Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:04:40 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:14:35 | Badalgama (Maha Oya) | 2.17 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:00:40 | Thanthirimale (Malwathu Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:07:28 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-03 10:20:50 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-08-03 10:05:30 | Holombuwa (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-08-03 10:06:43 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2026-08-03 10:02:08 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | -0.020 |  |
| 2026-08-03 10:03:47 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.033 |  |
| 2026-08-03 10:13:46 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.038 |  |
| 2026-08-03 10:04:00 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.068 |  |
| 2026-08-03 10:12:12 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | -0.084 |  |
| 2026-08-03 10:03:30 | Pitabeddara (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.168 |  |
| 2026-08-03 10:01:59 | Glencourse (Kelani Ganga) | 14.21 | 🟢 Normal | -0.172 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)