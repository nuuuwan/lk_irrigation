# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_05:02:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,479 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Thalgahagoda — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 05:02:53 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-11-02 05:02:50 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-11-02 05:02:47 | Glencourse (Kelani Ganga) | 11.33 | 🟢 Normal | -0.090 |  |
| 2026-11-02 05:02:38 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:01:50 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-02 05:01:39 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-11-02 05:01:36 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-11-02 05:01:34 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-02 05:01:12 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 05:00:51 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-11-02 05:00:40 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 05:00:06 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.012 |  |
| 2026-11-02 04:56:00 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 04:00:57 | Thalgahagoda (Nilwala Ganga) | 1.40 | 🟡 Alert | -0.032 |  |
| 2026-11-02 03:11:08 | Magura (Kalu Ganga) | 3.24 | 🟢 Normal | 324.000 | 🔺 Rising |
| 2026-11-02 05:02:50 | Rathnapura (Kalu Ganga) | 2.97 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-11-02 05:01:50 | Kuda Oya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-02 03:05:02 | Thanamalwila (Kirindi Oya) | 1.46 | 🟢 Normal | 0.113 | 🔺 Rising |
| 2026-11-02 04:08:07 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-02 05:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.92 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-01 18:02:39 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-02 04:04:49 | Badalgama (Maha Oya) | 2.61 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-02 05:00:40 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 05:01:12 | Ellagawa (Kalu Ganga) | 6.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 04:02:08 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-02 04:03:36 | Hanwella (Kelani Ganga) | 3.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-02 05:01:34 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:00:51 | Pitabeddara (Nilwala Ganga) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:03:48 | Norwood (Kelani Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:01:08 | Baddegama (Gin Ganga) | 2.47 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:56:00 | Panadugama (Nilwala Ganga) | 4.64 | 🟢 Normal | 0.000 |  |
| 2026-11-02 02:02:38 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:02:59 | Moraketiya (Walawe Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-02 05:02:38 | Dunamale (Aththanagalu Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:02:45 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-11-01 18:01:13 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-02 04:01:23 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.005 |  |
| 2026-11-02 05:02:53 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | -0.010 |  |
| 2026-11-02 05:01:39 | Moragaswewa (Deduru Oya) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-11-02 05:00:51 | Nawalapitiya (Mahaweli Ganga) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-11-02 05:00:06 | Siyambalanduwa (Heda Oya) | 1.05 | 🟢 Normal | -0.012 |  |
| 2026-11-02 04:04:55 | Urawa (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.020 |  |
| 2026-11-02 05:01:36 | Holombuwa (Kelani Ganga) | 0.79 | 🟢 Normal | -0.021 |  |
| 2026-11-02 04:05:35 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | -0.029 |  |
| 2026-11-01 18:02:14 | Galgamuwa (Mee Oya) | 0.96 | 🟢 Normal | -0.030 |  |
| 2026-11-02 04:01:28 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.031 |  |
| 2026-11-02 04:01:06 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | -0.032 |  |
| 2026-11-02 04:02:56 | Manampitiya (Mahaweli Ganga) | 0.37 | 🟢 Normal | -0.041 |  |
| 2026-11-02 04:09:51 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.045 |  |
| 2026-11-02 04:16:47 | Putupaula (Kalu Ganga) | 0.98 | 🟢 Normal | -0.058 |  |
| 2026-11-02 05:02:47 | Glencourse (Kelani Ganga) | 11.33 | 🟢 Normal | -0.090 |  |
| 2026-11-02 04:03:46 | Wellawaya (Kirindi Oya) | 1.39 | 🟢 Normal | -180.000 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)