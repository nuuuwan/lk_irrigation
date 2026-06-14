# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_01:17:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **179,609 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 01:17:43 | Rathnapura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.074 |  |
| 2026-06-15 01:15:31 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.068 |  |
| 2026-06-15 01:12:34 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:10:13 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:09:59 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:08:49 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:08:44 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-15 01:07:59 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | -54.000 |  |
| 2026-06-15 01:07:57 | Magura (Kalu Ganga) | 2.36 | 🟢 Normal | -54.000 |  |
| 2026-06-15 01:06:50 | Putupaula (Kalu Ganga) | 2.47 | 🟢 Normal | -0.030 |  |
| 2026-06-15 01:05:20 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:05:06 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.014 |  |
| 2026-06-15 01:04:46 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.021 |  |
| 2026-06-15 01:04:33 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.174 |  |
| 2026-06-15 01:04:28 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-06-15 01:04:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-15 01:03:46 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:03:43 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-06-15 01:03:27 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:03:16 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-06-15 01:03:16 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.052 |  |
| 2026-06-15 01:03:02 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:02:03 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:02:02 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 01:01:59 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-06-15 01:01:44 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | -0.101 |  |
| 2026-06-15 01:01:41 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-06-15 01:01:17 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:00:49 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.078 |  |
| 2026-06-15 01:00:25 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:48:58 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.068 |  |
| 2026-06-15 00:42:32 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.006 |  |
| 2026-06-15 00:42:12 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | 1.220 | 🔺 Rising |
| 2026-06-15 00:41:13 | Panadugama (Nilwala Ganga) | 3.50 | 🟢 Normal | 1.220 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 00:13:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.96 | 🟡 Alert | -0.009 |  |
| 2026-06-15 00:42:12 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | 1.220 | 🔺 Rising |
| 2026-06-15 01:08:44 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-06-15 01:04:04 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-15 01:02:02 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 01:08:49 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:00:25 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:01:41 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:03:46 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:03:27 | Horowpothana (Yan Oya) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:10:13 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:05:20 | Moraketiya (Walawe Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:12:34 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:02:03 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:03:02 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:09:59 | Holombuwa (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-06-15 01:01:17 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:03:27 | Thanamalwila (Kirindi Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-15 00:42:32 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | -0.006 |  |
| 2026-06-14 18:04:23 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.009 |  |
| 2026-06-15 01:04:28 | Norwood (Kelani Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-06-15 00:02:56 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-06-14 18:01:41 | Thanthirimale (Malwathu Oya) | 1.55 | 🟢 Normal | -0.010 |  |
| 2026-06-15 01:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-06-15 01:05:06 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.014 |  |
| 2026-06-15 01:01:59 | Giriulla (Maha Oya) | 1.55 | 🟢 Normal | -0.020 |  |
| 2026-06-15 01:03:16 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-06-14 18:03:42 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-06-15 00:02:34 | Thawalama (Gin Ganga) | 1.98 | 🟢 Normal | -0.020 |  |
| 2026-06-15 01:04:46 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.021 |  |
| 2026-06-15 01:03:43 | Baddegama (Gin Ganga) | 2.36 | 🟢 Normal | -0.021 |  |
| 2026-06-15 01:06:50 | Putupaula (Kalu Ganga) | 2.47 | 🟢 Normal | -0.030 |  |
| 2026-06-15 01:03:16 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.052 |  |
| 2026-06-15 01:15:31 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.068 |  |
| 2026-06-15 01:17:43 | Rathnapura (Kalu Ganga) | 2.47 | 🟢 Normal | -0.074 |  |
| 2026-06-15 01:00:49 | Dunamale (Aththanagalu Oya) | 2.60 | 🟢 Normal | -0.078 |  |
| 2026-06-15 01:01:44 | Ellagawa (Kalu Ganga) | 7.34 | 🟢 Normal | -0.101 |  |
| 2026-06-15 01:04:33 | Peradeniya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.174 |  |
| 2026-06-15 01:07:59 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)