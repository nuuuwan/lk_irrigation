# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--20_01:31:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **320,519 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 01:31:35 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-20 01:11:45 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-20 01:11:17 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.009 |  |
| 2026-11-20 01:11:02 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:09:17 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-20 01:07:40 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 01:06:55 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:06:47 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:06:06 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 01:05:43 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:05:38 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-11-20 01:05:34 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-20 01:04:55 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:04:17 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:04:10 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-20 01:04:06 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 01:03:56 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:03:11 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:02:17 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:02:09 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-20 01:01:51 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-20 01:01:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:01:35 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:01:32 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:01:25 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:01:25 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 01:01:08 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:00:41 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-20 01:00:35 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 01:04:10 | Glencourse (Kelani Ganga) | 9.63 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-11-20 00:04:51 | Thalgahagoda (Nilwala Ganga) | 0.60 | 🟢 Normal | 0.084 | 🔺 Rising |
| 2026-11-20 01:06:06 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-20 01:01:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-20 01:05:34 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-20 01:09:17 | Moraketiya (Walawe Ganga) | 1.88 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-11-20 01:31:35 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-11-20 01:07:40 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 01:01:25 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 01:04:06 | Thawalama (Gin Ganga) | 1.61 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-19 18:00:52 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:01:35 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:05:40 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:01:32 | Moragaswewa (Deduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:00:35 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:01:25 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:05:43 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:04:17 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:01:08 | Ellagawa (Kalu Ganga) | 4.81 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:01:45 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:06:55 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:18:54 | Dunamale (Aththanagalu Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-20 00:02:29 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:11:02 | Badalgama (Maha Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:06:47 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:03:56 | Manampitiya (Mahaweli Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-11-19 18:01:52 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:04:55 | Peradeniya (Mahaweli Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:03:59 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:01:51 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-20 01:11:17 | Katharagama (Menik Ganga) | 0.14 | 🟢 Normal | -0.009 |  |
| 2026-11-19 18:05:17 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-11-20 00:07:56 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-11-20 01:11:45 | Rathnapura (Kalu Ganga) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-11-20 01:00:41 | Magura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-20 01:02:09 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-20 00:07:01 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -0.014 |  |
| 2026-11-20 01:05:38 | Hanwella (Kelani Ganga) | 1.18 | 🟢 Normal | -0.020 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)