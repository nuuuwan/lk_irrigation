# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--04_00:14:33-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **224,223 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 00:14:33 | Badalgama (Maha Oya) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:08:53 | Rathnapura (Kalu Ganga) | 7.90 | 🟠 Minor Flood | -0.102 |  |
| 2026-08-04 00:06:57 | Pitabeddara (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-08-04 00:06:26 | Hanwella (Kelani Ganga) | 7.01 | 🟡 Alert | 0.094 | 🔺 Rising |
| 2026-08-04 00:06:04 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.039 |  |
| 2026-08-04 00:06:04 | Kithulgala (Kelani Ganga) | 3.05 | 🟡 Alert | -0.032 |  |
| 2026-08-04 00:06:02 | Badalgama (Maha Oya) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:05:54 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-04 00:05:34 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-04 00:04:52 | Norwood (Kelani Ganga) | 1.56 | 🟡 Alert | -0.116 |  |
| 2026-08-04 00:04:52 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | -0.088 |  |
| 2026-08-04 00:04:50 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:04:45 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:04:45 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:03:52 | Giriulla (Maha Oya) | 4.53 | 🟢 Normal | -0.198 |  |
| 2026-08-04 00:03:25 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:02:55 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-04 00:02:39 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-04 00:02:38 | Panadugama (Nilwala Ganga) | 4.85 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-08-04 00:02:35 | Deraniyagala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.079 |  |
| 2026-08-04 00:02:34 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-04 00:02:30 | Peradeniya (Mahaweli Ganga) | 7.76 | 🟠 Minor Flood | -0.339 |  |
| 2026-08-04 00:02:29 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:02:28 | Thawalama (Gin Ganga) | 3.58 | 🟢 Normal | -0.129 |  |
| 2026-08-04 00:01:50 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:01:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:01:42 | Ellagawa (Kalu Ganga) | 8.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-04 00:01:38 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:01:35 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:01:18 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:01:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:01:02 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-04 00:00:42 | Nawalapitiya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.313 |  |
| 2026-08-03 23:41:20 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-04 00:08:53 | Rathnapura (Kalu Ganga) | 7.90 | 🟠 Minor Flood | -0.102 |  |
| 2026-08-04 00:02:30 | Peradeniya (Mahaweli Ganga) | 7.76 | 🟠 Minor Flood | -0.339 |  |
| 2026-08-04 00:06:26 | Hanwella (Kelani Ganga) | 7.01 | 🟡 Alert | 0.094 | 🔺 Rising |
| 2026-08-04 00:06:04 | Kithulgala (Kelani Ganga) | 3.05 | 🟡 Alert | -0.032 |  |
| 2026-08-03 23:11:01 | Glencourse (Kelani Ganga) | 16.38 | 🟡 Alert | -0.045 |  |
| 2026-08-04 00:04:52 | Norwood (Kelani Ganga) | 1.56 | 🟡 Alert | -0.116 |  |
| 2026-08-04 00:02:38 | Panadugama (Nilwala Ganga) | 4.85 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-08-04 00:06:57 | Pitabeddara (Nilwala Ganga) | 2.63 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-08-04 00:02:34 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-03 23:08:11 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | 0.067 | 🔺 Rising |
| 2026-08-04 00:02:55 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-08-04 00:05:54 | Moraketiya (Walawe Ganga) | 1.32 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-04 00:01:42 | Ellagawa (Kalu Ganga) | 8.24 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-03 22:36:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.80 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-04 00:01:02 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-04 00:05:34 | Baddegama (Gin Ganga) | 2.39 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-04 00:01:18 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:01:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:01:38 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:01:03 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:01:35 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:03:25 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:04:50 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:14:33 | Badalgama (Maha Oya) | 3.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:02:29 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-03 18:03:22 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:04:45 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:01:50 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:04:45 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-04 00:02:39 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-04 00:06:04 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.039 |  |
| 2026-08-03 23:13:30 | Magura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.058 |  |
| 2026-08-03 18:00:23 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | -0.070 |  |
| 2026-08-04 00:02:35 | Deraniyagala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.079 |  |
| 2026-08-04 00:04:52 | Holombuwa (Kelani Ganga) | 1.49 | 🟢 Normal | -0.088 |  |
| 2026-08-04 00:02:28 | Thawalama (Gin Ganga) | 3.58 | 🟢 Normal | -0.129 |  |
| 2026-08-04 00:03:52 | Giriulla (Maha Oya) | 4.53 | 🟢 Normal | -0.198 |  |
| 2026-08-04 00:00:42 | Nawalapitiya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.313 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)