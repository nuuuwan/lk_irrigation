# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_10:04:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **305,599 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 10:04:03 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.048 |  |
| 2026-11-03 10:04:03 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:04:02 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-11-03 10:03:55 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-11-03 10:03:55 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.011 |  |
| 2026-11-03 10:03:53 | Horowpothana (Yan Oya) | 2.78 | 🟢 Normal | -0.105 |  |
| 2026-11-03 10:03:49 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | -0.070 |  |
| 2026-11-03 10:03:42 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:03:39 | Hanwella (Kelani Ganga) | 3.32 | 🟢 Normal | -0.080 |  |
| 2026-11-03 10:03:36 | Manampitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-11-03 10:03:35 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:03:29 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 10:03:14 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-03 10:03:12 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-03 10:03:12 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.019 |  |
| 2026-11-03 10:03:09 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:03:00 | Moragaswewa (Deduru Oya) | 4.09 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-03 10:02:50 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-03 10:02:39 | Rathnapura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.114 |  |
| 2026-11-03 10:02:27 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 10:02:03 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.056 |  |
| 2026-11-03 10:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:01:42 | Wellawaya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.060 |  |
| 2026-11-03 10:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:01:30 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:01:08 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 10:00:50 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.085 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 10:03:36 | Manampitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | 0.232 | 🔺 Rising |
| 2026-11-03 10:03:00 | Moragaswewa (Deduru Oya) | 4.09 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-11-03 10:02:50 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | 0.109 | 🔺 Rising |
| 2026-11-03 10:03:12 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-03 09:05:20 | Badalgama (Maha Oya) | 3.82 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-03 10:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.93 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-03 09:03:53 | Pitabeddara (Nilwala Ganga) | 1.48 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-11-03 10:03:29 | Deraniyagala (Kelani Ganga) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 10:01:08 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-03 09:03:23 | Kithulgala (Kelani Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:03:09 | Nakkala (Kumbukkan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:01:39 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:03:42 | Ellagawa (Kalu Ganga) | 6.66 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:07:17 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:04:03 | Dunamale (Aththanagalu Oya) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:01:30 | Katharagama (Menik Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:03:35 | Thalgahagoda (Nilwala Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-11-03 09:06:19 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-11-03 10:04:02 | Moraketiya (Walawe Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-11-03 10:03:14 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -0.010 |  |
| 2026-11-03 09:06:55 | Magura (Kalu Ganga) | 2.12 | 🟢 Normal | -0.010 |  |
| 2026-11-03 10:03:55 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | -0.011 |  |
| 2026-11-03 09:14:25 | Urawa (Nilwala Ganga) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-11-03 10:03:12 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.019 |  |
| 2026-11-03 10:03:55 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.019 |  |
| 2026-11-03 09:21:32 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.025 |  |
| 2026-11-03 09:06:03 | Holombuwa (Kelani Ganga) | 1.13 | 🟢 Normal | -0.030 |  |
| 2026-11-03 09:06:44 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | -0.030 |  |
| 2026-11-03 10:04:03 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.048 |  |
| 2026-11-03 10:02:03 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.056 |  |
| 2026-11-03 10:01:42 | Wellawaya (Kirindi Oya) | 1.66 | 🟢 Normal | -0.060 |  |
| 2026-11-03 10:03:49 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | -0.070 |  |
| 2026-11-03 10:03:39 | Hanwella (Kelani Ganga) | 3.32 | 🟢 Normal | -0.080 |  |
| 2026-11-03 10:00:50 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | -0.085 |  |
| 2026-11-03 08:06:23 | Giriulla (Maha Oya) | 2.89 | 🟢 Normal | -0.098 |  |
| 2026-11-03 10:03:53 | Horowpothana (Yan Oya) | 2.78 | 🟢 Normal | -0.105 |  |
| 2026-11-03 10:02:39 | Rathnapura (Kalu Ganga) | 2.88 | 🟢 Normal | -0.114 |  |
| 2026-11-03 09:06:40 | Glencourse (Kelani Ganga) | 11.08 | 🟢 Normal | -0.179 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)