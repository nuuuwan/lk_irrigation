# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--09_13:14:57-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **283,187 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 13:14:57 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:08:34 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-10-09 13:08:19 | Giriulla (Maha Oya) | 3.17 | 🟢 Normal | -0.063 |  |
| 2026-10-09 13:07:47 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:07:44 | Baddegama (Gin Ganga) | 2.77 | 🟢 Normal | -0.028 |  |
| 2026-10-09 13:07:17 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.106 |  |
| 2026-10-09 13:06:25 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.134 |  |
| 2026-10-09 13:05:41 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | -0.041 |  |
| 2026-10-09 13:05:39 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2026-10-09 13:05:33 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-10-09 13:05:26 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | -0.077 |  |
| 2026-10-09 13:05:22 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-09 13:05:20 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:05:01 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-09 13:04:58 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.222 |  |
| 2026-10-09 13:04:45 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | -0.097 |  |
| 2026-10-09 13:04:32 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.223 |  |
| 2026-10-09 13:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-09 13:04:12 | Hanwella (Kelani Ganga) | 3.52 | 🟢 Normal | -0.098 |  |
| 2026-10-09 13:03:19 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | -0.108 |  |
| 2026-10-09 13:02:49 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-09 13:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.86 | 🟢 Normal | -0.030 |  |
| 2026-10-09 13:02:44 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.072 |  |
| 2026-10-09 13:02:43 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | -0.050 |  |
| 2026-10-09 13:02:42 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:02:25 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:02:23 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-10-09 13:02:01 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.102 |  |
| 2026-10-09 13:02:00 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:01:36 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-09 13:01:14 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-10-09 13:01:09 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-09 13:01:06 | Thanthirimale (Malwathu Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:01:06 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.020 |  |
| 2026-10-09 13:01:02 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:00:35 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-09 13:00:24 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:00:13 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-09 13:08:34 | Urawa (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.255 | 🔺 Rising |
| 2026-10-09 13:02:23 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-10-09 13:05:01 | Putupaula (Kalu Ganga) | 1.42 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-09 13:01:36 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-09 13:00:35 | Siyambalanduwa (Heda Oya) | 0.33 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-09 13:00:24 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:00:13 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:02:00 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:01:02 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:14:57 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:02:25 | Pitabeddara (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:07:47 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:05:20 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:02:42 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:01:06 | Thanthirimale (Malwathu Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-09 12:07:08 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-09 13:02:49 | Moraketiya (Walawe Ganga) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-10-09 13:05:22 | Thanamalwila (Kirindi Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-10-09 13:01:09 | Manampitiya (Mahaweli Ganga) | -0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-09 13:04:20 | Nawalapitiya (Mahaweli Ganga) | 1.26 | 🟢 Normal | -0.010 |  |
| 2026-10-09 13:01:14 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.011 |  |
| 2026-10-09 13:01:06 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.020 |  |
| 2026-10-09 13:05:33 | Norwood (Kelani Ganga) | 0.94 | 🟢 Normal | -0.020 |  |
| 2026-10-09 13:07:44 | Baddegama (Gin Ganga) | 2.77 | 🟢 Normal | -0.028 |  |
| 2026-10-09 13:02:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.86 | 🟢 Normal | -0.030 |  |
| 2026-10-09 13:05:39 | Magura (Kalu Ganga) | 2.19 | 🟢 Normal | -0.031 |  |
| 2026-10-09 13:05:41 | Holombuwa (Kelani Ganga) | 1.36 | 🟢 Normal | -0.041 |  |
| 2026-10-09 13:02:43 | Ellagawa (Kalu Ganga) | 6.55 | 🟢 Normal | -0.050 |  |
| 2026-10-09 13:08:19 | Giriulla (Maha Oya) | 3.17 | 🟢 Normal | -0.063 |  |
| 2026-10-09 13:02:44 | Thawalama (Gin Ganga) | 2.12 | 🟢 Normal | -0.072 |  |
| 2026-10-09 13:05:26 | Panadugama (Nilwala Ganga) | 3.94 | 🟢 Normal | -0.077 |  |
| 2026-10-09 13:04:45 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | -0.097 |  |
| 2026-10-09 13:04:12 | Hanwella (Kelani Ganga) | 3.52 | 🟢 Normal | -0.098 |  |
| 2026-10-09 13:02:01 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | -0.102 |  |
| 2026-10-09 13:07:17 | Badalgama (Maha Oya) | 4.20 | 🟢 Normal | -0.106 |  |
| 2026-10-09 13:03:19 | Glencourse (Kelani Ganga) | 11.31 | 🟢 Normal | -0.108 |  |
| 2026-10-09 13:06:25 | Rathnapura (Kalu Ganga) | 2.59 | 🟢 Normal | -0.134 |  |
| 2026-10-09 13:04:58 | Peradeniya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -0.222 |  |
| 2026-10-09 13:04:32 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | -0.223 |  |

## River Water Level Charts by Station

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)