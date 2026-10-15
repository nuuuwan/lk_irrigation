# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_16:17:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,706 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Urawa — Alert; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 16:17:01 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 16:16:48 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-15 16:16:40 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.106 |  |
| 2026-10-15 16:16:10 | Magura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.017 |  |
| 2026-10-15 16:09:55 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.111 |  |
| 2026-10-15 16:08:36 | Dunamale (Aththanagalu Oya) | 3.79 | 🟡 Alert | 0.000 |  |
| 2026-10-15 16:07:48 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.058 |  |
| 2026-10-15 16:07:19 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 16:07:04 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-15 16:06:41 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 16:06:20 | Glencourse (Kelani Ganga) | 11.83 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-15 16:06:19 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 16:06:16 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-10-15 16:06:01 | Panadugama (Nilwala Ganga) | 5.71 | 🟡 Alert | 0.177 | 🔺 Rising |
| 2026-10-15 16:05:39 | Moragaswewa (Deduru Oya) | 2.15 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-15 16:05:23 | Galgamuwa (Mee Oya) | 0.55 | 🟢 Normal | -0.106 |  |
| 2026-10-15 16:05:20 | Hanwella (Kelani Ganga) | 4.25 | 🟢 Normal | -0.039 |  |
| 2026-10-15 16:05:07 | Ellagawa (Kalu Ganga) | 8.04 | 🟢 Normal | -0.020 |  |
| 2026-10-15 16:04:53 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 16:04:25 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 16:04:22 | Thawalama (Gin Ganga) | 3.46 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-10-15 16:03:45 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-15 16:03:45 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 16:03:42 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-15 16:03:08 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-15 16:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.030 |  |
| 2026-10-15 16:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | -0.010 |  |
| 2026-10-15 16:02:42 | Urawa (Nilwala Ganga) | 3.32 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-10-15 16:02:31 | Pitabeddara (Nilwala Ganga) | 3.94 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-10-15 16:02:31 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-15 16:02:25 | Baddegama (Gin Ganga) | 2.50 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-15 16:02:15 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.077 |  |
| 2026-10-15 16:02:13 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 16:01:52 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.041 |  |
| 2026-10-15 16:01:32 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-15 16:01:06 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 16:00:50 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-15 16:00:38 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 16:17:01 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 16:06:01 | Panadugama (Nilwala Ganga) | 5.71 | 🟡 Alert | 0.177 | 🔺 Rising |
| 2026-10-15 16:02:42 | Urawa (Nilwala Ganga) | 3.32 | 🟡 Alert | 0.059 | 🔺 Rising |
| 2026-10-15 16:08:36 | Dunamale (Aththanagalu Oya) | 3.79 | 🟡 Alert | 0.000 |  |
| 2026-10-15 16:02:43 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.91 | 🟡 Alert | -0.010 |  |
| 2026-10-15 16:04:22 | Thawalama (Gin Ganga) | 3.46 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-10-15 16:02:31 | Pitabeddara (Nilwala Ganga) | 3.94 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-10-15 16:06:16 | Moraketiya (Walawe Ganga) | 1.65 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-10-15 16:05:39 | Moragaswewa (Deduru Oya) | 2.15 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-10-15 16:03:08 | Norwood (Kelani Ganga) | 1.37 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-15 16:02:31 | Thanthirimale (Malwathu Oya) | 1.36 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-15 16:06:20 | Glencourse (Kelani Ganga) | 11.83 | 🟢 Normal | 0.077 | 🔺 Rising |
| 2026-10-15 16:02:25 | Baddegama (Gin Ganga) | 2.50 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-10-15 16:07:04 | Manampitiya (Mahaweli Ganga) | 0.32 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-15 16:03:45 | Peradeniya (Mahaweli Ganga) | 3.23 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 16:06:41 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-15 16:04:25 | Putupaula (Kalu Ganga) | 2.40 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 16:00:38 | Horowpothana (Yan Oya) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 15:03:41 | Holombuwa (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 16:01:06 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 16:02:13 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 16:04:53 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 16:03:42 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-15 16:16:48 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-15 16:07:19 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-10-15 16:06:19 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 16:03:45 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:03:03 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-15 16:00:50 | Wellawaya (Kirindi Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-15 16:16:10 | Magura (Kalu Ganga) | 3.28 | 🟢 Normal | -0.017 |  |
| 2026-10-15 16:01:32 | Thanamalwila (Kirindi Oya) | 0.98 | 🟢 Normal | -0.020 |  |
| 2026-10-15 16:05:07 | Ellagawa (Kalu Ganga) | 8.04 | 🟢 Normal | -0.020 |  |
| 2026-10-15 16:02:57 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.030 |  |
| 2026-10-15 16:05:20 | Hanwella (Kelani Ganga) | 4.25 | 🟢 Normal | -0.039 |  |
| 2026-10-15 16:01:52 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.041 |  |
| 2026-10-15 16:07:48 | Badalgama (Maha Oya) | 3.51 | 🟢 Normal | -0.058 |  |
| 2026-10-15 16:02:15 | Rathnapura (Kalu Ganga) | 3.11 | 🟢 Normal | -0.077 |  |
| 2026-10-15 16:16:40 | Galgamuwa (Mee Oya) | 0.53 | 🟢 Normal | -0.106 |  |
| 2026-10-15 16:09:55 | Kithulgala (Kelani Ganga) | 1.81 | 🟢 Normal | -0.111 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)