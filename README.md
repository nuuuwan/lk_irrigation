# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_15:36:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,668 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Urawa — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 15:36:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:12:50 | Moragaswewa (Deduru Oya) | 2.05 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-10-15 15:12:00 | Urawa (Nilwala Ganga) | 3.27 | 🟡 Alert | 0.168 | 🔺 Rising |
| 2026-10-15 15:08:43 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-10-15 15:08:17 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | 23.625 | 🔺 Rising |
| 2026-10-15 15:08:02 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.076 |  |
| 2026-10-15 15:07:45 | Panadugama (Nilwala Ganga) | 5.33 | 🟡 Alert | 23.625 | 🔺 Rising |
| 2026-10-15 15:06:32 | Ellagawa (Kalu Ganga) | 8.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:06:01 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:05:57 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | -0.029 |  |
| 2026-10-15 15:05:29 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | -0.051 |  |
| 2026-10-15 15:05:23 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-15 15:05:01 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:04:53 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-10-15 15:04:25 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 15:04:24 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-15 15:04:20 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | -0.091 |  |
| 2026-10-15 15:04:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:04:06 | Putupaula (Kalu Ganga) | 2.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 15:04:01 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.072 |  |
| 2026-10-15 15:03:56 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 15:03:42 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:03:41 | Holombuwa (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 15:03:31 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-15 15:03:17 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:03:09 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-15 15:02:46 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 15:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.000 |  |
| 2026-10-15 15:02:42 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.050 |  |
| 2026-10-15 15:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 15:02:26 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-15 15:02:02 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-10-15 15:02:01 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 15:01:40 | Dunamale (Aththanagalu Oya) | 3.79 | 🟡 Alert | -0.043 |  |
| 2026-10-15 15:01:39 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:01:31 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-15 15:01:30 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 15:00:42 | Pitabeddara (Nilwala Ganga) | 3.70 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-10-15 15:00:37 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.052 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 15:08:43 | Thalgahagoda (Nilwala Ganga) | 1.81 | 🟠 Minor Flood | 0.009 | 🔺 Rising |
| 2026-10-15 15:08:17 | Panadugama (Nilwala Ganga) | 5.54 | 🟡 Alert | 23.625 | 🔺 Rising |
| 2026-10-15 15:12:00 | Urawa (Nilwala Ganga) | 3.27 | 🟡 Alert | 0.168 | 🔺 Rising |
| 2026-10-15 15:02:45 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.92 | 🟡 Alert | 0.000 |  |
| 2026-10-15 15:01:40 | Dunamale (Aththanagalu Oya) | 3.79 | 🟡 Alert | -0.043 |  |
| 2026-10-15 15:00:42 | Pitabeddara (Nilwala Ganga) | 3.70 | 🟢 Normal | 0.379 | 🔺 Rising |
| 2026-10-15 15:04:53 | Thawalama (Gin Ganga) | 3.22 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-10-15 15:03:09 | Moraketiya (Walawe Ganga) | 1.50 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-15 15:01:31 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-15 15:12:50 | Moragaswewa (Deduru Oya) | 2.05 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-10-15 15:04:24 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-15 15:03:31 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-15 15:00:37 | Thanthirimale (Malwathu Oya) | 1.28 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-15 15:05:23 | Baddegama (Gin Ganga) | 2.43 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-15 15:03:56 | Glencourse (Kelani Ganga) | 11.75 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 15:04:06 | Putupaula (Kalu Ganga) | 2.38 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 15:02:30 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 15:04:25 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 15:02:46 | Horowpothana (Yan Oya) | 1.83 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 15:01:30 | Galgamuwa (Mee Oya) | 0.54 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 15:02:01 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 15:03:41 | Holombuwa (Kelani Ganga) | 1.43 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 15:05:01 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:01:39 | Wellawaya (Kirindi Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:03:42 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:36:39 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:06:32 | Ellagawa (Kalu Ganga) | 8.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:04:10 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:03:17 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:06:01 | Katharagama (Menik Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-15 14:03:03 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-15 15:02:26 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-10-15 15:02:02 | Manampitiya (Mahaweli Ganga) | 0.28 | 🟢 Normal | -0.020 |  |
| 2026-10-15 15:05:57 | Giriulla (Maha Oya) | 2.25 | 🟢 Normal | -0.029 |  |
| 2026-10-15 15:02:42 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | -0.050 |  |
| 2026-10-15 15:05:29 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | -0.051 |  |
| 2026-10-15 15:04:01 | Magura (Kalu Ganga) | 3.30 | 🟢 Normal | -0.072 |  |
| 2026-10-15 15:08:02 | Rathnapura (Kalu Ganga) | 3.18 | 🟢 Normal | -0.076 |  |
| 2026-10-15 15:04:20 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)