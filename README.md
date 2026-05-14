# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_05:24:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,284 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 05:24:59 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | -0.063 |  |
| 2026-05-14 05:21:05 | Magura (Kalu Ganga) | 4.70 | 🟡 Alert | -0.064 |  |
| 2026-05-14 05:15:32 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.060 |  |
| 2026-05-14 05:14:19 | Rathnapura (Kalu Ganga) | 4.76 | 🟢 Normal | -0.129 |  |
| 2026-05-14 05:11:11 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:10:43 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:10:33 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:08:38 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.037 |  |
| 2026-05-14 05:07:59 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | 6.261 | 🔺 Rising |
| 2026-05-14 05:07:52 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.018 |  |
| 2026-05-14 05:07:11 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-14 05:06:24 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-14 05:06:09 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-05-14 05:06:04 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 6.261 | 🔺 Rising |
| 2026-05-14 05:05:38 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-14 05:05:35 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.012 |  |
| 2026-05-14 05:05:35 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -0.060 |  |
| 2026-05-14 05:05:16 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -0.060 |  |
| 2026-05-14 05:05:11 | Moragaswewa (Deduru Oya) | 1.86 | 🟢 Normal | -0.158 |  |
| 2026-05-14 05:04:56 | Hanwella (Kelani Ganga) | 2.61 | 🟢 Normal | -0.047 |  |
| 2026-05-14 05:04:43 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:04:21 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.054 |  |
| 2026-05-14 05:03:27 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-05-14 05:03:25 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-05-14 05:03:08 | Ellagawa (Kalu Ganga) | 8.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-14 05:03:01 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:02:42 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.092 |  |
| 2026-05-14 05:02:34 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-05-14 05:02:34 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:02:32 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:02:32 | Dunamale (Aththanagalu Oya) | 3.34 | 🟡 Alert | -0.020 |  |
| 2026-05-14 05:02:18 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-14 05:02:11 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-14 05:01:43 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.042 |  |
| 2026-05-14 05:01:13 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.040 |  |
| 2026-05-14 05:00:44 | Moraketiya (Walawe Ganga) | 1.81 | 🟢 Normal | 1.004 | 🔺 Rising |
| 2026-05-14 04:52:50 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:52:48 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 04:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-05-14 05:02:32 | Dunamale (Aththanagalu Oya) | 3.34 | 🟡 Alert | -0.020 |  |
| 2026-05-14 05:21:05 | Magura (Kalu Ganga) | 4.70 | 🟡 Alert | -0.064 |  |
| 2026-05-14 05:07:59 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | 6.261 | 🔺 Rising |
| 2026-05-14 05:00:44 | Moraketiya (Walawe Ganga) | 1.81 | 🟢 Normal | 1.004 | 🔺 Rising |
| 2026-05-14 05:06:09 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-14 05:06:24 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-14 05:05:38 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-14 05:03:08 | Ellagawa (Kalu Ganga) | 8.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 05:07:11 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-14 05:02:34 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:03:01 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:04:43 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:10:43 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:06:39 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:11:11 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:10:33 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-05-14 03:05:57 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:02:11 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-14 05:02:18 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-14 05:05:35 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.012 |  |
| 2026-05-14 05:07:52 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.018 |  |
| 2026-05-14 04:28:54 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.023 |  |
| 2026-05-14 05:03:25 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-05-14 05:03:27 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-05-14 05:02:34 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-05-14 05:08:38 | Urawa (Nilwala Ganga) | 0.47 | 🟢 Normal | -0.037 |  |
| 2026-05-14 05:01:13 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.040 |  |
| 2026-05-14 05:01:43 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.042 |  |
| 2026-05-14 05:04:56 | Hanwella (Kelani Ganga) | 2.61 | 🟢 Normal | -0.047 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-14 05:04:21 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.054 |  |
| 2026-05-14 05:15:32 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | -0.060 |  |
| 2026-05-14 05:24:59 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | -0.063 |  |
| 2026-05-14 05:02:42 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.092 |  |
| 2026-05-14 05:14:19 | Rathnapura (Kalu Ganga) | 4.76 | 🟢 Normal | -0.129 |  |
| 2026-05-14 05:05:11 | Moragaswewa (Deduru Oya) | 1.86 | 🟢 Normal | -0.158 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)