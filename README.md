# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--02_14:03:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **304,840 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 14:03:46 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.049 |  |
| 2026-11-02 14:03:35 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:03:17 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-11-02 14:02:30 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.031 |  |
| 2026-11-02 14:02:28 | Thalgahagoda (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.023 |  |
| 2026-11-02 14:02:28 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.022 |  |
| 2026-11-02 14:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.91 | 🟢 Normal | -0.051 |  |
| 2026-11-02 14:02:16 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:02:12 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-02 14:01:53 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:01:38 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:01:26 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-11-02 14:01:21 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:01:09 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-02 14:01:09 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 14:01:03 | Moragaswewa (Deduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:01:02 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:00:33 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-02 14:00:25 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.140 |  |
| 2026-11-02 14:00:22 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-02 14:01:09 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-02 13:02:18 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 14:01:09 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-02 13:04:44 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-02 14:02:16 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:01:03 | Moragaswewa (Deduru Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:01:38 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:00:50 | Horowpothana (Yan Oya) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:07:35 | Galgamuwa (Mee Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:03:35 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:04:06 | Ellagawa (Kalu Ganga) | 6.24 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:01:53 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:01:30 | Dunamale (Aththanagalu Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:01:21 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-02 14:01:02 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-02 13:14:55 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | -0.008 |  |
| 2026-11-02 13:08:57 | Holombuwa (Kelani Ganga) | 0.76 | 🟢 Normal | -0.009 |  |
| 2026-11-02 14:00:33 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-11-02 14:02:12 | Moraketiya (Walawe Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-02 14:00:22 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-11-02 13:03:38 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.011 |  |
| 2026-11-02 14:01:26 | Kuda Oya (Kirindi Oya) | 1.47 | 🟢 Normal | -0.011 |  |
| 2026-11-02 13:06:02 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | -0.015 |  |
| 2026-11-02 13:02:51 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.021 |  |
| 2026-11-02 14:02:28 | Siyambalanduwa (Heda Oya) | 0.69 | 🟢 Normal | -0.022 |  |
| 2026-11-02 14:02:28 | Thalgahagoda (Nilwala Ganga) | 1.33 | 🟢 Normal | -0.023 |  |
| 2026-11-02 14:03:17 | Giriulla (Maha Oya) | 1.40 | 🟢 Normal | -0.030 |  |
| 2026-11-02 13:05:06 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.030 |  |
| 2026-11-02 14:02:30 | Thanamalwila (Kirindi Oya) | 1.17 | 🟢 Normal | -0.031 |  |
| 2026-11-02 13:06:04 | Magura (Kalu Ganga) | 2.27 | 🟢 Normal | -0.031 |  |
| 2026-11-02 13:04:51 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.038 |  |
| 2026-11-02 13:05:55 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | -0.047 |  |
| 2026-11-02 14:03:46 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -0.049 |  |
| 2026-11-02 14:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.91 | 🟢 Normal | -0.051 |  |
| 2026-11-02 13:02:53 | Hanwella (Kelani Ganga) | 2.81 | 🟢 Normal | -0.070 |  |
| 2026-11-02 13:03:45 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.090 |  |
| 2026-11-02 14:00:25 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | -0.140 |  |
| 2026-11-02 13:12:14 | Panadugama (Nilwala Ganga) | 4.56 | 🟢 Normal | -1.511 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)