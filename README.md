# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_05:17:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **73,420 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 05:17:36 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.016 |  |
| 2026-02-15 05:15:41 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -270.000 |  |
| 2026-02-15 05:15:39 | Magura (Kalu Ganga) | 1.94 | 🟢 Normal | -270.000 |  |
| 2026-02-15 05:15:16 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:14:17 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:13:57 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:09:36 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-02-15 05:09:32 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:07:32 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:05:41 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-15 05:05:35 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-15 05:03:56 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-02-15 05:03:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-02-15 05:03:34 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 05:03:13 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.040 |  |
| 2026-02-15 05:03:13 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:03:09 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:02:54 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.010 |  |
| 2026-02-15 05:02:48 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-15 05:02:17 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.200 |  |
| 2026-02-15 05:01:55 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:01:50 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 05:01:37 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:01:19 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 05:01:13 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-15 05:01:12 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.165 |  |
| 2026-02-15 05:00:48 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.026 |  |
| 2026-02-15 05:00:24 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:00:12 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.108 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 00:07:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.28 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-02-15 05:00:12 | Manampitiya (Mahaweli Ganga) | 2.40 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-02-15 04:07:12 | Glencourse (Kelani Ganga) | 8.41 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-15 05:05:35 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-15 04:07:52 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-02-15 05:01:19 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 05:01:40 | Nawalapitiya (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-14 18:02:04 | Weraganthota (Mahaweli Ganga) | -1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 05:03:34 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 05:05:41 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-15 05:01:13 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-02-15 04:20:37 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.004 |  |
| 2026-02-15 05:01:37 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:01:50 | Moragaswewa (Deduru Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:01:55 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:03:27 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:09:32 | Pitabeddara (Nilwala Ganga) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:03:13 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:03:09 | Hanwella (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:07:32 | Baddegama (Gin Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:00:24 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:13:57 | Dunamale (Aththanagalu Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:15:16 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:14:17 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-02-14 18:01:28 | Thanthirimale (Malwathu Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-02-15 04:13:21 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-15 05:02:54 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | -0.010 |  |
| 2026-02-15 05:02:48 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-02-15 05:09:36 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | -0.010 |  |
| 2026-02-15 05:17:36 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.016 |  |
| 2026-02-15 03:04:47 | Padiyathalawa (Maduru Oya) | 1.56 | 🟢 Normal | -0.020 |  |
| 2026-02-15 05:00:48 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.026 |  |
| 2026-02-15 05:03:56 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-02-15 05:03:48 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.032 |  |
| 2026-02-15 05:03:13 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.040 |  |
| 2026-02-15 04:10:27 | Thawalama (Gin Ganga) | 1.34 | 🟢 Normal | -0.053 |  |
| 2026-02-15 05:01:12 | Peradeniya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.165 |  |
| 2026-02-15 05:02:17 | Kithulgala (Kelani Ganga) | 1.15 | 🟢 Normal | -0.200 |  |
| 2026-02-15 05:15:41 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -270.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)