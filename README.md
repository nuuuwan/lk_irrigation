# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--18_09:28:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **291,135 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 09:28:14 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-10-18 09:09:36 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.104 |  |
| 2026-10-18 09:08:53 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-10-18 09:06:54 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.149 |  |
| 2026-10-18 09:05:52 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-10-18 09:05:50 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.022 |  |
| 2026-10-18 09:05:42 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-18 09:05:33 | Panadugama (Nilwala Ganga) | 6.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 09:05:30 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.097 |  |
| 2026-10-18 09:04:52 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.137 |  |
| 2026-10-18 09:04:35 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 09:04:31 | Horowpothana (Yan Oya) | 3.08 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-18 09:04:24 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-18 09:04:17 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 09:03:39 | Putupaula (Kalu Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-10-18 09:03:16 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.158 |  |
| 2026-10-18 09:03:16 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.069 |  |
| 2026-10-18 09:03:11 | Thalgahagoda (Nilwala Ganga) | 2.03 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-18 09:03:10 | Hanwella (Kelani Ganga) | 4.16 | 🟢 Normal | -0.122 |  |
| 2026-10-18 09:03:09 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-18 09:03:02 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | -0.076 |  |
| 2026-10-18 09:02:59 | Dunamale (Aththanagalu Oya) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-10-18 09:02:40 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-18 09:02:39 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-10-18 09:02:34 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-10-18 09:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.22 | 🟡 Alert | -0.031 |  |
| 2026-10-18 09:02:13 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-18 09:02:07 | Rathnapura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.115 |  |
| 2026-10-18 09:02:04 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 09:01:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-18 09:01:46 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.060 |  |
| 2026-10-18 09:01:44 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-18 09:01:30 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | -0.053 |  |
| 2026-10-18 09:01:17 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-18 09:01:08 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-18 09:01:04 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.171 |  |
| 2026-10-18 09:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-10-18 09:00:08 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-18 09:05:33 | Panadugama (Nilwala Ganga) | 6.00 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-18 09:03:11 | Thalgahagoda (Nilwala Ganga) | 2.03 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-18 09:02:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.22 | 🟡 Alert | -0.031 |  |
| 2026-10-18 09:04:31 | Horowpothana (Yan Oya) | 3.08 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-18 09:01:44 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-18 09:05:42 | Galgamuwa (Mee Oya) | 0.69 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-18 09:04:35 | Ellagawa (Kalu Ganga) | 7.72 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-18 09:04:24 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-10-18 09:02:04 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-10-18 09:01:17 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-18 09:05:52 | Baddegama (Gin Ganga) | 3.18 | 🟢 Normal | 0.000 |  |
| 2026-10-18 09:00:08 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-10-18 09:04:17 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-18 09:28:14 | Thanthirimale (Malwathu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-10-18 09:01:08 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-18 09:03:39 | Putupaula (Kalu Ganga) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-10-18 09:02:13 | Thanamalwila (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-18 09:02:40 | Moragaswewa (Deduru Oya) | 1.11 | 🟢 Normal | -0.010 |  |
| 2026-10-18 09:01:54 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-10-18 09:00:38 | Nawalapitiya (Mahaweli Ganga) | 1.37 | 🟢 Normal | -0.011 |  |
| 2026-10-18 09:02:34 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.011 |  |
| 2026-10-18 09:02:59 | Dunamale (Aththanagalu Oya) | 2.41 | 🟢 Normal | -0.020 |  |
| 2026-10-18 09:03:09 | Norwood (Kelani Ganga) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-18 09:05:50 | Magura (Kalu Ganga) | 2.31 | 🟢 Normal | -0.022 |  |
| 2026-10-18 09:08:53 | Holombuwa (Kelani Ganga) | 1.25 | 🟢 Normal | -0.028 |  |
| 2026-10-18 09:02:39 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.029 |  |
| 2026-10-18 09:01:30 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | -0.053 |  |
| 2026-10-18 09:01:46 | Nagalagam Street (Kelani Ganga) | 0.73 | 🟢 Normal | -0.060 |  |
| 2026-10-18 09:03:16 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.069 |  |
| 2026-10-18 09:03:02 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | -0.076 |  |
| 2026-10-18 09:05:30 | Padiyathalawa (Maduru Oya) | 0.50 | 🟢 Normal | -0.097 |  |
| 2026-10-18 09:09:36 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.104 |  |
| 2026-10-18 09:02:07 | Rathnapura (Kalu Ganga) | 3.87 | 🟢 Normal | -0.115 |  |
| 2026-10-18 09:03:10 | Hanwella (Kelani Ganga) | 4.16 | 🟢 Normal | -0.122 |  |
| 2026-10-18 09:04:52 | Urawa (Nilwala Ganga) | 1.26 | 🟢 Normal | -0.137 |  |
| 2026-10-18 08:00:54 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.147 |  |
| 2026-10-18 09:06:54 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | -0.149 |  |
| 2026-10-18 09:03:16 | Giriulla (Maha Oya) | 2.08 | 🟢 Normal | -0.158 |  |
| 2026-10-18 09:01:04 | Pitabeddara (Nilwala Ganga) | 2.20 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)