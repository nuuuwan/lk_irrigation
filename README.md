# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_13:03:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,799 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 13:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.051 |  |
| 2026-11-02 13:02:53 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.070 |  |
| 2026-11-02 13:02:51 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.021 |  |
| 2026-11-02 13:02:47 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-11-02 13:02:44 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:02:34 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.040 |  |
| 2026-11-02 13:02:19 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-02 13:02:18 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-02 13:02:18 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 13:02:13 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 13:01:41 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:01:30 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:01:17 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:01:10 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-02 13:01:01 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-11-02 13:00:50 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:00:13 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.164 |  |
| 2026-11-02 13:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 12:31:44 | Panadugama (Nilwala Ganga) | 5.58 | 🟡 Alert | 0.689 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 12:31:44 | Panadugama (Nilwala Ganga) | 5.58 | 🟡 Alert | 0.689 | 🔺 Rising |
| 2026-11-02 13:02:19 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-02 13:01:10 | Manampitiya (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-02 13:02:18 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 12:01:55 | Thawalama (Gin Ganga) | 2.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 13:02:13 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 12:05:31 | Badalgama (Maha Oya) | 2.68 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 12:05:06 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:01:17 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:00:50 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-02 12:05:00 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-02 12:02:08 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | 0.000 |  |
| 2026-11-02 12:01:22 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:02:44 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:01:30 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-02 12:03:17 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:01:41 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 12:02:52 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-02 12:03:17 | Urawa (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:02:18 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-11-02 12:05:08 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.011 |  |
| 2026-11-02 13:01:01 | Wellawaya (Kirindi Oya) | 1.19 | 🟢 Normal | -0.020 |  |
| 2026-11-02 12:00:43 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.020 |  |
| 2026-11-02 13:02:47 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | -0.021 |  |
| 2026-11-02 13:02:51 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.021 |  |
| 2026-11-02 12:04:08 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.023 |  |
| 2026-11-02 12:01:32 | Kuda Oya (Kirindi Oya) | 1.48 | 🟢 Normal | -0.030 |  |
| 2026-11-02 12:08:54 | Thalgahagoda (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-11-02 12:05:30 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.032 |  |
| 2026-11-02 12:04:46 | Thanamalwila (Kirindi Oya) | 1.23 | 🟢 Normal | -0.034 |  |
| 2026-11-02 12:06:47 | Putupaula (Kalu Ganga) | 1.06 | 🟢 Normal | -0.037 |  |
| 2026-11-02 13:02:34 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.040 |  |
| 2026-11-02 13:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.96 | 🟢 Normal | -0.051 |  |
| 2026-11-02 12:02:14 | Glencourse (Kelani Ganga) | 10.65 | 🟢 Normal | -0.054 |  |
| 2026-11-02 13:02:53 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.070 |  |
| 2026-11-02 12:08:16 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.080 |  |
| 2026-11-02 12:03:34 | Rathnapura (Kalu Ganga) | 2.49 | 🟢 Normal | -0.111 |  |
| 2026-11-02 13:00:13 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.164 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)