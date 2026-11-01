# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_01:02:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,341 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 01:02:56 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-02 01:02:21 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:02:08 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:02:03 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-11-02 01:02:01 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:54 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-02 01:01:36 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:30 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:20 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 01:01:11 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:03 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:00:43 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | -0.010 |  |
| 2026-11-02 01:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-02 00:18:49 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | 0.103 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 01:00:43 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | -0.010 |  |
| 2026-11-02 01:02:56 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-02 00:18:49 | Magura (Kalu Ganga) | 2.96 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-11-02 00:13:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.86 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-02 00:10:14 | Kithulgala (Kelani Ganga) | 2.31 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-11-01 18:02:39 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-02 01:01:20 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 00:07:57 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 00:08:24 | Thawalama (Gin Ganga) | 3.15 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-02 01:01:54 | Dunamale (Aththanagalu Oya) | 1.68 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-02 00:01:29 | Giriulla (Maha Oya) | 1.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 00:02:03 | Moraketiya (Walawe Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 01:02:08 | Wellawaya (Kirindi Oya) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:03 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:02:21 | Moragaswewa (Deduru Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:30 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 00:02:05 | Horowpothana (Yan Oya) | 2.21 | 🟢 Normal | 0.000 |  |
| 2026-11-02 00:03:22 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:36 | Ellagawa (Kalu Ganga) | 5.99 | 🟢 Normal | 0.000 |  |
| 2026-11-02 00:07:46 | Panadugama (Nilwala Ganga) | 4.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:02:01 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 00:06:23 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 00:04:32 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-02 00:13:27 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-02 00:04:19 | Badalgama (Maha Oya) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-11-02 00:04:05 | Rathnapura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 01:01:11 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-02 00:05:38 | Thanamalwila (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-11-02 00:03:13 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-11-02 00:09:38 | Baddegama (Gin Ganga) | 2.42 | 🟢 Normal | -0.020 |  |
| 2026-11-02 01:02:03 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.020 |  |
| 2026-11-02 01:00:36 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.021 |  |
| 2026-11-02 00:11:54 | Manampitiya (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.027 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-02 00:05:23 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.030 |  |
| 2026-11-02 00:03:12 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | -0.112 |  |
| 2026-11-02 00:03:59 | Holombuwa (Kelani Ganga) | 1.18 | 🟢 Normal | -0.150 |  |
| 2026-11-02 00:11:35 | Urawa (Nilwala Ganga) | 0.96 | 🟢 Normal | -3.600 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)