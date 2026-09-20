# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_07:13:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **265,832 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Nawalapitiya — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 07:13:48 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-09-20 07:11:46 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.017 |  |
| 2026-09-20 07:10:45 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-20 07:10:15 | Magura (Kalu Ganga) | 4.39 | 🟡 Alert | 0.168 | 🔺 Rising |
| 2026-09-20 07:09:39 | Ellagawa (Kalu Ganga) | 5.83 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-20 07:09:30 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.001 |  |
| 2026-09-20 07:09:27 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-20 07:08:57 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-09-20 07:08:38 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-09-20 07:08:12 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:07:39 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2026-09-20 07:06:48 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-20 07:06:43 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 07:06:11 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-09-20 07:05:57 | Rathnapura (Kalu Ganga) | 2.47 | 🟢 Normal | 0.521 | 🔺 Rising |
| 2026-09-20 07:05:41 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:05:15 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-20 07:04:56 | Nawalapitiya (Mahaweli Ganga) | 4.73 | 🟡 Alert | 1.165 | 🔺 Rising |
| 2026-09-20 07:04:40 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:04:38 | Kithulgala (Kelani Ganga) | 2.95 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-09-20 07:04:31 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:03:49 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 07:03:46 | Deraniyagala (Kelani Ganga) | 3.15 | 🟢 Normal | 0.555 | 🔺 Rising |
| 2026-09-20 07:03:42 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-20 07:03:31 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:03:17 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-20 07:02:45 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:02:35 | Pitabeddara (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.778 |  |
| 2026-09-20 07:02:16 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:02:12 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:02:08 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:02:04 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:01:55 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.002 |  |
| 2026-09-20 07:01:53 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-09-20 07:01:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:01:23 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:01:08 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:00:10 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 07:04:56 | Nawalapitiya (Mahaweli Ganga) | 4.73 | 🟡 Alert | 1.165 | 🔺 Rising |
| 2026-09-20 07:10:15 | Magura (Kalu Ganga) | 4.39 | 🟡 Alert | 0.168 | 🔺 Rising |
| 2026-09-20 07:03:46 | Deraniyagala (Kelani Ganga) | 3.15 | 🟢 Normal | 0.555 | 🔺 Rising |
| 2026-09-20 07:05:57 | Rathnapura (Kalu Ganga) | 2.47 | 🟢 Normal | 0.521 | 🔺 Rising |
| 2026-09-20 07:07:39 | Thawalama (Gin Ganga) | 3.23 | 🟢 Normal | 0.352 | 🔺 Rising |
| 2026-09-20 06:07:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.56 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-09-20 07:08:57 | Putupaula (Kalu Ganga) | 1.17 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-09-20 07:04:38 | Kithulgala (Kelani Ganga) | 2.95 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-09-20 07:08:38 | Baddegama (Gin Ganga) | 2.41 | 🟢 Normal | 0.150 | 🔺 Rising |
| 2026-09-20 07:13:48 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.147 | 🔺 Rising |
| 2026-09-20 07:03:17 | Panadugama (Nilwala Ganga) | 3.18 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-09-20 07:09:39 | Ellagawa (Kalu Ganga) | 5.83 | 🟢 Normal | 0.129 | 🔺 Rising |
| 2026-09-20 07:06:11 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-09-20 07:06:48 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-09-20 07:03:42 | Dunamale (Aththanagalu Oya) | 1.76 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-09-20 07:05:15 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-09-20 07:10:45 | Peradeniya (Mahaweli Ganga) | 1.94 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-09-20 07:06:43 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 07:09:27 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-20 07:03:49 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 07:01:55 | Thanthirimale (Malwathu Oya) | 0.45 | 🟢 Normal | 0.002 |  |
| 2026-09-20 07:09:30 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.001 |  |
| 2026-09-20 07:02:08 | Weraganthota (Mahaweli Ganga) | -2.90 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:02:45 | Wellawaya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:03:31 | Moragaswewa (Deduru Oya) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:01:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:04:31 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:00:10 | Horowpothana (Yan Oya) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:05:41 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:04:40 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:01:08 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:08:12 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:01:23 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:02:04 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:02:12 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:02:16 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 07:01:53 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-09-20 07:11:46 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.017 |  |
| 2026-09-20 07:02:35 | Pitabeddara (Nilwala Ganga) | 0.09 | 🟢 Normal | -0.778 |  |

## River Water Level Charts by Station

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)