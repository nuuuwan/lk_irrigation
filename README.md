# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_01:05:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,125 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 01:05:47 | Holombuwa (Kelani Ganga) | 2.61 | 🟢 Normal | -0.475 |  |
| 2026-10-15 01:05:42 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-10-15 01:05:23 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -1.271 |  |
| 2026-10-15 01:05:18 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.040 |  |
| 2026-10-15 01:05:07 | Dunamale (Aththanagalu Oya) | 3.60 | 🟡 Alert | 0.099 | 🔺 Rising |
| 2026-10-15 01:04:26 | Rathnapura (Kalu Ganga) | 4.92 | 🟢 Normal | -0.222 |  |
| 2026-10-15 01:04:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.116 |  |
| 2026-10-15 01:04:02 | Hanwella (Kelani Ganga) | 4.46 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-10-15 01:03:54 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.097 |  |
| 2026-10-15 01:03:37 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.180 |  |
| 2026-10-15 01:03:03 | Giriulla (Maha Oya) | 3.78 | 🟢 Normal | 0.559 | 🔺 Rising |
| 2026-10-15 01:02:58 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 01:02:51 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | -0.040 |  |
| 2026-10-15 01:02:42 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 01:02:41 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-15 01:02:17 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 8.000 | 🔺 Rising |
| 2026-10-15 01:02:16 | Peradeniya (Mahaweli Ganga) | 3.86 | 🟢 Normal | -0.201 |  |
| 2026-10-15 01:01:45 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 01:01:41 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 8.000 | 🔺 Rising |
| 2026-10-15 01:01:38 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 01:01:32 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 01:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.000 |  |
| 2026-10-15 01:01:27 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-15 01:01:15 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 01:00:57 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.723 |  |
| 2026-10-15 01:00:48 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 00:34:01 | Panadugama (Nilwala Ganga) | 5.31 | 🟡 Alert | -0.059 |  |
| 2026-10-15 00:32:21 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | -1.271 |  |
| 2026-10-15 00:24:41 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 01:05:07 | Dunamale (Aththanagalu Oya) | 3.60 | 🟡 Alert | 0.099 | 🔺 Rising |
| 2026-10-15 01:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.000 |  |
| 2026-10-15 00:34:01 | Panadugama (Nilwala Ganga) | 5.31 | 🟡 Alert | -0.059 |  |
| 2026-10-15 00:05:43 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.068 |  |
| 2026-10-15 01:02:17 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 8.000 | 🔺 Rising |
| 2026-10-15 00:03:23 | Glencourse (Kelani Ganga) | 13.27 | 🟢 Normal | 1.109 | 🔺 Rising |
| 2026-10-15 01:03:03 | Giriulla (Maha Oya) | 3.78 | 🟢 Normal | 0.559 | 🔺 Rising |
| 2026-10-15 01:04:02 | Hanwella (Kelani Ganga) | 4.46 | 🟢 Normal | 0.219 | 🔺 Rising |
| 2026-10-15 00:13:15 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-10-15 01:05:42 | Badalgama (Maha Oya) | 2.98 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-10-15 00:12:03 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-15 01:01:38 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 01:01:32 | Manampitiya (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-15 01:02:42 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 01:00:48 | Thaldena (Mahaweli Ganga) | 0.45 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 00:14:59 | Putupaula (Kalu Ganga) | 2.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 01:01:15 | Horowpothana (Yan Oya) | 1.73 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-14 18:02:30 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-15 01:01:27 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-15 01:02:58 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 01:02:41 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-10-15 00:10:35 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:47 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-15 01:01:45 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 00:07:53 | Baddegama (Gin Ganga) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-10-15 00:24:41 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.012 |  |
| 2026-10-15 00:02:16 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.033 |  |
| 2026-10-15 01:05:18 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.040 |  |
| 2026-10-15 01:02:51 | Norwood (Kelani Ganga) | 1.28 | 🟢 Normal | -0.040 |  |
| 2026-10-15 00:04:20 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | -0.089 |  |
| 2026-10-15 01:03:54 | Yaka Wewa (Ma Oya) | 0.82 | 🟢 Normal | -0.097 |  |
| 2026-10-15 01:04:13 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | -0.116 |  |
| 2026-10-15 01:03:37 | Deraniyagala (Kelani Ganga) | 1.21 | 🟢 Normal | -0.180 |  |
| 2026-10-15 01:02:16 | Peradeniya (Mahaweli Ganga) | 3.86 | 🟢 Normal | -0.201 |  |
| 2026-10-15 01:04:26 | Rathnapura (Kalu Ganga) | 4.92 | 🟢 Normal | -0.222 |  |
| 2026-10-15 01:05:47 | Holombuwa (Kelani Ganga) | 2.61 | 🟢 Normal | -0.475 |  |
| 2026-10-15 01:00:57 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.723 |  |
| 2026-10-15 01:05:23 | Thalgahagoda (Nilwala Ganga) | 1.05 | 🟢 Normal | -1.271 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)