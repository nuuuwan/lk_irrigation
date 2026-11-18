# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--18_13:03:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **319,170 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 13:03:11 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 13:02:58 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-18 13:02:54 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-11-18 13:02:34 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-18 13:02:27 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-11-18 13:02:07 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-18 13:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-18 13:01:52 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 13:01:52 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 13:01:48 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 13:01:48 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-18 13:01:36 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-18 13:01:25 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-18 13:01:15 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 13:00:48 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-18 12:03:34 | Moraketiya (Walawe Ganga) | 1.72 | 🟢 Normal | 0.615 | 🔺 Rising |
| 2026-11-18 12:01:34 | Manampitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-18 13:01:25 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-18 12:05:52 | Glencourse (Kelani Ganga) | 10.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-18 13:01:48 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-18 13:00:48 | Nakkala (Kumbukkan Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 13:01:52 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-18 13:03:11 | Giriulla (Maha Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-11-18 12:09:50 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-18 13:01:48 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-11-18 12:02:20 | Pitabeddara (Nilwala Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-11-18 12:02:17 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | 0.000 |  |
| 2026-11-18 12:00:46 | Baddegama (Gin Ganga) | 1.48 | 🟢 Normal | 0.000 |  |
| 2026-11-18 13:01:15 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-18 12:01:52 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-18 13:01:52 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-18 12:13:55 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-11-18 12:00:37 | Thalgahagoda (Nilwala Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-18 12:02:13 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-18 12:04:48 | Katharagama (Menik Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-11-18 13:02:34 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-11-18 12:01:04 | Moragaswewa (Deduru Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-11-18 12:05:47 | Badalgama (Maha Oya) | 2.54 | 🟢 Normal | -0.010 |  |
| 2026-11-18 13:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-11-18 13:02:07 | Thanamalwila (Kirindi Oya) | 1.34 | 🟢 Normal | -0.010 |  |
| 2026-11-18 13:02:58 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-18 13:01:36 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-11-18 12:02:38 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.011 |  |
| 2026-11-18 12:01:11 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.021 |  |
| 2026-11-18 12:09:51 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.028 |  |
| 2026-11-18 12:07:09 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.028 |  |
| 2026-11-18 13:02:27 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.030 |  |
| 2026-11-18 12:02:49 | Dunamale (Aththanagalu Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-11-18 13:02:54 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-11-18 12:02:08 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.035 |  |
| 2026-11-18 12:04:11 | Rathnapura (Kalu Ganga) | 1.43 | 🟢 Normal | -0.038 |  |
| 2026-11-18 12:05:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.66 | 🟢 Normal | -0.040 |  |
| 2026-11-18 12:02:33 | Deraniyagala (Kelani Ganga) | 0.53 | 🟢 Normal | -0.040 |  |
| 2026-11-18 12:05:27 | Holombuwa (Kelani Ganga) | 0.63 | 🟢 Normal | -0.049 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)