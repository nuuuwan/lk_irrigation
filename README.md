# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--03_23:26:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **306,106 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moraketiya — Alert; 🟡 Urawa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 23:26:42 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:25:40 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:22:03 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.008 |  |
| 2026-11-03 23:19:04 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:11:59 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-03 23:10:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-03 23:10:01 | Thawalama (Gin Ganga) | 3.02 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-11-03 23:08:54 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.078 |  |
| 2026-11-03 23:07:05 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-03 23:07:01 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | -0.071 |  |
| 2026-11-03 23:06:28 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-03 23:05:19 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.032 |  |
| 2026-11-03 23:05:08 | Moragaswewa (Deduru Oya) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:04:55 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:04:24 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.069 |  |
| 2026-11-03 23:04:10 | Moragaswewa (Deduru Oya) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:04:08 | Magura (Kalu Ganga) | 3.04 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-11-03 23:03:55 | Dunamale (Aththanagalu Oya) | 1.83 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:03:23 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.049 |  |
| 2026-11-03 23:03:15 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-03 23:03:11 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | 0.501 | 🔺 Rising |
| 2026-11-03 23:03:07 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:03:03 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:02:37 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-11-03 23:02:34 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.031 |  |
| 2026-11-03 23:02:27 | Norwood (Kelani Ganga) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-11-03 23:02:16 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.050 |  |
| 2026-11-03 23:02:11 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-11-03 23:02:06 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-11-03 23:01:38 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:01:24 | Thanamalwila (Kirindi Oya) | 2.31 | 🟢 Normal | -0.251 |  |
| 2026-11-03 23:01:19 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-03 23:01:15 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | -0.032 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-03 22:04:41 | Moraketiya (Walawe Ganga) | 3.12 | 🟡 Alert | 0.451 | 🔺 Rising |
| 2026-11-03 22:03:37 | Urawa (Nilwala Ganga) | 3.20 | 🟡 Alert | 0.212 | 🔺 Rising |
| 2026-11-03 23:03:11 | Giriulla (Maha Oya) | 3.05 | 🟢 Normal | 0.501 | 🔺 Rising |
| 2026-11-03 21:07:37 | Kuda Oya (Kirindi Oya) | 2.89 | 🟢 Normal | 0.449 | 🔺 Rising |
| 2026-11-03 23:02:11 | Hanwella (Kelani Ganga) | 2.58 | 🟢 Normal | 0.263 | 🔺 Rising |
| 2026-11-03 18:06:38 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.248 | 🔺 Rising |
| 2026-11-03 23:10:01 | Thawalama (Gin Ganga) | 3.02 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-11-03 23:04:08 | Magura (Kalu Ganga) | 3.04 | 🟢 Normal | 0.229 | 🔺 Rising |
| 2026-11-03 23:02:06 | Glencourse (Kelani Ganga) | 11.39 | 🟢 Normal | 0.189 | 🔺 Rising |
| 2026-11-03 23:10:57 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.88 | 🟢 Normal | 0.140 | 🔺 Rising |
| 2026-11-03 23:02:37 | Pitabeddara (Nilwala Ganga) | 1.70 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-11-03 18:04:27 | Weraganthota (Mahaweli Ganga) | -2.51 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-11-03 23:07:05 | Rathnapura (Kalu Ganga) | 2.91 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-11-03 22:00:10 | Horowpothana (Yan Oya) | 2.86 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-11-03 23:06:28 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-11-03 23:01:19 | Peradeniya (Mahaweli Ganga) | 3.58 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-03 23:03:15 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-11-03 22:33:15 | Panadugama (Nilwala Ganga) | 4.19 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-11-03 23:11:59 | Ellagawa (Kalu Ganga) | 6.28 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-11-03 23:01:38 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:05:08 | Moragaswewa (Deduru Oya) | 4.19 | 🟢 Normal | 0.000 |  |
| 2026-11-03 22:49:38 | Yaka Wewa (Ma Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:04:55 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:26:42 | Dunamale (Aththanagalu Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:19:04 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-11-03 18:50:18 | Thanthirimale (Malwathu Oya) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:03:03 | Thalgahagoda (Nilwala Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-11-03 23:22:03 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | -0.008 |  |
| 2026-11-03 23:02:27 | Norwood (Kelani Ganga) | 1.43 | 🟢 Normal | -0.021 |  |
| 2026-11-03 23:02:34 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | -0.031 |  |
| 2026-11-03 23:01:15 | Padiyathalawa (Maduru Oya) | 0.70 | 🟢 Normal | -0.032 |  |
| 2026-11-03 23:05:19 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.032 |  |
| 2026-11-03 22:08:07 | Wellawaya (Kirindi Oya) | 1.62 | 🟢 Normal | -0.037 |  |
| 2026-11-03 23:03:23 | Nawalapitiya (Mahaweli Ganga) | 1.56 | 🟢 Normal | -0.049 |  |
| 2026-11-03 23:02:16 | Siyambalanduwa (Heda Oya) | 0.68 | 🟢 Normal | -0.050 |  |
| 2026-11-03 23:04:24 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | -0.069 |  |
| 2026-11-03 23:07:01 | Holombuwa (Kelani Ganga) | 1.74 | 🟢 Normal | -0.071 |  |
| 2026-11-03 23:08:54 | Thaldena (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.078 |  |
| 2026-11-03 23:01:24 | Thanamalwila (Kirindi Oya) | 2.31 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)