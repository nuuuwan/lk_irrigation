# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--24_22:02:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **324,786 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 22:02:59 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-11-24 22:02:52 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-24 22:02:51 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-11-24 22:02:46 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-11-24 22:02:41 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 22:02:32 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 22:02:29 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-11-24 22:02:10 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.404 | 🔺 Rising |
| 2026-11-24 22:01:36 | Holombuwa (Kelani Ganga) | 2.02 | 🟢 Normal | -0.368 |  |
| 2026-11-24 22:01:32 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-24 22:01:18 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-11-24 22:00:39 | Moraketiya (Walawe Ganga) | 3.50 | 🟡 Alert | 0.104 | 🔺 Rising |
| 2026-11-24 21:59:59 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-24 21:03:13 | Dunamale (Aththanagalu Oya) | 3.46 | 🟡 Alert | 0.302 | 🔺 Rising |
| 2026-11-24 22:00:39 | Moraketiya (Walawe Ganga) | 3.50 | 🟡 Alert | 0.104 | 🔺 Rising |
| 2026-11-24 22:02:10 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | 0.404 | 🔺 Rising |
| 2026-11-24 21:04:18 | Glencourse (Kelani Ganga) | 12.50 | 🟢 Normal | 0.372 | 🔺 Rising |
| 2026-11-24 21:07:54 | Hanwella (Kelani Ganga) | 2.76 | 🟢 Normal | 0.368 | 🔺 Rising |
| 2026-11-24 22:02:59 | Siyambalanduwa (Heda Oya) | 1.18 | 🟢 Normal | 0.300 | 🔺 Rising |
| 2026-11-24 21:00:34 | Magura (Kalu Ganga) | 3.10 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-11-24 22:02:46 | Pitabeddara (Nilwala Ganga) | 1.68 | 🟢 Normal | 0.201 | 🔺 Rising |
| 2026-11-24 21:04:13 | Baddegama (Gin Ganga) | 1.96 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-11-24 21:10:16 | Urawa (Nilwala Ganga) | 1.85 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-11-24 21:08:12 | Ellagawa (Kalu Ganga) | 5.70 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-11-24 22:01:18 | Kuda Oya (Kirindi Oya) | 1.88 | 🟢 Normal | 0.169 | 🔺 Rising |
| 2026-11-24 21:06:14 | Deraniyagala (Kelani Ganga) | 0.76 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-11-24 21:02:30 | Nakkala (Kumbukkan Oya) | 1.02 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-24 22:02:52 | Wellawaya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-11-24 21:10:34 | Thawalama (Gin Ganga) | 2.85 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-24 21:09:32 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-11-24 21:07:00 | Moragaswewa (Deduru Oya) | 1.22 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-24 22:01:32 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-11-24 21:01:08 | Horowpothana (Yan Oya) | 2.37 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-11-24 22:02:41 | Manampitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-24 21:04:27 | Giriulla (Maha Oya) | 2.65 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-11-24 21:10:48 | Norwood (Kelani Ganga) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-24 22:02:51 | Kithulgala (Kelani Ganga) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-11-24 22:02:32 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:02:13 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-11-24 22:02:29 | Panadugama (Nilwala Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-11-24 21:59:59 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-11-24 21:20:56 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-11-24 21:08:30 | Badalgama (Maha Oya) | 3.57 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:01:28 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-24 21:08:48 | Thalgahagoda (Nilwala Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-11-24 21:00:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | 0.000 |  |
| 2026-11-24 18:04:37 | Weraganthota (Mahaweli Ganga) | -2.50 | 🟢 Normal | -0.019 |  |
| 2026-11-24 21:04:31 | Peradeniya (Mahaweli Ganga) | 4.04 | 🟢 Normal | -0.020 |  |
| 2026-11-22 17:02:02⌛ | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.022 |  |
| 2026-11-24 19:07:58 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | -0.073 |  |
| 2026-11-24 21:04:58 | Nawalapitiya (Mahaweli Ganga) | 1.93 | 🟢 Normal | -0.220 |  |
| 2026-11-24 22:01:36 | Holombuwa (Kelani Ganga) | 2.02 | 🟢 Normal | -0.368 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)