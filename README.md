# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_02:09:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,036 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 02:09:24 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.005 |  |
| 2026-02-02 02:09:14 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-02-02 02:09:12 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:05:30 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 02:05:24 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-02 02:05:05 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-02-02 02:04:57 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:04:21 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:03:30 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-02 02:03:12 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-02-02 02:02:57 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:02:53 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-02-02 02:02:48 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-02 02:02:43 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:02:30 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.020 |  |
| 2026-02-02 02:02:24 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-02 02:02:08 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.053 |  |
| 2026-02-02 02:02:05 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:01:56 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:01:16 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:01:09 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.110 |  |
| 2026-02-02 02:00:52 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 01:27:49 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 01:17:16 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.018 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 02:02:24 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-02-02 02:05:24 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-02 01:02:13 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-02 01:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.87 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-02-01 18:00:43 | Thanthirimale (Malwathu Oya) | 2.31 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-02-02 02:05:30 | Norwood (Kelani Ganga) | 0.46 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 02:09:24 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.005 |  |
| 2026-02-02 02:01:56 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:04:57 | Wellawaya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:01:16 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:02:43 | Moragaswewa (Deduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:07:29 | Magura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 01:06:30 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:09:12 | Glencourse (Kelani Ganga) | 8.31 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:02:57 | Moraketiya (Walawe Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-02 00:03:39 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-02-01 22:00:24 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 01:09:57 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:04:21 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:00:52 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-02 02:02:05 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 01:04:59 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.009 |  |
| 2026-02-02 02:03:30 | Padiyathalawa (Maduru Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-02-02 02:02:48 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-02-02 01:06:43 | Holombuwa (Kelani Ganga) | 0.35 | 🟢 Normal | -0.010 |  |
| 2026-02-01 18:02:53 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-02-02 02:09:14 | Pitabeddara (Nilwala Ganga) | 0.82 | 🟢 Normal | -0.011 |  |
| 2026-02-01 23:47:08 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.012 |  |
| 2026-02-02 01:17:16 | Yaka Wewa (Ma Oya) | 0.86 | 🟢 Normal | -0.018 |  |
| 2026-02-02 02:03:12 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.020 |  |
| 2026-02-02 02:02:30 | Ellagawa (Kalu Ganga) | 4.56 | 🟢 Normal | -0.020 |  |
| 2026-02-02 02:05:05 | Rathnapura (Kalu Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-02-02 01:04:14 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.030 |  |
| 2026-02-02 02:02:53 | Hanwella (Kelani Ganga) | 0.36 | 🟢 Normal | -0.031 |  |
| 2026-02-02 01:03:59 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.043 |  |
| 2026-02-01 18:01:47 | Weraganthota (Mahaweli Ganga) | -2.15 | 🟢 Normal | -0.050 |  |
| 2026-02-02 02:02:08 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | -0.053 |  |
| 2026-02-02 02:01:09 | Manampitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.110 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)