# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--16_20:12:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **262,744 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **2** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 20:12:16 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-16 20:12:12 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-16 20:04:09 | Thawalama (Gin Ganga) | 2.38 | 🟢 Normal | 0.294 | 🔺 Rising |
| 2026-09-16 20:03:24 | Peradeniya (Mahaweli Ganga) | 2.27 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-09-16 20:01:38 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-09-16 20:02:15 | Magura (Kalu Ganga) | 3.05 | 🟢 Normal | 0.146 | 🔺 Rising |
| 2026-09-16 20:12:16 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-16 20:01:40 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-16 20:08:05 | Urawa (Nilwala Ganga) | 0.02 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-09-16 20:02:37 | Manampitiya (Mahaweli Ganga) | 0.02 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-16 20:02:16 | Thanamalwila (Kirindi Oya) | 1.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-16 20:10:34 | Putupaula (Kalu Ganga) | 1.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-16 19:17:02 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-09-16 18:02:49 | Weraganthota (Mahaweli Ganga) | -3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:01:28 | Wellawaya (Kirindi Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:00:57 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:04:49 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:01:10 | Nawalapitiya (Mahaweli Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:01:40 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:02:34 | Giriulla (Maha Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:01:54 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-09-16 18:01:06 | Galgamuwa (Mee Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:12:12 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:00:28 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:02:10 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:05:06 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:05:40 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:04:40 | Rathnapura (Kalu Ganga) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:01:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.67 | 🟢 Normal | 0.000 |  |
| 2026-09-16 20:02:43 | Deraniyagala (Kelani Ganga) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-09-16 20:01:10 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-16 18:00:42 | Thanthirimale (Malwathu Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-09-16 20:02:08 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | -0.010 |  |
| 2026-09-16 20:06:26 | Baddegama (Gin Ganga) | 3.01 | 🟢 Normal | -0.013 |  |
| 2026-09-16 20:05:36 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.020 |  |
| 2026-09-16 20:02:32 | Dunamale (Aththanagalu Oya) | 1.82 | 🟢 Normal | -0.020 |  |
| 2026-09-16 20:02:34 | Norwood (Kelani Ganga) | 0.63 | 🟢 Normal | -0.031 |  |
| 2026-09-16 20:07:13 | Ellagawa (Kalu Ganga) | 5.24 | 🟢 Normal | -0.038 |  |
| 2026-09-16 20:02:22 | Hanwella (Kelani Ganga) | 1.29 | 🟢 Normal | -0.040 |  |
| 2026-09-16 20:04:06 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.050 |  |
| 2026-09-16 20:01:59 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)