# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--30_10:27:58-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,617 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 10:27:58 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:25:53 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.015 |  |
| 2026-05-30 10:21:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-30 10:14:32 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:12:37 | Baddegama (Gin Ganga) | 2.94 | 🟢 Normal | -0.025 |  |
| 2026-05-30 10:11:44 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.027 |  |
| 2026-05-30 10:09:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:08:50 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.052 |  |
| 2026-05-30 10:08:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.47 | 🟡 Alert | -0.018 |  |
| 2026-05-30 10:08:11 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.018 |  |
| 2026-05-30 10:07:34 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-30 10:06:10 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-05-30 10:06:04 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.040 |  |
| 2026-05-30 10:05:46 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:05:44 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-05-30 10:05:28 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | -0.057 |  |
| 2026-05-30 10:04:06 | Magura (Kalu Ganga) | 3.14 | 🟢 Normal | -0.054 |  |
| 2026-05-30 10:03:45 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:03:41 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:03:36 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:03:09 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:02:54 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:02:51 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-30 10:02:25 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 10:02:21 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-05-30 10:02:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-30 10:02:19 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-05-30 10:01:49 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:01:46 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-05-30 10:01:27 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:01:08 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-05-30 10:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:01:05 | Ellagawa (Kalu Ganga) | 7.91 | 🟢 Normal | -0.041 |  |
| 2026-05-30 10:00:50 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-30 10:00:45 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:00:39 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:00:35 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-30 10:08:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.47 | 🟡 Alert | -0.018 |  |
| 2026-05-30 10:02:20 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-05-30 10:00:50 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-05-30 09:01:23 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-30 10:07:34 | Holombuwa (Kelani Ganga) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-30 10:02:25 | Giriulla (Maha Oya) | 1.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-30 10:21:17 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-30 10:03:09 | Wellawaya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:00:39 | Nakkala (Kumbukkan Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:27:58 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:01:07 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:09:59 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:01:27 | Galgamuwa (Mee Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:02:54 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:00:45 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:03:36 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:03:45 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:01:49 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:03:41 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | 0.000 |  |
| 2026-05-30 09:02:02 | Thanthirimale (Malwathu Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:14:32 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:05:46 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-30 10:06:10 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.009 |  |
| 2026-05-30 10:02:21 | Putupaula (Kalu Ganga) | 2.60 | 🟢 Normal | -0.010 |  |
| 2026-05-30 10:01:08 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-05-30 10:02:19 | Dunamale (Aththanagalu Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2026-05-30 10:02:51 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-05-30 10:01:46 | Peradeniya (Mahaweli Ganga) | 1.68 | 🟢 Normal | -0.011 |  |
| 2026-05-30 10:25:53 | Thalgahagoda (Nilwala Ganga) | 0.68 | 🟢 Normal | -0.015 |  |
| 2026-05-30 10:08:11 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.018 |  |
| 2026-05-30 10:00:35 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | -0.020 |  |
| 2026-05-30 10:12:37 | Baddegama (Gin Ganga) | 2.94 | 🟢 Normal | -0.025 |  |
| 2026-05-30 10:11:44 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | -0.027 |  |
| 2026-05-30 10:06:04 | Rathnapura (Kalu Ganga) | 2.80 | 🟢 Normal | -0.040 |  |
| 2026-05-30 10:01:05 | Ellagawa (Kalu Ganga) | 7.91 | 🟢 Normal | -0.041 |  |
| 2026-05-30 10:05:44 | Kithulgala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.050 |  |
| 2026-05-30 10:08:50 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.052 |  |
| 2026-05-30 10:04:06 | Magura (Kalu Ganga) | 3.14 | 🟢 Normal | -0.054 |  |
| 2026-05-30 10:05:28 | Hanwella (Kelani Ganga) | 3.00 | 🟢 Normal | -0.057 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)