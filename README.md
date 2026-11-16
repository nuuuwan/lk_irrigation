# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--16_15:08:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **317,497 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 15:08:02 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-11-16 15:07:56 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-16 15:07:52 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | -0.009 |  |
| 2026-11-16 15:07:23 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.019 |  |
| 2026-11-16 15:07:22 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.009 |  |
| 2026-11-16 15:06:23 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:06:06 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.012 |  |
| 2026-11-16 15:05:46 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:05:42 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-11-16 15:05:25 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:05:18 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:04:48 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:04:48 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.041 |  |
| 2026-11-16 15:04:39 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:04:27 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:04:17 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-16 15:04:08 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:04:03 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:03:52 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:03:38 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-16 15:03:02 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:02:45 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:02:42 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:02:42 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-11-16 15:02:26 | Hanwella (Kelani Ganga) | 2.15 | 🟢 Normal | -0.020 |  |
| 2026-11-16 15:02:23 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:01:53 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:01:52 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-16 15:01:45 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-16 15:01:41 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:01:35 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-16 15:01:34 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.051 |  |
| 2026-11-16 15:01:11 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:00:59 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.635 |  |
| 2026-11-16 15:00:57 | Thalgahagoda (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.047 |  |
| 2026-11-16 15:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:00:38 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:00:35 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:58:09 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -0.635 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-16 15:01:35 | Weraganthota (Mahaweli Ganga) | -1.92 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-11-16 15:01:45 | Thaldena (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-16 15:01:52 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-11-16 15:03:38 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-16 15:07:56 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-16 15:04:17 | Rathnapura (Kalu Ganga) | 1.68 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-11-16 15:04:27 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:00:41 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:01:41 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:04:08 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:06:23 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:05:46 | Siyambalanduwa (Heda Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:01:53 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:03:52 | Katharagama (Menik Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:00:35 | Manampitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-11-16 14:01:26 | Thanthirimale (Malwathu Oya) | 1.51 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:03:02 | Peradeniya (Mahaweli Ganga) | 2.88 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:04:48 | Urawa (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:02:42 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:02:42 | Thanamalwila (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-11-16 15:07:22 | Ellagawa (Kalu Ganga) | 5.30 | 🟢 Normal | -0.009 |  |
| 2026-11-16 15:07:52 | Panadugama (Nilwala Ganga) | 4.38 | 🟢 Normal | -0.009 |  |
| 2026-11-16 15:02:45 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:04:03 | Giriulla (Maha Oya) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:00:38 | Horowpothana (Yan Oya) | 2.02 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:01:11 | Moragaswewa (Deduru Oya) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:02:23 | Deraniyagala (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:05:25 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:05:18 | Badalgama (Maha Oya) | 2.70 | 🟢 Normal | -0.010 |  |
| 2026-11-16 15:06:06 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.012 |  |
| 2026-11-16 15:07:23 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.019 |  |
| 2026-11-16 15:08:02 | Moraketiya (Walawe Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-11-16 15:02:26 | Hanwella (Kelani Ganga) | 2.15 | 🟢 Normal | -0.020 |  |
| 2026-11-16 15:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-11-16 15:05:42 | Padiyathalawa (Maduru Oya) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-11-16 15:04:48 | Glencourse (Kelani Ganga) | 10.31 | 🟢 Normal | -0.041 |  |
| 2026-11-16 15:00:57 | Thalgahagoda (Nilwala Ganga) | 1.35 | 🟢 Normal | -0.047 |  |
| 2026-11-16 15:01:34 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | -0.051 |  |
| 2026-11-16 15:00:59 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.635 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)