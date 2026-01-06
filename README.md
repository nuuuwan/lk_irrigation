# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--06_17:03:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **38,350 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 17:03:37 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-06 17:03:24 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 17:03:15 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-06 17:03:03 | Nakkala (Kumbukkan Oya) | 2.11 | 🟢 Normal | -0.093 |  |
| 2026-01-06 17:02:53 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-01-06 17:02:52 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.052 |  |
| 2026-01-06 17:02:52 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.091 |  |
| 2026-01-06 17:02:40 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:02:40 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-06 17:02:40 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:02:38 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:02:36 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.012 |  |
| 2026-01-06 17:02:25 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.061 |  |
| 2026-01-06 17:02:03 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-06 17:01:55 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-06 17:01:17 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:00:59 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:00:37 | Thanthirimale (Malwathu Oya) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 17:00:33 | Siyambalanduwa (Heda Oya) | 4.76 | 🟡 Alert | -0.370 |  |
| 2026-01-06 17:00:20 | Weraganthota (Mahaweli Ganga) | -0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-06 16:56:46 | Weraganthota (Mahaweli Ganga) | -0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-06 16:24:36 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 16:16:31 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-01-06 16:14:06 | Manampitiya (Mahaweli Ganga) | 3.75 | 🟡 Alert | 0.044 | 🔺 Rising |
| 2026-01-06 16:12:58 | Nawalapitiya (Mahaweli Ganga) | 0.81 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-06 16:12:04 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 16:10:52 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.012 |  |
| 2026-01-06 16:10:43 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.030 |  |
| 2026-01-06 16:09:58 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-06 16:09:24 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-06 16:09:12 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-06 16:08:32 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-01-06 16:06:27 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-06 16:14:06 | Manampitiya (Mahaweli Ganga) | 3.75 | 🟡 Alert | 0.044 | 🔺 Rising |
| 2026-01-06 17:00:33 | Siyambalanduwa (Heda Oya) | 4.76 | 🟡 Alert | -0.370 |  |
| 2026-01-06 16:05:59 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-01-06 16:09:58 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-01-06 16:01:01 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-01-06 16:05:53 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-01-06 17:02:40 | Katharagama (Menik Ganga) | 0.65 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-01-06 17:03:15 | Glencourse (Kelani Ganga) | 8.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-01-06 17:01:50 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-01-06 16:04:06 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 16:03:57 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-01-06 17:03:24 | Hanwella (Kelani Ganga) | 0.48 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 17:00:37 | Thanthirimale (Malwathu Oya) | 1.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-06 17:00:20 | Weraganthota (Mahaweli Ganga) | -0.57 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:01:17 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:02:40 | Yaka Wewa (Ma Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-01-06 16:24:36 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-01-06 16:09:24 | Galgamuwa (Mee Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-01-06 16:12:04 | Magura (Kalu Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-01-06 16:09:12 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:02:25 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:01:55 | Ellagawa (Kalu Ganga) | 4.44 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:02:40 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-01-06 16:03:47 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-01-06 16:06:00 | Badalgama (Maha Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-01-06 17:02:38 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-01-06 16:16:31 | Urawa (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.009 |  |
| 2026-01-06 16:08:32 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.009 |  |
| 2026-01-06 16:06:27 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-01-06 17:02:03 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-01-06 17:03:37 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-01-06 17:02:36 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.012 |  |
| 2026-01-06 17:02:53 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.020 |  |
| 2026-01-06 16:10:43 | Panadugama (Nilwala Ganga) | 2.73 | 🟢 Normal | -0.030 |  |
| 2026-01-06 17:02:52 | Thaldena (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.052 |  |
| 2026-01-06 17:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.93 | 🟢 Normal | -0.061 |  |
| 2026-01-06 17:02:52 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.091 |  |
| 2026-01-06 17:03:03 | Nakkala (Kumbukkan Oya) | 2.11 | 🟢 Normal | -0.093 |  |
| 2026-01-06 16:03:21 | Padiyathalawa (Maduru Oya) | 2.15 | 🟢 Normal | -522.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)