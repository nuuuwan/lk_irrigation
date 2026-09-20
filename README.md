# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_12:20:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,027 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Nawalapitiya — Minor Flood; 🟡 Peradeniya — Alert; 🟡 Deraniyagala — Alert; 🟡 Panadugama — Alert; 🟡 Rathnapura — Alert; 🟡 Thawalama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 12:20:29 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:15:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.39 | 🟡 Alert | 0.106 | 🔺 Rising |
| 2026-09-20 12:12:18 | Ellagawa (Kalu Ganga) | 7.36 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-09-20 12:09:48 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:09:06 | Magura (Kalu Ganga) | 5.03 | 🟡 Alert | 0.121 | 🔺 Rising |
| 2026-09-20 12:08:50 | Thawalama (Gin Ganga) | 4.84 | 🟡 Alert | 0.182 | 🔺 Rising |
| 2026-09-20 12:07:33 | Holombuwa (Kelani Ganga) | 2.83 | 🟢 Normal | 0.660 | 🔺 Rising |
| 2026-09-20 12:07:06 | Rathnapura (Kalu Ganga) | 6.60 | 🟡 Alert | 0.312 | 🔺 Rising |
| 2026-09-20 12:06:21 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:05:57 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-20 12:05:54 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-20 12:05:16 | Glencourse (Kelani Ganga) | 14.30 | 🟢 Normal | 0.649 | 🔺 Rising |
| 2026-09-20 12:05:13 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-20 12:05:09 | Urawa (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-09-20 12:05:02 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.015 |  |
| 2026-09-20 12:04:40 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 12:03:43 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | 0.701 | 🔺 Rising |
| 2026-09-20 12:03:32 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-09-20 12:03:24 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-20 12:03:13 | Panadugama (Nilwala Ganga) | 5.09 | 🟡 Alert | 0.397 | 🔺 Rising |
| 2026-09-20 12:03:11 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:03:09 | Deraniyagala (Kelani Ganga) | 4.83 | 🟡 Alert | 0.550 | 🔺 Rising |
| 2026-09-20 12:02:51 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:02:44 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:02:44 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 12:02:44 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-20 12:02:31 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 12:02:28 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:02:17 | Norwood (Kelani Ganga) | 2.33 | 🟡 Alert | -0.351 |  |
| 2026-09-20 12:02:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:01:58 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:01:32 | Nawalapitiya (Mahaweli Ganga) | 5.36 | 🟠 Minor Flood | -0.346 |  |
| 2026-09-20 12:01:24 | Peradeniya (Mahaweli Ganga) | 6.02 | 🟡 Alert | 1.069 | 🔺 Rising |
| 2026-09-20 12:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:01:09 | Kithulgala (Kelani Ganga) | 3.20 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-09-20 12:01:07 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-09-20 12:01:02 | Pitabeddara (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-20 12:00:37 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-20 12:00:12 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-20 11:52:44 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 12:01:32 | Nawalapitiya (Mahaweli Ganga) | 5.36 | 🟠 Minor Flood | -0.346 |  |
| 2026-09-20 12:01:24 | Peradeniya (Mahaweli Ganga) | 6.02 | 🟡 Alert | 1.069 | 🔺 Rising |
| 2026-09-20 12:03:09 | Deraniyagala (Kelani Ganga) | 4.83 | 🟡 Alert | 0.550 | 🔺 Rising |
| 2026-09-20 12:03:13 | Panadugama (Nilwala Ganga) | 5.09 | 🟡 Alert | 0.397 | 🔺 Rising |
| 2026-09-20 12:07:06 | Rathnapura (Kalu Ganga) | 6.60 | 🟡 Alert | 0.312 | 🔺 Rising |
| 2026-09-20 12:08:50 | Thawalama (Gin Ganga) | 4.84 | 🟡 Alert | 0.182 | 🔺 Rising |
| 2026-09-20 12:09:06 | Magura (Kalu Ganga) | 5.03 | 🟡 Alert | 0.121 | 🔺 Rising |
| 2026-09-20 12:15:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.39 | 🟡 Alert | 0.106 | 🔺 Rising |
| 2026-09-20 12:01:09 | Kithulgala (Kelani Ganga) | 3.20 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-09-20 12:02:17 | Norwood (Kelani Ganga) | 2.33 | 🟡 Alert | -0.351 |  |
| 2026-09-20 12:03:43 | Hanwella (Kelani Ganga) | 3.50 | 🟢 Normal | 0.701 | 🔺 Rising |
| 2026-09-20 12:07:33 | Holombuwa (Kelani Ganga) | 2.83 | 🟢 Normal | 0.660 | 🔺 Rising |
| 2026-09-20 12:05:16 | Glencourse (Kelani Ganga) | 14.30 | 🟢 Normal | 0.649 | 🔺 Rising |
| 2026-09-20 12:12:18 | Ellagawa (Kalu Ganga) | 7.36 | 🟢 Normal | 0.278 | 🔺 Rising |
| 2026-09-20 12:01:02 | Pitabeddara (Nilwala Ganga) | 2.77 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-09-20 12:05:09 | Urawa (Nilwala Ganga) | 1.47 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-09-20 12:02:44 | Dunamale (Aththanagalu Oya) | 2.28 | 🟢 Normal | 0.132 | 🔺 Rising |
| 2026-09-20 12:01:07 | Thalgahagoda (Nilwala Ganga) | 0.66 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-09-20 12:03:32 | Putupaula (Kalu Ganga) | 1.47 | 🟢 Normal | 0.118 | 🔺 Rising |
| 2026-09-20 12:05:13 | Baddegama (Gin Ganga) | 3.06 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-09-20 12:03:24 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-09-20 12:05:57 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-09-20 12:02:31 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 12:02:44 | Badalgama (Maha Oya) | 1.93 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 12:04:40 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 12:05:54 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-20 12:01:58 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:20:29 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:06:21 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:00:12 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:09:48 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:03:11 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:02:16 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:02:44 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:02:51 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:02:28 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:00:37 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | -0.010 |  |
| 2026-09-20 12:05:02 | Nagalagam Street (Kelani Ganga) | 0.44 | 🟢 Normal | -0.015 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)