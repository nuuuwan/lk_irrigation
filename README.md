# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--21_04:44:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **78,738 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 04:44:50 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:35:23 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-21 04:34:00 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.103 |  |
| 2026-02-21 04:17:37 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:12:03 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 04:11:58 | Padiyathalawa (Maduru Oya) | 1.85 | 🟢 Normal | -0.027 |  |
| 2026-02-21 04:08:46 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.159 |  |
| 2026-02-21 04:08:28 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-02-21 04:08:27 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-02-21 04:08:18 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-21 04:08:10 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-21 04:06:20 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:06:19 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-21 04:05:12 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-02-21 04:04:43 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:04:19 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-21 04:03:51 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:03:38 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.141 |  |
| 2026-02-21 04:03:28 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | -0.019 |  |
| 2026-02-21 04:03:15 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-21 04:02:42 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-21 04:02:34 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 04:02:28 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:02:28 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:02:18 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.045 |  |
| 2026-02-21 04:02:12 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:02:00 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:01:34 | Manampitiya (Mahaweli Ganga) | 2.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-21 04:01:31 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:01:21 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:01:09 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:01:07 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.061 |  |
| 2026-02-21 04:01:03 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-02-21 04:00:53 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:00:24 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-21 04:08:28 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-02-21 04:06:19 | Glencourse (Kelani Ganga) | 8.43 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-21 04:04:19 | Baddegama (Gin Ganga) | 1.40 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-02-21 04:08:10 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-02-21 04:03:15 | Urawa (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-21 04:01:34 | Manampitiya (Mahaweli Ganga) | 2.93 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-21 04:08:18 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-02-21 04:02:34 | Thaldena (Mahaweli Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-21 04:12:03 | Panadugama (Nilwala Ganga) | 2.30 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-21 04:35:23 | Rathnapura (Kalu Ganga) | 0.79 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-02-21 04:03:38 | Kithulgala (Kelani Ganga) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:00:53 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:02:03 | Nawalapitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:02:28 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:02:12 | Giriulla (Maha Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:01:31 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:04:38 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:17:37 | Pitabeddara (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:02:28 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:03:51 | Hanwella (Kelani Ganga) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:44:50 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:06:20 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:01:09 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:04:43 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-20 18:01:33 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:01:21 | Kuda Oya (Kirindi Oya) | 1.17 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:02:00 | Thanamalwila (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-21 04:05:12 | Siyambalanduwa (Heda Oya) | 0.85 | 🟢 Normal | -0.009 |  |
| 2026-02-21 04:02:42 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-02-21 04:03:28 | Ellagawa (Kalu Ganga) | 4.32 | 🟢 Normal | -0.019 |  |
| 2026-02-21 04:01:03 | Nakkala (Kumbukkan Oya) | 1.14 | 🟢 Normal | -0.020 |  |
| 2026-02-21 04:11:58 | Padiyathalawa (Maduru Oya) | 1.85 | 🟢 Normal | -0.027 |  |
| 2026-02-21 04:00:24 | Deraniyagala (Kelani Ganga) | 0.08 | 🟢 Normal | -0.032 |  |
| 2026-02-21 04:02:18 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.045 |  |
| 2026-02-20 18:02:20 | Weraganthota (Mahaweli Ganga) | -1.32 | 🟢 Normal | -0.051 |  |
| 2026-02-21 04:01:07 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.061 |  |
| 2026-02-21 04:34:00 | Magura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.103 |  |
| 2026-02-21 04:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.141 |  |
| 2026-02-21 04:08:46 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.159 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)