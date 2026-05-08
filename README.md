# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--09_02:31:37-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,682 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 02:31:37 | Norwood (Kelani Ganga) | 1.34 | 🟢 Normal | 1.037 | 🔺 Rising |
| 2026-05-09 02:30:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.574 | 🔺 Rising |
| 2026-05-09 02:27:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.21 | 🟢 Normal | 0.574 | 🔺 Rising |
| 2026-05-09 02:27:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.16 | 🟢 Normal | 0.574 | 🔺 Rising |
| 2026-05-09 02:27:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.11 | 🟢 Normal | 0.574 | 🔺 Rising |
| 2026-05-09 02:17:02 | Magura (Kalu Ganga) | 3.36 | 🟢 Normal | -270.000 |  |
| 2026-05-09 02:17:00 | Magura (Kalu Ganga) | 3.51 | 🟢 Normal | -270.000 |  |
| 2026-05-09 02:16:04 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.008 |  |
| 2026-05-09 02:14:23 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-09 02:08:45 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 02:07:30 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.062 |  |
| 2026-05-09 02:06:48 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-05-09 02:06:44 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-09 02:06:40 | Katharagama (Menik Ganga) | 1.04 | 🟢 Normal | 1.306 | 🔺 Rising |
| 2026-05-09 02:06:19 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-05-09 02:06:09 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-09 02:06:00 | Thanamalwila (Kirindi Oya) | 6.39 | 🔴 Major Flood | -0.119 |  |
| 2026-05-09 02:05:42 | Wellawaya (Kirindi Oya) | 2.65 | 🟢 Normal | -0.374 |  |
| 2026-05-09 02:05:41 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.113 |  |
| 2026-05-09 02:05:12 | Moragaswewa (Deduru Oya) | 2.46 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-05-09 02:04:40 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-09 02:04:21 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.100 |  |
| 2026-05-09 02:04:07 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 02:03:02 | Glencourse (Kelani Ganga) | 10.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-09 02:02:34 | Moraketiya (Walawe Ganga) | 2.34 | 🟢 Normal | -0.173 |  |
| 2026-05-09 02:02:17 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-09 02:02:13 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.109 |  |
| 2026-05-09 02:02:09 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | -0.197 |  |
| 2026-05-09 02:01:31 | Kuda Oya (Kirindi Oya) | 6.20 | 🟢 Normal | -0.489 |  |
| 2026-05-09 02:01:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-09 02:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 02:01:08 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-09 02:01:07 | Thaldena (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.073 |  |
| 2026-05-09 02:00:45 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-09 02:06:00 | Thanamalwila (Kirindi Oya) | 6.39 | 🔴 Major Flood | -0.119 |  |
| 2026-05-08 18:13:42 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | 1.954 | 🔺 Rising |
| 2026-05-09 02:06:40 | Katharagama (Menik Ganga) | 1.04 | 🟢 Normal | 1.306 | 🔺 Rising |
| 2026-05-09 02:31:37 | Norwood (Kelani Ganga) | 1.34 | 🟢 Normal | 1.037 | 🔺 Rising |
| 2026-05-09 02:30:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.24 | 🟢 Normal | 0.574 | 🔺 Rising |
| 2026-05-09 02:06:48 | Rathnapura (Kalu Ganga) | 3.69 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-05-09 02:05:12 | Moragaswewa (Deduru Oya) | 2.46 | 🟢 Normal | 0.212 | 🔺 Rising |
| 2026-05-09 02:01:20 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-05-09 02:14:23 | Hanwella (Kelani Ganga) | 1.60 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-09 02:03:02 | Glencourse (Kelani Ganga) | 10.22 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-05-09 02:04:07 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-08 18:01:43 | Thanthirimale (Malwathu Oya) | 2.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 02:01:15 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-09 02:04:40 | Dunamale (Aththanagalu Oya) | 1.27 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-09 02:01:08 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-08 23:01:55 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-09 00:03:06 | Pitabeddara (Nilwala Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-09 02:06:09 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-09 02:00:45 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-05-09 02:08:45 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-09 02:06:44 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-05-09 02:16:04 | Thalgahagoda (Nilwala Ganga) | 0.78 | 🟢 Normal | -0.008 |  |
| 2026-05-09 02:02:17 | Giriulla (Maha Oya) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-05-09 00:08:05 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | -0.019 |  |
| 2026-05-09 00:01:45 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | -0.020 |  |
| 2026-05-09 02:06:19 | Baddegama (Gin Ganga) | 2.31 | 🟢 Normal | -0.020 |  |
| 2026-05-09 01:01:04 | Manampitiya (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.023 |  |
| 2026-05-09 00:10:38 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.036 |  |
| 2026-05-08 18:01:19 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.040 |  |
| 2026-05-09 02:07:30 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | -0.062 |  |
| 2026-05-09 02:01:07 | Thaldena (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.073 |  |
| 2026-05-09 02:04:21 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.100 |  |
| 2026-05-09 02:02:13 | Peradeniya (Mahaweli Ganga) | 2.16 | 🟢 Normal | -0.109 |  |
| 2026-05-09 02:05:41 | Thawalama (Gin Ganga) | 2.10 | 🟢 Normal | -0.113 |  |
| 2026-05-09 02:02:34 | Moraketiya (Walawe Ganga) | 2.34 | 🟢 Normal | -0.173 |  |
| 2026-05-09 02:02:09 | Nakkala (Kumbukkan Oya) | 1.45 | 🟢 Normal | -0.197 |  |
| 2026-05-09 02:05:42 | Wellawaya (Kirindi Oya) | 2.65 | 🟢 Normal | -0.374 |  |
| 2026-05-09 02:01:31 | Kuda Oya (Kirindi Oya) | 6.20 | 🟢 Normal | -0.489 |  |
| 2026-05-09 02:17:02 | Magura (Kalu Ganga) | 3.36 | 🟢 Normal | -270.000 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)