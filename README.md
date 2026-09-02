# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_23:33:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **250,214 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 23:33:28 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:14:03 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-09-02 23:11:43 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:08:12 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 1.800 | 🔺 Rising |
| 2026-09-02 23:08:05 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:07:52 | Thawalama (Gin Ganga) | 1.43 | 🟢 Normal | 1.800 | 🔺 Rising |
| 2026-09-02 23:07:06 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-09-02 23:06:33 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:05:45 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-09-02 23:05:15 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:05:03 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-09-02 23:04:54 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:04:05 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:04:01 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:03:58 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-02 23:03:42 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:03:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:03:06 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-09-02 23:02:42 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-02 23:02:37 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:02:29 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:02:15 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-02 23:02:12 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-02 23:02:05 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:01:25 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:01:05 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:00:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:00:45 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:00:25 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:00:14 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:00:09 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 23:08:12 | Thawalama (Gin Ganga) | 1.44 | 🟢 Normal | 1.800 | 🔺 Rising |
| 2026-09-02 23:03:06 | Peradeniya (Mahaweli Ganga) | 3.12 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-09-02 21:10:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.18 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-02 23:02:12 | Glencourse (Kelani Ganga) | 9.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-02 23:02:42 | Manampitiya (Mahaweli Ganga) | 0.05 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-02 23:03:58 | Deraniyagala (Kelani Ganga) | 0.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-02 23:06:33 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:00:09 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:00:25 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:00:45 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:01:12 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:03:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:00:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 18:04:32 | Galgamuwa (Mee Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-09-02 22:06:19 | Magura (Kalu Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:04:01 | Pitabeddara (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:02:29 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-02 22:09:23 | Ellagawa (Kalu Ganga) | 4.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:03:42 | Panadugama (Nilwala Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:00:14 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:04:54 | Nagalagam Street (Kelani Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:08:05 | Moraketiya (Walawe Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:04:05 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:11:43 | Dunamale (Aththanagalu Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:02:05 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:02:37 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:33:28 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:05:15 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-02 18:03:25 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-02 22:03:40 | Urawa (Nilwala Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:01:25 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-02 23:01:05 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 22:02:18 | Rathnapura (Kalu Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-09-02 23:02:15 | Hanwella (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-09-02 23:05:03 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-09-02 23:07:06 | Baddegama (Gin Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-09-02 23:14:03 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.020 |  |
| 2026-09-02 23:05:45 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.031 |  |
| 2026-09-02 18:00:38 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)