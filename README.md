# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_02:15:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,067 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert; 🟡 Pitabeddara — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 02:15:19 | Panadugama (Nilwala Ganga) | 6.64 | 🟠 Minor Flood | 0.026 | 🔺 Rising |
| 2026-10-16 02:14:54 | Magura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:14:53 | Magura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:14:52 | Magura (Kalu Ganga) | 3.95 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:11:26 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:09:00 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-10-16 02:08:46 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-16 02:07:23 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -72.000 |  |
| 2026-10-16 02:07:22 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -72.000 |  |
| 2026-10-16 02:06:30 | Pitabeddara (Nilwala Ganga) | 4.48 | 🟡 Alert | -0.102 |  |
| 2026-10-16 02:06:20 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-10-16 02:05:56 | Badalgama (Maha Oya) | 3.37 | 🟢 Normal | -0.010 |  |
| 2026-10-16 02:05:46 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.039 |  |
| 2026-10-16 02:04:59 | Urawa (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.142 |  |
| 2026-10-16 02:04:58 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:04:57 | Ellagawa (Kalu Ganga) | 7.62 | 🟢 Normal | -0.029 |  |
| 2026-10-16 02:04:55 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:03:55 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.019 |  |
| 2026-10-16 02:03:49 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.059 |  |
| 2026-10-16 02:03:46 | Dunamale (Aththanagalu Oya) | 3.79 | 🟡 Alert | -0.025 |  |
| 2026-10-16 02:03:39 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:03:32 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:03:12 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:03:06 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-16 02:02:38 | Moragaswewa (Deduru Oya) | 2.94 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-16 02:02:21 | Peradeniya (Mahaweli Ganga) | 3.11 | 🟢 Normal | -0.040 |  |
| 2026-10-16 02:02:16 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-10-16 02:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.83 | 🟡 Alert | -0.010 |  |
| 2026-10-16 02:01:44 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | -0.051 |  |
| 2026-10-16 02:01:23 | Moraketiya (Walawe Ganga) | 2.26 | 🟢 Normal | -1.018 |  |
| 2026-10-16 02:00:52 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:00:47 | Thawalama (Gin Ganga) | 3.78 | 🟢 Normal | -0.188 |  |
| 2026-10-16 01:50:20 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.006 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 02:15:19 | Panadugama (Nilwala Ganga) | 6.64 | 🟠 Minor Flood | 0.026 | 🔺 Rising |
| 2026-10-16 01:05:40 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 02:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.83 | 🟡 Alert | -0.010 |  |
| 2026-10-16 02:03:46 | Dunamale (Aththanagalu Oya) | 3.79 | 🟡 Alert | -0.025 |  |
| 2026-10-16 02:06:30 | Pitabeddara (Nilwala Ganga) | 4.48 | 🟡 Alert | -0.102 |  |
| 2026-10-16 02:03:06 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-10-16 01:02:33 | Rathnapura (Kalu Ganga) | 3.50 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-10-16 02:02:38 | Moragaswewa (Deduru Oya) | 2.94 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-16 02:08:46 | Baddegama (Gin Ganga) | 2.97 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-16 01:02:01 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 18:18:48 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-15 18:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:11:26 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:00:52 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:04:58 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:14:54 | Magura (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:03:39 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:04:55 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:03:32 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-16 02:03:12 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-16 00:05:02 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 01:50:20 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.006 |  |
| 2026-10-16 01:09:33 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | -0.009 |  |
| 2026-10-16 02:05:56 | Badalgama (Maha Oya) | 3.37 | 🟢 Normal | -0.010 |  |
| 2026-10-16 02:03:55 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.019 |  |
| 2026-10-16 02:06:20 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | -0.020 |  |
| 2026-10-16 02:02:16 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.021 |  |
| 2026-10-16 02:09:00 | Holombuwa (Kelani Ganga) | 1.27 | 🟢 Normal | -0.028 |  |
| 2026-10-16 02:04:57 | Ellagawa (Kalu Ganga) | 7.62 | 🟢 Normal | -0.029 |  |
| 2026-10-16 02:05:46 | Norwood (Kelani Ganga) | 1.31 | 🟢 Normal | -0.039 |  |
| 2026-10-16 02:02:21 | Peradeniya (Mahaweli Ganga) | 3.11 | 🟢 Normal | -0.040 |  |
| 2026-10-16 00:04:59 | Putupaula (Kalu Ganga) | 2.48 | 🟢 Normal | -0.044 |  |
| 2026-10-16 02:01:44 | Hanwella (Kelani Ganga) | 3.85 | 🟢 Normal | -0.051 |  |
| 2026-10-16 02:03:49 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.059 |  |
| 2026-10-16 02:04:59 | Urawa (Nilwala Ganga) | 2.22 | 🟢 Normal | -0.142 |  |
| 2026-10-16 02:00:47 | Thawalama (Gin Ganga) | 3.78 | 🟢 Normal | -0.188 |  |
| 2026-10-16 02:01:23 | Moraketiya (Walawe Ganga) | 2.26 | 🟢 Normal | -1.018 |  |
| 2026-10-16 02:07:23 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)