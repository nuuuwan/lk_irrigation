# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--11_23:03:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,279 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Urawa — Alert; 🟡 Thawalama — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 23:03:05 | Thawalama (Gin Ganga) | 5.10 | 🟡 Alert | 0.115 | 🔺 Rising |
| 2026-11-11 23:02:58 | Thaldena (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.101 |  |
| 2026-11-11 23:02:57 | Thanamalwila (Kirindi Oya) | 2.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-11 23:02:27 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.084 | 🔺 Rising |
| 2026-11-11 23:02:24 | Kuda Oya (Kirindi Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-11 23:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | -0.011 |  |
| 2026-11-11 23:02:13 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-11-11 23:02:07 | Moraketiya (Walawe Ganga) | 4.15 | 🟡 Alert | 0.000 |  |
| 2026-11-11 23:01:54 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 23:01:46 | Ellagawa (Kalu Ganga) | 8.38 | 🟢 Normal | -0.010 |  |
| 2026-11-11 23:01:28 | Moragaswewa (Deduru Oya) | 3.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 23:01:07 | Wellawaya (Kirindi Oya) | 3.64 | 🟢 Normal | 1.005 | 🔺 Rising |
| 2026-11-11 22:16:22 | Magura (Kalu Ganga) | 5.05 | 🟡 Alert | 0.073 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-11 23:01:54 | Thalgahagoda (Nilwala Ganga) | 1.78 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-11 22:09:43 | Baddegama (Gin Ganga) | 4.06 | 🟠 Minor Flood | -0.018 |  |
| 2026-11-11 22:03:29 | Urawa (Nilwala Ganga) | 3.02 | 🟡 Alert | 0.270 | 🔺 Rising |
| 2026-11-11 23:03:05 | Thawalama (Gin Ganga) | 5.10 | 🟡 Alert | 0.115 | 🔺 Rising |
| 2026-11-11 23:02:27 | Dunamale (Aththanagalu Oya) | 3.98 | 🟡 Alert | 0.084 | 🔺 Rising |
| 2026-11-11 22:16:22 | Magura (Kalu Ganga) | 5.05 | 🟡 Alert | 0.073 | 🔺 Rising |
| 2026-11-11 22:02:32 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-11 23:02:07 | Moraketiya (Walawe Ganga) | 4.15 | 🟡 Alert | 0.000 |  |
| 2026-11-11 23:02:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.44 | 🟡 Alert | -0.011 |  |
| 2026-11-11 22:03:59 | Nakkala (Kumbukkan Oya) | 3.65 | 🟢 Normal | 1.949 | 🔺 Rising |
| 2026-11-11 23:01:07 | Wellawaya (Kirindi Oya) | 3.64 | 🟢 Normal | 1.005 | 🔺 Rising |
| 2026-11-11 22:04:36 | Holombuwa (Kelani Ganga) | 2.88 | 🟢 Normal | 0.494 | 🔺 Rising |
| 2026-11-11 22:04:17 | Glencourse (Kelani Ganga) | 12.89 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-11-11 22:05:40 | Katharagama (Menik Ganga) | 0.97 | 🟢 Normal | 0.242 | 🔺 Rising |
| 2026-11-11 22:03:16 | Pitabeddara (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-11-11 23:02:13 | Hanwella (Kelani Ganga) | 4.58 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-11-11 22:05:25 | Nawalapitiya (Mahaweli Ganga) | 2.85 | 🟢 Normal | 0.142 | 🔺 Rising |
| 2026-11-11 22:08:10 | Kithulgala (Kelani Ganga) | 2.37 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-11-11 22:03:25 | Giriulla (Maha Oya) | 2.30 | 🟢 Normal | 0.114 | 🔺 Rising |
| 2026-11-11 22:06:53 | Norwood (Kelani Ganga) | 1.42 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-11-11 22:01:28 | Peradeniya (Mahaweli Ganga) | 4.75 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-11 23:02:57 | Thanamalwila (Kirindi Oya) | 2.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-11 22:00:05 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-11 22:12:54 | Badalgama (Maha Oya) | 3.48 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-11 22:09:02 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-11-11 23:01:28 | Moragaswewa (Deduru Oya) | 3.67 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 22:03:43 | Padiyathalawa (Maduru Oya) | 0.92 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-11 18:01:56 | Weraganthota (Mahaweli Ganga) | -2.72 | 🟢 Normal | 0.000 |  |
| 2026-11-11 18:01:41 | Galgamuwa (Mee Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-11-11 23:02:24 | Kuda Oya (Kirindi Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-11-11 18:01:30 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.010 |  |
| 2026-11-11 22:02:54 | Putupaula (Kalu Ganga) | 2.63 | 🟢 Normal | -0.010 |  |
| 2026-11-11 23:01:46 | Ellagawa (Kalu Ganga) | 8.38 | 🟢 Normal | -0.010 |  |
| 2026-11-11 22:03:39 | Rathnapura (Kalu Ganga) | 5.00 | 🟢 Normal | -0.023 |  |
| 2026-11-11 22:01:29 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.025 |  |
| 2026-11-11 22:01:27 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.063 |  |
| 2026-11-11 22:05:59 | Manampitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.066 |  |
| 2026-11-11 23:02:58 | Thaldena (Mahaweli Ganga) | 2.85 | 🟢 Normal | -0.101 |  |
| 2026-11-11 22:06:21 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | -0.362 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)