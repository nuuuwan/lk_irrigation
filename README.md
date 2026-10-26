# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_22:14:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,825 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟠 Rathnapura — Minor Flood; 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Panadugama — Minor Flood…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **0** measurements in the last **1 hour**.*

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-26 22:02:30 | Dunamale (Aththanagalu Oya) | 4.44 | 🟠 Minor Flood | 0.081 | 🔺 Rising |
| 2026-10-26 22:07:08 | Rathnapura (Kalu Ganga) | 8.56 | 🟠 Minor Flood | 0.051 | 🔺 Rising |
| 2026-10-26 22:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.78 | 🟠 Minor Flood | 0.035 | 🔺 Rising |
| 2026-10-26 22:11:09 | Panadugama (Nilwala Ganga) | 6.13 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-26 22:06:15 | Holombuwa (Kelani Ganga) | 3.40 | 🟠 Minor Flood | -0.236 |  |
| 2026-10-26 22:03:18 | Badalgama (Maha Oya) | 5.29 | 🟡 Alert | 0.190 | 🔺 Rising |
| 2026-10-26 22:04:27 | Thawalama (Gin Ganga) | 5.00 | 🟡 Alert | 0.122 | 🔺 Rising |
| 2026-10-26 22:03:23 | Magura (Kalu Ganga) | 5.03 | 🟡 Alert | 0.048 | 🔺 Rising |
| 2026-10-26 22:02:57 | Thalgahagoda (Nilwala Ganga) | 1.42 | 🟡 Alert | 0.031 | 🔺 Rising |
| 2026-10-26 22:09:45 | Urawa (Nilwala Ganga) | 2.53 | 🟡 Alert | 0.000 |  |
| 2026-10-26 22:03:19 | Glencourse (Kelani Ganga) | 15.27 | 🟡 Alert | -0.021 |  |
| 2026-10-26 22:11:39 | Norwood (Kelani Ganga) | 1.90 | 🟡 Alert | -0.046 |  |
| 2026-10-26 18:02:01 | Thanthirimale (Malwathu Oya) | 2.50 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-10-26 22:03:37 | Manampitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-10-26 22:02:42 | Hanwella (Kelani Ganga) | 6.54 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-26 22:03:51 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-26 22:06:14 | Putupaula (Kalu Ganga) | 2.93 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-10-26 22:08:24 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-26 18:05:52 | Galgamuwa (Mee Oya) | 4.21 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-26 22:04:19 | Pitabeddara (Nilwala Ganga) | 3.62 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-26 22:00:26 | Wellawaya (Kirindi Oya) | 1.38 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-10-26 22:02:11 | Ellagawa (Kalu Ganga) | 9.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-26 22:07:00 | Baddegama (Gin Ganga) | 3.39 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-26 22:03:45 | Kuda Oya (Kirindi Oya) | 1.58 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-26 22:03:02 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-26 22:01:22 | Moragaswewa (Deduru Oya) | 4.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 22:03:31 | Nakkala (Kumbukkan Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-10-26 22:06:37 | Horowpothana (Yan Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-10-26 22:08:32 | Padiyathalawa (Maduru Oya) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-10-26 21:03:46 | Siyambalanduwa (Heda Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-26 22:02:03 | Yaka Wewa (Ma Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-10-26 22:14:00 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.017 |  |
| 2026-10-26 22:02:53 | Moraketiya (Walawe Ganga) | 2.22 | 🟢 Normal | -0.031 |  |
| 2026-10-26 18:02:45 | Weraganthota (Mahaweli Ganga) | -2.38 | 🟢 Normal | -0.058 |  |
| 2026-10-26 22:03:12 | Giriulla (Maha Oya) | 5.05 | 🟢 Normal | -0.060 |  |
| 2026-10-26 22:05:22 | Nawalapitiya (Mahaweli Ganga) | 2.26 | 🟢 Normal | -0.107 |  |
| 2026-10-26 22:02:29 | Deraniyagala (Kelani Ganga) | 1.96 | 🟢 Normal | -0.110 |  |
| 2026-10-26 22:04:11 | Peradeniya (Mahaweli Ganga) | 4.96 | 🟢 Normal | -0.179 |  |
| 2026-10-26 22:08:39 | Kithulgala (Kelani Ganga) | 2.38 | 🟢 Normal | -0.182 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)