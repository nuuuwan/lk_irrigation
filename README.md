# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--30_06:08:45-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **301,823 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Baddegama — Alert; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 06:08:45 | Panadugama (Nilwala Ganga) | 5.63 | 🟡 Alert | -0.055 |  |
| 2026-10-30 06:08:21 | Pitabeddara (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.073 |  |
| 2026-10-30 06:07:48 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.019 |  |
| 2026-10-30 06:07:11 | Ellagawa (Kalu Ganga) | 9.17 | 🟢 Normal | -0.032 |  |
| 2026-10-30 06:06:39 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | -0.030 |  |
| 2026-10-30 06:06:36 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:06:24 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.115 |  |
| 2026-10-30 06:06:13 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:05:56 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-30 06:05:45 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-10-30 06:05:07 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | -0.055 |  |
| 2026-10-30 06:04:54 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 06:04:41 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-10-30 06:04:40 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.026 |  |
| 2026-10-30 06:04:37 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:04:05 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.067 |  |
| 2026-10-30 06:03:49 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:03:41 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 06:03:02 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-10-30 06:02:57 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.025 |  |
| 2026-10-30 06:02:48 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.013 |  |
| 2026-10-30 06:02:31 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.022 |  |
| 2026-10-30 06:02:24 | Rathnapura (Kalu Ganga) | 3.48 | 🟢 Normal | -0.074 |  |
| 2026-10-30 06:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | -0.012 |  |
| 2026-10-30 06:02:04 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:01:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:01:36 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.127 |  |
| 2026-10-30 06:01:35 | Putupaula (Kalu Ganga) | 3.49 | 🟡 Alert | -0.076 |  |
| 2026-10-30 06:01:27 | Dunamale (Aththanagalu Oya) | 2.09 | 🟢 Normal | -0.044 |  |
| 2026-10-30 06:01:19 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.052 |  |
| 2026-10-30 06:01:08 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | -0.010 |  |
| 2026-10-30 06:00:57 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.052 |  |
| 2026-10-30 06:00:55 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-10-30 06:00:27 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.025 |  |
| 2026-10-30 05:43:15 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.055 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-30 06:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | -0.012 |  |
| 2026-10-30 05:15:41 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | -0.016 |  |
| 2026-10-30 06:06:39 | Baddegama (Gin Ganga) | 3.60 | 🟡 Alert | -0.030 |  |
| 2026-10-30 06:08:45 | Panadugama (Nilwala Ganga) | 5.63 | 🟡 Alert | -0.055 |  |
| 2026-10-30 06:01:35 | Putupaula (Kalu Ganga) | 3.49 | 🟡 Alert | -0.076 |  |
| 2026-10-30 06:05:56 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-30 06:04:54 | Holombuwa (Kelani Ganga) | 0.89 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 06:03:41 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-30 06:06:36 | Moragaswewa (Deduru Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:04:08 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:01:54 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:06:13 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:04:37 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:02:04 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:03:49 | Katharagama (Menik Ganga) | -0.20 | 🟢 Normal | 0.000 |  |
| 2026-10-30 06:04:41 | Nakkala (Kumbukkan Oya) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-10-30 06:05:45 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -0.010 |  |
| 2026-10-29 18:06:21 | Galgamuwa (Mee Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-10-30 06:01:08 | Hanwella (Kelani Ganga) | 3.21 | 🟢 Normal | -0.010 |  |
| 2026-10-30 06:00:55 | Moraketiya (Walawe Ganga) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-10-30 06:02:48 | Wellawaya (Kirindi Oya) | 1.15 | 🟢 Normal | -0.013 |  |
| 2026-10-30 06:07:48 | Badalgama (Maha Oya) | 2.93 | 🟢 Normal | -0.019 |  |
| 2026-10-30 05:02:47 | Horowpothana (Yan Oya) | 2.11 | 🟢 Normal | -0.020 |  |
| 2026-10-30 06:03:02 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-10-30 06:02:31 | Giriulla (Maha Oya) | 1.58 | 🟢 Normal | -0.022 |  |
| 2026-10-30 06:00:27 | Weraganthota (Mahaweli Ganga) | -2.85 | 🟢 Normal | -0.025 |  |
| 2026-10-30 06:02:57 | Thawalama (Gin Ganga) | 2.25 | 🟢 Normal | -0.025 |  |
| 2026-10-30 06:04:40 | Urawa (Nilwala Ganga) | 1.15 | 🟢 Normal | -0.026 |  |
| 2026-10-30 06:07:11 | Ellagawa (Kalu Ganga) | 9.17 | 🟢 Normal | -0.032 |  |
| 2026-10-30 06:01:27 | Dunamale (Aththanagalu Oya) | 2.09 | 🟢 Normal | -0.044 |  |
| 2026-10-30 06:00:57 | Manampitiya (Mahaweli Ganga) | 0.52 | 🟢 Normal | -0.052 |  |
| 2026-10-30 06:01:19 | Glencourse (Kelani Ganga) | 10.90 | 🟢 Normal | -0.052 |  |
| 2026-10-30 06:05:07 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | -0.055 |  |
| 2026-10-29 18:01:49 | Thanthirimale (Malwathu Oya) | 1.44 | 🟢 Normal | -0.059 |  |
| 2026-10-30 06:04:05 | Deraniyagala (Kelani Ganga) | 0.88 | 🟢 Normal | -0.067 |  |
| 2026-10-30 06:08:21 | Pitabeddara (Nilwala Ganga) | 1.93 | 🟢 Normal | -0.073 |  |
| 2026-10-30 06:02:24 | Rathnapura (Kalu Ganga) | 3.48 | 🟢 Normal | -0.074 |  |
| 2026-10-30 06:06:24 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.115 |  |
| 2026-10-30 06:01:36 | Magura (Kalu Ganga) | 2.68 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)