# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_02:33:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,772 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟡 Ellagawa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 02:33:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.62 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 02:32:54 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.62 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 02:22:23 | Pitabeddara (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.031 |  |
| 2026-10-29 02:16:27 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.034 |  |
| 2026-10-29 02:11:32 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-29 02:08:31 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-29 02:07:59 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:07:49 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:07:36 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-29 02:07:08 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:06:42 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.029 |  |
| 2026-10-29 02:06:27 | Panadugama (Nilwala Ganga) | 6.06 | 🟠 Minor Flood | -0.036 |  |
| 2026-10-29 02:05:28 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:05:22 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:04:38 | Rathnapura (Kalu Ganga) | 5.39 | 🟡 Alert | -0.070 |  |
| 2026-10-29 02:04:32 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.059 |  |
| 2026-10-29 02:04:00 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.049 |  |
| 2026-10-29 02:03:22 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | -0.061 |  |
| 2026-10-29 02:03:10 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:02:26 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.050 |  |
| 2026-10-29 02:02:23 | Hanwella (Kelani Ganga) | 4.07 | 🟢 Normal | -0.036 |  |
| 2026-10-29 02:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-10-29 02:02:08 | Ellagawa (Kalu Ganga) | 10.25 | 🟡 Alert | 0.000 |  |
| 2026-10-29 02:01:52 | Moragaswewa (Deduru Oya) | 2.14 | 🟢 Normal | -0.170 |  |
| 2026-10-29 02:01:21 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.069 |  |
| 2026-10-29 02:01:06 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:00:41 | Magura (Kalu Ganga) | 4.10 | 🟡 Alert | -0.041 |  |
| 2026-10-29 01:52:41 | Putupaula (Kalu Ganga) | 3.74 | 🟡 Alert | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 01:34:43 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 02:33:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.62 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 01:08:16 | Baddegama (Gin Ganga) | 4.21 | 🟠 Minor Flood | -0.009 |  |
| 2026-10-29 02:06:27 | Panadugama (Nilwala Ganga) | 6.06 | 🟠 Minor Flood | -0.036 |  |
| 2026-10-29 02:02:08 | Ellagawa (Kalu Ganga) | 10.25 | 🟡 Alert | 0.000 |  |
| 2026-10-29 01:52:41 | Putupaula (Kalu Ganga) | 3.74 | 🟡 Alert | 0.000 |  |
| 2026-10-29 02:00:41 | Magura (Kalu Ganga) | 4.10 | 🟡 Alert | -0.041 |  |
| 2026-10-29 02:04:38 | Rathnapura (Kalu Ganga) | 5.39 | 🟡 Alert | -0.070 |  |
| 2026-10-29 01:02:36 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 78.828 | 🔺 Rising |
| 2026-10-29 01:05:27 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-10-29 02:08:31 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-10-28 18:01:08 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-29 02:11:32 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-10-29 01:02:38 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-29 02:07:36 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-28 18:08:56 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-29 02:03:10 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:07:59 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:05:22 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:01:06 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:07:49 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:05:28 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:07:08 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-29 01:03:49 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-10-29 01:07:48 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.018 |  |
| 2026-10-29 02:06:42 | Badalgama (Maha Oya) | 3.31 | 🟢 Normal | -0.029 |  |
| 2026-10-29 02:22:23 | Pitabeddara (Nilwala Ganga) | 2.76 | 🟢 Normal | -0.031 |  |
| 2026-10-29 02:16:27 | Manampitiya (Mahaweli Ganga) | 0.34 | 🟢 Normal | -0.034 |  |
| 2026-10-29 02:02:23 | Hanwella (Kelani Ganga) | 4.07 | 🟢 Normal | -0.036 |  |
| 2026-10-29 02:04:00 | Glencourse (Kelani Ganga) | 11.55 | 🟢 Normal | -0.049 |  |
| 2026-10-29 02:02:26 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.050 |  |
| 2026-10-29 01:03:33 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | -0.054 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-29 02:04:32 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | -0.059 |  |
| 2026-10-29 02:03:22 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | -0.061 |  |
| 2026-10-29 02:01:21 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.069 |  |
| 2026-10-29 02:01:52 | Moragaswewa (Deduru Oya) | 2.14 | 🟢 Normal | -0.170 |  |
| 2026-10-29 01:06:38 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.354 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)