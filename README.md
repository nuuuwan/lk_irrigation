# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_08:03:20-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,510 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 08:03:20 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.021 |  |
| 2026-11-03 08:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.87 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-03 08:03:06 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.096 |  |
| 2026-11-03 08:02:43 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -144.000 |  |
| 2026-11-03 08:02:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:02:42 | Kithulgala (Kelani Ganga) | 1.62 | 🟢 Normal | -144.000 |  |
| 2026-11-03 08:02:33 | Moragaswewa (Deduru Oya) | 3.82 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-03 08:02:18 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-03 08:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-03 08:02:12 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-03 08:02:11 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-11-03 08:02:04 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-03 08:01:57 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:01:56 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-03 08:01:45 | Wellawaya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.030 |  |
| 2026-11-03 08:01:36 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:01:25 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.089 |  |
| 2026-11-03 08:00:59 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | -0.042 |  |
| 2026-11-03 08:00:57 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.082 |  |
| 2026-11-03 07:43:38 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.012 |  |
| 2026-11-03 07:23:03 | Horowpothana (Yan Oya) | 3.09 | 🟢 Normal | -0.057 |  |
| 2026-11-03 07:21:59 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | 0.015 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 08:02:33 | Moragaswewa (Deduru Oya) | 3.82 | 🟢 Normal | 0.204 | 🔺 Rising |
| 2026-11-03 07:00:52 | Manampitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-03 08:03:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.87 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-03 07:01:24 | Pitabeddara (Nilwala Ganga) | 1.45 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-03 08:02:18 | Katharagama (Menik Ganga) | 0.08 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-03 08:02:12 | Thawalama (Gin Ganga) | 2.50 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-03 07:04:37 | Ellagawa (Kalu Ganga) | 6.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-03 08:01:56 | Thanthirimale (Malwathu Oya) | 1.53 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-11-03 07:07:54 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-03 08:01:36 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 07:03:57 | Galgamuwa (Mee Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:01:57 | Baddegama (Gin Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-03 08:02:42 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-03 07:12:17 | Badalgama (Maha Oya) | 3.60 | 🟢 Normal | 0.000 |  |
| 2026-11-03 07:02:10 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-03 07:05:04 | Dunamale (Aththanagalu Oya) | 1.89 | 🟢 Normal | -0.010 |  |
| 2026-11-03 08:02:04 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-11-03 08:02:12 | Nawalapitiya (Mahaweli Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-11-03 07:43:38 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.012 |  |
| 2026-11-03 08:02:11 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.020 |  |
| 2026-11-03 08:03:20 | Hanwella (Kelani Ganga) | 3.45 | 🟢 Normal | -0.021 |  |
| 2026-11-03 07:15:19 | Panadugama (Nilwala Ganga) | 4.04 | 🟢 Normal | -0.025 |  |
| 2026-11-03 08:01:45 | Wellawaya (Kirindi Oya) | 1.68 | 🟢 Normal | -0.030 |  |
| 2026-11-03 08:00:59 | Moraketiya (Walawe Ganga) | 1.43 | 🟢 Normal | -0.042 |  |
| 2026-11-03 07:11:47 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.043 |  |
| 2026-11-03 07:03:26 | Thaldena (Mahaweli Ganga) | 0.92 | 🟢 Normal | -0.051 |  |
| 2026-11-03 07:23:03 | Horowpothana (Yan Oya) | 3.09 | 🟢 Normal | -0.057 |  |
| 2026-11-03 07:04:21 | Siyambalanduwa (Heda Oya) | 0.89 | 🟢 Normal | -0.059 |  |
| 2026-11-03 07:06:05 | Holombuwa (Kelani Ganga) | 1.22 | 🟢 Normal | -0.061 |  |
| 2026-11-03 08:00:57 | Nakkala (Kumbukkan Oya) | 1.33 | 🟢 Normal | -0.082 |  |
| 2026-11-03 07:05:16 | Giriulla (Maha Oya) | 2.99 | 🟢 Normal | -0.087 |  |
| 2026-11-03 08:01:25 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.089 |  |
| 2026-11-03 08:03:06 | Kuda Oya (Kirindi Oya) | 2.00 | 🟢 Normal | -0.096 |  |
| 2026-11-03 07:04:25 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal | -0.116 |  |
| 2026-11-03 07:20:18 | Rathnapura (Kalu Ganga) | 3.22 | 🟢 Normal | -0.120 |  |
| 2026-11-03 07:11:06 | Glencourse (Kelani Ganga) | 11.43 | 🟢 Normal | -0.157 |  |
| 2026-11-03 07:01:59 | Thanamalwila (Kirindi Oya) | 2.20 | 🟢 Normal | -0.215 |  |
| 2026-11-03 07:05:40 | Peradeniya (Mahaweli Ganga) | 3.46 | 🟢 Normal | -0.278 |  |
| 2026-11-03 08:02:43 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | -144.000 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)