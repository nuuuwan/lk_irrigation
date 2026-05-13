# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_05:06:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,273 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 05:06:24 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-14 05:06:09 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-05-14 05:06:04 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.102 |  |
| 2026-05-14 05:05:38 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-14 05:05:35 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.012 |  |
| 2026-05-14 05:05:35 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -1.895 |  |
| 2026-05-14 05:05:16 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | -1.895 |  |
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
| 2026-05-14 04:28:54 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.023 |  |
| 2026-05-14 04:23:37 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-14 04:19:41 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.054 |  |
| 2026-05-14 04:15:21 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 04:05:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.24 | 🟡 Alert | 0.037 | 🔺 Rising |
| 2026-05-14 05:02:32 | Dunamale (Aththanagalu Oya) | 3.34 | 🟡 Alert | -0.020 |  |
| 2026-05-14 04:05:38 | Magura (Kalu Ganga) | 4.78 | 🟡 Alert | -0.105 |  |
| 2026-05-14 05:00:44 | Moraketiya (Walawe Ganga) | 1.81 | 🟢 Normal | 1.004 | 🔺 Rising |
| 2026-05-14 05:06:09 | Wellawaya (Kirindi Oya) | 1.65 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-14 05:06:24 | Glencourse (Kelani Ganga) | 10.39 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-14 05:05:38 | Badalgama (Maha Oya) | 2.88 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-05-14 04:03:48 | Putupaula (Kalu Ganga) | 2.39 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-05-14 04:23:37 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-05-14 05:03:08 | Ellagawa (Kalu Ganga) | 8.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 05:02:34 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:03:01 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:04:43 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:52:50 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:06:39 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 03:05:57 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-14 05:02:11 | Siyambalanduwa (Heda Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-14 05:02:18 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-05-14 05:05:35 | Thaldena (Mahaweli Ganga) | 0.61 | 🟢 Normal | -0.012 |  |
| 2026-05-14 04:00:35 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-05-14 04:28:54 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.023 |  |
| 2026-05-14 05:03:25 | Norwood (Kelani Ganga) | 0.80 | 🟢 Normal | -0.030 |  |
| 2026-05-14 05:03:27 | Manampitiya (Mahaweli Ganga) | 0.79 | 🟢 Normal | -0.030 |  |
| 2026-05-14 05:02:34 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-05-14 05:01:13 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.040 |  |
| 2026-05-14 04:04:25 | Urawa (Nilwala Ganga) | 0.51 | 🟢 Normal | -0.042 |  |
| 2026-05-14 05:01:43 | Thawalama (Gin Ganga) | 2.54 | 🟢 Normal | -0.042 |  |
| 2026-05-14 05:04:56 | Hanwella (Kelani Ganga) | 2.61 | 🟢 Normal | -0.047 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-14 05:04:21 | Deraniyagala (Kelani Ganga) | 0.75 | 🟢 Normal | -0.054 |  |
| 2026-05-14 02:05:26 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | -0.065 |  |
| 2026-05-14 04:06:24 | Holombuwa (Kelani Ganga) | 0.69 | 🟢 Normal | -0.074 |  |
| 2026-05-14 05:02:42 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.092 |  |
| 2026-05-14 05:06:04 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | -0.102 |  |
| 2026-05-14 04:04:24 | Rathnapura (Kalu Ganga) | 4.91 | 🟢 Normal | -0.144 |  |
| 2026-05-14 05:05:11 | Moragaswewa (Deduru Oya) | 1.86 | 🟢 Normal | -0.158 |  |
| 2026-05-14 05:05:35 | Nakkala (Kumbukkan Oya) | 1.09 | 🟢 Normal | -1.895 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)