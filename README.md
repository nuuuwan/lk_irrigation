# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--13_01:01:10-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **150,230 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 01:01:10 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:00:27 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-05-13 00:20:49 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.032 |  |
| 2026-05-13 00:13:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-13 00:11:51 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-13 00:11:44 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.009 |  |
| 2026-05-13 00:10:08 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-13 00:09:04 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.115 |  |
| 2026-05-13 00:09:01 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-13 00:08:57 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-13 00:02:08 | Ellagawa (Kalu Ganga) | 5.88 | 🟢 Normal | 0.279 | 🔺 Rising |
| 2026-05-13 00:08:47 | Hanwella (Kelani Ganga) | 2.18 | 🟢 Normal | 0.128 | 🔺 Rising |
| 2026-05-13 00:01:47 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-05-13 00:13:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.50 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-13 00:02:34 | Dunamale (Aththanagalu Oya) | 2.93 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-05-13 00:08:57 | Baddegama (Gin Ganga) | 1.98 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-05-13 00:03:47 | Peradeniya (Mahaweli Ganga) | 1.53 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-13 00:05:30 | Glencourse (Kelani Ganga) | 10.62 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-13 00:11:51 | Putupaula (Kalu Ganga) | 1.01 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-12 18:00:31 | Galgamuwa (Mee Oya) | 1.68 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 00:06:03 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-13 00:03:15 | Yaka Wewa (Ma Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 00:03:26 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-13 00:03:35 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-13 00:02:55 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-13 00:09:01 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-13 00:10:08 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-05-13 00:01:31 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-05-13 00:05:32 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-05-13 00:11:44 | Horowpothana (Yan Oya) | 2.14 | 🟢 Normal | -0.009 |  |
| 2026-05-13 00:03:04 | Giriulla (Maha Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-05-13 00:02:28 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-05-13 01:01:10 | Wellawaya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-05-13 00:03:15 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-05-12 18:01:07 | Thanthirimale (Malwathu Oya) | 3.38 | 🟢 Normal | -0.020 |  |
| 2026-05-13 00:02:15 | Katharagama (Menik Ganga) | 1.60 | 🟢 Normal | -0.021 |  |
| 2026-05-13 01:00:27 | Manampitiya (Mahaweli Ganga) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-05-13 00:03:15 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-05-12 18:02:40 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.031 |  |
| 2026-05-13 00:20:49 | Thawalama (Gin Ganga) | 2.46 | 🟢 Normal | -0.032 |  |
| 2026-05-12 23:01:35 | Moragaswewa (Deduru Oya) | 1.39 | 🟢 Normal | -0.065 |  |
| 2026-05-13 00:02:10 | Panadugama (Nilwala Ganga) | 3.84 | 🟢 Normal | -0.073 |  |
| 2026-05-13 00:07:45 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | -0.114 |  |
| 2026-05-13 00:09:04 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.115 |  |
| 2026-05-13 00:08:04 | Siyambalanduwa (Heda Oya) | 2.55 | 🟢 Normal | -0.128 |  |
| 2026-05-13 00:01:39 | Thaldena (Mahaweli Ganga) | 1.12 | 🟢 Normal | -0.161 |  |
| 2026-05-13 00:02:57 | Nakkala (Kumbukkan Oya) | 1.90 | 🟢 Normal | -0.587 |  |
| 2026-05-13 00:07:55 | Magura (Kalu Ganga) | 3.25 | 🟢 Normal | -396.000 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)