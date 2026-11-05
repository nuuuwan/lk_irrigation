# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--05_13:03:26-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **307,513 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 13:03:26 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:03:15 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:03:15 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:03:12 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-05 13:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:02:59 | Dunamale (Aththanagalu Oya) | 2.69 | 🟢 Normal | -0.059 |  |
| 2026-11-05 13:02:54 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-11-05 13:02:43 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.040 |  |
| 2026-11-05 13:02:31 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.138 |  |
| 2026-11-05 13:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.010 |  |
| 2026-11-05 13:02:27 | Ellagawa (Kalu Ganga) | 6.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-05 13:02:26 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:02:25 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:02:21 | Putupaula (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:02:20 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.021 |  |
| 2026-11-05 13:01:48 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:01:47 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:01:37 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:01:30 | Moragaswewa (Deduru Oya) | 3.49 | 🟢 Normal | -0.030 |  |
| 2026-11-05 13:00:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.100 |  |
| 2026-11-05 13:00:48 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-05 12:39:04 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.087 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-05 13:02:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.15 | 🟡 Alert | -0.010 |  |
| 2026-11-05 12:04:23 | Kuda Oya (Kirindi Oya) | 2.47 | 🟢 Normal | 1.573 | 🔺 Rising |
| 2026-11-05 13:02:27 | Ellagawa (Kalu Ganga) | 6.46 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-05 13:00:48 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-05 12:07:53 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-05 12:14:20 | Thalgahagoda (Nilwala Ganga) | 1.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-05 12:04:08 | Baddegama (Gin Ganga) | 2.12 | 🟢 Normal | 0.006 | 🔺 Rising |
| 2026-11-05 13:01:48 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:01:37 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:03:15 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:03:26 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:01:47 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 12:00:44 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:02:21 | Putupaula (Kalu Ganga) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-11-05 12:02:26 | Thanthirimale (Malwathu Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:02:25 | Peradeniya (Mahaweli Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-11-05 13:03:07 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:02:26 | Wellawaya (Kirindi Oya) | 1.54 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:03:15 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.010 |  |
| 2026-11-05 13:03:12 | Moraketiya (Walawe Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-11-05 13:02:54 | Hanwella (Kelani Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-11-05 12:06:07 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-11-05 12:08:28 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.021 |  |
| 2026-11-05 13:02:20 | Thanamalwila (Kirindi Oya) | 2.05 | 🟢 Normal | -0.021 |  |
| 2026-11-05 12:02:35 | Katharagama (Menik Ganga) | 0.00 | 🟢 Normal | -0.021 |  |
| 2026-11-05 12:05:15 | Galgamuwa (Mee Oya) | 0.64 | 🟢 Normal | -0.029 |  |
| 2026-11-05 13:01:30 | Moragaswewa (Deduru Oya) | 3.49 | 🟢 Normal | -0.030 |  |
| 2026-11-05 12:06:17 | Glencourse (Kelani Ganga) | 10.63 | 🟢 Normal | -0.031 |  |
| 2026-11-05 12:04:44 | Horowpothana (Yan Oya) | 2.31 | 🟢 Normal | -0.031 |  |
| 2026-11-05 12:03:55 | Magura (Kalu Ganga) | 2.13 | 🟢 Normal | -0.035 |  |
| 2026-11-05 13:02:43 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.040 |  |
| 2026-11-05 12:02:59 | Giriulla (Maha Oya) | 2.16 | 🟢 Normal | -0.052 |  |
| 2026-11-05 13:02:59 | Dunamale (Aththanagalu Oya) | 2.69 | 🟢 Normal | -0.059 |  |
| 2026-11-05 12:01:48 | Pitabeddara (Nilwala Ganga) | 1.55 | 🟢 Normal | -0.061 |  |
| 2026-11-05 12:06:08 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.068 |  |
| 2026-11-05 12:03:29 | Panadugama (Nilwala Ganga) | 4.52 | 🟢 Normal | -0.076 |  |
| 2026-11-05 12:39:04 | Urawa (Nilwala Ganga) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-11-05 13:00:49 | Weraganthota (Mahaweli Ganga) | -2.65 | 🟢 Normal | -0.100 |  |
| 2026-11-05 13:02:31 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.138 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

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

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)