# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_05:05:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,658 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **27** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 05:05:57 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:05:54 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:05:45 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-10-01 05:04:43 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-10-01 05:04:37 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-10-01 05:04:35 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | -0.019 |  |
| 2026-10-01 05:04:05 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:03:54 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:03:23 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-10-01 05:03:15 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.019 |  |
| 2026-10-01 05:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:03:11 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:02:57 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.015 |  |
| 2026-10-01 05:02:54 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-10-01 05:02:38 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:01:55 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:01:51 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:01:30 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:01:26 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.010 |  |
| 2026-10-01 05:01:09 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.043 |  |
| 2026-10-01 05:01:05 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-01 05:00:55 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:00:49 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:00:15 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-10-01 05:00:06 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-01 04:59:37 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.000 |  |
| 2026-10-01 04:57:16 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 04:07:11 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.330 | 🔺 Rising |
| 2026-10-01 05:05:45 | Giriulla (Maha Oya) | 1.22 | 🟢 Normal | 0.183 | 🔺 Rising |
| 2026-10-01 05:03:23 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-09-30 18:00:36 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-01 04:09:11 | Thalgahagoda (Nilwala Ganga) | 0.61 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-01 05:01:05 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-01 05:01:51 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:03:12 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:27:28 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 02:07:23 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-01 04:02:56 | Norwood (Kelani Ganga) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:02:38 | Deraniyagala (Kelani Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:05:57 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:05:54 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:03:11 | Glencourse (Kelani Ganga) | 10.30 | 🟢 Normal | 0.000 |  |
| 2026-10-01 02:59:56 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:01:30 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:00:49 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:01:55 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-01 04:10:25 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:04:05 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:03:54 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-09-30 17:00:54 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:00:55 | Urawa (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-01 04:06:15 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 05:04:43 | Badalgama (Maha Oya) | 2.13 | 🟢 Normal | -0.010 |  |
| 2026-10-01 05:02:54 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-10-01 05:01:26 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.010 |  |
| 2026-10-01 05:00:15 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.011 |  |
| 2026-10-01 04:33:54 | Panadugama (Nilwala Ganga) | 3.20 | 🟢 Normal | -0.014 |  |
| 2026-10-01 05:02:57 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.015 |  |
| 2026-10-01 05:04:35 | Hanwella (Kelani Ganga) | 1.99 | 🟢 Normal | -0.019 |  |
| 2026-10-01 05:03:15 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | -0.019 |  |
| 2026-10-01 04:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.52 | 🟢 Normal | -0.021 |  |
| 2026-10-01 05:04:37 | Dunamale (Aththanagalu Oya) | 1.03 | 🟢 Normal | -0.030 |  |
| 2026-10-01 05:01:09 | Peradeniya (Mahaweli Ganga) | 2.58 | 🟢 Normal | -0.043 |  |
| 2026-10-01 04:03:48 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | -0.109 |  |
| 2026-10-01 04:15:03 | Thanamalwila (Kirindi Oya) | 0.38 | 🟢 Normal | -0.118 |  |
| 2026-10-01 04:04:18 | Magura (Kalu Ganga) | 1.66 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)