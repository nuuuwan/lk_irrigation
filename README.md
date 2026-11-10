# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_14:03:24-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **312,036 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Dunamale — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 14:03:24 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:03:23 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:03:20 | Glencourse (Kelani Ganga) | 12.16 | 🟢 Normal | -0.194 |  |
| 2026-11-10 14:03:16 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.000 |  |
| 2026-11-10 14:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-10 14:03:13 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | -0.010 |  |
| 2026-11-10 14:03:06 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-10 14:02:58 | Hanwella (Kelani Ganga) | 5.28 | 🟢 Normal | -0.171 |  |
| 2026-11-10 14:02:38 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.022 |  |
| 2026-11-10 14:02:28 | Wellawaya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-10 14:02:27 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-11-10 14:02:26 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-10 14:02:13 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-10 14:02:10 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | -0.093 |  |
| 2026-11-10 14:02:09 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:01:57 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:01:56 | Moragaswewa (Deduru Oya) | 4.18 | 🟢 Normal | -0.020 |  |
| 2026-11-10 14:01:52 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.089 |  |
| 2026-11-10 14:01:46 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-11-10 14:01:38 | Thanamalwila (Kirindi Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:00:38 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 13:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.63 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-11-10 13:03:15 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-11-10 13:05:21 | Dunamale (Aththanagalu Oya) | 4.60 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-10 14:03:16 | Thalgahagoda (Nilwala Ganga) | 1.65 | 🟡 Alert | 0.000 |  |
| 2026-11-10 13:06:04 | Panadugama (Nilwala Ganga) | 5.89 | 🟡 Alert | -0.028 |  |
| 2026-11-10 13:09:45 | Magura (Kalu Ganga) | 4.73 | 🟡 Alert | -0.107 |  |
| 2026-11-10 14:02:28 | Wellawaya (Kirindi Oya) | 1.87 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-10 14:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-10 13:03:27 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-11-10 13:00:10 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-11-10 14:03:06 | Manampitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-11-10 13:01:32 | Kithulgala (Kelani Ganga) | 2.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-11-10 14:02:13 | Putupaula (Kalu Ganga) | 2.58 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-11-10 14:02:09 | Yaka Wewa (Ma Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-11-10 12:02:57 | Galgamuwa (Mee Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46⌛ | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:01:57 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:03:23 | Katharagama (Menik Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:03:24 | Peradeniya (Mahaweli Ganga) | 3.15 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:01:38 | Thanamalwila (Kirindi Oya) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-11-10 14:01:46 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.010 |  |
| 2026-11-10 13:00:28 | Nakkala (Kumbukkan Oya) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-11-10 14:03:13 | Ellagawa (Kalu Ganga) | 8.64 | 🟢 Normal | -0.010 |  |
| 2026-11-10 13:04:37 | Holombuwa (Kelani Ganga) | 1.19 | 🟢 Normal | -0.010 |  |
| 2026-11-10 14:02:26 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-11-10 14:00:38 | Thanthirimale (Malwathu Oya) | 1.93 | 🟢 Normal | -0.011 |  |
| 2026-11-10 13:08:48 | Urawa (Nilwala Ganga) | 1.38 | 🟢 Normal | -0.019 |  |
| 2026-11-10 14:02:27 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-11-10 14:01:56 | Moragaswewa (Deduru Oya) | 4.18 | 🟢 Normal | -0.020 |  |
| 2026-11-10 14:02:38 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.022 |  |
| 2026-11-10 13:08:41 | Moraketiya (Walawe Ganga) | 2.90 | 🟢 Normal | -0.027 |  |
| 2026-11-10 13:12:42 | Giriulla (Maha Oya) | 2.39 | 🟢 Normal | -0.059 |  |
| 2026-11-10 13:09:28 | Rathnapura (Kalu Ganga) | 4.45 | 🟢 Normal | -0.082 |  |
| 2026-11-10 14:01:52 | Weraganthota (Mahaweli Ganga) | -2.52 | 🟢 Normal | -0.089 |  |
| 2026-11-10 14:02:10 | Thawalama (Gin Ganga) | 2.80 | 🟢 Normal | -0.093 |  |
| 2026-11-10 13:05:10 | Badalgama (Maha Oya) | 3.71 | 🟢 Normal | -0.105 |  |
| 2026-11-10 13:03:03 | Pitabeddara (Nilwala Ganga) | 1.90 | 🟢 Normal | -0.149 |  |
| 2026-11-10 14:02:58 | Hanwella (Kelani Ganga) | 5.28 | 🟢 Normal | -0.171 |  |
| 2026-11-10 14:03:20 | Glencourse (Kelani Ganga) | 12.16 | 🟢 Normal | -0.194 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)