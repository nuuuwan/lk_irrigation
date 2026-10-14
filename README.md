# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_00:34:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,099 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert; 🟡 Holombuwa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 00:34:01 | Panadugama (Nilwala Ganga) | 5.31 | 🟡 Alert | -0.059 |  |
| 2026-10-15 00:32:21 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 00:24:41 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.012 |  |
| 2026-10-15 00:14:59 | Putupaula (Kalu Ganga) | 2.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 00:13:15 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-10-15 00:12:03 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-15 00:11:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-15 00:10:35 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-15 00:10:33 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-15 00:10:11 | Holombuwa (Kelani Ganga) | 3.05 | 🟡 Alert | -0.733 |  |
| 2026-10-15 00:09:16 | Hanwella (Kelani Ganga) | 4.26 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-10-15 00:08:26 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.105 |  |
| 2026-10-15 00:08:25 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-15 00:07:53 | Baddegama (Gin Ganga) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-10-15 00:07:17 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 00:06:30 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-15 00:05:50 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.058 |  |
| 2026-10-15 00:05:43 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.068 |  |
| 2026-10-15 00:05:34 | Peradeniya (Mahaweli Ganga) | 4.05 | 🟢 Normal | -0.207 |  |
| 2026-10-15 00:05:04 | Rathnapura (Kalu Ganga) | 5.14 | 🟢 Normal | -0.164 |  |
| 2026-10-15 00:04:46 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-15 00:04:20 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | -0.089 |  |
| 2026-10-15 00:03:44 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.202 |  |
| 2026-10-15 00:03:32 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-10-15 00:03:23 | Glencourse (Kelani Ganga) | 13.27 | 🟢 Normal | 1.109 | 🔺 Rising |
| 2026-10-15 00:03:14 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-15 00:02:55 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 00:02:54 | Giriulla (Maha Oya) | 3.22 | 🟢 Normal | 1.024 | 🔺 Rising |
| 2026-10-15 00:02:50 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 00:02:44 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-15 00:02:42 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 00:02:16 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.033 |  |
| 2026-10-15 00:01:54 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-15 00:01:10 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.706 | 🔺 Rising |
| 2026-10-15 00:00:53 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-10-15 00:00:33 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.060 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 00:32:21 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 23:03:28 | Dunamale (Aththanagalu Oya) | 3.40 | 🟡 Alert | 0.155 | 🔺 Rising |
| 2026-10-15 00:11:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-15 00:34:01 | Panadugama (Nilwala Ganga) | 5.31 | 🟡 Alert | -0.059 |  |
| 2026-10-15 00:05:43 | Magura (Kalu Ganga) | 4.27 | 🟡 Alert | -0.068 |  |
| 2026-10-15 00:10:11 | Holombuwa (Kelani Ganga) | 3.05 | 🟡 Alert | -0.733 |  |
| 2026-10-15 00:03:23 | Glencourse (Kelani Ganga) | 13.27 | 🟢 Normal | 1.109 | 🔺 Rising |
| 2026-10-15 00:02:54 | Giriulla (Maha Oya) | 3.22 | 🟢 Normal | 1.024 | 🔺 Rising |
| 2026-10-15 00:01:10 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | 0.706 | 🔺 Rising |
| 2026-10-15 00:09:16 | Hanwella (Kelani Ganga) | 4.26 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-10-15 00:13:15 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-10-15 00:12:03 | Ellagawa (Kalu Ganga) | 7.92 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-15 00:00:33 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-15 00:01:54 | Manampitiya (Mahaweli Ganga) | 0.03 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-15 00:06:30 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-15 00:08:25 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-10-15 00:14:59 | Putupaula (Kalu Ganga) | 2.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 00:04:46 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-10-15 00:07:17 | Kithulgala (Kelani Ganga) | 2.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 00:02:42 | Thanamalwila (Kirindi Oya) | 0.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 18:02:30 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-15 00:02:44 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-15 00:03:14 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-15 00:02:55 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 00:10:35 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:47 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-15 00:02:50 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 00:07:53 | Baddegama (Gin Ganga) | 2.50 | 🟢 Normal | -0.010 |  |
| 2026-10-15 00:24:41 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.012 |  |
| 2026-10-15 00:03:32 | Norwood (Kelani Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-10-15 00:00:53 | Thaldena (Mahaweli Ganga) | 0.43 | 🟢 Normal | -0.032 |  |
| 2026-10-15 00:02:16 | Urawa (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.033 |  |
| 2026-10-15 00:05:50 | Nawalapitiya (Mahaweli Ganga) | 1.39 | 🟢 Normal | -0.058 |  |
| 2026-10-15 00:04:20 | Thawalama (Gin Ganga) | 2.84 | 🟢 Normal | -0.089 |  |
| 2026-10-15 00:08:26 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | -0.105 |  |
| 2026-10-15 00:05:04 | Rathnapura (Kalu Ganga) | 5.14 | 🟢 Normal | -0.164 |  |
| 2026-10-15 00:03:44 | Deraniyagala (Kelani Ganga) | 1.39 | 🟢 Normal | -0.202 |  |
| 2026-10-15 00:05:34 | Peradeniya (Mahaweli Ganga) | 4.05 | 🟢 Normal | -0.207 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)