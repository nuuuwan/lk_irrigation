# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--15_15:23:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **234,229 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 15:23:19 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | -0.007 |  |
| 2026-08-15 15:16:42 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:12:18 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:09:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-15 15:09:35 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.018 |  |
| 2026-08-15 15:09:09 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-15 15:08:11 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-15 15:05:30 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-15 15:05:30 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:04:56 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:04:40 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.022 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-15 15:01:32 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-08-15 15:01:43 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-15 15:08:11 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-15 15:09:48 | Holombuwa (Kelani Ganga) | 0.42 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-15 15:09:09 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-15 15:03:53 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-15 15:00:50 | Kithulgala (Kelani Ganga) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:02:37 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:02:03 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:01:58 | Moragaswewa (Deduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:01:26 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:03:08 | Giriulla (Maha Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:00:42 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:02:17 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:00:46 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:12:18 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:04:16 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:02:46 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:05:30 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:16:42 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:04:56 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:01:18 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:02:12 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.19 | 🟢 Normal | 0.000 |  |
| 2026-08-15 15:23:19 | Thanthirimale (Malwathu Oya) | 0.70 | 🟢 Normal | -0.007 |  |
| 2026-08-15 15:05:30 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-15 15:02:29 | Deraniyagala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-08-15 15:02:45 | Thawalama (Gin Ganga) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-08-15 15:01:08 | Ellagawa (Kalu Ganga) | 6.08 | 🟢 Normal | -0.011 |  |
| 2026-08-15 15:09:35 | Dunamale (Aththanagalu Oya) | 0.38 | 🟢 Normal | -0.018 |  |
| 2026-08-15 15:03:34 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.020 |  |
| 2026-08-15 15:03:26 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-08-15 15:04:40 | Panadugama (Nilwala Ganga) | 2.54 | 🟢 Normal | -0.022 |  |
| 2026-08-15 15:02:31 | Magura (Kalu Ganga) | 1.74 | 🟢 Normal | -0.029 |  |
| 2026-08-15 15:02:32 | Rathnapura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.051 |  |
| 2026-08-15 15:02:32 | Weraganthota (Mahaweli Ganga) | -3.07 | 🟢 Normal | -0.058 |  |
| 2026-08-15 15:02:53 | Hanwella (Kelani Ganga) | 2.40 | 🟢 Normal | -0.061 |  |
| 2026-08-15 15:02:55 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.085 |  |
| 2026-08-15 15:03:26 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)