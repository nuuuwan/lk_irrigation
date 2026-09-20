# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--20_18:34:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,265 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Panadugama — Alert; 🟡 Magura — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Thawalama — Alert; 🟡 Baddegama — Alert; 🟡 Glencourse — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 18:34:53 | Norwood (Kelani Ganga) | 1.97 | 🟡 Alert | -1.868 |  |
| 2026-09-20 18:12:05 | Holombuwa (Kelani Ganga) | 2.65 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-09-20 18:11:11 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.009 |  |
| 2026-09-20 18:10:31 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-20 18:05:37 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:05:29 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-09-20 18:05:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:05:08 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | 0.086 | 🔺 Rising |
| 2026-09-20 18:05:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:04:41 | Urawa (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.050 |  |
| 2026-09-20 18:04:36 | Baddegama (Gin Ganga) | 3.50 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-09-20 18:04:34 | Pitabeddara (Nilwala Ganga) | 3.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-20 18:04:16 | Deraniyagala (Kelani Ganga) | 3.61 | 🟢 Normal | -0.171 |  |
| 2026-09-20 18:04:13 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-09-20 18:04:01 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:03:45 | Glencourse (Kelani Ganga) | 15.53 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-09-20 18:03:21 | Rathnapura (Kalu Ganga) | 6.75 | 🟡 Alert | -0.055 |  |
| 2026-09-20 18:03:19 | Hanwella (Kelani Ganga) | 6.04 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-09-20 18:03:10 | Kithulgala (Kelani Ganga) | 2.95 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-20 18:03:01 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 18:02:59 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-20 18:02:49 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:02:46 | Norwood (Kelani Ganga) | 2.97 | 🟡 Alert | -1.868 |  |
| 2026-09-20 18:02:37 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:02:16 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:02:11 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 18:02:11 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:02:05 | Thawalama (Gin Ganga) | 5.39 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-09-20 18:01:57 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 18:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-09-20 18:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:01:33 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | 0.666 | 🔺 Rising |
| 2026-09-20 18:01:26 | Ellagawa (Kalu Ganga) | 8.20 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-09-20 18:01:22 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-09-20 18:01:16 | Peradeniya (Mahaweli Ganga) | 6.20 | 🟡 Alert | -0.364 |  |
| 2026-09-20 18:00:50 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:00:34 | Magura (Kalu Ganga) | 5.46 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-09-20 18:00:17 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-20 18:00:09 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | 0.054 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-20 18:05:08 | Panadugama (Nilwala Ganga) | 5.95 | 🟡 Alert | 0.086 | 🔺 Rising |
| 2026-09-20 18:00:34 | Magura (Kalu Ganga) | 5.46 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-09-20 18:01:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | 0.063 | 🔺 Rising |
| 2026-09-20 18:02:05 | Thawalama (Gin Ganga) | 5.39 | 🟡 Alert | 0.049 | 🔺 Rising |
| 2026-09-20 18:04:36 | Baddegama (Gin Ganga) | 3.50 | 🟡 Alert | 0.042 | 🔺 Rising |
| 2026-09-20 18:03:45 | Glencourse (Kelani Ganga) | 15.53 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-09-20 18:03:21 | Rathnapura (Kalu Ganga) | 6.75 | 🟡 Alert | -0.055 |  |
| 2026-09-20 18:01:16 | Peradeniya (Mahaweli Ganga) | 6.20 | 🟡 Alert | -0.364 |  |
| 2026-09-20 18:34:53 | Norwood (Kelani Ganga) | 1.97 | 🟡 Alert | -1.868 |  |
| 2026-09-20 18:01:33 | Giriulla (Maha Oya) | 3.10 | 🟢 Normal | 0.666 | 🔺 Rising |
| 2026-09-20 18:03:19 | Hanwella (Kelani Ganga) | 6.04 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-09-20 18:05:29 | Thaldena (Mahaweli Ganga) | 0.47 | 🟢 Normal | 0.159 | 🔺 Rising |
| 2026-09-20 18:04:13 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-09-20 18:02:59 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-09-20 18:12:05 | Holombuwa (Kelani Ganga) | 2.65 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-09-20 18:01:26 | Ellagawa (Kalu Ganga) | 8.20 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-09-20 18:10:31 | Dunamale (Aththanagalu Oya) | 3.00 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-09-20 18:03:10 | Kithulgala (Kelani Ganga) | 2.95 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-09-20 18:00:09 | Putupaula (Kalu Ganga) | 2.03 | 🟢 Normal | 0.054 | 🔺 Rising |
| 2026-09-20 18:03:01 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-20 18:01:57 | Kuda Oya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-20 18:04:34 | Pitabeddara (Nilwala Ganga) | 3.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-09-20 18:02:11 | Thanthirimale (Malwathu Oya) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-20 18:02:49 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:00:50 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:02:37 | Moragaswewa (Deduru Oya) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:01:45 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:05:37 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:05:10 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:04:01 | Moraketiya (Walawe Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:02:11 | Siyambalanduwa (Heda Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:05:07 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:02:16 | Thanamalwila (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-09-20 18:11:11 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | -0.009 |  |
| 2026-09-20 18:01:22 | Horowpothana (Yan Oya) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-09-20 18:00:17 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.010 |  |
| 2026-09-20 17:03:47 | Nawalapitiya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.048 |  |
| 2026-09-20 18:04:41 | Urawa (Nilwala Ganga) | 1.67 | 🟢 Normal | -0.050 |  |
| 2026-09-20 18:04:16 | Deraniyagala (Kelani Ganga) | 3.61 | 🟢 Normal | -0.171 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)