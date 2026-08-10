# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_10:25:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,558 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **5** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 10:25:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-10 10:15:32 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-08-10 10:15:03 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:14:32 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.079 |  |
| 2026-08-10 10:13:50 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.035 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 10:01:47 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-08-10 10:02:24 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-10 10:02:02 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-10 10:00:50 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 10:05:40 | Hanwella (Kelani Ganga) | 2.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 10:25:27 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-10 10:02:41 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:00:58 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:02:04 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:03:28 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:00:49 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:01:21 | Baddegama (Gin Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:15:03 | Panadugama (Nilwala Ganga) | 3.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:03:25 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:04:48 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:03:16 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:03:21 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:05:08 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:05:02 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:01:48 | Thanthirimale (Malwathu Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:04:17 | Thalgahagoda (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:00:46 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:03:02 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 10:15:32 | Urawa (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.009 |  |
| 2026-08-10 10:05:40 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-08-10 10:01:49 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-08-10 10:02:42 | Deraniyagala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-08-10 10:06:11 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | -0.019 |  |
| 2026-08-10 10:03:26 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | -0.019 |  |
| 2026-08-10 10:01:14 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | -0.020 |  |
| 2026-08-10 10:01:35 | Nawalapitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | -0.020 |  |
| 2026-08-10 10:01:09 | Ellagawa (Kalu Ganga) | 6.32 | 🟢 Normal | -0.020 |  |
| 2026-08-10 10:07:47 | Peradeniya (Mahaweli Ganga) | 3.68 | 🟢 Normal | -0.027 |  |
| 2026-08-10 10:13:50 | Thawalama (Gin Ganga) | 2.06 | 🟢 Normal | -0.035 |  |
| 2026-08-10 10:04:05 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.060 |  |
| 2026-08-10 10:06:10 | Glencourse (Kelani Ganga) | 10.83 | 🟢 Normal | -0.072 |  |
| 2026-08-10 10:14:32 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | -0.079 |  |
| 2026-08-10 10:05:03 | Rathnapura (Kalu Ganga) | 2.65 | 🟢 Normal | -0.088 |  |
| 2026-08-10 10:04:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.60 | 🟢 Normal | -0.121 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)