# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_04:39:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **145,853 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 04:39:59 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-08 04:39:42 | Thawalama (Gin Ganga) | 2.89 | 🟢 Normal | 1.055 | 🔺 Rising |
| 2026-05-08 04:22:58 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.206 |  |
| 2026-05-08 04:16:16 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.064 |  |
| 2026-05-08 04:15:15 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.051 |  |
| 2026-05-08 04:14:04 | Kuda Oya (Kirindi Oya) | 2.72 | 🟢 Normal | -0.315 |  |
| 2026-05-08 04:12:15 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.017 |  |
| 2026-05-08 04:08:45 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.082 |  |
| 2026-05-08 04:08:11 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-08 04:08:02 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -6.207 |  |
| 2026-05-08 04:07:45 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.050 |  |
| 2026-05-08 04:07:33 | Urawa (Nilwala Ganga) | 0.46 | 🟢 Normal | -6.207 |  |
| 2026-05-08 04:06:45 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | -1.853 |  |
| 2026-05-08 04:06:11 | Pitabeddara (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.103 |  |
| 2026-05-08 04:04:53 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-05-08 04:04:29 | Rathnapura (Kalu Ganga) | 2.34 | 🟢 Normal | -1.853 |  |
| 2026-05-08 04:04:24 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 04:04:11 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.076 |  |
| 2026-05-08 04:03:58 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 04:03:38 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.090 |  |
| 2026-05-08 04:03:23 | Glencourse (Kelani Ganga) | 11.47 | 🟢 Normal | -0.039 |  |
| 2026-05-08 04:03:13 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 04:02:57 | Thanamalwila (Kirindi Oya) | 2.78 | 🟢 Normal | -0.565 |  |
| 2026-05-08 04:02:40 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.036 |  |
| 2026-05-08 04:02:06 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-05-08 04:01:56 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.038 |  |
| 2026-05-08 04:01:50 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-08 04:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.052 |  |
| 2026-05-08 04:01:47 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-08 04:01:22 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-08 04:00:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 04:00:40 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.141 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 03:15:48 | Panadugama (Nilwala Ganga) | 5.04 | 🟡 Alert | 0.068 | 🔺 Rising |
| 2026-05-08 04:39:42 | Thawalama (Gin Ganga) | 2.89 | 🟢 Normal | 1.055 | 🔺 Rising |
| 2026-05-07 23:00:34 | Weraganthota (Mahaweli Ganga) | 0.72 | 🟢 Normal | 0.746 | 🔺 Rising |
| 2026-05-08 04:04:53 | Hanwella (Kelani Ganga) | 2.45 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-05-08 04:02:06 | Badalgama (Maha Oya) | 2.30 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-05-08 04:01:47 | Ellagawa (Kalu Ganga) | 5.31 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-05-08 02:04:38 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-05-08 04:39:59 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-08 04:00:51 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 04:03:13 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 04:03:58 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-05-08 03:15:40 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-05-08 04:04:24 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-08 03:01:45 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-08 04:08:11 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-05-07 18:02:03 | Thanthirimale (Malwathu Oya) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-05-08 04:01:50 | Moragaswewa (Deduru Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-05-08 04:01:22 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-05-08 04:12:15 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | -0.017 |  |
| 2026-05-08 03:03:56 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | -0.031 |  |
| 2026-05-08 04:02:40 | Dunamale (Aththanagalu Oya) | 1.17 | 🟢 Normal | -0.036 |  |
| 2026-05-08 04:01:56 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.038 |  |
| 2026-05-08 04:03:23 | Glencourse (Kelani Ganga) | 11.47 | 🟢 Normal | -0.039 |  |
| 2026-05-08 04:07:45 | Baddegama (Gin Ganga) | 1.64 | 🟢 Normal | -0.050 |  |
| 2026-05-08 04:15:15 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.051 |  |
| 2026-05-08 04:01:48 | Nawalapitiya (Mahaweli Ganga) | 0.90 | 🟢 Normal | -0.052 |  |
| 2026-05-07 18:00:09 | Galgamuwa (Mee Oya) | 0.88 | 🟢 Normal | -0.063 |  |
| 2026-05-08 04:16:16 | Wellawaya (Kirindi Oya) | 1.45 | 🟢 Normal | -0.064 |  |
| 2026-05-08 04:04:11 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.076 |  |
| 2026-05-08 04:08:45 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.082 |  |
| 2026-05-08 04:03:38 | Giriulla (Maha Oya) | 2.45 | 🟢 Normal | -0.090 |  |
| 2026-05-08 04:06:11 | Pitabeddara (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.103 |  |
| 2026-05-08 04:00:40 | Peradeniya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.141 |  |
| 2026-05-08 04:22:58 | Nakkala (Kumbukkan Oya) | 1.20 | 🟢 Normal | -0.206 |  |
| 2026-05-08 04:14:04 | Kuda Oya (Kirindi Oya) | 2.72 | 🟢 Normal | -0.315 |  |
| 2026-05-08 04:02:57 | Thanamalwila (Kirindi Oya) | 2.78 | 🟢 Normal | -0.565 |  |
| 2026-05-08 04:06:45 | Rathnapura (Kalu Ganga) | 2.27 | 🟢 Normal | -1.853 |  |
| 2026-05-08 04:08:02 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -6.207 |  |
| 2026-05-08 03:35:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.29 | 🟢 Normal | -6.495 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)