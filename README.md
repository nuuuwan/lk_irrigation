# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_00:08:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **297,990 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Rathnapura — Alert; 🟡 Norwood — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 00:08:59 | Holombuwa (Kelani Ganga) | 1.86 | 🟢 Normal | -0.191 |  |
| 2026-10-26 00:08:55 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-10-26 00:08:20 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-26 00:08:04 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-26 00:07:03 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-10-26 00:06:39 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 00:06:38 | Norwood (Kelani Ganga) | 1.61 | 🟡 Alert | -0.029 |  |
| 2026-10-26 00:06:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-26 00:06:27 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-26 00:06:20 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-26 00:05:59 | Rathnapura (Kalu Ganga) | 6.10 | 🟡 Alert | 0.146 | 🔺 Rising |
| 2026-10-26 00:05:55 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-26 00:05:53 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 00:05:38 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 00:05:29 | Glencourse (Kelani Ganga) | 12.19 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-10-26 00:05:25 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.047 |  |
| 2026-10-26 00:05:11 | Hanwella (Kelani Ganga) | 3.51 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-26 00:04:15 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 00:03:51 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-26 00:03:50 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-26 00:03:49 | Ellagawa (Kalu Ganga) | 7.88 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-10-26 00:03:48 | Kithulgala (Kelani Ganga) | 2.51 | 🟢 Normal | -0.071 |  |
| 2026-10-26 00:03:37 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.044 |  |
| 2026-10-26 00:03:15 | Thawalama (Gin Ganga) | 3.18 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-26 00:03:02 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -0.109 |  |
| 2026-10-26 00:02:18 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-26 00:02:13 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-26 00:02:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-10-26 00:01:56 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 00:01:40 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 00:01:36 | Nawalapitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.042 |  |
| 2026-10-26 00:01:28 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 00:01:08 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-26 00:00:48 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.356 | 🔺 Rising |
| 2026-10-25 23:37:23 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-25 23:37:05 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 00:05:59 | Rathnapura (Kalu Ganga) | 6.10 | 🟡 Alert | 0.146 | 🔺 Rising |
| 2026-10-26 00:06:38 | Norwood (Kelani Ganga) | 1.61 | 🟡 Alert | -0.029 |  |
| 2026-10-26 00:00:48 | Moragaswewa (Deduru Oya) | 1.78 | 🟢 Normal | 0.356 | 🔺 Rising |
| 2026-10-26 00:07:03 | Badalgama (Maha Oya) | 3.52 | 🟢 Normal | 0.316 | 🔺 Rising |
| 2026-10-25 23:09:59 | Giriulla (Maha Oya) | 2.61 | 🟢 Normal | 0.200 | 🔺 Rising |
| 2026-10-26 00:05:29 | Glencourse (Kelani Ganga) | 12.19 | 🟢 Normal | 0.181 | 🔺 Rising |
| 2026-10-26 00:02:09 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.177 | 🔺 Rising |
| 2026-10-26 00:03:49 | Ellagawa (Kalu Ganga) | 7.88 | 🟢 Normal | 0.163 | 🔺 Rising |
| 2026-10-26 00:05:11 | Hanwella (Kelani Ganga) | 3.51 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-10-25 18:03:46 | Galgamuwa (Mee Oya) | 1.82 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-26 00:05:55 | Magura (Kalu Ganga) | 3.44 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-10-26 00:02:13 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-10-26 00:02:18 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-25 22:04:38 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-10-26 00:03:15 | Thawalama (Gin Ganga) | 3.18 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-26 00:08:04 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-10-26 00:06:27 | Baddegama (Gin Ganga) | 2.38 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-26 00:06:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.58 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-26 00:01:56 | Manampitiya (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 00:05:53 | Putupaula (Kalu Ganga) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 00:01:40 | Panadugama (Nilwala Ganga) | 4.63 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 00:06:39 | Urawa (Nilwala Ganga) | 1.33 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-26 00:01:28 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 00:05:38 | Deraniyagala (Kelani Ganga) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 00:03:50 | Wellawaya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-10-26 00:03:51 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-26 00:04:15 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 00:08:20 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-25 18:02:16 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-10-26 00:06:20 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-26 00:08:55 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | -0.009 |  |
| 2026-10-26 00:01:08 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.010 |  |
| 2026-10-26 00:01:36 | Nawalapitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | -0.042 |  |
| 2026-10-26 00:03:37 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.044 |  |
| 2026-10-26 00:05:25 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.047 |  |
| 2026-10-25 18:03:32 | Weraganthota (Mahaweli Ganga) | -3.24 | 🟢 Normal | -0.069 |  |
| 2026-10-26 00:03:48 | Kithulgala (Kelani Ganga) | 2.51 | 🟢 Normal | -0.071 |  |
| 2026-10-26 00:03:02 | Nakkala (Kumbukkan Oya) | 1.51 | 🟢 Normal | -0.109 |  |
| 2026-10-26 00:08:59 | Holombuwa (Kelani Ganga) | 1.86 | 🟢 Normal | -0.191 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)