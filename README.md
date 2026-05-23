# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_21:18:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,960 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 21:18:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | 0.008 | 🔺 Rising |
| 2026-05-23 21:13:27 | Ellagawa (Kalu Ganga) | 10.26 | 🟡 Alert | 0.000 |  |
| 2026-05-23 21:10:45 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | -0.021 |  |
| 2026-05-23 21:08:51 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:08:04 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:06:45 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-05-23 21:05:55 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-23 21:05:41 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:04:54 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:04:45 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.021 |  |
| 2026-05-23 21:04:42 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-05-23 21:04:14 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-05-23 21:04:08 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-05-23 21:04:07 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-23 21:04:01 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.020 |  |
| 2026-05-23 21:03:58 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 21:03:49 | Putupaula (Kalu Ganga) | 3.20 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 21:03:33 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:03:31 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-23 21:03:23 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:03:22 | Rathnapura (Kalu Ganga) | 5.38 | 🟡 Alert | -0.082 |  |
| 2026-05-23 21:03:13 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | -0.031 |  |
| 2026-05-23 21:03:07 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-23 21:02:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-23 21:02:33 | Dunamale (Aththanagalu Oya) | 4.75 | 🟠 Minor Flood | -0.063 |  |
| 2026-05-23 21:02:31 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:02:30 | Hanwella (Kelani Ganga) | 5.76 | 🟢 Normal | -0.090 |  |
| 2026-05-23 21:02:20 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-23 21:02:12 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:02:01 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-23 21:01:56 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-23 21:01:29 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:01:29 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.177 |  |
| 2026-05-23 21:01:06 | Magura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.077 |  |
| 2026-05-23 21:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-05-23 21:00:11 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 21:18:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.68 | 🟠 Minor Flood | 0.008 | 🔺 Rising |
| 2026-05-23 21:02:33 | Dunamale (Aththanagalu Oya) | 4.75 | 🟠 Minor Flood | -0.063 |  |
| 2026-05-23 21:03:49 | Putupaula (Kalu Ganga) | 3.20 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-05-23 21:13:27 | Ellagawa (Kalu Ganga) | 10.26 | 🟡 Alert | 0.000 |  |
| 2026-05-23 21:03:22 | Rathnapura (Kalu Ganga) | 5.38 | 🟡 Alert | -0.082 |  |
| 2026-05-23 21:04:07 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-05-23 21:02:58 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-23 21:03:31 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-23 21:05:55 | Peradeniya (Mahaweli Ganga) | 1.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-05-23 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 21:03:58 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 21:05:41 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:03:23 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:01:29 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:00:11 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:04:23 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:02:31 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:02:12 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:03:33 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:04:54 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:08:51 | Manampitiya (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:08:04 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-23 21:01:56 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-23 21:04:42 | Panadugama (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.010 |  |
| 2026-05-23 21:03:07 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-05-23 18:01:26 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-23 21:00:55 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-05-23 21:02:01 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-05-23 21:02:20 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-05-23 21:04:14 | Deraniyagala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-05-23 21:04:01 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.020 |  |
| 2026-05-23 21:06:45 | Giriulla (Maha Oya) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-05-23 21:04:08 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-05-23 21:04:45 | Holombuwa (Kelani Ganga) | 0.62 | 🟢 Normal | -0.021 |  |
| 2026-05-23 21:10:45 | Baddegama (Gin Ganga) | 2.25 | 🟢 Normal | -0.021 |  |
| 2026-05-23 21:03:13 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | -0.031 |  |
| 2026-05-23 21:01:06 | Magura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.077 |  |
| 2026-05-23 21:02:30 | Hanwella (Kelani Ganga) | 5.76 | 🟢 Normal | -0.090 |  |
| 2026-05-23 21:01:29 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.177 |  |

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)