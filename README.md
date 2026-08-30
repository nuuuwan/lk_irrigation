# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_15:02:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,236 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 15:02:52 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:51 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:47 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.010 |  |
| 2026-08-30 15:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:34 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-30 15:02:34 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:19 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:18 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:17 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.032 |  |
| 2026-08-30 15:01:51 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:01:47 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-08-30 15:01:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-30 15:01:34 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-08-30 15:01:21 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-30 15:01:14 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:01:12 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.022 |  |
| 2026-08-30 15:00:45 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-30 15:00:44 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:00:42 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:00:36 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-30 14:15:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.061 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 14:02:12 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-08-30 15:01:43 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-30 15:02:34 | Deraniyagala (Kelani Ganga) | 0.74 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-30 15:01:21 | Weraganthota (Mahaweli Ganga) | -3.60 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-30 15:00:45 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-30 15:01:14 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:18 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:52 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-30 14:03:25 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:34 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-08-30 14:01:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:01:51 | Giriulla (Maha Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:00:36 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-30 14:12:16 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-30 14:09:25 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:51 | Hanwella (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:34 | Baddegama (Gin Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-08-30 14:04:28 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 14:01:13 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-30 14:05:17 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:02:19 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-30 14:01:42 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 14:06:52 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-30 14:04:13 | Thalgahagoda (Nilwala Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-30 15:00:44 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 14:14:08 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.009 |  |
| 2026-08-30 15:02:47 | Ellagawa (Kalu Ganga) | 5.02 | 🟢 Normal | -0.010 |  |
| 2026-08-30 15:01:47 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-08-30 14:03:46 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-08-30 14:03:37 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-30 15:01:34 | Pitabeddara (Nilwala Ganga) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-08-30 14:04:07 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | -0.011 |  |
| 2026-08-30 14:02:10 | Dunamale (Aththanagalu Oya) | 0.37 | 🟢 Normal | -0.021 |  |
| 2026-08-30 15:01:12 | Peradeniya (Mahaweli Ganga) | 2.48 | 🟢 Normal | -0.022 |  |
| 2026-08-30 14:06:22 | Panadugama (Nilwala Ganga) | 3.33 | 🟢 Normal | -0.029 |  |
| 2026-08-30 15:02:17 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.032 |  |
| 2026-08-30 14:06:32 | Rathnapura (Kalu Ganga) | 1.30 | 🟢 Normal | -0.047 |  |
| 2026-08-30 14:07:22 | Glencourse (Kelani Ganga) | 9.83 | 🟢 Normal | -0.059 |  |
| 2026-08-30 14:15:44 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)