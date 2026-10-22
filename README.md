# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--22_19:31:27-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **295,142 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Moragaswewa — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 19:31:27 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:29:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.74 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-22 19:20:32 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.746 |  |
| 2026-10-22 19:20:04 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.016 |  |
| 2026-10-22 19:11:43 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-22 19:11:01 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-22 19:10:50 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:09:25 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-22 19:08:49 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-22 19:08:34 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-10-22 19:07:23 | Holombuwa (Kelani Ganga) | 2.40 | 🟢 Normal | -0.102 |  |
| 2026-10-22 19:07:00 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-22 19:06:05 | Panadugama (Nilwala Ganga) | 4.44 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-22 19:06:04 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:05:39 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-10-22 19:05:12 | Glencourse (Kelani Ganga) | 12.47 | 🟢 Normal | -0.019 |  |
| 2026-10-22 19:04:50 | Rathnapura (Kalu Ganga) | 4.30 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-22 19:04:25 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-22 19:04:06 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-22 19:04:05 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-22 19:03:56 | Pitabeddara (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-22 19:03:54 | Moragaswewa (Deduru Oya) | 4.78 | 🟡 Alert | 0.047 | 🔺 Rising |
| 2026-10-22 19:03:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:03:52 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-22 19:03:44 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:03:06 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-22 19:02:56 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:02:39 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-22 19:02:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:02:10 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:01:57 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-22 19:01:49 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-22 19:01:27 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 19:01:17 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-22 19:00:57 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-22 19:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-10-22 19:00:22 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-22 19:03:54 | Moragaswewa (Deduru Oya) | 4.78 | 🟡 Alert | 0.047 | 🔺 Rising |
| 2026-10-22 19:01:57 | Dunamale (Aththanagalu Oya) | 2.58 | 🟢 Normal | 0.173 | 🔺 Rising |
| 2026-10-22 19:03:56 | Pitabeddara (Nilwala Ganga) | 1.87 | 🟢 Normal | 0.166 | 🔺 Rising |
| 2026-10-22 19:11:43 | Thawalama (Gin Ganga) | 2.59 | 🟢 Normal | 0.117 | 🔺 Rising |
| 2026-10-22 19:09:25 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | 0.106 | 🔺 Rising |
| 2026-10-22 19:04:50 | Rathnapura (Kalu Ganga) | 4.30 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-22 19:01:17 | Magura (Kalu Ganga) | 2.16 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-10-22 19:06:05 | Panadugama (Nilwala Ganga) | 4.44 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-10-22 19:04:05 | Giriulla (Maha Oya) | 2.35 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-22 19:02:39 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-22 19:03:52 | Hanwella (Kelani Ganga) | 4.54 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-22 19:04:25 | Deraniyagala (Kelani Ganga) | 1.34 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-22 19:08:49 | Badalgama (Maha Oya) | 3.55 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-10-22 19:11:01 | Ellagawa (Kalu Ganga) | 7.78 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-22 19:07:00 | Putupaula (Kalu Ganga) | 1.80 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-22 19:29:38 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.74 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-22 19:04:06 | Thaldena (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-22 18:02:23 | Thanthirimale (Malwathu Oya) | 2.18 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-22 18:02:35 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-22 19:01:27 | Norwood (Kelani Ganga) | 1.11 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-22 19:02:10 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:31:27 | Wellawaya (Kirindi Oya) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:06:04 | Baddegama (Gin Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:03:53 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:02:10 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:10:50 | Manampitiya (Mahaweli Ganga) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:03:44 | Kuda Oya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-22 19:08:34 | Thalgahagoda (Nilwala Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-10-22 19:01:49 | Yaka Wewa (Ma Oya) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-10-22 19:03:06 | Siyambalanduwa (Heda Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-22 19:00:57 | Thanamalwila (Kirindi Oya) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-10-22 19:00:22 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-22 19:20:04 | Moraketiya (Walawe Ganga) | 1.10 | 🟢 Normal | -0.016 |  |
| 2026-10-22 19:05:12 | Glencourse (Kelani Ganga) | 12.47 | 🟢 Normal | -0.019 |  |
| 2026-10-22 19:05:39 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.021 |  |
| 2026-10-22 19:00:25 | Nawalapitiya (Mahaweli Ganga) | 1.48 | 🟢 Normal | -0.021 |  |
| 2026-10-22 18:01:15 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.070 |  |
| 2026-10-22 19:07:23 | Holombuwa (Kelani Ganga) | 2.40 | 🟢 Normal | -0.102 |  |
| 2026-10-22 19:20:32 | Horowpothana (Yan Oya) | 2.04 | 🟢 Normal | -0.746 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)