# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--17_00:03:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,805 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 00:03:39 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-17 00:03:15 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.019 |  |
| 2026-11-17 00:03:10 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-17 00:03:10 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 00:03:03 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | -0.030 |  |
| 2026-11-17 00:02:47 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.045 |  |
| 2026-11-17 00:02:43 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 00:02:34 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-11-17 00:02:28 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-11-17 00:02:26 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.032 |  |
| 2026-11-17 00:01:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-17 00:01:47 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.010 |  |
| 2026-11-17 00:01:12 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-17 00:01:02 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-17 00:00:59 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-17 00:00:40 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.011 |  |
| 2026-11-16 23:30:11 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-17 00:03:39 | Kithulgala (Kelani Ganga) | 2.11 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-17 00:00:59 | Moragaswewa (Deduru Oya) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-16 23:05:32 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 00:02:43 | Thanamalwila (Kirindi Oya) | 1.41 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 00:03:10 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-17 00:01:02 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:30:11 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-17 00:01:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-17 00:03:10 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:01:14 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-16 18:04:42 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:16:19 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:03:10 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:04:45 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:05:03 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | 0.000 |  |
| 2026-11-17 00:02:34 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:02:58 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:23:17 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:07:15 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:04:41 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-16 18:00:40 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:29:18 | Thalgahagoda (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-17 00:01:12 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:05:23 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:10:18 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:00:17 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-11-17 00:01:47 | Peradeniya (Mahaweli Ganga) | 2.94 | 🟢 Normal | -0.010 |  |
| 2026-11-17 00:02:28 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-11-17 00:00:40 | Thawalama (Gin Ganga) | 1.85 | 🟢 Normal | -0.011 |  |
| 2026-11-17 00:03:15 | Urawa (Nilwala Ganga) | 0.99 | 🟢 Normal | -0.019 |  |
| 2026-11-16 22:06:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | -0.024 |  |
| 2026-11-16 23:05:16 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.026 |  |
| 2026-11-17 00:03:03 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | -0.030 |  |
| 2026-11-16 22:01:58 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-11-17 00:02:26 | Panadugama (Nilwala Ganga) | 4.17 | 🟢 Normal | -0.032 |  |
| 2026-11-16 18:02:17 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | -0.041 |  |
| 2026-11-17 00:02:47 | Manampitiya (Mahaweli Ganga) | 1.30 | 🟢 Normal | -0.045 |  |
| 2026-11-16 23:10:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.058 |  |
| 2026-11-16 23:07:40 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)