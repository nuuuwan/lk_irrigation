# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--13_06:34:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **286,491 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 06:34:23 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.001 |  |
| 2026-10-13 06:22:23 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.145 |  |
| 2026-10-13 06:20:20 | Panadugama (Nilwala Ganga) | 6.35 | 🟠 Minor Flood | -0.036 |  |
| 2026-10-13 06:17:59 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.004 |  |
| 2026-10-13 06:15:06 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 06:13:59 | Thalgahagoda (Nilwala Ganga) | 1.44 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-10-13 06:11:29 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.052 |  |
| 2026-10-13 06:10:43 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.070 |  |
| 2026-10-13 06:10:19 | Pitabeddara (Nilwala Ganga) | 2.91 | 🟢 Normal | -0.264 |  |
| 2026-10-13 06:10:17 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.126 |  |
| 2026-10-13 06:08:36 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-13 06:08:11 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-13 06:07:09 | Urawa (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.031 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-13 06:20:20 | Panadugama (Nilwala Ganga) | 6.35 | 🟠 Minor Flood | -0.036 |  |
| 2026-10-13 06:13:59 | Thalgahagoda (Nilwala Ganga) | 1.44 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-10-13 06:01:26 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.24 | 🟡 Alert | -0.043 |  |
| 2026-10-13 06:01:10 | Putupaula (Kalu Ganga) | 1.91 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-13 06:07:09 | Urawa (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-13 06:01:33 | Ellagawa (Kalu Ganga) | 7.06 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-13 06:00:18 | Moraketiya (Walawe Ganga) | 1.35 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-13 06:02:23 | Giriulla (Maha Oya) | 1.62 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-13 06:08:11 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-13 06:08:36 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-10-13 06:05:40 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-13 06:03:00 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-13 06:15:06 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-13 06:00:24 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal | 0.000 |  |
| 2026-10-13 06:03:57 | Dunamale (Aththanagalu Oya) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-10-12 18:01:38 | Thanthirimale (Malwathu Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-13 06:34:23 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | -0.001 |  |
| 2026-10-13 06:17:59 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.004 |  |
| 2026-10-13 06:05:08 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.009 |  |
| 2026-10-13 06:05:31 | Norwood (Kelani Ganga) | 1.06 | 🟢 Normal | -0.010 |  |
| 2026-10-13 06:02:16 | Nakkala (Kumbukkan Oya) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-10-13 06:02:37 | Kuda Oya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.010 |  |
| 2026-10-13 06:01:19 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-13 06:05:00 | Badalgama (Maha Oya) | 2.90 | 🟢 Normal | -0.019 |  |
| 2026-10-13 06:01:48 | Magura (Kalu Ganga) | 2.86 | 🟢 Normal | -0.020 |  |
| 2026-10-13 06:02:54 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | -0.021 |  |
| 2026-10-13 06:01:28 | Thanamalwila (Kirindi Oya) | 0.87 | 🟢 Normal | -0.024 |  |
| 2026-10-13 06:00:53 | Moragaswewa (Deduru Oya) | 0.85 | 🟢 Normal | -0.030 |  |
| 2026-10-13 06:02:28 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.039 |  |
| 2026-10-13 06:01:35 | Hanwella (Kelani Ganga) | 3.70 | 🟢 Normal | -0.040 |  |
| 2026-10-13 06:11:29 | Holombuwa (Kelani Ganga) | 0.94 | 🟢 Normal | -0.052 |  |
| 2026-10-13 06:05:07 | Deraniyagala (Kelani Ganga) | 0.68 | 🟢 Normal | -0.057 |  |
| 2026-10-13 06:10:43 | Rathnapura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.070 |  |
| 2026-10-13 06:04:34 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | -0.098 |  |
| 2026-10-13 06:10:17 | Peradeniya (Mahaweli Ganga) | 2.96 | 🟢 Normal | -0.126 |  |
| 2026-10-13 06:04:39 | Thawalama (Gin Ganga) | 2.39 | 🟢 Normal | -0.143 |  |
| 2026-10-13 06:22:23 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | -0.145 |  |
| 2026-10-13 06:10:19 | Pitabeddara (Nilwala Ganga) | 2.91 | 🟢 Normal | -0.264 |  |
| 2026-10-13 06:01:38 | Glencourse (Kelani Ganga) | 11.24 | 🟢 Normal | -10.080 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)