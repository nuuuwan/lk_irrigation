# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--12_13:08:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **149,811 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 13:08:22 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-05-12 13:07:24 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.047 |  |
| 2026-05-12 13:06:59 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 13:06:46 | Moragaswewa (Deduru Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-05-12 13:06:22 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:06:10 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-12 13:06:08 | Katharagama (Menik Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-05-12 13:05:25 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 13:05:18 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.048 |  |
| 2026-05-12 13:04:55 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.125 |  |
| 2026-05-12 13:04:55 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.094 |  |
| 2026-05-12 13:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.021 |  |
| 2026-05-12 13:04:28 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 13:04:21 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 13:04:17 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:03:43 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-12 13:02:59 | Thanamalwila (Kirindi Oya) | 1.99 | 🟢 Normal | -0.032 |  |
| 2026-05-12 13:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 13:02:45 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-12 13:02:22 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.030 |  |
| 2026-05-12 13:02:17 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-05-12 13:02:03 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:02:01 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-05-12 13:02:00 | Kuda Oya (Kirindi Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-05-12 13:01:45 | Manampitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 13:01:42 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:01:21 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.050 |  |
| 2026-05-12 13:01:18 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | -0.161 |  |
| 2026-05-12 13:01:14 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-12 13:01:11 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-05-12 13:00:15 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:00:10 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:00:06 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-05-12 12:59:25 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.021 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-12 13:01:11 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.309 | 🔺 Rising |
| 2026-05-12 13:08:22 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-05-12 13:02:45 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-05-12 13:06:10 | Panadugama (Nilwala Ganga) | 2.85 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-05-12 13:01:45 | Manampitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-12 12:05:58 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-05-12 12:59:25 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-12 13:04:21 | Putupaula (Kalu Ganga) | 1.12 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-12 13:01:14 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-05-12 13:04:28 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-12 13:06:59 | Badalgama (Maha Oya) | 2.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 13:02:49 | Nawalapitiya (Mahaweli Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 13:05:25 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-12 13:04:17 | Wellawaya (Kirindi Oya) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:02:03 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:00:10 | Horowpothana (Yan Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:00:15 | Galgamuwa (Mee Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-05-12 12:04:32 | Baddegama (Gin Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:01:42 | Dunamale (Aththanagalu Oya) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:06:22 | Thalgahagoda (Nilwala Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-12 13:03:43 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-05-12 13:02:00 | Kuda Oya (Kirindi Oya) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-05-12 13:06:08 | Katharagama (Menik Ganga) | 2.05 | 🟢 Normal | -0.010 |  |
| 2026-05-12 13:06:46 | Moragaswewa (Deduru Oya) | 2.32 | 🟢 Normal | -0.020 |  |
| 2026-05-12 13:00:06 | Nakkala (Kumbukkan Oya) | 1.12 | 🟢 Normal | -0.021 |  |
| 2026-05-12 13:04:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.90 | 🟢 Normal | -0.021 |  |
| 2026-05-12 13:02:17 | Holombuwa (Kelani Ganga) | 0.78 | 🟢 Normal | -0.021 |  |
| 2026-05-12 13:02:01 | Siyambalanduwa (Heda Oya) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-05-12 12:02:35 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.030 |  |
| 2026-05-12 13:02:22 | Glencourse (Kelani Ganga) | 9.87 | 🟢 Normal | -0.030 |  |
| 2026-05-12 13:02:59 | Thanamalwila (Kirindi Oya) | 1.99 | 🟢 Normal | -0.032 |  |
| 2026-05-12 12:07:38 | Magura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.033 |  |
| 2026-05-12 12:04:15 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.041 |  |
| 2026-05-12 13:07:24 | Hanwella (Kelani Ganga) | 1.87 | 🟢 Normal | -0.047 |  |
| 2026-05-12 13:05:18 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.048 |  |
| 2026-05-12 13:01:21 | Ellagawa (Kalu Ganga) | 5.72 | 🟢 Normal | -0.050 |  |
| 2026-05-12 13:04:55 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.094 |  |
| 2026-05-12 13:04:55 | Peradeniya (Mahaweli Ganga) | 1.55 | 🟢 Normal | -0.125 |  |
| 2026-05-12 13:01:18 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)