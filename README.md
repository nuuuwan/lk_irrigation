# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_23:30:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,789 measurements** from **39** stations.
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
| 2026-11-16 23:30:11 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:23:17 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:10:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.058 |  |
| 2026-11-16 23:10:18 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:08:54 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.018 |  |
| 2026-11-16 23:07:40 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.093 |  |
| 2026-11-16 23:07:15 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:07:13 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-16 23:05:49 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.029 |  |
| 2026-11-16 23:05:32 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 23:05:23 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:05:16 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.026 |  |
| 2026-11-16 23:05:11 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:05:03 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:05:02 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.011 |  |
| 2026-11-16 23:04:45 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:04:41 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:04:06 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.020 |  |
| 2026-11-16 23:03:06 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:02:58 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:02:28 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:02:24 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-11-16 23:02:24 | Hanwella (Kelani Ganga) | 2.07 | 🟢 Normal | -0.022 |  |
| 2026-11-16 23:02:16 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:02:12 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-11-16 23:02:08 | Thanamalwila (Kirindi Oya) | 1.38 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-11-16 23:02:00 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-16 23:01:27 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:01:14 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:01:08 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:00:56 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:00:17 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 23:02:24 | Thanamalwila (Kirindi Oya) | 1.40 | 🟢 Normal | 4.500 | 🔺 Rising |
| 2026-11-16 23:02:00 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-16 23:05:32 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-16 23:07:13 | Moraketiya (Walawe Ganga) | 1.71 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-16 23:02:16 | Moragaswewa (Deduru Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:30:11 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:01:14 | Horowpothana (Yan Oya) | 2.01 | 🟢 Normal | 0.000 |  |
| 2026-11-16 18:04:42 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:16:19 | Pitabeddara (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:03:10 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:02:28 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:04:45 | Padiyathalawa (Maduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:05:03 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:02:58 | Dunamale (Aththanagalu Oya) | 1.75 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:23:17 | Thaldena (Mahaweli Ganga) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:07:15 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:04:41 | Holombuwa (Kelani Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-11-16 18:00:40 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-16 22:29:18 | Thalgahagoda (Nilwala Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-11-16 23:05:11 | Badalgama (Maha Oya) | 2.67 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:01:27 | Nakkala (Kumbukkan Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:05:23 | Rathnapura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:03:06 | Giriulla (Maha Oya) | 1.36 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:10:18 | Magura (Kalu Ganga) | 1.71 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:00:17 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:01:08 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:00:56 | Urawa (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-11-16 23:05:02 | Thawalama (Gin Ganga) | 1.86 | 🟢 Normal | -0.011 |  |
| 2026-11-16 23:08:54 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | -0.018 |  |
| 2026-11-16 23:04:06 | Peradeniya (Mahaweli Ganga) | 2.95 | 🟢 Normal | -0.020 |  |
| 2026-11-16 23:02:12 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.020 |  |
| 2026-11-16 23:02:24 | Hanwella (Kelani Ganga) | 2.07 | 🟢 Normal | -0.022 |  |
| 2026-11-16 22:06:10 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | -0.024 |  |
| 2026-11-16 23:05:16 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | -0.026 |  |
| 2026-11-16 23:05:49 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.029 |  |
| 2026-11-16 22:01:58 | Wellawaya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.030 |  |
| 2026-11-16 18:02:17 | Weraganthota (Mahaweli Ganga) | -1.91 | 🟢 Normal | -0.041 |  |
| 2026-11-16 23:10:25 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | -0.058 |  |
| 2026-11-16 23:07:40 | Putupaula (Kalu Ganga) | 0.72 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)