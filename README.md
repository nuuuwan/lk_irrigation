# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_05:03:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **309,898 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Magura — Alert; 🟡 Panadugama — Alert; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 05:03:08 | Wellawaya (Kirindi Oya) | 2.32 | 🟢 Normal | -0.544 |  |
| 2026-11-08 05:02:46 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:02:21 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.021 |  |
| 2026-11-08 05:02:13 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-08 05:01:39 | Giriulla (Maha Oya) | 3.40 | 🟢 Normal | -0.091 |  |
| 2026-11-08 05:01:19 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -1.865 |  |
| 2026-11-08 05:01:09 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:00:53 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2026-11-08 05:00:03 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | 2.466 | 🔺 Rising |
| 2026-11-08 04:58:06 | Nakkala (Kumbukkan Oya) | 1.54 | 🟢 Normal | -1.865 |  |
| 2026-11-08 04:57:01 | Thawalama (Gin Ganga) | 3.35 | 🟢 Normal | -0.043 |  |
| 2026-11-08 04:54:06 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-11-08 04:54:05 | Pitabeddara (Nilwala Ganga) | 2.47 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-11-08 04:52:45 | Magura (Kalu Ganga) | 3.90 | 🟢 Normal | 2.466 | 🔺 Rising |
| 2026-11-08 04:44:59 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-08 04:28:03 | Thanamalwila (Kirindi Oya) | 3.40 | 🟢 Normal | 0.611 | 🔺 Rising |
| 2026-11-08 04:24:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.029 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 05:00:03 | Magura (Kalu Ganga) | 4.20 | 🟡 Alert | 2.466 | 🔺 Rising |
| 2026-11-08 04:01:46 | Panadugama (Nilwala Ganga) | 5.89 | 🟡 Alert | 0.457 | 🔺 Rising |
| 2026-11-08 04:11:08 | Moraketiya (Walawe Ganga) | 4.66 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-11-08 03:34:25 | Dunamale (Aththanagalu Oya) | 3.79 | 🟡 Alert | 0.000 |  |
| 2026-11-08 04:08:31 | Urawa (Nilwala Ganga) | 3.02 | 🟡 Alert | -0.252 |  |
| 2026-11-08 04:54:06 | Pitabeddara (Nilwala Ganga) | 2.58 | 🟢 Normal | 396.000 | 🔺 Rising |
| 2026-11-08 04:28:03 | Thanamalwila (Kirindi Oya) | 3.40 | 🟢 Normal | 0.611 | 🔺 Rising |
| 2026-11-08 04:02:46 | Kuda Oya (Kirindi Oya) | 2.98 | 🟢 Normal | 0.340 | 🔺 Rising |
| 2026-11-08 04:07:23 | Rathnapura (Kalu Ganga) | 4.91 | 🟢 Normal | 0.249 | 🔺 Rising |
| 2026-11-08 04:02:53 | Moragaswewa (Deduru Oya) | 2.03 | 🟢 Normal | 0.148 | 🔺 Rising |
| 2026-11-08 04:05:28 | Putupaula (Kalu Ganga) | 1.52 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-11-08 05:02:13 | Ellagawa (Kalu Ganga) | 7.08 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-08 04:02:59 | Baddegama (Gin Ganga) | 2.76 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-08 04:02:12 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-11-08 04:10:15 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-08 04:03:28 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-08 04:10:29 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:02:46 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-07 18:03:13 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-11-08 04:21:16 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-11-08 04:03:40 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 05:01:09 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-11-08 04:04:32 | Katharagama (Menik Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-11-08 04:12:33 | Holombuwa (Kelani Ganga) | 1.35 | 🟢 Normal | -0.009 |  |
| 2026-11-07 18:01:10 | Thanthirimale (Malwathu Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-11-08 04:01:06 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | -0.020 |  |
| 2026-11-07 18:00:15 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.021 |  |
| 2026-11-08 05:02:21 | Hanwella (Kelani Ganga) | 3.25 | 🟢 Normal | -0.021 |  |
| 2026-11-08 04:24:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.90 | 🟢 Normal | -0.029 |  |
| 2026-11-08 05:00:53 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.031 |  |
| 2026-11-08 04:03:15 | Manampitiya (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.040 |  |
| 2026-11-08 04:57:01 | Thawalama (Gin Ganga) | 3.35 | 🟢 Normal | -0.043 |  |
| 2026-11-08 03:05:05 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.058 |  |
| 2026-11-08 04:01:42 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | -0.085 |  |
| 2026-11-08 05:01:39 | Giriulla (Maha Oya) | 3.40 | 🟢 Normal | -0.091 |  |
| 2026-11-08 04:03:50 | Thaldena (Mahaweli Ganga) | 0.99 | 🟢 Normal | -0.160 |  |
| 2026-11-08 04:00:49 | Peradeniya (Mahaweli Ganga) | 3.42 | 🟢 Normal | -0.260 |  |
| 2026-11-08 05:03:08 | Wellawaya (Kirindi Oya) | 2.32 | 🟢 Normal | -0.544 |  |
| 2026-11-08 05:01:19 | Nakkala (Kumbukkan Oya) | 1.44 | 🟢 Normal | -1.865 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)