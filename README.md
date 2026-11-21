# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--21_21:03:11-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **322,128 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 21:03:11 | Badalgama (Maha Oya) | 3.92 | 🟢 Normal | -0.149 |  |
| 2026-11-21 21:03:07 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.052 |  |
| 2026-11-21 21:03:05 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.118 |  |
| 2026-11-21 21:03:02 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:02:40 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-11-21 21:02:22 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:02:21 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:02:20 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.040 |  |
| 2026-11-21 21:02:01 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | -0.020 |  |
| 2026-11-21 21:01:28 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 21:01:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:01:15 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 21:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-21 21:01:13 | Giriulla (Maha Oya) | 2.46 | 🟢 Normal | -0.073 |  |
| 2026-11-21 21:01:12 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.060 |  |
| 2026-11-21 21:00:36 | Horowpothana (Yan Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:00:13 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-21 20:25:50 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-21 20:17:20 | Panadugama (Nilwala Ganga) | 4.62 | 🟢 Normal | -0.058 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-21 20:06:06 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-11-21 20:04:59 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-11-21 20:02:51 | Peradeniya (Mahaweli Ganga) | 2.92 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-11-21 21:00:13 | Wellawaya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-21 21:01:28 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 21:01:15 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-21 18:00:46 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:01:22 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:00:36 | Horowpothana (Yan Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:00:19 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-11-21 20:25:50 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52⌛ | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-21 20:03:55 | Moraketiya (Walawe Ganga) | 2.97 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:02:01 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:02:21 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:03:02 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-11-21 20:07:03 | Manampitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-21 18:02:22 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-21 20:00:12 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-11-21 20:13:39 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-11-21 20:02:47 | Thanamalwila (Kirindi Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-11-21 21:01:14 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-11-21 21:02:40 | Deraniyagala (Kelani Ganga) | 0.56 | 🟢 Normal | -0.020 |  |
| 2026-11-21 21:01:39 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.46 | 🟢 Normal | -0.020 |  |
| 2026-11-21 20:02:27 | Putupaula (Kalu Ganga) | 0.83 | 🟢 Normal | -0.031 |  |
| 2026-11-21 20:02:15 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.033 |  |
| 2026-11-21 21:02:20 | Baddegama (Gin Ganga) | 1.77 | 🟢 Normal | -0.040 |  |
| 2026-11-21 21:03:07 | Glencourse (Kelani Ganga) | 9.48 | 🟢 Normal | -0.052 |  |
| 2026-11-21 20:17:20 | Panadugama (Nilwala Ganga) | 4.62 | 🟢 Normal | -0.058 |  |
| 2026-11-21 20:04:05 | Dunamale (Aththanagalu Oya) | 1.56 | 🟢 Normal | -0.060 |  |
| 2026-11-21 21:01:12 | Kuda Oya (Kirindi Oya) | 2.15 | 🟢 Normal | -0.060 |  |
| 2026-11-21 20:04:02 | Hanwella (Kelani Ganga) | 1.70 | 🟢 Normal | -0.063 |  |
| 2026-11-21 21:01:13 | Giriulla (Maha Oya) | 2.46 | 🟢 Normal | -0.073 |  |
| 2026-11-21 20:04:58 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.078 |  |
| 2026-11-21 20:05:26 | Ellagawa (Kalu Ganga) | 5.92 | 🟢 Normal | -0.079 |  |
| 2026-11-21 20:05:35 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.088 |  |
| 2026-11-21 20:06:46 | Rathnapura (Kalu Ganga) | 1.91 | 🟢 Normal | -0.104 |  |
| 2026-11-21 21:03:05 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.118 |  |
| 2026-11-21 21:03:11 | Badalgama (Maha Oya) | 3.92 | 🟢 Normal | -0.149 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)