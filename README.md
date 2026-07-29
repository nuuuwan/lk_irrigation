# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--30_05:04:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **220,000 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 05:04:38 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-30 05:04:04 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:03:50 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:03:26 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:03:11 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.031 |  |
| 2026-07-30 05:02:44 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:02:35 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:02:32 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:01:47 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:01:45 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-30 05:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:01:38 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:01:11 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.170 |  |
| 2026-07-30 05:01:05 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-30 05:01:04 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:00:51 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:00:45 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:00:11 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-07-30 04:56:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 7.714 | 🔺 Rising |
| 2026-07-30 04:56:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.31 | 🟢 Normal | 7.714 | 🔺 Rising |
| 2026-07-30 04:56:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.24 | 🟢 Normal | 7.714 | 🔺 Rising |
| 2026-07-30 04:55:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.17 | 🟢 Normal | 7.714 | 🔺 Rising |
| 2026-07-30 04:55:45 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-07-30 04:55:41 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 7.714 | 🔺 Rising |
| 2026-07-30 04:40:36 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-07-30 04:34:28 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -54.000 |  |
| 2026-07-30 04:34:26 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -54.000 |  |
| 2026-07-30 04:30:25 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-30 04:24:10 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-30 04:16:04 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-30 04:56:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 7.714 | 🔺 Rising |
| 2026-07-30 04:13:02 | Urawa (Nilwala Ganga) | -0.03 | 🟢 Normal | 1.385 | 🔺 Rising |
| 2026-07-30 04:30:25 | Katharagama (Menik Ganga) | 0.19 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-07-30 05:00:11 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-07-30 03:06:09 | Glencourse (Kelani Ganga) | 9.16 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-07-30 04:55:45 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-07-30 04:01:30 | Panadugama (Nilwala Ganga) | 2.02 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-07-30 05:01:45 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-07-30 05:04:38 | Hanwella (Kelani Ganga) | 0.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-30 05:01:05 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-30 05:00:51 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:01:47 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:01:04 | Nakkala (Kumbukkan Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:00:45 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:01:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:01:38 | Giriulla (Maha Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:02:35 | Horowpothana (Yan Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:46 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 04:06:09 | Pitabeddara (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:02:44 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-07-30 04:12:52 | Deraniyagala (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:03:26 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:04:04 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-07-30 04:00:40 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:03:50 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-30 05:02:32 | Dunamale (Aththanagalu Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-30 04:03:18 | Badalgama (Maha Oya) | 1.81 | 🟢 Normal | 0.000 |  |
| 2026-07-30 03:01:13 | Kuda Oya (Kirindi Oya) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-30 04:02:39 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-07-29 18:01:01 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | -0.005 |  |
| 2026-07-30 04:01:36 | Ellagawa (Kalu Ganga) | 4.82 | 🟢 Normal | -0.030 |  |
| 2026-07-30 05:03:11 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.031 |  |
| 2026-07-30 04:12:00 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.031 |  |
| 2026-07-30 04:04:38 | Nawalapitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | -0.032 |  |
| 2026-07-29 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.35 | 🟢 Normal | -0.034 |  |
| 2026-07-30 04:13:45 | Rathnapura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.037 |  |
| 2026-07-30 04:07:01 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.090 |  |
| 2026-07-30 05:01:11 | Peradeniya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.170 |  |
| 2026-07-30 04:34:28 | Magura (Kalu Ganga) | 1.18 | 🟢 Normal | -54.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)