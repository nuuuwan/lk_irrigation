# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--20_05:35:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **320,654 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 05:35:25 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.076 |  |
| 2026-11-20 05:30:32 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-20 05:22:26 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -1.125 |  |
| 2026-11-20 05:21:54 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -1.125 |  |
| 2026-11-20 05:21:37 | Panadugama (Nilwala Ganga) | 3.29 | 🟢 Normal | -1.125 |  |
| 2026-11-20 05:21:15 | Panadugama (Nilwala Ganga) | 3.30 | 🟢 Normal | -1.125 |  |
| 2026-11-20 05:14:43 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-20 05:10:20 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-20 05:08:15 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-20 05:08:04 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-11-20 05:06:31 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-20 05:06:29 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:05:51 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.127 |  |
| 2026-11-20 05:05:47 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:05:45 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:05:27 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:05:02 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-11-20 05:04:40 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 05:03:51 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-20 05:03:08 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:02:48 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 05:02:44 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:02:39 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:02:37 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 05:02:35 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:02:22 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.092 |  |
| 2026-11-20 05:01:59 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:01:37 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-20 05:01:35 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-20 05:01:21 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:01:09 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.010 |  |
| 2026-11-20 05:00:56 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:00:37 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:00:33 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-20 05:08:15 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-20 04:03:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-20 05:03:51 | Deraniyagala (Kelani Ganga) | 0.55 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-11-20 05:06:31 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-11-20 05:02:37 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 05:02:48 | Horowpothana (Yan Oya) | 1.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 05:04:40 | Thanamalwila (Kirindi Oya) | 1.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-20 05:14:43 | Thawalama (Gin Ganga) | 1.60 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-20 05:10:20 | Holombuwa (Kelani Ganga) | 0.59 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-11-20 05:30:32 | Yaka Wewa (Ma Oya) | 0.48 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-11-19 18:00:52 | Weraganthota (Mahaweli Ganga) | -2.03 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:01:59 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:00:56 | Moragaswewa (Deduru Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:00:37 | Nawalapitiya (Mahaweli Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-11-20 04:05:19 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:05:27 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-11-20 03:07:06 | Pitabeddara (Nilwala Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-11-19 14:01:52 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:02:44 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:01:21 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:03:08 | Dunamale (Aththanagalu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:00:33 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:05:47 | Katharagama (Menik Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:06:29 | Badalgama (Maha Oya) | 2.42 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:02:39 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:05:45 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-11-19 18:01:52 | Thanthirimale (Malwathu Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-20 05:02:35 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.000 |  |
| 2026-11-19 23:03:59 | Urawa (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-11-19 18:05:17 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | -0.009 |  |
| 2026-11-20 05:01:37 | Wellawaya (Kirindi Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-11-20 05:01:09 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.010 |  |
| 2026-11-20 05:01:35 | Moraketiya (Walawe Ganga) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-11-20 05:08:04 | Thalgahagoda (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.019 |  |
| 2026-11-20 05:05:02 | Baddegama (Gin Ganga) | 1.16 | 🟢 Normal | -0.021 |  |
| 2026-11-20 05:35:25 | Kuda Oya (Kirindi Oya) | 1.71 | 🟢 Normal | -0.076 |  |
| 2026-11-20 05:02:22 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.092 |  |
| 2026-11-20 05:05:51 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | -0.127 |  |
| 2026-11-20 05:22:26 | Panadugama (Nilwala Ganga) | 3.28 | 🟢 Normal | -1.125 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)