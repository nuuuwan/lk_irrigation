# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--01_20:30:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **222,300 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 20:30:55 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:20:43 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | -0.140 |  |
| 2026-08-01 20:20:05 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.071 |  |
| 2026-08-01 20:11:30 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.018 |  |
| 2026-08-01 20:09:07 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:08:54 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:07:53 | Badalgama (Maha Oya) | 3.72 | 🟢 Normal | -0.149 |  |
| 2026-08-01 20:06:44 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:06:08 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:05:46 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-08-01 20:05:39 | Giriulla (Maha Oya) | 2.06 | 🟢 Normal | -0.231 |  |
| 2026-08-01 20:05:34 | Glencourse (Kelani Ganga) | 12.46 | 🟢 Normal | -0.398 |  |
| 2026-08-01 20:04:29 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:04:23 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.052 |  |
| 2026-08-01 20:04:02 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-08-01 20:03:42 | Peradeniya (Mahaweli Ganga) | 3.44 | 🟢 Normal | -0.077 |  |
| 2026-08-01 20:03:35 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:03:27 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-01 20:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-08-01 20:03:04 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-01 20:02:40 | Ellagawa (Kalu Ganga) | 7.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-01 20:02:37 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 20:02:34 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:02:29 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.100 |  |
| 2026-08-01 20:02:16 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.044 |  |
| 2026-08-01 20:02:13 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:02:13 | Hanwella (Kelani Ganga) | 5.30 | 🟢 Normal | -0.140 |  |
| 2026-08-01 20:01:56 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:01:54 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:01:51 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:01:39 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:01:35 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.060 |  |
| 2026-08-01 20:00:58 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:00:13 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-01 20:05:46 | Putupaula (Kalu Ganga) | 1.25 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-08-01 20:03:27 | Kithulgala (Kelani Ganga) | 1.96 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-08-01 20:02:40 | Ellagawa (Kalu Ganga) | 7.14 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-01 20:00:13 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-01 20:02:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.34 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-08-01 20:02:37 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 18:03:08 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-01 20:04:29 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:30:55 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:01:51 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:02:34 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:01:39 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-08-01 18:03:57 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:08:54 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:09:07 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:01:54 | Panadugama (Nilwala Ganga) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:02:13 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:00:58 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:03:04 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:06:44 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:01:56 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:03:35 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-01 19:01:09 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:06:08 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-01 20:11:30 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | -0.018 |  |
| 2026-08-01 20:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.020 |  |
| 2026-08-01 20:04:02 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-08-01 18:00:26 | Weraganthota (Mahaweli Ganga) | -3.32 | 🟢 Normal | -0.042 |  |
| 2026-08-01 20:02:16 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | -0.044 |  |
| 2026-08-01 20:04:23 | Deraniyagala (Kelani Ganga) | 1.08 | 🟢 Normal | -0.052 |  |
| 2026-08-01 20:01:35 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | -0.060 |  |
| 2026-08-01 20:20:05 | Magura (Kalu Ganga) | 2.34 | 🟢 Normal | -0.071 |  |
| 2026-08-01 20:03:42 | Peradeniya (Mahaweli Ganga) | 3.44 | 🟢 Normal | -0.077 |  |
| 2026-08-01 20:02:29 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | -0.100 |  |
| 2026-08-01 20:20:43 | Rathnapura (Kalu Ganga) | 2.92 | 🟢 Normal | -0.140 |  |
| 2026-08-01 20:02:13 | Hanwella (Kelani Ganga) | 5.30 | 🟢 Normal | -0.140 |  |
| 2026-08-01 20:07:53 | Badalgama (Maha Oya) | 3.72 | 🟢 Normal | -0.149 |  |
| 2026-08-01 20:05:39 | Giriulla (Maha Oya) | 2.06 | 🟢 Normal | -0.231 |  |
| 2026-08-01 20:05:34 | Glencourse (Kelani Ganga) | 12.46 | 🟢 Normal | -0.398 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)