# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--23_11:24:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **159,574 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 11:24:58 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.015 |  |
| 2026-05-23 11:16:02 | Moragaswewa (Deduru Oya) | 0.74 | 🟢 Normal | -0.031 |  |
| 2026-05-23 11:11:57 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-05-23 11:10:06 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-05-23 11:08:12 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.076 |  |
| 2026-05-23 11:07:06 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-23 11:06:45 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 11:06:27 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:05:39 | Glencourse (Kelani Ganga) | 12.17 | 🟢 Normal | -0.059 |  |
| 2026-05-23 11:04:40 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:04:20 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.029 |  |
| 2026-05-23 11:04:10 | Baddegama (Gin Ganga) | 2.53 | 🟢 Normal | -0.012 |  |
| 2026-05-23 11:03:53 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:03:52 | Putupaula (Kalu Ganga) | 3.04 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-23 11:03:21 | Hanwella (Kelani Ganga) | 6.76 | 🟢 Normal | -0.090 |  |
| 2026-05-23 11:03:11 | Rathnapura (Kalu Ganga) | 6.04 | 🟡 Alert | -0.102 |  |
| 2026-05-23 11:03:06 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:03:01 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:02:57 | Nagalagam Street (Kelani Ganga) | 1.31 | 🟡 Alert | -0.033 |  |
| 2026-05-23 11:02:49 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:02:35 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 11:02:29 | Dunamale (Aththanagalu Oya) | 5.10 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-23 11:02:28 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 11:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-23 11:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.58 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-23 11:01:48 | Deraniyagala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.083 |  |
| 2026-05-23 11:01:36 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-05-23 11:01:31 | Ellagawa (Kalu Ganga) | 10.19 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-23 11:01:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:01:24 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:01:10 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:01:10 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:01:08 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:00:48 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-23 11:00:21 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.021 |  |
| 2026-05-23 11:00:21 | Magura (Kalu Ganga) | 3.76 | 🟢 Normal | -0.042 |  |
| 2026-05-23 11:00:15 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:00:15 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-23 11:02:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.58 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-05-23 11:02:29 | Dunamale (Aththanagalu Oya) | 5.10 | 🟠 Minor Flood | -0.020 |  |
| 2026-05-23 11:01:31 | Ellagawa (Kalu Ganga) | 10.19 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-23 11:03:52 | Putupaula (Kalu Ganga) | 3.04 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-05-23 11:02:57 | Nagalagam Street (Kelani Ganga) | 1.31 | 🟡 Alert | -0.033 |  |
| 2026-05-23 11:03:11 | Rathnapura (Kalu Ganga) | 6.04 | 🟡 Alert | -0.102 |  |
| 2026-05-23 11:07:06 | Badalgama (Maha Oya) | 3.29 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-23 11:02:27 | Nawalapitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-23 11:06:45 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 11:02:35 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 11:02:28 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 11:01:10 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:01:25 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:03:06 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:00:15 | Galgamuwa (Mee Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:01:10 | Padiyathalawa (Maduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:01:08 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:04:40 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:02:49 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:01:24 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:06:27 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:03:53 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:03:01 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-23 11:10:06 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | -0.009 |  |
| 2026-05-23 10:06:22 | Moraketiya (Walawe Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-05-23 11:00:15 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.010 |  |
| 2026-05-23 11:01:36 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-05-23 11:00:48 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-05-23 11:04:10 | Baddegama (Gin Ganga) | 2.53 | 🟢 Normal | -0.012 |  |
| 2026-05-23 11:24:58 | Giriulla (Maha Oya) | 1.56 | 🟢 Normal | -0.015 |  |
| 2026-05-23 11:11:57 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.019 |  |
| 2026-05-23 11:00:21 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.021 |  |
| 2026-05-23 11:04:20 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.029 |  |
| 2026-05-23 11:16:02 | Moragaswewa (Deduru Oya) | 0.74 | 🟢 Normal | -0.031 |  |
| 2026-05-23 11:00:21 | Magura (Kalu Ganga) | 3.76 | 🟢 Normal | -0.042 |  |
| 2026-05-23 11:05:39 | Glencourse (Kelani Ganga) | 12.17 | 🟢 Normal | -0.059 |  |
| 2026-05-23 11:08:12 | Panadugama (Nilwala Ganga) | 2.84 | 🟢 Normal | -0.076 |  |
| 2026-05-23 11:01:48 | Deraniyagala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.083 |  |
| 2026-05-23 11:03:21 | Hanwella (Kelani Ganga) | 6.76 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)