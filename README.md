# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--01_04:42:44-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **61,205 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 04:42:44 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.007 |  |
| 2026-02-01 04:28:58 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.042 |  |
| 2026-02-01 04:23:25 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:22:56 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:20:11 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:18:34 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-02-01 04:13:53 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:08:25 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-01 04:08:05 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:07:49 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:07:35 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 04:07:23 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:05:45 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:05:37 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:05:32 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:05:22 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 04:05:03 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:04:50 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:04:46 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-02-01 04:04:39 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 04:04:17 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 04:03:46 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:03:41 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:03:40 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-02-01 04:03:39 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-01 04:02:20 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.005 |  |
| 2026-02-01 04:02:14 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:01:57 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.093 |  |
| 2026-02-01 04:01:25 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-02-01 04:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-01 04:01:12 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:01:06 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:00:55 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 04:00:42 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-01 03:04:52 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.57 | 🟢 Normal | 1.688 | 🔺 Rising |
| 2026-02-01 04:18:34 | Glencourse (Kelani Ganga) | 8.81 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-02-01 04:03:39 | Rathnapura (Kalu Ganga) | 0.84 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-01 04:04:39 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-01 04:08:25 | Hanwella (Kelani Ganga) | 0.32 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-02-01 04:04:17 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-02-01 03:03:00 | Thanamalwila (Kirindi Oya) | 0.52 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-02-01 04:00:55 | Moraketiya (Walawe Ganga) | 0.85 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-01 04:05:22 | Giriulla (Maha Oya) | 0.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-01 04:07:35 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-01 04:02:20 | Horowpothana (Yan Oya) | 1.50 | 🟢 Normal | 0.005 |  |
| 2026-02-01 04:03:46 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-02-01 03:07:27 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:20:11 | Moragaswewa (Deduru Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:23:25 | Yaka Wewa (Ma Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:08:19 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:04:50 | Magura (Kalu Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:01:12 | Pitabeddara (Nilwala Ganga) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-02-01 03:05:38 | Ellagawa (Kalu Ganga) | 3.83 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:05:32 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:08:05 | Panadugama (Nilwala Ganga) | 2.11 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:05:37 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:07:49 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:02:14 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:01:06 | Badalgama (Maha Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-01-31 18:01:52 | Thanthirimale (Malwathu Oya) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:05:45 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-01 04:13:53 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-01 03:15:08 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.005 |  |
| 2026-02-01 04:42:44 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.007 |  |
| 2026-02-01 04:01:14 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-02-01 04:01:25 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-01-31 22:00:43 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.011 |  |
| 2026-02-01 04:00:42 | Manampitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.021 |  |
| 2026-02-01 04:03:40 | Padiyathalawa (Maduru Oya) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-02-01 04:04:46 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.040 |  |
| 2026-02-01 04:28:58 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.042 |  |
| 2026-01-31 18:00:08 | Weraganthota (Mahaweli Ganga) | -1.81 | 🟢 Normal | -0.051 |  |
| 2026-02-01 04:01:57 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)