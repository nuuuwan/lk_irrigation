# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_08:20:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,097 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 08:20:42 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.034 |  |
| 2026-10-18 08:14:32 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | -0.202 |  |
| 2026-10-18 08:12:20 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.106 |  |
| 2026-10-18 08:10:41 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.031 |  |
| 2026-10-18 08:08:22 | Pitabeddara (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:07:59 | Horowpothana (Yan Oya) | 3.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 08:07:49 | Badalgama (Maha Oya) | 3.64 | 🟢 Normal | -0.067 |  |
| 2026-10-18 08:07:48 | Pitabeddara (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:07:11 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-10-18 08:06:26 | Panadugama (Nilwala Ganga) | 6.00 | 🟠 Minor Flood | -0.041 |  |
| 2026-10-18 08:05:55 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | -0.159 |  |
| 2026-10-18 08:05:19 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:04:57 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.051 |  |
| 2026-10-18 08:04:39 | Rathnapura (Kalu Ganga) | 3.98 | 🟢 Normal | -0.170 |  |
| 2026-10-18 08:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | -0.029 |  |
| 2026-10-18 08:04:05 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.127 |  |
| 2026-10-18 08:04:02 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-18 08:03:57 | Hanwella (Kelani Ganga) | 4.28 | 🟢 Normal | -0.101 |  |
| 2026-10-18 08:03:51 | Putupaula (Kalu Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-10-18 08:03:49 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.271 |  |
| 2026-10-18 08:03:49 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-10-18 08:03:43 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-18 08:03:19 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-10-18 08:03:16 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-18 08:03:14 | Ellagawa (Kalu Ganga) | 7.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 08:02:58 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-10-18 08:02:43 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:02:43 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-18 08:02:39 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.062 |  |
| 2026-10-18 08:02:30 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-18 08:02:06 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:02:02 | Thalgahagoda (Nilwala Ganga) | 2.04 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 08:01:34 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:01:30 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:01:13 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.012 |  |
| 2026-10-18 08:00:55 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.032 |  |
| 2026-10-18 08:00:54 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.147 |  |
| 2026-10-18 08:00:27 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:00:20 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 08:02:02 | Thalgahagoda (Nilwala Ganga) | 2.04 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 08:06:26 | Panadugama (Nilwala Ganga) | 6.00 | 🟠 Minor Flood | -0.041 |  |
| 2026-10-18 08:04:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.25 | 🟡 Alert | -0.029 |  |
| 2026-10-18 08:02:43 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-18 08:07:59 | Horowpothana (Yan Oya) | 3.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-18 08:03:14 | Ellagawa (Kalu Ganga) | 7.71 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 08:01:34 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:01:30 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:02:43 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:08:22 | Pitabeddara (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:05:19 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:00:27 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:02:06 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:04:02 | Manampitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:00:20 | Kuda Oya (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 08:03:58 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-18 08:03:16 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-10-18 08:02:30 | Thanamalwila (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-18 08:03:49 | Dunamale (Aththanagalu Oya) | 2.43 | 🟢 Normal | -0.010 |  |
| 2026-10-18 08:03:43 | Holombuwa (Kelani Ganga) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-18 08:03:51 | Putupaula (Kalu Ganga) | 1.97 | 🟢 Normal | -0.010 |  |
| 2026-10-18 08:01:13 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | -0.012 |  |
| 2026-10-18 08:07:11 | Moraketiya (Walawe Ganga) | 1.28 | 🟢 Normal | -0.019 |  |
| 2026-10-18 08:03:19 | Galgamuwa (Mee Oya) | 0.66 | 🟢 Normal | -0.022 |  |
| 2026-10-18 08:02:58 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.030 |  |
| 2026-10-18 08:10:41 | Magura (Kalu Ganga) | 2.33 | 🟢 Normal | -0.031 |  |
| 2026-10-18 08:00:55 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | -0.032 |  |
| 2026-10-18 08:20:42 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.034 |  |
| 2026-10-18 08:04:57 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.051 |  |
| 2026-10-18 08:02:39 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.062 |  |
| 2026-10-18 08:07:49 | Badalgama (Maha Oya) | 3.64 | 🟢 Normal | -0.067 |  |
| 2026-10-18 08:03:57 | Hanwella (Kelani Ganga) | 4.28 | 🟢 Normal | -0.101 |  |
| 2026-10-18 08:12:20 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.106 |  |
| 2026-10-18 08:04:05 | Norwood (Kelani Ganga) | 1.20 | 🟢 Normal | -0.127 |  |
| 2026-10-18 08:00:54 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.147 |  |
| 2026-10-18 08:05:55 | Glencourse (Kelani Ganga) | 11.80 | 🟢 Normal | -0.159 |  |
| 2026-10-18 08:04:39 | Rathnapura (Kalu Ganga) | 3.98 | 🟢 Normal | -0.170 |  |
| 2026-10-18 08:14:32 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | -0.202 |  |
| 2026-10-18 08:03:49 | Padiyathalawa (Maduru Oya) | 0.60 | 🟢 Normal | -0.271 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)