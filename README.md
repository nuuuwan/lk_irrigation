# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_08:09:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **299,192 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Baddegama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 08:09:54 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-27 08:08:36 | Galgamuwa (Mee Oya) | 4.10 | 🟢 Normal | -0.121 |  |
| 2026-10-27 08:08:09 | Holombuwa (Kelani Ganga) | 1.90 | 🟢 Normal | -0.099 |  |
| 2026-10-27 08:07:42 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | -0.102 |  |
| 2026-10-27 08:07:27 | Glencourse (Kelani Ganga) | 13.80 | 🟢 Normal | -0.225 |  |
| 2026-10-27 08:06:58 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.147 |  |
| 2026-10-27 08:06:48 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.126 |  |
| 2026-10-27 08:06:46 | Moragaswewa (Deduru Oya) | 5.25 | 🟡 Alert | -0.030 |  |
| 2026-10-27 08:05:37 | Thanthirimale (Malwathu Oya) | 3.05 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-27 08:05:21 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 08:05:19 | Ellagawa (Kalu Ganga) | 9.86 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-27 08:04:51 | Norwood (Kelani Ganga) | 1.52 | 🟡 Alert | -0.030 |  |
| 2026-10-27 08:04:46 | Baddegama (Gin Ganga) | 3.89 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-10-27 08:04:32 | Badalgama (Maha Oya) | 5.55 | 🟡 Alert | -0.145 |  |
| 2026-10-27 08:04:11 | Thawalama (Gin Ganga) | 4.71 | 🟡 Alert | -0.148 |  |
| 2026-10-27 08:03:55 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-27 08:03:54 | Rathnapura (Kalu Ganga) | 8.60 | 🟠 Minor Flood | -0.022 |  |
| 2026-10-27 08:03:24 | Hanwella (Kelani Ganga) | 6.56 | 🟢 Normal | -0.071 |  |
| 2026-10-27 08:03:04 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-27 08:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.31 | 🟠 Minor Flood | 0.110 | 🔺 Rising |
| 2026-10-27 08:02:36 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-10-27 08:02:35 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.039 |  |
| 2026-10-27 08:02:34 | Dunamale (Aththanagalu Oya) | 4.79 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 08:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.031 |  |
| 2026-10-27 08:02:15 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-27 08:02:12 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-27 08:02:11 | Putupaula (Kalu Ganga) | 3.22 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-10-27 08:02:08 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-10-27 08:01:46 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 08:01:37 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-27 08:01:27 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 08:01:22 | Panadugama (Nilwala Ganga) | 6.45 | 🟠 Minor Flood | -0.032 |  |
| 2026-10-27 08:01:02 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-10-27 08:00:32 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-10-27 08:00:26 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 08:00:18 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.450 |  |
| 2026-10-27 08:00:15 | Nagalagam Street (Kelani Ganga) | 1.05 | 🟢 Normal | -0.048 |  |
| 2026-10-27 08:00:10 | Magura (Kalu Ganga) | 5.32 | 🟡 Alert | 0.000 |  |
| 2026-10-27 07:39:02 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 08:03:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.31 | 🟠 Minor Flood | 0.110 | 🔺 Rising |
| 2026-10-27 08:02:34 | Dunamale (Aththanagalu Oya) | 4.79 | 🟠 Minor Flood | 0.020 | 🔺 Rising |
| 2026-10-27 08:03:54 | Rathnapura (Kalu Ganga) | 8.60 | 🟠 Minor Flood | -0.022 |  |
| 2026-10-27 08:01:22 | Panadugama (Nilwala Ganga) | 6.45 | 🟠 Minor Flood | -0.032 |  |
| 2026-10-27 08:04:46 | Baddegama (Gin Ganga) | 3.89 | 🟡 Alert | 0.023 | 🔺 Rising |
| 2026-10-27 08:02:11 | Putupaula (Kalu Ganga) | 3.22 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-10-27 08:00:10 | Magura (Kalu Ganga) | 5.32 | 🟡 Alert | 0.000 |  |
| 2026-10-27 08:05:21 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-10-27 08:04:51 | Norwood (Kelani Ganga) | 1.52 | 🟡 Alert | -0.030 |  |
| 2026-10-27 08:06:46 | Moragaswewa (Deduru Oya) | 5.25 | 🟡 Alert | -0.030 |  |
| 2026-10-27 08:04:32 | Badalgama (Maha Oya) | 5.55 | 🟡 Alert | -0.145 |  |
| 2026-10-27 08:04:11 | Thawalama (Gin Ganga) | 4.71 | 🟡 Alert | -0.148 |  |
| 2026-10-27 08:01:02 | Horowpothana (Yan Oya) | 2.76 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-10-27 08:01:37 | Kithulgala (Kelani Ganga) | 2.45 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-27 08:02:15 | Thanamalwila (Kirindi Oya) | 1.35 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-27 08:05:37 | Thanthirimale (Malwathu Oya) | 3.05 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-27 08:05:19 | Ellagawa (Kalu Ganga) | 9.86 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-27 08:01:46 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-10-27 08:00:26 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 08:01:27 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 08:02:12 | Manampitiya (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-27 08:09:54 | Kuda Oya (Kirindi Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-27 08:03:04 | Thaldena (Mahaweli Ganga) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-10-27 08:02:08 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | -0.010 |  |
| 2026-10-27 08:00:32 | Nakkala (Kumbukkan Oya) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-10-27 07:16:04 | Urawa (Nilwala Ganga) | 1.88 | 🟢 Normal | -0.018 |  |
| 2026-10-27 08:02:36 | Deraniyagala (Kelani Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2026-10-27 08:02:20 | Nawalapitiya (Mahaweli Ganga) | 1.83 | 🟢 Normal | -0.031 |  |
| 2026-10-27 08:02:35 | Yaka Wewa (Ma Oya) | 0.78 | 🟢 Normal | -0.039 |  |
| 2026-10-27 08:00:15 | Nagalagam Street (Kelani Ganga) | 1.05 | 🟢 Normal | -0.048 |  |
| 2026-10-27 08:03:24 | Hanwella (Kelani Ganga) | 6.56 | 🟢 Normal | -0.071 |  |
| 2026-10-27 08:08:09 | Holombuwa (Kelani Ganga) | 1.90 | 🟢 Normal | -0.099 |  |
| 2026-10-27 08:07:42 | Peradeniya (Mahaweli Ganga) | 3.64 | 🟢 Normal | -0.102 |  |
| 2026-10-27 08:08:36 | Galgamuwa (Mee Oya) | 4.10 | 🟢 Normal | -0.121 |  |
| 2026-10-27 08:06:48 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.126 |  |
| 2026-10-27 08:06:58 | Pitabeddara (Nilwala Ganga) | 3.10 | 🟢 Normal | -0.147 |  |
| 2026-10-27 07:05:39 | Giriulla (Maha Oya) | 4.22 | 🟢 Normal | -0.192 |  |
| 2026-10-27 08:07:27 | Glencourse (Kelani Ganga) | 13.80 | 🟢 Normal | -0.225 |  |
| 2026-10-27 08:00:18 | Moraketiya (Walawe Ganga) | 1.90 | 🟢 Normal | -0.450 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)