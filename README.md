# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--23_05:18:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **80,586 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 05:18:46 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.114 |  |
| 2026-02-23 05:17:35 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.008 |  |
| 2026-02-23 05:16:50 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:15:30 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.771 | 🔺 Rising |
| 2026-02-23 05:14:49 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 150.000 | 🔺 Rising |
| 2026-02-23 05:14:25 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 150.000 | 🔺 Rising |
| 2026-02-23 05:13:59 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:11:26 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.027 |  |
| 2026-02-23 05:10:08 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.091 |  |
| 2026-02-23 05:08:18 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-23 05:07:35 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:07:19 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-02-23 05:06:56 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.028 |  |
| 2026-02-23 05:06:15 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:06:10 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-02-23 05:05:50 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-02-23 05:04:37 | Putupaula (Kalu Ganga) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-02-23 05:04:30 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 05:04:19 | Manampitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.031 |  |
| 2026-02-23 05:04:02 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:02:35 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-23 05:02:30 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:01:59 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.039 |  |
| 2026-02-23 05:01:48 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | -0.200 |  |
| 2026-02-23 05:01:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | -0.026 |  |
| 2026-02-23 05:01:24 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.023 |  |
| 2026-02-23 05:01:19 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.110 |  |
| 2026-02-23 05:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-23 05:00:40 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-23 05:00:39 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-23 05:00:20 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.038 |  |
| 2026-02-23 05:00:08 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:00:02 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.032 |  |
| 2026-02-23 04:35:45 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.023 |  |
| 2026-02-23 04:30:57 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-23 05:14:49 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 150.000 | 🔺 Rising |
| 2026-02-23 05:15:30 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.771 | 🔺 Rising |
| 2026-02-23 05:00:39 | Glencourse (Kelani Ganga) | 9.26 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-22 18:04:47 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-02-23 05:04:30 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-23 05:08:18 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-23 05:02:30 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:04:02 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:16:50 | Yaka Wewa (Ma Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:00:08 | Horowpothana (Yan Oya) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-02-22 18:01:10 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:06:15 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 04:01:51 | Padiyathalawa (Maduru Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:07:35 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:13:59 | Thaldena (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-23 05:17:35 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | -0.008 |  |
| 2026-02-23 05:06:10 | Thalgahagoda (Nilwala Ganga) | 0.69 | 🟢 Normal | -0.009 |  |
| 2026-02-23 04:07:52 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-02-23 05:00:40 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-02-23 05:02:35 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-02-23 05:01:11 | Nawalapitiya (Mahaweli Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-02-23 05:05:50 | Hanwella (Kelani Ganga) | 1.00 | 🟢 Normal | -0.020 |  |
| 2026-02-23 05:01:24 | Nakkala (Kumbukkan Oya) | 1.17 | 🟢 Normal | -0.023 |  |
| 2026-02-23 05:01:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.88 | 🟢 Normal | -0.026 |  |
| 2026-02-23 05:11:26 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | -0.027 |  |
| 2026-02-23 05:06:56 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.028 |  |
| 2026-02-23 04:03:56 | Giriulla (Maha Oya) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-02-23 05:07:19 | Deraniyagala (Kelani Ganga) | 0.39 | 🟢 Normal | -0.030 |  |
| 2026-02-23 05:04:37 | Putupaula (Kalu Ganga) | 1.77 | 🟢 Normal | -0.030 |  |
| 2026-02-23 05:04:19 | Manampitiya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.031 |  |
| 2026-02-23 04:22:57 | Thawalama (Gin Ganga) | 1.64 | 🟢 Normal | -0.031 |  |
| 2026-02-23 05:00:02 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.032 |  |
| 2026-02-23 05:00:20 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.038 |  |
| 2026-02-23 05:01:59 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | -0.039 |  |
| 2026-02-23 05:10:08 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.091 |  |
| 2026-02-22 18:01:38 | Weraganthota (Mahaweli Ganga) | -1.57 | 🟢 Normal | -0.108 |  |
| 2026-02-23 05:01:19 | Peradeniya (Mahaweli Ganga) | 1.69 | 🟢 Normal | -0.110 |  |
| 2026-02-23 05:18:46 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.114 |  |
| 2026-02-23 05:01:48 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | -0.200 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)