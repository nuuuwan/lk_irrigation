# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_04:02:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,448 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 04:02:59 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:02:56 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.041 |  |
| 2026-11-02 04:02:45 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:02:42 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:02:36 | Glencourse (Kelani Ganga) | 11.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 04:02:08 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-02 04:02:05 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-11-02 04:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.87 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-02 04:01:28 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.031 |  |
| 2026-11-02 04:01:28 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:01:23 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.005 |  |
| 2026-11-02 04:01:12 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 04:01:08 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-02 04:01:08 | Baddegama (Gin Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:01:06 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.032 |  |
| 2026-11-02 04:01:01 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 04:00:57 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | -0.032 |  |
| 2026-11-02 03:55:58 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.017 |  |
| 2026-11-02 03:52:10 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 04:00:57 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | -0.032 |  |
| 2026-11-02 03:11:08 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-11-02 03:07:18 | Rathnapura (Kalu Ganga) | 2.58 | 🟢 Normal | 0.346 | 🔺 Rising |
| 2026-11-02 03:05:02 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-02 03:00:23 | Siyambalanduwa (Heda Oya) | 1.08 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-11-02 03:07:56 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-02 03:02:48 | Hanwella (Kelani Ganga) | 3.22 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-02 04:01:08 | Kuda Oya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-11-01 18:02:39 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-02 04:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.87 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-11-02 04:01:01 | Nakkala (Kumbukkan Oya) | 0.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 04:02:08 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-02 04:01:12 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 04:02:36 | Glencourse (Kelani Ganga) | 11.42 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 01:02:08 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:02:42 | Moragaswewa (Deduru Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:01:28 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 03:00:19 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:01:08 | Baddegama (Gin Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-02 03:04:24 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-11-02 02:02:38 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:02:59 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-02 03:52:10 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:02:45 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 03:07:37 | Badalgama (Maha Oya) | 2.58 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:01:23 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.005 |  |
| 2026-11-02 04:02:05 | Horowpothana (Yan Oya) | 2.18 | 🟢 Normal | -0.010 |  |
| 2026-11-02 03:01:24 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-11-02 03:03:48 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | -0.011 |  |
| 2026-11-02 03:55:58 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | -0.017 |  |
| 2026-11-02 03:03:44 | Urawa (Nilwala Ganga) | 0.92 | 🟢 Normal | -0.020 |  |
| 2026-11-02 03:04:01 | Thawalama (Gin Ganga) | 2.98 | 🟢 Normal | -0.021 |  |
| 2026-11-02 03:03:00 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | -0.021 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-02 04:01:28 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.031 |  |
| 2026-11-02 04:01:06 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.032 |  |
| 2026-11-02 04:02:56 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.041 |  |
| 2026-11-02 03:09:55 | Holombuwa (Kelani Ganga) | 0.88 | 🟢 Normal | -0.180 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)