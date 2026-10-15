# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--16_00:22:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **289,004 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Pitabeddara — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **1** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 00:22:40 | Rathnapura (Kalu Ganga) | 3.42 | 🟢 Normal | 0.134 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-16 00:05:40 | Panadugama (Nilwala Ganga) | 6.58 | 🟠 Minor Flood | 0.039 | 🔺 Rising |
| 2026-10-16 00:00:34 | Thalgahagoda (Nilwala Ganga) | 1.90 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-16 00:03:31 | Dunamale (Aththanagalu Oya) | 3.81 | 🟡 Alert | 0.000 |  |
| 2026-10-16 00:02:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.85 | 🟡 Alert | 0.000 |  |
| 2026-10-16 00:00:33 | Pitabeddara (Nilwala Ganga) | 4.65 | 🟡 Alert | -0.070 |  |
| 2026-10-16 00:06:26 | Urawa (Nilwala Ganga) | 2.50 | 🟡 Alert | -0.115 |  |
| 2026-10-16 00:01:54 | Moragaswewa (Deduru Oya) | 2.82 | 🟢 Normal | 0.207 | 🔺 Rising |
| 2026-10-16 00:22:40 | Rathnapura (Kalu Ganga) | 3.42 | 🟢 Normal | 0.134 | 🔺 Rising |
| 2026-10-16 00:02:22 | Peradeniya (Mahaweli Ganga) | 3.06 | 🟢 Normal | 0.100 | 🔺 Rising |
| 2026-10-16 00:03:13 | Kithulgala (Kelani Ganga) | 2.17 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-10-15 18:04:44 | Thanthirimale (Malwathu Oya) | 1.47 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-16 00:04:50 | Giriulla (Maha Oya) | 2.23 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-15 23:06:21 | Magura (Kalu Ganga) | 3.92 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-10-16 00:03:01 | Baddegama (Gin Ganga) | 2.89 | 🟢 Normal | 0.043 | 🔺 Rising |
| 2026-10-16 00:13:24 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-16 00:04:57 | Thaldena (Mahaweli Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-16 00:10:06 | Wellawaya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-15 18:18:48 | Galgamuwa (Mee Oya) | 0.58 | 🟢 Normal | 0.016 | 🔺 Rising |
| 2026-10-16 00:01:22 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 00:00:08 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-16 00:00:46 | Moraketiya (Walawe Ganga) | 2.28 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 18:02:23 | Weraganthota (Mahaweli Ganga) | -3.25 | 🟢 Normal | 0.000 |  |
| 2026-10-16 00:02:18 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-10-16 00:05:13 | Ellagawa (Kalu Ganga) | 7.70 | 🟢 Normal | 0.000 |  |
| 2026-10-16 00:02:39 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-10-16 00:12:17 | Glencourse (Kelani Ganga) | 11.38 | 🟢 Normal | 0.000 |  |
| 2026-10-16 00:04:38 | Manampitiya (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-10-16 00:05:02 | Kuda Oya (Kirindi Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-10-16 00:02:51 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-10-16 00:03:22 | Yaka Wewa (Ma Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-10-16 00:04:54 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-10-16 00:01:04 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-10-16 00:08:21 | Katharagama (Menik Ganga) | 0.18 | 🟢 Normal | -0.018 |  |
| 2026-10-16 00:05:36 | Holombuwa (Kelani Ganga) | 1.31 | 🟢 Normal | -0.020 |  |
| 2026-10-16 00:04:50 | Badalgama (Maha Oya) | 3.40 | 🟢 Normal | -0.020 |  |
| 2026-10-16 00:04:59 | Putupaula (Kalu Ganga) | 2.48 | 🟢 Normal | -0.044 |  |
| 2026-10-16 00:04:54 | Hanwella (Kelani Ganga) | 3.95 | 🟢 Normal | -0.053 |  |
| 2026-10-16 00:02:53 | Thawalama (Gin Ganga) | 3.97 | 🟢 Normal | -0.058 |  |
| 2026-10-16 00:03:43 | Norwood (Kelani Ganga) | 1.38 | 🟢 Normal | -0.061 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)