# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_06:16:02-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,924 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Panadugama — Alert; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 06:16:02 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:14:44 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:11:16 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.073 |  |
| 2026-10-29 06:09:09 | Urawa (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.078 |  |
| 2026-10-29 06:07:58 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:07:41 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.095 |  |
| 2026-10-29 06:06:45 | Panadugama (Nilwala Ganga) | 5.94 | 🟡 Alert | 0.000 |  |
| 2026-10-29 06:06:44 | Panadugama (Nilwala Ganga) | 5.94 | 🟡 Alert | 0.000 |  |
| 2026-10-29 06:06:41 | Hanwella (Kelani Ganga) | 3.97 | 🟢 Normal | -0.021 |  |
| 2026-10-29 06:06:33 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | -0.020 |  |
| 2026-10-29 06:06:10 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-29 06:05:40 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.015 |  |
| 2026-10-29 06:05:17 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.019 |  |
| 2026-10-29 06:04:41 | Ellagawa (Kalu Ganga) | 10.17 | 🟡 Alert | -0.030 |  |
| 2026-10-29 06:03:41 | Glencourse (Kelani Ganga) | 11.36 | 🟢 Normal | -0.049 |  |
| 2026-10-29 06:03:33 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-29 06:03:06 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:03:04 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:02:54 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-29 06:02:43 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.033 |  |
| 2026-10-29 06:02:27 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-10-29 06:02:26 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:02:25 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.037 |  |
| 2026-10-29 06:02:21 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.030 |  |
| 2026-10-29 06:02:20 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 06:02:16 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | -0.087 |  |
| 2026-10-29 06:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.52 | 🟠 Minor Flood | -0.038 |  |
| 2026-10-29 06:02:09 | Putupaula (Kalu Ganga) | 3.75 | 🟡 Alert | 0.000 |  |
| 2026-10-29 06:02:01 | Magura (Kalu Ganga) | 3.74 | 🟢 Normal | -0.107 |  |
| 2026-10-29 06:02:01 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:01:40 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:01:17 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-10-29 06:01:06 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-29 06:01:03 | Pitabeddara (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.022 |  |
| 2026-10-29 06:01:03 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-10-29 06:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-10-29 06:00:43 | Rathnapura (Kalu Ganga) | 5.10 | 🟢 Normal | -0.083 |  |
| 2026-10-29 06:00:37 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | -0.146 |  |
| 2026-10-29 06:00:01 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 06:02:20 | Thalgahagoda (Nilwala Ganga) | 1.87 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 06:03:33 | Baddegama (Gin Ganga) | 4.17 | 🟠 Minor Flood | -0.011 |  |
| 2026-10-29 06:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.52 | 🟠 Minor Flood | -0.038 |  |
| 2026-10-29 06:06:45 | Panadugama (Nilwala Ganga) | 5.94 | 🟡 Alert | 0.000 |  |
| 2026-10-29 06:02:09 | Putupaula (Kalu Ganga) | 3.75 | 🟡 Alert | 0.000 |  |
| 2026-10-29 06:04:41 | Ellagawa (Kalu Ganga) | 10.17 | 🟡 Alert | -0.030 |  |
| 2026-10-29 06:06:10 | Peradeniya (Mahaweli Ganga) | 2.87 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-29 06:02:54 | Horowpothana (Yan Oya) | 2.17 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-29 06:01:06 | Weraganthota (Mahaweli Ganga) | -2.40 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-29 06:00:01 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-28 18:08:56 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-29 06:01:40 | Nakkala (Kumbukkan Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:03:04 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:02:26 | Norwood (Kelani Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:03:06 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:02:01 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:16:02 | Holombuwa (Kelani Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:07:58 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-29 06:02:27 | Giriulla (Maha Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-10-29 06:01:02 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | -0.010 |  |
| 2026-10-29 06:01:03 | Wellawaya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.011 |  |
| 2026-10-29 06:05:40 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | -0.015 |  |
| 2026-10-29 06:05:17 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.019 |  |
| 2026-10-29 06:06:33 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | -0.020 |  |
| 2026-10-29 06:06:41 | Hanwella (Kelani Ganga) | 3.97 | 🟢 Normal | -0.021 |  |
| 2026-10-29 06:01:17 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | -0.021 |  |
| 2026-10-29 06:01:03 | Pitabeddara (Nilwala Ganga) | 2.68 | 🟢 Normal | -0.022 |  |
| 2026-10-29 06:02:21 | Manampitiya (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.030 |  |
| 2026-10-29 06:02:43 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.033 |  |
| 2026-10-29 06:02:25 | Thanamalwila (Kirindi Oya) | 1.13 | 🟢 Normal | -0.037 |  |
| 2026-10-29 06:03:41 | Glencourse (Kelani Ganga) | 11.36 | 🟢 Normal | -0.049 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-29 06:11:16 | Dunamale (Aththanagalu Oya) | 2.52 | 🟢 Normal | -0.073 |  |
| 2026-10-29 06:09:09 | Urawa (Nilwala Ganga) | 1.45 | 🟢 Normal | -0.078 |  |
| 2026-10-29 06:00:43 | Rathnapura (Kalu Ganga) | 5.10 | 🟢 Normal | -0.083 |  |
| 2026-10-29 06:02:16 | Thawalama (Gin Ganga) | 2.57 | 🟢 Normal | -0.087 |  |
| 2026-10-29 06:07:41 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.095 |  |
| 2026-10-29 06:02:01 | Magura (Kalu Ganga) | 3.74 | 🟢 Normal | -0.107 |  |
| 2026-10-29 06:00:37 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)