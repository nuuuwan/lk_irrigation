# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--08_11:03:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **310,143 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Dunamale — Alert; 🟡 Moraketiya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **19** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 11:03:25 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | -0.061 |  |
| 2026-11-08 11:02:38 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-11-08 11:02:31 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-11-08 11:02:15 | Giriulla (Maha Oya) | 2.77 | 🟢 Normal | -0.092 |  |
| 2026-11-08 11:02:11 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:02:08 | Rathnapura (Kalu Ganga) | 4.56 | 🟢 Normal | -0.181 |  |
| 2026-11-08 11:02:00 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | -0.030 |  |
| 2026-11-08 11:01:57 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-11-08 11:01:56 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.107 |  |
| 2026-11-08 11:01:54 | Moragaswewa (Deduru Oya) | 2.92 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-08 11:01:51 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.150 |  |
| 2026-11-08 11:01:46 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-11-08 11:01:24 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 1.140 | 🔺 Rising |
| 2026-11-08 11:01:19 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:01:15 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-11-08 11:00:58 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 11:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-08 11:00:04 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-11-08 10:23:27 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-08 10:08:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.42 | 🟡 Alert | 0.022 | 🔺 Rising |
| 2026-11-08 10:12:45 | Panadugama (Nilwala Ganga) | 5.98 | 🟡 Alert | -0.035 |  |
| 2026-11-08 10:05:49 | Dunamale (Aththanagalu Oya) | 3.62 | 🟡 Alert | -0.050 |  |
| 2026-11-08 10:09:49 | Moraketiya (Walawe Ganga) | 3.21 | 🟡 Alert | -0.055 |  |
| 2026-11-08 11:01:24 | Manampitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 1.140 | 🔺 Rising |
| 2026-11-08 11:01:57 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-11-08 11:01:54 | Moragaswewa (Deduru Oya) | 2.92 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-11-08 10:05:03 | Ellagawa (Kalu Ganga) | 7.36 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-11-08 11:00:58 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-08 10:06:26 | Baddegama (Gin Ganga) | 3.01 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-11-08 10:18:08 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:00:55 | Horowpothana (Yan Oya) | 2.43 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:01:22 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:02:11 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:04:30 | Putupaula (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-11-08 11:01:19 | Thanthirimale (Malwathu Oya) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:01:05 | Thalgahagoda (Nilwala Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-11-08 10:23:27 | Norwood (Kelani Ganga) | 1.08 | 🟢 Normal | -0.008 |  |
| 2026-11-08 10:08:36 | Galgamuwa (Mee Oya) | 0.82 | 🟢 Normal | -0.009 |  |
| 2026-11-08 11:00:43 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-11-08 11:01:15 | Katharagama (Menik Ganga) | 0.07 | 🟢 Normal | -0.011 |  |
| 2026-11-08 10:02:19 | Hanwella (Kelani Ganga) | 3.15 | 🟢 Normal | -0.020 |  |
| 2026-11-08 11:02:31 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.021 |  |
| 2026-11-08 11:00:04 | Thaldena (Mahaweli Ganga) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-11-08 11:02:38 | Nakkala (Kumbukkan Oya) | 1.18 | 🟢 Normal | -0.030 |  |
| 2026-11-08 11:01:46 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-11-08 11:02:00 | Kuda Oya (Kirindi Oya) | 1.92 | 🟢 Normal | -0.030 |  |
| 2026-11-08 10:07:58 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.037 |  |
| 2026-11-08 10:08:26 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.056 |  |
| 2026-11-08 11:03:25 | Badalgama (Maha Oya) | 4.01 | 🟢 Normal | -0.061 |  |
| 2026-11-08 10:05:24 | Thanamalwila (Kirindi Oya) | 1.95 | 🟢 Normal | -0.063 |  |
| 2026-11-08 10:02:11 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | -0.064 |  |
| 2026-11-08 10:05:22 | Urawa (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.071 |  |
| 2026-11-08 11:02:15 | Giriulla (Maha Oya) | 2.77 | 🟢 Normal | -0.092 |  |
| 2026-11-08 11:01:56 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.107 |  |
| 2026-11-08 10:01:16 | Pitabeddara (Nilwala Ganga) | 3.02 | 🟢 Normal | -0.107 |  |
| 2026-11-08 10:07:36 | Magura (Kalu Ganga) | 3.98 | 🟢 Normal | -0.149 |  |
| 2026-11-08 11:01:51 | Weraganthota (Mahaweli Ganga) | -2.05 | 🟢 Normal | -0.150 |  |
| 2026-11-08 11:02:08 | Rathnapura (Kalu Ganga) | 4.56 | 🟢 Normal | -0.181 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)