# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--27_02:08:38-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,959 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Dunamale — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟡 Moragaswewa — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 02:08:38 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.060 |  |
| 2026-10-27 02:07:29 | Ellagawa (Kalu Ganga) | 9.70 | 🟢 Normal | 0.000 |  |
| 2026-10-27 02:06:37 | Glencourse (Kelani Ganga) | 15.00 | 🟡 Alert | -0.038 |  |
| 2026-10-27 02:06:20 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.029 |  |
| 2026-10-27 02:06:18 | Dunamale (Aththanagalu Oya) | 4.66 | 🟠 Minor Flood | 0.057 | 🔺 Rising |
| 2026-10-27 02:05:58 | Norwood (Kelani Ganga) | 1.76 | 🟡 Alert | -0.040 |  |
| 2026-10-27 02:05:49 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-10-27 02:05:20 | Baddegama (Gin Ganga) | 3.66 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2026-10-27 02:04:50 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.057 |  |
| 2026-10-27 02:04:30 | Panadugama (Nilwala Ganga) | 6.45 | 🟠 Minor Flood | 0.091 | 🔺 Rising |
| 2026-10-27 02:04:23 | Hanwella (Kelani Ganga) | 6.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-27 02:04:06 | Deraniyagala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.070 |  |
| 2026-10-27 02:03:22 | Giriulla (Maha Oya) | 5.13 | 🟢 Normal | -0.050 |  |
| 2026-10-27 02:03:17 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.030 |  |
| 2026-10-27 02:03:17 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-10-27 02:03:16 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 3.130 | 🔺 Rising |
| 2026-10-27 02:03:05 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.005 |  |
| 2026-10-27 02:02:53 | Thanamalwila (Kirindi Oya) | 1.25 | 🟢 Normal | 3.130 | 🔺 Rising |
| 2026-10-27 02:02:31 | Thalgahagoda (Nilwala Ganga) | 1.48 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-10-27 02:02:30 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 02:02:20 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-27 02:02:14 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 02:02:07 | Badalgama (Maha Oya) | 5.70 | 🟡 Alert | 0.074 | 🔺 Rising |
| 2026-10-27 02:01:56 | Peradeniya (Mahaweli Ganga) | 4.40 | 🟢 Normal | -0.121 |  |
| 2026-10-27 02:01:19 | Holombuwa (Kelani Ganga) | 2.41 | 🟢 Normal | -0.445 |  |
| 2026-10-27 02:01:05 | Thawalama (Gin Ganga) | 5.35 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-27 02:01:00 | Magura (Kalu Ganga) | 5.20 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-27 02:00:46 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-27 02:04:30 | Panadugama (Nilwala Ganga) | 6.45 | 🟠 Minor Flood | 0.091 | 🔺 Rising |
| 2026-10-27 00:06:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.89 | 🟠 Minor Flood | 0.061 | 🔺 Rising |
| 2026-10-27 02:06:18 | Dunamale (Aththanagalu Oya) | 4.66 | 🟠 Minor Flood | 0.057 | 🔺 Rising |
| 2026-10-27 01:04:00 | Rathnapura (Kalu Ganga) | 8.64 | 🟠 Minor Flood | 0.011 | 🔺 Rising |
| 2026-10-27 01:01:47 | Moragaswewa (Deduru Oya) | 4.82 | 🟡 Alert | 0.108 | 🔺 Rising |
| 2026-10-27 02:02:07 | Badalgama (Maha Oya) | 5.70 | 🟡 Alert | 0.074 | 🔺 Rising |
| 2026-10-27 02:05:20 | Baddegama (Gin Ganga) | 3.66 | 🟡 Alert | 0.069 | 🔺 Rising |
| 2026-10-27 01:07:12 | Putupaula (Kalu Ganga) | 3.07 | 🟡 Alert | 0.060 | 🔺 Rising |
| 2026-10-27 02:01:00 | Magura (Kalu Ganga) | 5.20 | 🟡 Alert | 0.040 | 🔺 Rising |
| 2026-10-27 02:02:31 | Thalgahagoda (Nilwala Ganga) | 1.48 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-10-27 02:01:05 | Thawalama (Gin Ganga) | 5.35 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-10-27 01:11:28 | Urawa (Nilwala Ganga) | 2.50 | 🟡 Alert | -0.037 |  |
| 2026-10-27 02:06:37 | Glencourse (Kelani Ganga) | 15.00 | 🟡 Alert | -0.038 |  |
| 2026-10-27 02:05:58 | Norwood (Kelani Ganga) | 1.76 | 🟡 Alert | -0.040 |  |
| 2026-10-27 02:03:16 | Thanamalwila (Kirindi Oya) | 1.27 | 🟢 Normal | 3.130 | 🔺 Rising |
| 2026-10-27 01:00:45 | Horowpothana (Yan Oya) | 2.35 | 🟢 Normal | 0.239 | 🔺 Rising |
| 2026-10-26 18:02:01 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-27 01:04:23 | Nagalagam Street (Kelani Ganga) | 1.16 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-10-26 18:05:52 | Galgamuwa (Mee Oya) | 4.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-27 02:04:23 | Hanwella (Kelani Ganga) | 6.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-27 01:06:58 | Pitabeddara (Nilwala Ganga) | 3.72 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-27 01:00:12 | Moraketiya (Walawe Ganga) | 2.38 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-27 02:02:20 | Wellawaya (Kirindi Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-10-27 02:07:29 | Ellagawa (Kalu Ganga) | 9.70 | 🟢 Normal | 0.000 |  |
| 2026-10-27 02:02:14 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-27 02:02:30 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-27 02:03:05 | Yaka Wewa (Ma Oya) | 0.87 | 🟢 Normal | -0.005 |  |
| 2026-10-27 02:05:49 | Kuda Oya (Kirindi Oya) | 1.60 | 🟢 Normal | -0.010 |  |
| 2026-10-27 02:00:46 | Nakkala (Kumbukkan Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-10-27 02:03:17 | Thaldena (Mahaweli Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-10-27 02:06:20 | Katharagama (Menik Ganga) | -0.02 | 🟢 Normal | -0.029 |  |
| 2026-10-27 02:03:17 | Nawalapitiya (Mahaweli Ganga) | 2.03 | 🟢 Normal | -0.030 |  |
| 2026-10-27 02:03:22 | Giriulla (Maha Oya) | 5.13 | 🟢 Normal | -0.050 |  |
| 2026-10-27 02:04:50 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | -0.057 |  |
| 2026-10-26 18:02:45 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.058 |  |
| 2026-10-27 02:08:38 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.060 |  |
| 2026-10-27 02:04:06 | Deraniyagala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.070 |  |
| 2026-10-27 02:01:56 | Peradeniya (Mahaweli Ganga) | 4.40 | 🟢 Normal | -0.121 |  |
| 2026-10-27 02:01:19 | Holombuwa (Kelani Ganga) | 2.41 | 🟢 Normal | -0.445 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)