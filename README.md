# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_16:13:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,186 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Glencourse — Alert; 🟡 Thawalama — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Rathnapura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 16:13:55 | Panadugama (Nilwala Ganga) | 5.79 | 🟡 Alert | 0.119 | 🔺 Rising |
| 2026-09-20 16:09:11 | Magura (Kalu Ganga) | 5.36 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-09-20 16:07:45 | Holombuwa (Kelani Ganga) | 2.78 | 🟢 Normal | -0.316 |  |
| 2026-09-20 16:07:00 | Urawa (Nilwala Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:06:13 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-20 16:06:03 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:05:44 | Baddegama (Gin Ganga) | 3.39 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-20 16:05:27 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 16:05:20 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 16:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.72 | 🟡 Alert | 0.082 | 🔺 Rising |
| 2026-09-20 16:04:47 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:04:43 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-20 16:04:30 | Peradeniya (Mahaweli Ganga) | 6.82 | 🟡 Alert | -0.171 |  |
| 2026-09-20 16:04:29 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-09-20 16:04:26 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-20 16:04:20 | Ellagawa (Kalu Ganga) | 8.01 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-20 16:04:16 | Hanwella (Kelani Ganga) | 5.52 | 🟢 Normal | 0.371 | 🔺 Rising |
| 2026-09-20 16:04:15 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-20 16:04:12 | Glencourse (Kelani Ganga) | 15.49 | 🟡 Alert | 0.229 | 🔺 Rising |
| 2026-09-20 16:04:05 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:04:02 | Deraniyagala (Kelani Ganga) | 3.45 | 🟢 Normal | -0.158 |  |
| 2026-09-20 16:03:48 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:03:48 | Norwood (Kelani Ganga) | 2.20 | 🟡 Alert | -0.068 |  |
| 2026-09-20 16:03:39 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-20 16:03:35 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-09-20 16:03:16 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:03:04 | Kithulgala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.214 |  |
| 2026-09-20 16:02:33 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:02:27 | Urawa (Nilwala Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:02:26 | Rathnapura (Kalu Ganga) | 6.85 | 🟡 Alert | -0.011 |  |
| 2026-09-20 16:02:08 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:01:48 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:01:21 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-20 16:01:19 | Nawalapitiya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.254 |  |
| 2026-09-20 16:01:09 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:01:08 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-20 16:00:52 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:00:38 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 16:00:24 | Thawalama (Gin Ganga) | 5.25 | 🟡 Alert | 0.124 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 16:04:12 | Glencourse (Kelani Ganga) | 15.49 | 🟡 Alert | 0.229 | 🔺 Rising |
| 2026-09-20 16:00:24 | Thawalama (Gin Ganga) | 5.25 | 🟡 Alert | 0.124 | 🔺 Rising |
| 2026-09-20 16:13:55 | Panadugama (Nilwala Ganga) | 5.79 | 🟡 Alert | 0.119 | 🔺 Rising |
| 2026-09-20 16:05:03 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.72 | 🟡 Alert | 0.082 | 🔺 Rising |
| 2026-09-20 16:09:11 | Magura (Kalu Ganga) | 5.36 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-09-20 16:02:26 | Rathnapura (Kalu Ganga) | 6.85 | 🟡 Alert | -0.011 |  |
| 2026-09-20 16:03:48 | Norwood (Kelani Ganga) | 2.20 | 🟡 Alert | -0.068 |  |
| 2026-09-20 16:04:30 | Peradeniya (Mahaweli Ganga) | 6.82 | 🟡 Alert | -0.171 |  |
| 2026-09-20 16:04:16 | Hanwella (Kelani Ganga) | 5.52 | 🟢 Normal | 0.371 | 🔺 Rising |
| 2026-09-20 16:03:35 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | 0.269 | 🔺 Rising |
| 2026-09-20 16:04:20 | Ellagawa (Kalu Ganga) | 8.01 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-20 16:04:29 | Dunamale (Aththanagalu Oya) | 2.84 | 🟢 Normal | 0.119 | 🔺 Rising |
| 2026-09-20 16:06:13 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-09-20 16:01:08 | Thalgahagoda (Nilwala Ganga) | 0.98 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-09-20 16:04:43 | Putupaula (Kalu Ganga) | 1.85 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-09-20 16:05:44 | Baddegama (Gin Ganga) | 3.39 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-09-20 16:04:26 | Galgamuwa (Mee Oya) | 0.40 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-20 16:01:21 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-09-20 16:05:27 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-09-20 16:04:15 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-20 16:00:38 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 16:05:20 | Thanthirimale (Malwathu Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 16:02:33 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:00:52 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:04:47 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:01:37 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:06:03 | Horowpothana (Yan Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:03:16 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:01:48 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:03:48 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:04:05 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:07:00 | Urawa (Nilwala Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:01:09 | Kuda Oya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:02:08 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 16:03:39 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-09-20 16:04:02 | Deraniyagala (Kelani Ganga) | 3.45 | 🟢 Normal | -0.158 |  |
| 2026-09-20 16:03:04 | Kithulgala (Kelani Ganga) | 2.43 | 🟢 Normal | -0.214 |  |
| 2026-09-20 16:01:19 | Nawalapitiya (Mahaweli Ganga) | 3.25 | 🟢 Normal | -0.254 |  |
| 2026-09-20 16:07:45 | Holombuwa (Kelani Ganga) | 2.78 | 🟢 Normal | -0.316 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)