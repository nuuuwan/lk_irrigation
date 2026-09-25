# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--25_14:07:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **270,633 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Magura — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 14:07:48 | Nawalapitiya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.042 |  |
| 2026-09-25 14:07:20 | Panadugama (Nilwala Ganga) | 6.46 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-25 14:07:19 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:07:14 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.118 |  |
| 2026-09-25 14:06:44 | Rathnapura (Kalu Ganga) | 6.19 | 🟡 Alert | -0.050 |  |
| 2026-09-25 14:06:25 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-09-25 14:06:23 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:05:53 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.050 |  |
| 2026-09-25 14:05:12 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:04:57 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.039 |  |
| 2026-09-25 14:03:52 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.088 |  |
| 2026-09-25 14:03:44 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:03:43 | Dunamale (Aththanagalu Oya) | 2.89 | 🟢 Normal | -0.039 |  |
| 2026-09-25 14:03:37 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:03:16 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:03:09 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.052 |  |
| 2026-09-25 14:03:08 | Baddegama (Gin Ganga) | 4.71 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 14:03:01 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:03:01 | Nagalagam Street (Kelani Ganga) | 1.17 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-25 14:02:56 | Ellagawa (Kalu Ganga) | 8.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 14:02:55 | Glencourse (Kelani Ganga) | 13.97 | 🟢 Normal | -0.143 |  |
| 2026-09-25 14:02:31 | Hanwella (Kelani Ganga) | 6.18 | 🟢 Normal | -0.044 |  |
| 2026-09-25 14:02:26 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:02:23 | Putupaula (Kalu Ganga) | 2.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 14:02:19 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-09-25 14:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 14:02:13 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:02:13 | Kithulgala (Kelani Ganga) | 2.77 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-25 14:02:12 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:02:11 | Deraniyagala (Kelani Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2026-09-25 14:02:07 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-25 14:01:52 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.030 |  |
| 2026-09-25 14:01:49 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:01:01 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 13:30:55 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-25 14:03:08 | Baddegama (Gin Ganga) | 4.71 | 🟠 Minor Flood | 0.010 | 🔺 Rising |
| 2026-09-25 14:01:01 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 14:02:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.02 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-25 14:07:20 | Panadugama (Nilwala Ganga) | 6.46 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-25 13:08:05 | Magura (Kalu Ganga) | 4.81 | 🟡 Alert | 0.000 |  |
| 2026-09-25 14:06:44 | Rathnapura (Kalu Ganga) | 6.19 | 🟡 Alert | -0.050 |  |
| 2026-09-25 13:10:57 | Thawalama (Gin Ganga) | 4.09 | 🟡 Alert | -0.186 |  |
| 2026-09-25 14:02:13 | Kithulgala (Kelani Ganga) | 2.77 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-09-25 14:03:01 | Nagalagam Street (Kelani Ganga) | 1.17 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-25 14:02:23 | Putupaula (Kalu Ganga) | 2.79 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 14:02:56 | Ellagawa (Kalu Ganga) | 8.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-25 14:03:37 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:01:49 | Moragaswewa (Deduru Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:01:20 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:19:53 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-09-25 13:03:23 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:02:13 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:03:16 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:03:44 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:07:19 | Badalgama (Maha Oya) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:03:01 | Manampitiya (Mahaweli Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:02:12 | Thanthirimale (Malwathu Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:05:12 | Kuda Oya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:02:26 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-25 14:06:25 | Giriulla (Maha Oya) | 1.94 | 🟢 Normal | -0.010 |  |
| 2026-09-25 14:02:19 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | -0.010 |  |
| 2026-09-25 14:02:07 | Wellawaya (Kirindi Oya) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-09-25 13:02:24 | Pitabeddara (Nilwala Ganga) | 2.48 | 🟢 Normal | -0.011 |  |
| 2026-09-25 14:02:11 | Deraniyagala (Kelani Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2026-09-25 14:01:52 | Weraganthota (Mahaweli Ganga) | -2.70 | 🟢 Normal | -0.030 |  |
| 2026-09-25 14:03:43 | Dunamale (Aththanagalu Oya) | 2.89 | 🟢 Normal | -0.039 |  |
| 2026-09-25 14:04:57 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | -0.039 |  |
| 2026-09-25 14:07:48 | Nawalapitiya (Mahaweli Ganga) | 2.66 | 🟢 Normal | -0.042 |  |
| 2026-09-25 14:02:31 | Hanwella (Kelani Ganga) | 6.18 | 🟢 Normal | -0.044 |  |
| 2026-09-25 14:05:53 | Urawa (Nilwala Ganga) | 1.42 | 🟢 Normal | -0.050 |  |
| 2026-09-25 14:03:09 | Holombuwa (Kelani Ganga) | 1.30 | 🟢 Normal | -0.052 |  |
| 2026-09-25 14:03:52 | Norwood (Kelani Ganga) | 1.40 | 🟢 Normal | -0.088 |  |
| 2026-09-25 14:07:14 | Peradeniya (Mahaweli Ganga) | 3.98 | 🟢 Normal | -0.118 |  |
| 2026-09-25 14:02:55 | Glencourse (Kelani Ganga) | 13.97 | 🟢 Normal | -0.143 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)