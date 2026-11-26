# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--26_20:02:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **326,457 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Holombuwa — Alert; 🟡 Magura — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Dunamale — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 20:02:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-11-26 20:02:49 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-26 20:02:44 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-26 20:02:29 | Kuda Oya (Kirindi Oya) | 2.65 | 🟢 Normal | 0.799 | 🔺 Rising |
| 2026-11-26 20:02:27 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-11-26 20:02:09 | Hanwella (Kelani Ganga) | 3.28 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-26 20:02:03 | Moragaswewa (Deduru Oya) | 4.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 20:01:22 | Padiyathalawa (Maduru Oya) | 3.95 | 🟢 Normal | 2.135 | 🔺 Rising |
| 2026-11-26 20:01:09 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.085 |  |
| 2026-11-26 20:00:57 | Siyambalanduwa (Heda Oya) | 1.90 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-11-26 20:00:20 | Wellawaya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-26 19:28:23 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-26 19:27:27 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-26 19:05:05 | Moraketiya (Walawe Ganga) | 4.10 | 🟡 Alert | 0.636 | 🔺 Rising |
| 2026-11-26 19:01:48 | Holombuwa (Kelani Ganga) | 3.00 | 🟡 Alert | 0.612 | 🔺 Rising |
| 2026-11-26 19:07:44 | Magura (Kalu Ganga) | 4.30 | 🟡 Alert | 0.169 | 🔺 Rising |
| 2026-11-26 19:15:50 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.14 | 🟡 Alert | 0.016 | 🔺 Rising |
| 2026-11-26 19:03:25 | Dunamale (Aththanagalu Oya) | 3.35 | 🟡 Alert | 0.000 |  |
| 2026-11-26 20:01:22 | Padiyathalawa (Maduru Oya) | 3.95 | 🟢 Normal | 2.135 | 🔺 Rising |
| 2026-11-26 20:02:29 | Kuda Oya (Kirindi Oya) | 2.65 | 🟢 Normal | 0.799 | 🔺 Rising |
| 2026-11-26 19:10:35 | Rathnapura (Kalu Ganga) | 3.17 | 🟢 Normal | 0.766 | 🔺 Rising |
| 2026-11-26 20:00:57 | Siyambalanduwa (Heda Oya) | 1.90 | 🟢 Normal | 0.228 | 🔺 Rising |
| 2026-11-26 19:12:58 | Pitabeddara (Nilwala Ganga) | 1.84 | 🟢 Normal | 0.222 | 🔺 Rising |
| 2026-11-26 19:04:12 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-11-26 20:00:20 | Wellawaya (Kirindi Oya) | 1.92 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-11-26 20:02:09 | Hanwella (Kelani Ganga) | 3.28 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-11-26 20:02:49 | Ellagawa (Kalu Ganga) | 6.27 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-11-26 20:02:44 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 0.083 | 🔺 Rising |
| 2026-11-26 19:07:25 | Glencourse (Kelani Ganga) | 11.36 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-26 19:03:06 | Thanamalwila (Kirindi Oya) | 1.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-26 19:03:43 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-11-26 18:00:24 | Weraganthota (Mahaweli Ganga) | -1.98 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-26 20:02:03 | Moragaswewa (Deduru Oya) | 4.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-26 19:27:27 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-26 19:04:31 | Giriulla (Maha Oya) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-11-26 19:28:23 | Horowpothana (Yan Oya) | 2.40 | 🟢 Normal | 0.000 |  |
| 2026-11-26 18:02:07 | Thanthirimale (Malwathu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-11-26 19:18:47 | Thawalama (Gin Ganga) | 2.45 | 🟢 Normal | 0.000 |  |
| 2026-11-26 19:08:14 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-11-26 19:15:26 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.009 |  |
| 2026-11-26 19:11:19 | Badalgama (Maha Oya) | 3.82 | 🟢 Normal | -0.009 |  |
| 2026-11-26 19:09:27 | Katharagama (Menik Ganga) | 0.06 | 🟢 Normal | -0.010 |  |
| 2026-11-26 19:06:44 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-11-26 20:02:27 | Putupaula (Kalu Ganga) | 1.33 | 🟢 Normal | -0.020 |  |
| 2026-11-26 18:01:55 | Galgamuwa (Mee Oya) | 1.18 | 🟢 Normal | -0.021 |  |
| 2026-11-26 19:01:55 | Manampitiya (Mahaweli Ganga) | 1.73 | 🟢 Normal | -0.049 |  |
| 2026-11-26 19:04:10 | Panadugama (Nilwala Ganga) | 3.60 | 🟢 Normal | -0.054 |  |
| 2026-11-26 20:02:50 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.063 |  |
| 2026-11-26 20:01:09 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.085 |  |
| 2026-11-26 19:09:06 | Baddegama (Gin Ganga) | 1.62 | 🟢 Normal | -0.088 |  |
| 2026-11-26 19:05:41 | Nawalapitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.093 |  |
| 2026-11-26 19:04:54 | Kithulgala (Kelani Ganga) | 1.06 | 🟢 Normal | -0.878 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)