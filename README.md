# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--03_15:24:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **223,889 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 15:24:47 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:16:27 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | -0.025 |  |
| 2026-08-03 15:14:05 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:11:09 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:10:13 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:10:03 | Peradeniya (Mahaweli Ganga) | 9.20 | 🔴 Major Flood | 0.810 | 🔺 Rising |
| 2026-08-03 15:08:46 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:08:24 | Rathnapura (Kalu Ganga) | 7.65 | 🟠 Minor Flood | 0.433 | 🔺 Rising |
| 2026-08-03 15:08:18 | Glencourse (Kelani Ganga) | 14.60 | 🟢 Normal | 0.586 | 🔺 Rising |
| 2026-08-03 15:06:45 | Holombuwa (Kelani Ganga) | 3.75 | 🟠 Minor Flood | 0.715 | 🔺 Rising |
| 2026-08-03 15:06:04 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-03 15:05:52 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-08-03 15:05:47 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-08-03 15:05:22 | Kithulgala (Kelani Ganga) | 5.33 | 🟠 Minor Flood | -1.504 |  |
| 2026-08-03 15:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-03 15:04:44 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:04:43 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:04:41 | Norwood (Kelani Ganga) | 3.11 | 🟠 Minor Flood | -0.270 |  |
| 2026-08-03 15:04:16 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:03:51 | Deraniyagala (Kelani Ganga) | 5.85 | 🟠 Minor Flood | -0.389 |  |
| 2026-08-03 15:03:35 | Giriulla (Maha Oya) | 2.02 | 🟢 Normal | -0.240 |  |
| 2026-08-03 15:03:22 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-03 15:03:16 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:03:05 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-03 15:02:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:02:44 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-08-03 15:02:39 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:02:24 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:02:23 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:02:20 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 15:02:17 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | 0.341 | 🔺 Rising |
| 2026-08-03 15:02:06 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:01:50 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:01:45 | Nawalapitiya (Mahaweli Ganga) | 7.85 | 🔴 Major Flood | -0.270 |  |
| 2026-08-03 15:01:41 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:01:21 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:01:18 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:01:08 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-03 15:00:58 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:00:54 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | -0.005 |  |
| 2026-08-03 15:00:17 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-03 15:10:03 | Peradeniya (Mahaweli Ganga) | 9.20 | 🔴 Major Flood | 0.810 | 🔺 Rising |
| 2026-08-03 15:01:45 | Nawalapitiya (Mahaweli Ganga) | 7.85 | 🔴 Major Flood | -0.270 |  |
| 2026-08-03 15:06:45 | Holombuwa (Kelani Ganga) | 3.75 | 🟠 Minor Flood | 0.715 | 🔺 Rising |
| 2026-08-03 15:08:24 | Rathnapura (Kalu Ganga) | 7.65 | 🟠 Minor Flood | 0.433 | 🔺 Rising |
| 2026-08-03 15:04:41 | Norwood (Kelani Ganga) | 3.11 | 🟠 Minor Flood | -0.270 |  |
| 2026-08-03 15:03:51 | Deraniyagala (Kelani Ganga) | 5.85 | 🟠 Minor Flood | -0.389 |  |
| 2026-08-03 15:05:22 | Kithulgala (Kelani Ganga) | 5.33 | 🟠 Minor Flood | -1.504 |  |
| 2026-08-03 15:08:18 | Glencourse (Kelani Ganga) | 14.60 | 🟢 Normal | 0.586 | 🔺 Rising |
| 2026-08-03 15:02:44 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | 0.503 | 🔺 Rising |
| 2026-08-03 15:02:17 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | 0.341 | 🔺 Rising |
| 2026-08-03 15:05:47 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | 0.105 | 🔺 Rising |
| 2026-08-03 15:03:05 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-03 15:01:08 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-08-03 15:06:04 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-03 15:03:22 | Putupaula (Kalu Ganga) | 1.35 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-03 15:04:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.27 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-03 15:02:20 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-03 15:02:23 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:01:50 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:01:18 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:24:47 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:02:52 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:11:09 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:04:16 | Hanwella (Kelani Ganga) | 5.18 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:02:24 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:02:39 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:01:21 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:04:43 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:02:06 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:01:41 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:14:05 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:03:16 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:10:13 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:04:44 | Thanamalwila (Kirindi Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-03 15:00:54 | Thanthirimale (Malwathu Oya) | 1.01 | 🟢 Normal | -0.005 |  |
| 2026-08-03 15:00:17 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.020 |  |
| 2026-08-03 15:05:52 | Baddegama (Gin Ganga) | 2.27 | 🟢 Normal | -0.020 |  |
| 2026-08-03 15:16:27 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | -0.025 |  |
| 2026-08-03 15:03:35 | Giriulla (Maha Oya) | 2.02 | 🟢 Normal | -0.240 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)