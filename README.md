# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_13:18:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,065 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert; 🟡 Holombuwa — Alert; 🟡 Panadugama — Alert; 🟡 Rathnapura — Alert; 🟡 Thawalama — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 13:18:35 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-09-20 13:07:31 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:06:36 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:06:24 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-20 13:06:22 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:05:12 | Thawalama (Gin Ganga) | 4.98 | 🟡 Alert | 0.149 | 🔺 Rising |
| 2026-09-20 13:05:11 | Holombuwa (Kelani Ganga) | 3.14 | 🟡 Alert | 0.323 | 🔺 Rising |
| 2026-09-20 13:04:55 | Glencourse (Kelani Ganga) | 14.75 | 🟢 Normal | 0.453 | 🔺 Rising |
| 2026-09-20 13:04:44 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 13:04:43 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:04:39 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-20 13:04:36 | Rathnapura (Kalu Ganga) | 6.78 | 🟡 Alert | 0.188 | 🔺 Rising |
| 2026-09-20 13:04:23 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-09-20 13:03:59 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:03:54 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-09-20 13:03:51 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-09-20 13:03:45 | Magura (Kalu Ganga) | 5.09 | 🟡 Alert | 0.066 | 🔺 Rising |
| 2026-09-20 13:03:44 | Nawalapitiya (Mahaweli Ganga) | 4.80 | 🟡 Alert | -0.540 |  |
| 2026-09-20 13:03:30 | Deraniyagala (Kelani Ganga) | 4.60 | 🟢 Normal | -0.229 |  |
| 2026-09-20 13:03:21 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 13:03:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-20 13:03:12 | Urawa (Nilwala Ganga) | 1.59 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-09-20 13:02:43 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:02:37 | Hanwella (Kelani Ganga) | 4.14 | 🟢 Normal | 0.652 | 🔺 Rising |
| 2026-09-20 13:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.47 | 🟡 Alert | 0.102 | 🔺 Rising |
| 2026-09-20 13:02:26 | Peradeniya (Mahaweli Ganga) | 6.62 | 🟡 Alert | 0.590 | 🔺 Rising |
| 2026-09-20 13:02:22 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:02:20 | Panadugama (Nilwala Ganga) | 5.32 | 🟡 Alert | 0.233 | 🔺 Rising |
| 2026-09-20 13:02:14 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-09-20 13:02:13 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 13:01:51 | Norwood (Kelani Ganga) | 2.20 | 🟡 Alert | -0.131 |  |
| 2026-09-20 13:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:01:37 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:01:33 | Thanthirimale (Malwathu Oya) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 13:01:30 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | -0.219 |  |
| 2026-09-20 13:00:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:00:43 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:59:56 | Pitabeddara (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.122 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 13:02:26 | Peradeniya (Mahaweli Ganga) | 6.62 | 🟡 Alert | 0.590 | 🔺 Rising |
| 2026-09-20 13:05:11 | Holombuwa (Kelani Ganga) | 3.14 | 🟡 Alert | 0.323 | 🔺 Rising |
| 2026-09-20 13:02:20 | Panadugama (Nilwala Ganga) | 5.32 | 🟡 Alert | 0.233 | 🔺 Rising |
| 2026-09-20 13:04:36 | Rathnapura (Kalu Ganga) | 6.78 | 🟡 Alert | 0.188 | 🔺 Rising |
| 2026-09-20 13:05:12 | Thawalama (Gin Ganga) | 4.98 | 🟡 Alert | 0.149 | 🔺 Rising |
| 2026-09-20 13:02:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.47 | 🟡 Alert | 0.102 | 🔺 Rising |
| 2026-09-20 13:03:45 | Magura (Kalu Ganga) | 5.09 | 🟡 Alert | 0.066 | 🔺 Rising |
| 2026-09-20 13:01:51 | Norwood (Kelani Ganga) | 2.20 | 🟡 Alert | -0.131 |  |
| 2026-09-20 13:03:44 | Nawalapitiya (Mahaweli Ganga) | 4.80 | 🟡 Alert | -0.540 |  |
| 2026-09-20 13:02:37 | Hanwella (Kelani Ganga) | 4.14 | 🟢 Normal | 0.652 | 🔺 Rising |
| 2026-09-20 13:04:55 | Glencourse (Kelani Ganga) | 14.75 | 🟢 Normal | 0.453 | 🔺 Rising |
| 2026-09-20 13:18:35 | Galgamuwa (Mee Oya) | 0.36 | 🟢 Normal | 0.314 | 🔺 Rising |
| 2026-09-20 13:02:14 | Ellagawa (Kalu Ganga) | 7.56 | 🟢 Normal | 0.240 | 🔺 Rising |
| 2026-09-20 13:03:54 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | 0.149 | 🔺 Rising |
| 2026-09-20 13:04:23 | Dunamale (Aththanagalu Oya) | 2.42 | 🟢 Normal | 0.136 | 🔺 Rising |
| 2026-09-20 13:03:12 | Urawa (Nilwala Ganga) | 1.59 | 🟢 Normal | 0.124 | 🔺 Rising |
| 2026-09-20 12:59:56 | Pitabeddara (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-09-20 13:03:51 | Thalgahagoda (Nilwala Ganga) | 0.76 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-09-20 13:04:39 | Putupaula (Kalu Ganga) | 1.56 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-20 13:06:24 | Baddegama (Gin Ganga) | 3.15 | 🟢 Normal | 0.088 | 🔺 Rising |
| 2026-09-20 13:03:14 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-09-20 13:02:13 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 13:01:33 | Thanthirimale (Malwathu Oya) | 0.57 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 13:04:44 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 13:03:21 | Badalgama (Maha Oya) | 1.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 13:00:43 | Weraganthota (Mahaweli Ganga) | -2.93 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:02:43 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:00:45 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:06:36 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.000 |  |
| 2026-09-20 12:09:48 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:07:31 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:03:59 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:04:43 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:06:22 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:01:37 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:02:22 | Thanamalwila (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-20 13:01:30 | Kithulgala (Kelani Ganga) | 2.98 | 🟢 Normal | -0.219 |  |
| 2026-09-20 13:03:30 | Deraniyagala (Kelani Ganga) | 4.60 | 🟢 Normal | -0.229 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)