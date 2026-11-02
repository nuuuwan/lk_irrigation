# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_09:03:36-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,650 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **25** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 09:03:36 | Moragaswewa (Deduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:03:20 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:03:13 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.267 |  |
| 2026-11-02 09:03:08 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.041 |  |
| 2026-11-02 09:03:08 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.061 |  |
| 2026-11-02 09:03:01 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-02 09:03:01 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.037 |  |
| 2026-11-02 09:02:49 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-02 09:02:38 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.107 |  |
| 2026-11-02 09:02:34 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:02:28 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 09:02:28 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-02 09:02:18 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-02 09:02:12 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-11-02 09:02:10 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-02 09:01:58 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-02 09:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:19 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:10 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:09 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:00:54 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-02 09:00:37 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-02 09:00:27 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.027 |  |
| 2026-11-02 09:00:13 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.050 |  |
| 2026-11-02 09:00:05 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.056 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 08:05:42 | Thalgahagoda (Nilwala Ganga) | 1.41 | 🟡 Alert | 0.030 | 🔺 Rising |
| 2026-11-02 09:00:37 | Weraganthota (Mahaweli Ganga) | -2.97 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-02 09:02:49 | Ellagawa (Kalu Ganga) | 6.17 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-11-02 09:02:10 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-02 09:03:01 | Pitabeddara (Nilwala Ganga) | 1.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-02 09:01:58 | Putupaula (Kalu Ganga) | 1.15 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-11-02 08:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.05 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 09:02:28 | Giriulla (Maha Oya) | 1.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 09:00:54 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-02 09:03:36 | Moragaswewa (Deduru Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:21 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:19 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:12:08 | Baddegama (Gin Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:14:18 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:03:46 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:03:20 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:05:13 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:09:19 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:02:34 | Manampitiya (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:09 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 09:01:10 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.000 |  |
| 2026-11-02 08:15:39 | Galgamuwa (Mee Oya) | 0.44 | 🟢 Normal | -0.008 |  |
| 2026-11-02 08:12:34 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | -0.009 |  |
| 2026-11-02 09:02:18 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-11-02 09:02:28 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | -0.010 |  |
| 2026-11-02 09:02:12 | Horowpothana (Yan Oya) | 2.12 | 🟢 Normal | -0.011 |  |
| 2026-11-02 09:00:27 | Kuda Oya (Kirindi Oya) | 1.56 | 🟢 Normal | -0.027 |  |
| 2026-11-02 09:03:01 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.037 |  |
| 2026-11-02 08:02:30 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | -0.040 |  |
| 2026-11-02 09:03:08 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.041 |  |
| 2026-11-02 08:05:01 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | -0.044 |  |
| 2026-11-02 08:14:52 | Magura (Kalu Ganga) | 2.64 | 🟢 Normal | -0.048 |  |
| 2026-11-02 09:00:13 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.050 |  |
| 2026-11-02 09:00:05 | Siyambalanduwa (Heda Oya) | 0.79 | 🟢 Normal | -0.056 |  |
| 2026-11-02 09:03:08 | Hanwella (Kelani Ganga) | 3.13 | 🟢 Normal | -0.061 |  |
| 2026-11-02 09:02:38 | Rathnapura (Kalu Ganga) | 2.83 | 🟢 Normal | -0.107 |  |
| 2026-11-02 08:03:40 | Glencourse (Kelani Ganga) | 11.00 | 🟢 Normal | -0.107 |  |
| 2026-11-02 08:02:57 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | -0.154 |  |
| 2026-11-02 09:03:13 | Thawalama (Gin Ganga) | 2.30 | 🟢 Normal | -0.267 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)