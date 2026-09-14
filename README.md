# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--14_23:02:49-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **261,032 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 23:02:49 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 23:02:22 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-14 23:02:16 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:02:12 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:01:27 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:01:24 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.674 | 🔺 Rising |
| 2026-09-14 23:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.060 |  |
| 2026-09-14 23:01:08 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-09-14 23:00:51 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-14 22:20:49 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-14 23:01:24 | Magura (Kalu Ganga) | 3.80 | 🟢 Normal | 0.674 | 🔺 Rising |
| 2026-09-14 22:05:59 | Rathnapura (Kalu Ganga) | 2.46 | 🟢 Normal | 0.416 | 🔺 Rising |
| 2026-09-14 22:09:20 | Glencourse (Kelani Ganga) | 10.33 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-09-14 22:06:26 | Thawalama (Gin Ganga) | 1.96 | 🟢 Normal | 0.193 | 🔺 Rising |
| 2026-09-14 22:05:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.98 | 🟢 Normal | 0.179 | 🔺 Rising |
| 2026-09-14 22:05:48 | Hanwella (Kelani Ganga) | 1.38 | 🟢 Normal | 0.137 | 🔺 Rising |
| 2026-09-14 22:00:29 | Peradeniya (Mahaweli Ganga) | 2.63 | 🟢 Normal | 0.126 | 🔺 Rising |
| 2026-09-14 23:01:08 | Pitabeddara (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-09-14 23:02:22 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-09-14 22:03:02 | Ellagawa (Kalu Ganga) | 5.75 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-14 22:12:29 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-09-14 22:04:51 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-14 22:03:30 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 23:02:49 | Deraniyagala (Kelani Ganga) | 0.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 22:03:29 | Giriulla (Maha Oya) | 0.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-14 22:11:04 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-14 18:10:49 | Thanthirimale (Malwathu Oya) | 0.42 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-14 23:02:16 | Wellawaya (Kirindi Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:00:51 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-14 22:04:36 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:01:27 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 18:11:58 | Galgamuwa (Mee Oya) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-14 22:06:52 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-09-14 22:07:15 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-09-14 22:05:58 | Nagalagam Street (Kelani Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-14 22:20:49 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-14 22:02:15 | Katharagama (Menik Ganga) | -0.30 | 🟢 Normal | 0.000 |  |
| 2026-09-14 22:08:30 | Badalgama (Maha Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-14 22:08:53 | Holombuwa (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-14 22:10:34 | Urawa (Nilwala Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-14 22:01:23 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-14 23:02:12 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-09-14 22:01:08 | Manampitiya (Mahaweli Ganga) | -0.40 | 🟢 Normal | -0.010 |  |
| 2026-09-14 18:06:43 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-09-14 22:06:01 | Baddegama (Gin Ganga) | 1.90 | 🟢 Normal | -0.033 |  |
| 2026-09-14 23:01:09 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | -0.060 |  |
| 2026-09-14 22:07:55 | Thalgahagoda (Nilwala Ganga) | 0.24 | 🟢 Normal | -0.068 |  |
| 2026-09-14 22:10:32 | Kithulgala (Kelani Ganga) | 1.70 | 🟢 Normal | -0.143 |  |
| 2026-09-14 22:01:25 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | -18.000 |  |

## River Water Level Charts by Station

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)