# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--29_02:03:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,755 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Panadugama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Ellagawa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **15** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
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
| 2026-10-29 01:34:43 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 01:33:09 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-29 01:19:59 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.008 |  |
| 2026-10-29 01:16:39 | Panadugama (Nilwala Ganga) | 6.09 | 🟠 Minor Flood | -0.025 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-29 01:34:43 | Thalgahagoda (Nilwala Ganga) | 1.85 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-29 01:08:16 | Baddegama (Gin Ganga) | 4.21 | 🟠 Minor Flood | -0.009 |  |
| 2026-10-29 01:16:39 | Panadugama (Nilwala Ganga) | 6.09 | 🟠 Minor Flood | -0.025 |  |
| 2026-10-29 00:22:31 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.63 | 🟠 Minor Flood | -1.200 |  |
| 2026-10-29 02:02:08 | Ellagawa (Kalu Ganga) | 10.25 | 🟡 Alert | 0.000 |  |
| 2026-10-29 01:52:41 | Putupaula (Kalu Ganga) | 3.74 | 🟡 Alert | 0.000 |  |
| 2026-10-29 02:00:41 | Magura (Kalu Ganga) | 4.10 | 🟡 Alert | -0.041 |  |
| 2026-10-29 01:05:01 | Rathnapura (Kalu Ganga) | 5.46 | 🟡 Alert | -0.075 |  |
| 2026-10-29 01:02:36 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 78.828 | 🔺 Rising |
| 2026-10-29 01:05:27 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-10-29 01:08:15 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.143 | 🔺 Rising |
| 2026-10-28 18:01:08 | Weraganthota (Mahaweli Ganga) | -2.60 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-10-29 01:01:36 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-29 01:02:38 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 18:08:56 | Galgamuwa (Mee Oya) | 2.36 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-29 02:03:10 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-29 01:03:51 | Norwood (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 01:33:09 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-29 02:01:06 | Padiyathalawa (Maduru Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-29 01:02:16 | Glencourse (Kelani Ganga) | 11.60 | 🟢 Normal | 0.000 |  |
| 2026-10-29 01:05:21 | Badalgama (Maha Oya) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-29 01:08:06 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-29 01:03:49 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-10-29 01:02:43 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.005 |  |
| 2026-10-29 01:19:59 | Thaldena (Mahaweli Ganga) | 0.27 | 🟢 Normal | -0.008 |  |
| 2026-10-29 01:05:12 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.010 |  |
| 2026-10-29 02:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-10-29 01:01:22 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | -0.010 |  |
| 2026-10-29 01:07:48 | Horowpothana (Yan Oya) | 2.22 | 🟢 Normal | -0.018 |  |
| 2026-10-29 01:06:10 | Pitabeddara (Nilwala Ganga) | 2.80 | 🟢 Normal | -0.028 |  |
| 2026-10-29 02:02:23 | Hanwella (Kelani Ganga) | 4.07 | 🟢 Normal | -0.036 |  |
| 2026-10-29 02:02:26 | Giriulla (Maha Oya) | 1.98 | 🟢 Normal | -0.050 |  |
| 2026-10-29 01:03:33 | Dunamale (Aththanagalu Oya) | 2.76 | 🟢 Normal | -0.054 |  |
| 2026-10-28 18:02:07 | Thanthirimale (Malwathu Oya) | 1.82 | 🟢 Normal | -0.059 |  |
| 2026-10-29 02:03:22 | Thawalama (Gin Ganga) | 2.95 | 🟢 Normal | -0.061 |  |
| 2026-10-29 02:01:21 | Peradeniya (Mahaweli Ganga) | 2.81 | 🟢 Normal | -0.069 |  |
| 2026-10-29 01:03:43 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.101 |  |
| 2026-10-29 02:01:52 | Moragaswewa (Deduru Oya) | 2.14 | 🟢 Normal | -0.170 |  |
| 2026-10-29 01:06:38 | Urawa (Nilwala Ganga) | 1.00 | 🟢 Normal | -0.354 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)