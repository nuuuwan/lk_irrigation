# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_23:21:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,030 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 23:21:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 23:18:02 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:10:40 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.018 |  |
| 2026-05-23 23:10:09 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-23 23:09:22 | Rathnapura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.067 |  |
| 2026-05-23 23:07:25 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:06:56 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:06:32 | Ellagawa (Kalu Ganga) | 10.22 | 🟡 Alert | -0.025 |  |
| 2026-05-23 23:06:18 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 23:05:48 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | -0.030 |  |
| 2026-05-23 23:05:03 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-05-23 23:04:59 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-23 23:04:45 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-23 23:04:42 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:03:46 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.029 |  |
| 2026-05-23 23:03:45 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | -0.074 |  |
| 2026-05-23 23:03:43 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:03:43 | Putupaula (Kalu Ganga) | 3.23 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-23 23:03:42 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-23 23:03:37 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 23:03:33 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | -0.062 |  |
| 2026-05-23 23:03:17 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | -0.192 |  |
| 2026-05-23 23:03:03 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:02:43 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:02:25 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-23 23:02:23 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:02:14 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:02:12 | Hanwella (Kelani Ganga) | 5.56 | 🟢 Normal | -0.090 |  |
| 2026-05-23 23:02:03 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:01:54 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:01:50 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.031 |  |
| 2026-05-23 23:01:41 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-23 23:01:02 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:00:43 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 23:00:16 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:00:14 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 23:21:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-23 23:03:45 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | -0.074 |  |
| 2026-05-23 23:03:43 | Putupaula (Kalu Ganga) | 3.23 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-23 23:06:32 | Ellagawa (Kalu Ganga) | 10.22 | 🟡 Alert | -0.025 |  |
| 2026-05-23 23:09:22 | Rathnapura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.067 |  |
| 2026-05-23 23:01:41 | Peradeniya (Mahaweli Ganga) | 1.66 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-05-23 23:04:59 | Glencourse (Kelani Ganga) | 11.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-23 23:10:09 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-05-23 23:03:37 | Moragaswewa (Deduru Oya) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 23:06:18 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 23:00:43 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 21:03:58 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 23:18:02 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:03:03 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:04:42 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-23 22:01:18 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:00:16 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:04:23 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:07:25 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:00:14 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:01:54 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:01:02 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:02:43 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:06:56 | Holombuwa (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:02:14 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 23:02:25 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-05-23 23:03:42 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-05-23 18:01:26 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-23 23:04:45 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-05-23 23:05:03 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.011 |  |
| 2026-05-23 23:10:40 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.018 |  |
| 2026-05-23 22:06:16 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.019 |  |
| 2026-05-23 23:03:46 | Badalgama (Maha Oya) | 2.89 | 🟢 Normal | -0.029 |  |
| 2026-05-23 23:05:48 | Baddegama (Gin Ganga) | 2.18 | 🟢 Normal | -0.030 |  |
| 2026-05-23 23:01:50 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.031 |  |
| 2026-05-23 23:03:33 | Nagalagam Street (Kelani Ganga) | 1.07 | 🟢 Normal | -0.062 |  |
| 2026-05-23 23:02:12 | Hanwella (Kelani Ganga) | 5.56 | 🟢 Normal | -0.090 |  |
| 2026-05-23 23:03:17 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | -0.192 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)