# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--28_16:25:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **300,417 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Panadugama — Minor Flood; 🟠 Baddegama — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟡 Putupaula — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 16:25:48 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-28 16:18:05 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 16:12:00 | Glencourse (Kelani Ganga) | 11.72 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:11:27 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-28 16:10:15 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | 0.000 |  |
| 2026-10-28 16:10:11 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:10:11 | Moragaswewa (Deduru Oya) | 3.03 | 🟢 Normal | -0.027 |  |
| 2026-10-28 16:08:37 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | -0.046 |  |
| 2026-10-28 16:08:21 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:08:09 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 16:07:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.71 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-28 16:07:47 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-10-28 16:05:59 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:05:22 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:05:02 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:04:47 | Rathnapura (Kalu Ganga) | 6.02 | 🟡 Alert | -0.069 |  |
| 2026-10-28 16:04:38 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.058 |  |
| 2026-10-28 16:04:31 | Putupaula (Kalu Ganga) | 3.69 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 16:03:47 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-28 16:03:46 | Panadugama (Nilwala Ganga) | 6.00 | 🟠 Minor Flood | 0.051 | 🔺 Rising |
| 2026-10-28 16:03:39 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:03:38 | Urawa (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.144 |  |
| 2026-10-28 16:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 16:03:31 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-10-28 16:03:31 | Ellagawa (Kalu Ganga) | 10.41 | 🟡 Alert | -0.011 |  |
| 2026-10-28 16:03:22 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:03:06 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:02:51 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.049 |  |
| 2026-10-28 16:02:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:02:13 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-28 16:02:10 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:02:03 | Pitabeddara (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-10-28 16:01:53 | Dunamale (Aththanagalu Oya) | 3.37 | 🟡 Alert | -0.104 |  |
| 2026-10-28 16:01:38 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-10-28 16:01:33 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:01:26 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:01:20 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:01:10 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.052 |  |
| 2026-10-28 16:00:23 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-28 16:03:46 | Panadugama (Nilwala Ganga) | 6.00 | 🟠 Minor Flood | 0.051 | 🔺 Rising |
| 2026-10-28 16:08:09 | Baddegama (Gin Ganga) | 4.23 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 16:18:05 | Thalgahagoda (Nilwala Ganga) | 1.82 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-28 16:07:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.71 | 🟠 Minor Flood | -0.010 |  |
| 2026-10-28 16:04:31 | Putupaula (Kalu Ganga) | 3.69 | 🟡 Alert | 0.010 | 🔺 Rising |
| 2026-10-28 16:10:15 | Magura (Kalu Ganga) | 4.03 | 🟡 Alert | 0.000 |  |
| 2026-10-28 16:03:31 | Ellagawa (Kalu Ganga) | 10.41 | 🟡 Alert | -0.011 |  |
| 2026-10-28 16:04:47 | Rathnapura (Kalu Ganga) | 6.02 | 🟡 Alert | -0.069 |  |
| 2026-10-28 16:01:53 | Dunamale (Aththanagalu Oya) | 3.37 | 🟡 Alert | -0.104 |  |
| 2026-10-28 16:02:03 | Pitabeddara (Nilwala Ganga) | 2.88 | 🟢 Normal | 0.234 | 🔺 Rising |
| 2026-10-28 16:03:47 | Giriulla (Maha Oya) | 2.15 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-28 16:25:48 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-28 16:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-28 16:11:27 | Galgamuwa (Mee Oya) | 2.34 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-28 16:05:59 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:00:23 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:05:02 | Deraniyagala (Kelani Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:10:11 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:03:39 | Nagalagam Street (Kelani Ganga) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:12:00 | Glencourse (Kelani Ganga) | 11.72 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:01:33 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:01:20 | Thaldena (Mahaweli Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:03:22 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:01:26 | Manampitiya (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:08:21 | Peradeniya (Mahaweli Ganga) | 3.00 | 🟢 Normal | 0.000 |  |
| 2026-10-28 16:05:22 | Badalgama (Maha Oya) | 3.30 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:02:47 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:02:10 | Norwood (Kelani Ganga) | 1.17 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:03:06 | Hanwella (Kelani Ganga) | 4.29 | 🟢 Normal | -0.010 |  |
| 2026-10-28 16:07:47 | Moraketiya (Walawe Ganga) | 1.27 | 🟢 Normal | -0.019 |  |
| 2026-10-28 16:02:13 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-28 16:10:11 | Moragaswewa (Deduru Oya) | 3.03 | 🟢 Normal | -0.027 |  |
| 2026-10-28 16:03:31 | Holombuwa (Kelani Ganga) | 1.16 | 🟢 Normal | -0.030 |  |
| 2026-10-28 16:01:38 | Thanthirimale (Malwathu Oya) | 1.96 | 🟢 Normal | -0.040 |  |
| 2026-10-28 16:08:37 | Thawalama (Gin Ganga) | 3.30 | 🟢 Normal | -0.046 |  |
| 2026-10-28 16:02:51 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.049 |  |
| 2026-10-28 16:01:10 | Horowpothana (Yan Oya) | 2.57 | 🟢 Normal | -0.052 |  |
| 2026-10-28 16:04:38 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | -0.058 |  |
| 2026-10-28 16:03:38 | Urawa (Nilwala Ganga) | 2.34 | 🟢 Normal | -0.144 |  |

## River Water Level Charts by Station

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)