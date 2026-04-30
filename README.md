# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--30_19:16:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **139,350 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 19:16:59 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:12:05 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-30 19:11:45 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:11:18 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-04-30 19:10:14 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-04-30 19:10:01 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:08:07 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.009 |  |
| 2026-04-30 19:08:05 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-04-30 19:08:00 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:07:30 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.073 |  |
| 2026-04-30 19:06:32 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.019 |  |
| 2026-04-30 19:06:19 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.018 |  |
| 2026-04-30 19:05:27 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.038 |  |
| 2026-04-30 19:04:50 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-30 19:04:49 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 19:04:38 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:04:13 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-30 19:03:23 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-04-30 19:03:01 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-04-30 19:02:44 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:02:38 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.048 |  |
| 2026-04-30 19:02:37 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.018 |  |
| 2026-04-30 19:02:20 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-04-30 19:02:20 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-30 19:02:13 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.100 |  |
| 2026-04-30 19:02:07 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:01:48 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.031 |  |
| 2026-04-30 19:01:47 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:01:15 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:00:50 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-30 19:00:35 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 19:00:15 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-30 19:03:01 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-04-30 19:08:05 | Rathnapura (Kalu Ganga) | 1.31 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-04-30 19:04:13 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-04-30 19:04:50 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-04-30 19:00:35 | Moragaswewa (Deduru Oya) | 0.62 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-30 19:12:05 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-04-30 19:02:20 | Glencourse (Kelani Ganga) | 8.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-30 19:04:49 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-30 19:00:15 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:01:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:16:59 | Horowpothana (Yan Oya) | 1.99 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:01:15 | Pitabeddara (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:02:37 | Norwood (Kelani Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:11:45 | Panadugama (Nilwala Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:02:07 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:04:38 | Dunamale (Aththanagalu Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:08:00 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:02:44 | Manampitiya (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:32 | Thanthirimale (Malwathu Oya) | 3.03 | 🟢 Normal | 0.000 |  |
| 2026-04-30 18:02:55 | Thawalama (Gin Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:10:01 | Urawa (Nilwala Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:01:47 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-04-30 19:08:07 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.009 |  |
| 2026-04-30 19:11:18 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.009 |  |
| 2026-04-30 18:02:01 | Weraganthota (Mahaweli Ganga) | -3.16 | 🟢 Normal | -0.010 |  |
| 2026-04-30 19:00:50 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-04-30 18:03:14 | Galgamuwa (Mee Oya) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-04-30 19:02:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.02 | 🟢 Normal | -0.018 |  |
| 2026-04-30 19:06:19 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.018 |  |
| 2026-04-30 19:06:32 | Badalgama (Maha Oya) | 2.41 | 🟢 Normal | -0.019 |  |
| 2026-04-30 19:03:23 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-04-30 19:10:14 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | -0.027 |  |
| 2026-04-30 19:02:20 | Hanwella (Kelani Ganga) | 0.57 | 🟢 Normal | -0.030 |  |
| 2026-04-30 19:01:48 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | -0.031 |  |
| 2026-04-30 18:00:55 | Nawalapitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | -0.031 |  |
| 2026-04-30 19:05:27 | Thanamalwila (Kirindi Oya) | 1.28 | 🟢 Normal | -0.038 |  |
| 2026-04-30 19:02:38 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.048 |  |
| 2026-04-30 19:07:30 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.073 |  |
| 2026-04-30 19:02:13 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)