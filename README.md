# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_07:15:43-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **240,178 measurements** from **39** stations.
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
| 2026-08-22 07:15:43 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:15:04 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:13:43 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.035 |  |
| 2026-08-22 07:12:59 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:12:50 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:12:15 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:10:39 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:09:28 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-08-22 07:08:43 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-08-22 07:07:54 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.030 |  |
| 2026-08-22 07:07:49 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.051 |  |
| 2026-08-22 07:06:55 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.156 |  |
| 2026-08-22 07:06:40 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-08-22 07:05:52 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:05:40 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-22 07:05:25 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:05:16 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:05:05 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.038 |  |
| 2026-08-22 07:04:58 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:04:33 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-22 07:01:05 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-22 07:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 07:04:11 | Hanwella (Kelani Ganga) | 1.66 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-22 07:04:08 | Wellawaya (Kirindi Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-22 07:02:12 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:10:39 | Moragaswewa (Deduru Oya) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:02:05 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:05:52 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:12:59 | Galgamuwa (Mee Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:05:25 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:15:43 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:12:50 | Norwood (Kelani Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:03:17 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:04:17 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:01:18 | Moraketiya (Walawe Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:15:04 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:01:08 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:04:33 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:04:58 | Thanthirimale (Malwathu Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:03:45 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-22 06:01:54 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:05:16 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:02:10 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-22 07:06:40 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-08-22 07:05:40 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-22 07:09:28 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-08-22 07:02:13 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-08-22 07:00:11 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-08-22 07:03:59 | Thaldena (Mahaweli Ganga) | 0.05 | 🟢 Normal | -0.021 |  |
| 2026-08-22 07:02:16 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.022 |  |
| 2026-08-22 07:08:43 | Thawalama (Gin Ganga) | 1.57 | 🟢 Normal | -0.029 |  |
| 2026-08-22 07:07:54 | Ellagawa (Kalu Ganga) | 5.94 | 🟢 Normal | -0.030 |  |
| 2026-08-22 07:01:33 | Holombuwa (Kelani Ganga) | 0.34 | 🟢 Normal | -0.031 |  |
| 2026-08-22 07:13:43 | Rathnapura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.035 |  |
| 2026-08-22 07:05:05 | Putupaula (Kalu Ganga) | 0.85 | 🟢 Normal | -0.038 |  |
| 2026-08-22 07:07:49 | Glencourse (Kelani Ganga) | 9.98 | 🟢 Normal | -0.051 |  |
| 2026-08-22 07:03:53 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.078 |  |
| 2026-08-22 07:02:52 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.084 |  |
| 2026-08-22 07:06:55 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -0.156 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

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

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)