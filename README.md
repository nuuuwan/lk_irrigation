# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--25_21:05:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,865 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 21:05:02 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.077 |  |
| 2026-10-25 21:04:43 | Nawalapitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 21:04:36 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:04:19 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:04:15 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-25 21:04:04 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 21:03:40 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-25 21:03:32 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-10-25 21:03:15 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 21:03:10 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 21:02:52 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-25 21:02:31 | Rathnapura (Kalu Ganga) | 5.04 | 🟢 Normal | 0.555 | 🔺 Rising |
| 2026-10-25 21:01:45 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-25 21:01:38 | Thawalama (Gin Ganga) | 3.19 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:00:50 | Moragaswewa (Deduru Oya) | 1.31 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-25 21:00:27 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:00:15 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-25 21:02:31 | Rathnapura (Kalu Ganga) | 5.04 | 🟢 Normal | 0.555 | 🔺 Rising |
| 2026-10-25 20:08:39 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | 0.296 | 🔺 Rising |
| 2026-10-25 20:06:00 | Glencourse (Kelani Ganga) | 11.48 | 🟢 Normal | 0.252 | 🔺 Rising |
| 2026-10-25 20:06:39 | Holombuwa (Kelani Ganga) | 2.42 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-10-25 20:04:10 | Magura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.151 | 🔺 Rising |
| 2026-10-25 21:03:32 | Dunamale (Aththanagalu Oya) | 2.70 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-10-25 20:06:32 | Giriulla (Maha Oya) | 1.96 | 🟢 Normal | 0.144 | 🔺 Rising |
| 2026-10-25 18:03:46 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-25 20:02:49 | Peradeniya (Mahaweli Ganga) | 3.45 | 🟢 Normal | 0.112 | 🔺 Rising |
| 2026-10-25 21:03:40 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-25 21:04:15 | Thalgahagoda (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-10-25 20:03:10 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-25 21:02:52 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-25 21:00:50 | Moragaswewa (Deduru Oya) | 1.31 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-10-25 20:05:32 | Hanwella (Kelani Ganga) | 2.92 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-25 20:05:48 | Badalgama (Maha Oya) | 2.95 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-25 20:09:29 | Baddegama (Gin Ganga) | 2.20 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-25 21:04:43 | Nawalapitiya (Mahaweli Ganga) | 2.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 21:03:15 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-25 20:13:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.49 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-25 20:06:55 | Urawa (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-25 21:03:10 | Panadugama (Nilwala Ganga) | 4.58 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-25 21:04:04 | Moraketiya (Walawe Ganga) | 1.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-25 20:17:12 | Padiyathalawa (Maduru Oya) | 0.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-25 20:04:51 | Norwood (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-25 20:06:15 | Putupaula (Kalu Ganga) | 1.54 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-25 21:00:27 | Wellawaya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-25 20:03:19 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-10-25 20:05:10 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:04:19 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:04:36 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:01:38 | Thawalama (Gin Ganga) | 3.19 | 🟢 Normal | 0.000 |  |
| 2026-10-25 20:02:34 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-25 20:02:56 | Thanamalwila (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-25 21:01:45 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-10-25 21:00:15 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.032 |  |
| 2026-10-25 18:03:32 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.069 |  |
| 2026-10-25 21:05:02 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)