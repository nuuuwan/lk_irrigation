# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_17:27:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,810 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 17:27:21 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.008 |  |
| 2026-05-23 17:21:54 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:09:55 | Glencourse (Kelani Ganga) | 11.57 | 🟢 Normal | -0.112 |  |
| 2026-05-23 17:08:58 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-05-23 17:08:44 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:07:27 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-05-23 17:06:42 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.019 |  |
| 2026-05-23 17:06:35 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:06:20 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-23 17:05:48 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.022 |  |
| 2026-05-23 17:05:35 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:04:59 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:04:56 | Hanwella (Kelani Ganga) | 6.19 | 🟢 Normal | -0.107 |  |
| 2026-05-23 17:04:47 | Nagalagam Street (Kelani Ganga) | 1.23 | 🟡 Alert | 0.000 |  |
| 2026-05-23 17:04:47 | Rathnapura (Kalu Ganga) | 5.71 | 🟡 Alert | -0.052 |  |
| 2026-05-23 17:04:00 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-23 17:03:59 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.033 |  |
| 2026-05-23 17:03:43 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-05-23 17:03:37 | Magura (Kalu Ganga) | 3.42 | 🟢 Normal | -0.083 |  |
| 2026-05-23 17:03:18 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:03:14 | Dunamale (Aththanagalu Oya) | 4.94 | 🟠 Minor Flood | -0.043 |  |
| 2026-05-23 17:03:04 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-23 17:02:30 | Putupaula (Kalu Ganga) | 3.16 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-23 17:02:29 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-05-23 17:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 17:02:18 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:02:14 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:02:00 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:01:50 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:01:48 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-23 17:01:37 | Ellagawa (Kalu Ganga) | 10.28 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 17:01:22 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:01:16 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:01:11 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.083 |  |
| 2026-05-23 17:00:59 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 17:00:46 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-05-23 17:00:32 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:00:18 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:00:14 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 17:02:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.64 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-05-23 17:03:14 | Dunamale (Aththanagalu Oya) | 4.94 | 🟠 Minor Flood | -0.043 |  |
| 2026-05-23 17:02:30 | Putupaula (Kalu Ganga) | 3.16 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-23 17:01:37 | Ellagawa (Kalu Ganga) | 10.28 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 17:04:47 | Nagalagam Street (Kelani Ganga) | 1.23 | 🟡 Alert | 0.000 |  |
| 2026-05-23 17:04:47 | Rathnapura (Kalu Ganga) | 5.71 | 🟡 Alert | -0.052 |  |
| 2026-05-23 17:04:00 | Kithulgala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-23 17:00:59 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 17:00:14 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:02:14 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:06:35 | Nakkala (Kumbukkan Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:05:35 | Nawalapitiya (Mahaweli Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:01:50 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:00:32 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:02:00 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-05-23 16:07:40 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:01:16 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:03:18 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:04:59 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:08:44 | Thawalama (Gin Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:01:22 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:21:54 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:00:18 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 17:27:21 | Urawa (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.008 |  |
| 2026-05-23 17:06:20 | Holombuwa (Kelani Ganga) | 0.65 | 🟢 Normal | -0.010 |  |
| 2026-05-23 17:08:58 | Panadugama (Nilwala Ganga) | 2.72 | 🟢 Normal | -0.010 |  |
| 2026-05-23 17:03:04 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-23 17:01:48 | Thanthirimale (Malwathu Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-05-23 17:03:43 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-05-23 17:06:42 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | -0.019 |  |
| 2026-05-23 17:07:27 | Peradeniya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2026-05-23 17:02:29 | Giriulla (Maha Oya) | 1.44 | 🟢 Normal | -0.020 |  |
| 2026-05-23 17:00:46 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | -0.021 |  |
| 2026-05-23 17:05:48 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -0.022 |  |
| 2026-05-23 17:03:59 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.033 |  |
| 2026-05-23 17:03:37 | Magura (Kalu Ganga) | 3.42 | 🟢 Normal | -0.083 |  |
| 2026-05-23 17:01:11 | Deraniyagala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.083 |  |
| 2026-05-23 17:04:56 | Hanwella (Kelani Ganga) | 6.19 | 🟢 Normal | -0.107 |  |
| 2026-05-23 17:09:55 | Glencourse (Kelani Ganga) | 11.57 | 🟢 Normal | -0.112 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)