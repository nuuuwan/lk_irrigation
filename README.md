# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--02_03:30:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **249,453 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 03:30:57 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-02 03:13:32 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | -0.009 |  |
| 2026-09-02 03:13:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-02 03:10:10 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-09-02 03:09:47 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:08:23 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.003 |  |
| 2026-09-02 03:08:14 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-09-02 03:07:09 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.025 |  |
| 2026-09-02 03:05:45 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-09-02 03:05:29 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:05:19 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-09-02 03:05:12 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:04:51 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:04:33 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:04:31 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-02 03:04:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-02 03:04:23 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:04:11 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:03:47 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:03:46 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:03:40 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:03:26 | Peradeniya (Mahaweli Ganga) | 2.34 | 🟢 Normal | -0.251 |  |
| 2026-09-02 03:03:07 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:02:39 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:02:00 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.030 |  |
| 2026-09-02 03:01:42 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-02 03:01:34 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 03:01:13 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:00:39 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.069 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-02 03:04:24 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-02 03:00:39 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-02 03:13:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-09-02 03:01:42 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-02 03:30:57 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-02 03:04:31 | Hanwella (Kelani Ganga) | 1.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-02 03:01:34 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-02 02:12:35 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-02 01:02:52 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.005 |  |
| 2026-09-02 03:08:23 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.003 |  |
| 2026-09-02 00:04:58 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:05:29 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:05:12 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:03:40 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-02 01:00:48 | Horowpothana (Yan Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-09-02 02:09:14 | Pitabeddara (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:03:07 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-09-02 01:00:50 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:04:51 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:02:39 | Siyambalanduwa (Heda Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:09:47 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:01:13 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:04:11 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:03:46 | Badalgama (Maha Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-09-01 23:01:26 | Manampitiya (Mahaweli Ganga) | -0.62 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:04:33 | Rathnapura (Kalu Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-01 17:00:53 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-02 02:01:54 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-02 03:13:32 | Ellagawa (Kalu Ganga) | 4.62 | 🟢 Normal | -0.009 |  |
| 2026-09-02 03:10:10 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.009 |  |
| 2026-09-02 03:08:14 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-09-02 03:05:45 | Baddegama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-09-02 03:05:19 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.010 |  |
| 2026-09-01 18:04:47 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | -0.010 |  |
| 2026-09-02 00:04:39 | Magura (Kalu Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-09-02 03:07:09 | Holombuwa (Kelani Ganga) | 0.29 | 🟢 Normal | -0.025 |  |
| 2026-09-02 03:02:00 | Glencourse (Kelani Ganga) | 9.50 | 🟢 Normal | -0.030 |  |
| 2026-09-01 18:01:28 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.060 |  |
| 2026-09-02 03:03:26 | Peradeniya (Mahaweli Ganga) | 2.34 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)