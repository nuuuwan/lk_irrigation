# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_11:03:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,724 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 11:03:28 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-11-02 11:03:23 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-02 11:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | -0.020 |  |
| 2026-11-02 11:03:04 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.021 |  |
| 2026-11-02 11:03:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-02 11:02:57 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 11:02:56 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-11-02 11:02:43 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.052 |  |
| 2026-11-02 11:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 11:02:21 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.052 |  |
| 2026-11-02 11:01:55 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 11:01:41 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-11-02 11:01:35 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-02 11:01:17 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-11-02 11:01:16 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 11:00:52 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-11-02 11:00:43 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-11-02 11:00:43 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-02 11:00:31 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-11-02 11:00:09 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | -0.050 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 10:13:23 | Thalgahagoda (Nilwala Ganga) | 1.41 | 🟡 Alert | 0.000 |  |
| 2026-11-02 10:01:28 | Pitabeddara (Nilwala Ganga) | 1.39 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 11:01:55 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 10:06:14 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-02 11:02:57 | Thaldena (Mahaweli Ganga) | 0.35 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 11:01:17 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-11-02 11:03:23 | Moragaswewa (Deduru Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-02 11:02:23 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 11:01:16 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:06:36 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 11:03:00 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-11-02 11:01:35 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:01:35 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:08:07 | Badalgama (Maha Oya) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:02:00 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:02:37 | Urawa (Nilwala Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-11-02 10:11:14 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.009 |  |
| 2026-11-02 10:11:56 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-11-02 11:03:28 | Giriulla (Maha Oya) | 1.48 | 🟢 Normal | -0.010 |  |
| 2026-11-02 11:00:43 | Wellawaya (Kirindi Oya) | 1.24 | 🟢 Normal | -0.010 |  |
| 2026-11-02 11:00:52 | Siyambalanduwa (Heda Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-11-02 11:01:41 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | -0.011 |  |
| 2026-11-02 11:00:43 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.011 |  |
| 2026-11-02 10:01:08 | Panadugama (Nilwala Ganga) | 4.61 | 🟢 Normal | -0.012 |  |
| 2026-11-02 11:03:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | -0.020 |  |
| 2026-11-02 11:02:56 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.020 |  |
| 2026-11-02 11:00:31 | Nakkala (Kumbukkan Oya) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-11-02 10:05:11 | Baddegama (Gin Ganga) | 2.54 | 🟢 Normal | -0.020 |  |
| 2026-11-02 11:03:04 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.021 |  |
| 2026-11-02 10:02:23 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.041 |  |
| 2026-11-02 11:00:09 | Weraganthota (Mahaweli Ganga) | -2.39 | 🟢 Normal | -0.050 |  |
| 2026-11-02 11:02:43 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.052 |  |
| 2026-11-02 11:02:21 | Putupaula (Kalu Ganga) | 1.10 | 🟢 Normal | -0.052 |  |
| 2026-11-02 10:10:43 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.069 |  |
| 2026-11-02 10:03:22 | Hanwella (Kelani Ganga) | 3.06 | 🟢 Normal | -0.070 |  |
| 2026-11-02 10:03:11 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.079 |  |
| 2026-11-02 10:05:06 | Glencourse (Kelani Ganga) | 10.80 | 🟢 Normal | -0.090 |  |
| 2026-11-02 10:05:08 | Rathnapura (Kalu Ganga) | 2.71 | 🟢 Normal | -0.115 |  |
| 2026-11-02 10:08:56 | Magura (Kalu Ganga) | 2.44 | 🟢 Normal | -0.131 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)