# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--26_15:16:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **298,558 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Rathnapura — Minor Flood; 🟠 Holombuwa — Minor Flood; 🟡 Panadugama — Alert; 🟡 Peradeniya — Alert; 🟡 Norwood — Alert; 🟡 Dunamale — Alert…
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
| 2026-10-26 15:03:21 | Rathnapura (Kalu Ganga) | 7.96 | 🟠 Minor Flood | 0.083 | 🔺 Rising |
| 2026-10-26 15:06:12 | Holombuwa (Kelani Ganga) | 4.83 | 🟠 Minor Flood | -0.348 |  |
| 2026-10-26 15:11:04 | Panadugama (Nilwala Ganga) | 5.73 | 🟡 Alert | 0.493 | 🔺 Rising |
| 2026-10-26 15:01:06 | Peradeniya (Mahaweli Ganga) | 5.53 | 🟡 Alert | 0.211 | 🔺 Rising |
| 2026-10-26 15:03:59 | Norwood (Kelani Ganga) | 2.39 | 🟡 Alert | 0.117 | 🔺 Rising |
| 2026-10-26 15:06:48 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | 0.098 | 🔺 Rising |
| 2026-10-26 15:04:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | 0.089 | 🔺 Rising |
| 2026-10-26 15:01:47 | Magura (Kalu Ganga) | 4.24 | 🟡 Alert | 0.072 | 🔺 Rising |
| 2026-10-26 15:08:12 | Urawa (Nilwala Ganga) | 2.53 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-10-26 15:03:28 | Glencourse (Kelani Ganga) | 14.30 | 🟢 Normal | 0.540 | 🔺 Rising |
| 2026-10-26 15:02:08 | Giriulla (Maha Oya) | 3.78 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-10-26 15:03:40 | Hanwella (Kelani Ganga) | 4.90 | 🟢 Normal | 0.270 | 🔺 Rising |
| 2026-10-26 15:11:29 | Pitabeddara (Nilwala Ganga) | 3.15 | 🟢 Normal | 0.231 | 🔺 Rising |
| 2026-10-26 15:01:02 | Moraketiya (Walawe Ganga) | 2.05 | 🟢 Normal | 0.186 | 🔺 Rising |
| 2026-10-26 15:02:03 | Thawalama (Gin Ganga) | 3.42 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-10-26 15:04:00 | Thaldena (Mahaweli Ganga) | 0.68 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-10-26 15:03:25 | Ellagawa (Kalu Ganga) | 9.08 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-26 15:05:36 | Putupaula (Kalu Ganga) | 2.57 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-26 15:03:25 | Galgamuwa (Mee Oya) | 3.82 | 🟢 Normal | 0.073 | 🔺 Rising |
| 2026-10-26 15:02:06 | Thanthirimale (Malwathu Oya) | 2.13 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-10-26 15:09:09 | Baddegama (Gin Ganga) | 3.00 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-26 15:05:01 | Badalgama (Maha Oya) | 4.19 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-26 15:03:54 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-26 15:03:05 | Thanamalwila (Kirindi Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-26 15:03:35 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-26 15:16:30 | Moragaswewa (Deduru Oya) | 4.37 | 🟢 Normal | 0.000 |  |
| 2026-10-26 15:01:43 | Yaka Wewa (Ma Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-26 15:04:43 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 15:03:44 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-10-26 15:03:01 | Thalgahagoda (Nilwala Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-10-26 15:02:11 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-26 15:05:45 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.009 |  |
| 2026-10-26 15:01:13 | Nakkala (Kumbukkan Oya) | 0.93 | 🟢 Normal | -0.010 |  |
| 2026-10-26 15:01:28 | Wellawaya (Kirindi Oya) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-26 15:09:32 | Horowpothana (Yan Oya) | 2.47 | 🟢 Normal | -0.017 |  |
| 2026-10-26 15:00:07 | Weraganthota (Mahaweli Ganga) | -2.10 | 🟢 Normal | -0.033 |  |
| 2026-10-26 15:07:45 | Kithulgala (Kelani Ganga) | 2.90 | 🟢 Normal | -0.096 |  |
| 2026-10-26 15:03:40 | Nawalapitiya (Mahaweli Ganga) | 2.97 | 🟢 Normal | -0.293 |  |
| 2026-10-26 15:04:41 | Deraniyagala (Kelani Ganga) | 3.02 | 🟢 Normal | -0.566 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)