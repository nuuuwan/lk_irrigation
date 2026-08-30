# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_21:03:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **247,467 measurements** from **39** stations.
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
| 2026-08-30 21:03:09 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:03:08 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-30 21:02:43 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.138 |  |
| 2026-08-30 21:02:39 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:02:31 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.091 |  |
| 2026-08-30 21:02:28 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:02:23 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:02:15 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:02:12 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:01:51 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:01:45 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | -0.010 |  |
| 2026-08-30 21:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-30 21:01:24 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-30 21:01:15 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.125 |  |
| 2026-08-30 21:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-08-30 21:00:57 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:00:42 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:00:16 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-08-30 20:38:57 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 20:33:19 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-30 20:26:41 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 21:01:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.58 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-30 20:06:08 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-30 20:02:38 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-30 20:05:21 | Rathnapura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-30 18:04:01 | Weraganthota (Mahaweli Ganga) | -3.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 21:00:57 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 20:03:35 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:01:51 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:00:16 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:13 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:02:15 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-30 20:07:11 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-30 20:03:07 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 20:03:18 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:00:42 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:02:28 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:02:23 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-30 20:02:14 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:02:39 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-30 20:05:09 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-30 18:00:36 | Thanthirimale (Malwathu Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:03:09 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-30 20:26:41 | Urawa (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-08-30 20:33:19 | Thalgahagoda (Nilwala Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-08-30 20:02:14 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 20:08:14 | Thanamalwila (Kirindi Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-30 21:03:08 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | -0.010 |  |
| 2026-08-30 20:01:23 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-30 21:01:08 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.010 |  |
| 2026-08-30 21:01:24 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-08-30 21:01:45 | Ellagawa (Kalu Ganga) | 4.94 | 🟢 Normal | -0.010 |  |
| 2026-08-30 20:01:54 | Baddegama (Gin Ganga) | 1.71 | 🟢 Normal | -0.025 |  |
| 2026-08-30 20:05:40 | Panadugama (Nilwala Ganga) | 3.19 | 🟢 Normal | -0.029 |  |
| 2026-08-30 20:02:40 | Manampitiya (Mahaweli Ganga) | -0.33 | 🟢 Normal | -0.029 |  |
| 2026-08-30 20:02:23 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.031 |  |
| 2026-08-30 20:01:56 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | -0.054 |  |
| 2026-08-30 21:02:31 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.091 |  |
| 2026-08-30 21:01:15 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.125 |  |
| 2026-08-30 21:02:43 | Kithulgala (Kelani Ganga) | 1.87 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)