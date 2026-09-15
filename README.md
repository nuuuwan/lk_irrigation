# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--15_23:03:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,929 measurements** from **39** stations.
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
| 2026-09-15 23:03:16 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 23:03:10 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-15 23:03:09 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.070 |  |
| 2026-09-15 23:02:57 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-09-15 23:02:55 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-09-15 23:02:48 | Manampitiya (Mahaweli Ganga) | -0.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-15 23:02:29 | Dunamale (Aththanagalu Oya) | 2.71 | 🟢 Normal | -0.073 |  |
| 2026-09-15 23:02:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 23:02:18 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-09-15 23:02:06 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | 0.005 |  |
| 2026-09-15 23:01:45 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.012 |  |
| 2026-09-15 23:01:20 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 23:00:45 | Magura (Kalu Ganga) | 3.77 | 🟢 Normal | -0.133 |  |
| 2026-09-15 23:00:34 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-15 23:00:16 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-15 23:02:57 | Moragaswewa (Deduru Oya) | -0.21 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-09-15 23:02:18 | Norwood (Kelani Ganga) | 0.95 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-09-15 22:02:25 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-09-15 22:04:14 | Ellagawa (Kalu Ganga) | 5.39 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-09-15 23:02:48 | Manampitiya (Mahaweli Ganga) | -0.31 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-15 23:01:20 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-15 22:15:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.94 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-09-15 21:04:20 | Putupaula (Kalu Ganga) | 1.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-15 23:03:16 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 22:05:39 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 22:06:38 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-15 23:02:06 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | 0.005 |  |
| 2026-09-15 23:00:34 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-15 21:02:29 | Nawalapitiya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-15 23:02:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-15 23:03:10 | Horowpothana (Yan Oya) | 1.85 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:07:20 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-15 22:08:08 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-09-15 23:00:16 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-09-15 22:11:00 | Urawa (Nilwala Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-15 22:02:03 | Kuda Oya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-15 18:02:30 | Thanthirimale (Malwathu Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-09-15 22:02:42 | Kithulgala (Kelani Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-09-15 22:03:03 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-09-15 22:04:39 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | -0.010 |  |
| 2026-09-15 21:04:57 | Padiyathalawa (Maduru Oya) | 0.15 | 🟢 Normal | -0.010 |  |
| 2026-09-15 23:01:45 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.012 |  |
| 2026-09-15 22:06:18 | Nagalagam Street (Kelani Ganga) | 0.18 | 🟢 Normal | -0.016 |  |
| 2026-09-15 22:09:45 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-09-15 22:04:38 | Deraniyagala (Kelani Ganga) | 1.16 | 🟢 Normal | -0.019 |  |
| 2026-09-15 22:02:10 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | -0.021 |  |
| 2026-09-15 22:07:28 | Baddegama (Gin Ganga) | 3.43 | 🟢 Normal | -0.030 |  |
| 2026-09-15 18:02:40 | Weraganthota (Mahaweli Ganga) | -3.09 | 🟢 Normal | -0.039 |  |
| 2026-09-15 22:03:01 | Panadugama (Nilwala Ganga) | 3.31 | 🟢 Normal | -0.042 |  |
| 2026-09-15 23:03:09 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.070 |  |
| 2026-09-15 23:02:29 | Dunamale (Aththanagalu Oya) | 2.71 | 🟢 Normal | -0.073 |  |
| 2026-09-15 22:04:32 | Hanwella (Kelani Ganga) | 1.90 | 🟢 Normal | -0.088 |  |
| 2026-09-15 23:00:45 | Magura (Kalu Ganga) | 3.77 | 🟢 Normal | -0.133 |  |
| 2026-09-15 22:15:44 | Rathnapura (Kalu Ganga) | 4.01 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)