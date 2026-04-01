# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--02_03:15:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **113,760 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 03:15:59 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:12:51 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:11:52 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-04-02 03:10:36 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:09:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.124 |  |
| 2026-04-02 03:08:44 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:08:43 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:07:59 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:06:49 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.205 |  |
| 2026-04-02 03:06:47 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-02 03:06:13 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:04:09 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:03:47 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:03:45 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 03:03:39 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.217 |  |
| 2026-04-02 03:03:36 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 03:03:17 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:03:01 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:03:00 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-02 03:02:47 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-04-02 03:02:25 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:02:24 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 03:02:18 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-02 03:01:55 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:01:49 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-02 03:01:28 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 03:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:01:21 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:01:10 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:33:12 | Peradeniya (Mahaweli Ganga) | 1.59 | 🟢 Normal | -0.217 |  |
| 2026-04-02 02:25:17 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-02 02:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.31 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-04-02 03:11:52 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-04-02 03:01:49 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-04-02 03:03:00 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-04-02 00:01:31 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-02 03:01:28 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 03:02:24 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 03:03:45 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 03:03:36 | Baddegama (Gin Ganga) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-02 03:03:47 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:01:23 | Nawalapitiya (Mahaweli Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:02:06 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:01:10 | Giriulla (Maha Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:10:36 | Horowpothana (Yan Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-04-01 18:02:10 | Galgamuwa (Mee Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:08:44 | Magura (Kalu Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:01:29 | Pitabeddara (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:03:01 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:01:21 | Ellagawa (Kalu Ganga) | 3.75 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:02:25 | Panadugama (Nilwala Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:12:06 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:05:51 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:15:59 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:06:13 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:03:17 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:04:09 | Badalgama (Maha Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:12:51 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-04-02 02:11:58 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-02 01:04:52 | Urawa (Nilwala Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-04-02 03:07:59 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-04-01 18:05:01 | Thanthirimale (Malwathu Oya) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-04-02 03:06:47 | Hanwella (Kelani Ganga) | 0.18 | 🟢 Normal | -0.010 |  |
| 2026-04-02 03:02:18 | Rathnapura (Kalu Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-04-02 03:02:47 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | -0.020 |  |
| 2026-04-01 18:01:16 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.031 |  |
| 2026-04-02 00:04:28 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.031 |  |
| 2026-04-02 03:09:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.124 |  |
| 2026-04-02 03:06:49 | Kithulgala (Kelani Ganga) | 1.34 | 🟢 Normal | -0.205 |  |
| 2026-04-02 03:03:39 | Peradeniya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.217 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)