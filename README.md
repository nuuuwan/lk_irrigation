# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--21_09:15:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **266,815 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Baddegama — Alert; 🟡 Thalgahagoda — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 09:15:55 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.037 |  |
| 2026-09-21 09:10:02 | Rathnapura (Kalu Ganga) | 5.80 | 🟡 Alert | -0.064 |  |
| 2026-09-21 09:09:30 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.035 |  |
| 2026-09-21 09:09:05 | Magura (Kalu Ganga) | 5.57 | 🟡 Alert | -0.036 |  |
| 2026-09-21 09:08:45 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | -0.019 |  |
| 2026-09-21 09:06:57 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:06:33 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-21 09:06:30 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:06:22 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 09:05:45 | Badalgama (Maha Oya) | 3.77 | 🟢 Normal | -0.062 |  |
| 2026-09-21 09:05:27 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-21 09:05:08 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-09-21 09:05:04 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:05:01 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.028 |  |
| 2026-09-21 09:04:56 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-09-21 09:04:52 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-21 09:04:41 | Glencourse (Kelani Ganga) | 13.94 | 🟢 Normal | -0.238 |  |
| 2026-09-21 09:04:32 | Panadugama (Nilwala Ganga) | 5.85 | 🟡 Alert | -0.043 |  |
| 2026-09-21 09:04:06 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-21 09:04:02 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | -0.096 |  |
| 2026-09-21 09:03:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:03:27 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-21 09:03:24 | Deraniyagala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-09-21 09:03:23 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-09-21 09:02:58 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 09:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.73 | 🟠 Minor Flood | 0.061 | 🔺 Rising |
| 2026-09-21 09:02:33 | Baddegama (Gin Ganga) | 3.91 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-21 09:02:32 | Hanwella (Kelani Ganga) | 6.54 | 🟢 Normal | -0.103 |  |
| 2026-09-21 09:02:26 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:02:25 | Thawalama (Gin Ganga) | 3.66 | 🟢 Normal | -0.286 |  |
| 2026-09-21 09:02:11 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.122 |  |
| 2026-09-21 09:01:58 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.040 |  |
| 2026-09-21 09:01:50 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:01:44 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-21 09:01:16 | Nagalagam Street (Kelani Ganga) | 1.11 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-21 09:01:15 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:00:32 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-21 09:00:13 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:00:09 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-21 09:02:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.73 | 🟠 Minor Flood | 0.061 | 🔺 Rising |
| 2026-09-21 09:02:33 | Baddegama (Gin Ganga) | 3.91 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-09-21 09:06:33 | Thalgahagoda (Nilwala Ganga) | 1.45 | 🟡 Alert | 0.020 | 🔺 Rising |
| 2026-09-21 09:08:45 | Dunamale (Aththanagalu Oya) | 3.30 | 🟡 Alert | -0.019 |  |
| 2026-09-21 09:09:05 | Magura (Kalu Ganga) | 5.57 | 🟡 Alert | -0.036 |  |
| 2026-09-21 09:04:32 | Panadugama (Nilwala Ganga) | 5.85 | 🟡 Alert | -0.043 |  |
| 2026-09-21 09:10:02 | Rathnapura (Kalu Ganga) | 5.80 | 🟡 Alert | -0.064 |  |
| 2026-09-21 09:04:52 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-09-21 09:01:44 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-21 09:04:06 | Putupaula (Kalu Ganga) | 2.53 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-09-21 09:02:58 | Ellagawa (Kalu Ganga) | 8.91 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-09-21 09:01:16 | Nagalagam Street (Kelani Ganga) | 1.11 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-21 09:06:22 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-21 09:05:27 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-09-21 09:01:50 | Weraganthota (Mahaweli Ganga) | -2.84 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:01:15 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:06:57 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:00:13 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:02:26 | Horowpothana (Yan Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:05:04 | Galgamuwa (Mee Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:03:46 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:06:30 | Thanamalwila (Kirindi Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-09-21 09:03:24 | Deraniyagala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-09-21 09:00:32 | Kuda Oya (Kirindi Oya) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-09-21 09:03:27 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-09-21 09:00:09 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | -0.011 |  |
| 2026-09-21 09:05:08 | Holombuwa (Kelani Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-09-21 09:03:23 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | -0.020 |  |
| 2026-09-21 09:04:56 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | -0.021 |  |
| 2026-09-21 09:05:01 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.028 |  |
| 2026-09-21 09:09:30 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | -0.035 |  |
| 2026-09-21 09:15:55 | Urawa (Nilwala Ganga) | 0.71 | 🟢 Normal | -0.037 |  |
| 2026-09-21 09:01:58 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.040 |  |
| 2026-09-21 09:05:45 | Badalgama (Maha Oya) | 3.77 | 🟢 Normal | -0.062 |  |
| 2026-09-21 09:04:02 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | -0.096 |  |
| 2026-09-21 09:02:32 | Hanwella (Kelani Ganga) | 6.54 | 🟢 Normal | -0.103 |  |
| 2026-09-21 09:02:11 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | -0.122 |  |
| 2026-09-21 09:04:41 | Glencourse (Kelani Ganga) | 13.94 | 🟢 Normal | -0.238 |  |
| 2026-09-21 09:02:25 | Thawalama (Gin Ganga) | 3.66 | 🟢 Normal | -0.286 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)