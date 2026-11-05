# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_14:02:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,550 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 14:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.030 |  |
| 2026-11-05 14:02:39 | Moragaswewa (Deduru Oya) | 3.45 | 🟢 Normal | -0.039 |  |
| 2026-11-05 14:02:35 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:02:12 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.186 |  |
| 2026-11-05 14:02:09 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-11-05 14:02:03 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:01:57 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-05 14:01:55 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-05 14:01:53 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.026 |  |
| 2026-11-05 14:01:46 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:01:41 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 14:01:30 | Thanamalwila (Kirindi Oya) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-11-05 14:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-05 14:01:27 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.032 |  |
| 2026-11-05 14:00:50 | Thanthirimale (Malwathu Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:00:45 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.110 |  |
| 2026-11-05 14:00:33 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.036 |  |
| 2026-11-05 13:59:44 | Kuda Oya (Kirindi Oya) | 2.27 | 🟢 Normal | -0.067 |  |
| 2026-11-05 13:46:00 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.007 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 14:02:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.030 |  |
| 2026-11-05 14:01:55 | Manampitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-05 14:01:57 | Ellagawa (Kalu Ganga) | 6.50 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-05 14:01:41 | Kithulgala (Kelani Ganga) | 1.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-05 13:46:00 | Thalgahagoda (Nilwala Ganga) | 1.22 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-05 13:01:37 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:01:46 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:02:35 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:03:26 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:02:03 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:04:58 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:02:21 | Putupaula (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-05 14:00:50 | Thanthirimale (Malwathu Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:02:25 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:05:18 | Katharagama (Menik Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:02:26 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-05 14:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:07:29 | Galgamuwa (Mee Oya) | 0.62 | 🟢 Normal | -0.019 |  |
| 2026-11-05 13:03:12 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-05 13:02:54 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-11-05 14:01:30 | Thanamalwila (Kirindi Oya) | 2.03 | 🟢 Normal | -0.020 |  |
| 2026-11-05 13:04:36 | Holombuwa (Kelani Ganga) | 0.96 | 🟢 Normal | -0.021 |  |
| 2026-11-05 14:01:53 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -0.026 |  |
| 2026-11-05 13:19:40 | Magura (Kalu Ganga) | 2.09 | 🟢 Normal | -0.032 |  |
| 2026-11-05 14:01:27 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.032 |  |
| 2026-11-05 13:10:09 | Panadugama (Nilwala Ganga) | 4.48 | 🟢 Normal | -0.036 |  |
| 2026-11-05 14:00:33 | Horowpothana (Yan Oya) | 2.20 | 🟢 Normal | -0.036 |  |
| 2026-11-05 14:02:39 | Moragaswewa (Deduru Oya) | 3.45 | 🟢 Normal | -0.039 |  |
| 2026-11-05 13:08:34 | Thawalama (Gin Ganga) | 2.08 | 🟢 Normal | -0.040 |  |
| 2026-11-05 13:06:18 | Pitabeddara (Nilwala Ganga) | 1.50 | 🟢 Normal | -0.047 |  |
| 2026-11-05 13:05:20 | Nagalagam Street (Kelani Ganga) | 0.66 | 🟢 Normal | -0.048 |  |
| 2026-11-05 13:05:19 | Badalgama (Maha Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-11-05 13:07:51 | Glencourse (Kelani Ganga) | 10.57 | 🟢 Normal | -0.058 |  |
| 2026-11-05 13:02:59 | Dunamale (Aththanagalu Oya) | 2.69 | 🟢 Normal | -0.059 |  |
| 2026-11-05 14:02:09 | Deraniyagala (Kelani Ganga) | 0.70 | 🟢 Normal | -0.061 |  |
| 2026-11-05 13:59:44 | Kuda Oya (Kirindi Oya) | 2.27 | 🟢 Normal | -0.067 |  |
| 2026-11-05 14:00:45 | Weraganthota (Mahaweli Ganga) | -2.76 | 🟢 Normal | -0.110 |  |
| 2026-11-05 13:02:31 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.138 |  |
| 2026-11-05 14:02:12 | Urawa (Nilwala Ganga) | 1.12 | 🟢 Normal | -0.186 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)