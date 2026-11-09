# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--10_03:03:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **311,626 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Dunamale — Minor Flood; 🟡 Panadugama — Alert; 🟡 Magura — Alert; 🟡 Moraketiya — Alert; 🟡 Thawalama — Alert; 🟡 Baddegama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 03:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.161 |  |
| 2026-11-10 03:03:30 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.050 |  |
| 2026-11-10 03:03:26 | Giriulla (Maha Oya) | 3.44 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-11-10 03:03:25 | Wellawaya (Kirindi Oya) | 2.25 | 🟢 Normal | -0.099 |  |
| 2026-11-10 03:03:21 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-10 03:03:15 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.098 |  |
| 2026-11-10 03:02:56 | Peradeniya (Mahaweli Ganga) | 4.60 | 🟢 Normal | -0.470 |  |
| 2026-11-10 03:02:53 | Glencourse (Kelani Ganga) | 14.73 | 🟢 Normal | -0.137 |  |
| 2026-11-10 03:02:31 | Dunamale (Aththanagalu Oya) | 4.52 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-11-10 03:02:12 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.120 |  |
| 2026-11-10 03:01:59 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-10 03:01:57 | Moragaswewa (Deduru Oya) | 3.25 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-10 03:01:51 | Thawalama (Gin Ganga) | 4.84 | 🟡 Alert | 0.062 | 🔺 Rising |
| 2026-11-10 03:01:39 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.150 |  |
| 2026-11-10 03:01:37 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.005 |  |
| 2026-11-10 03:01:24 | Rathnapura (Kalu Ganga) | 5.40 | 🟡 Alert | -0.043 |  |
| 2026-11-10 03:01:15 | Panadugama (Nilwala Ganga) | 5.83 | 🟡 Alert | 0.377 | 🔺 Rising |
| 2026-11-10 03:01:05 | Pitabeddara (Nilwala Ganga) | 3.44 | 🟢 Normal | 0.099 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-10 03:02:31 | Dunamale (Aththanagalu Oya) | 4.52 | 🟠 Minor Flood | 0.021 | 🔺 Rising |
| 2026-11-10 03:01:15 | Panadugama (Nilwala Ganga) | 5.83 | 🟡 Alert | 0.377 | 🔺 Rising |
| 2026-11-09 23:06:17 | Magura (Kalu Ganga) | 4.83 | 🟡 Alert | 0.125 | 🔺 Rising |
| 2026-11-10 01:33:28 | Moraketiya (Walawe Ganga) | 4.45 | 🟡 Alert | 0.091 | 🔺 Rising |
| 2026-11-10 03:01:51 | Thawalama (Gin Ganga) | 4.84 | 🟡 Alert | 0.062 | 🔺 Rising |
| 2026-11-10 02:10:10 | Baddegama (Gin Ganga) | 3.95 | 🟡 Alert | 0.051 | 🔺 Rising |
| 2026-11-10 02:02:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.28 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-11-10 02:14:34 | Thalgahagoda (Nilwala Ganga) | 1.60 | 🟡 Alert | 0.000 |  |
| 2026-11-10 03:01:24 | Rathnapura (Kalu Ganga) | 5.40 | 🟡 Alert | -0.043 |  |
| 2026-11-10 03:03:26 | Giriulla (Maha Oya) | 3.44 | 🟢 Normal | 0.289 | 🔺 Rising |
| 2026-11-09 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.56 | 🟢 Normal | 0.225 | 🔺 Rising |
| 2026-11-10 00:06:44 | Thanamalwila (Kirindi Oya) | 3.22 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-11-10 02:05:46 | Hanwella (Kelani Ganga) | 6.02 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-11-10 03:01:05 | Pitabeddara (Nilwala Ganga) | 3.44 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-11-10 03:01:57 | Moragaswewa (Deduru Oya) | 3.25 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-11-10 02:13:14 | Nagalagam Street (Kelani Ganga) | 0.98 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-11-10 02:08:07 | Putupaula (Kalu Ganga) | 2.42 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-11-10 02:07:27 | Ellagawa (Kalu Ganga) | 8.55 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-11-10 02:02:00 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-11-10 03:01:59 | Horowpothana (Yan Oya) | 2.85 | 🟢 Normal | 0.000 |  |
| 2026-11-09 18:06:18 | Galgamuwa (Mee Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-11-09 14:08:46 | Padiyathalawa (Maduru Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-11-10 03:03:21 | Katharagama (Menik Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-11-10 02:02:16 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-11-10 03:01:37 | Siyambalanduwa (Heda Oya) | 0.51 | 🟢 Normal | -0.005 |  |
| 2026-11-10 02:05:55 | Urawa (Nilwala Ganga) | 1.16 | 🟢 Normal | -0.005 |  |
| 2026-11-09 18:01:00 | Thanthirimale (Malwathu Oya) | 1.86 | 🟢 Normal | -0.010 |  |
| 2026-11-10 02:02:10 | Badalgama (Maha Oya) | 3.67 | 🟢 Normal | -0.010 |  |
| 2026-11-10 01:06:19 | Holombuwa (Kelani Ganga) | 1.63 | 🟢 Normal | -0.030 |  |
| 2026-11-10 01:02:35 | Norwood (Kelani Ganga) | 1.39 | 🟢 Normal | -0.030 |  |
| 2026-11-10 01:01:23 | Kuda Oya (Kirindi Oya) | 2.89 | 🟢 Normal | -0.043 |  |
| 2026-11-10 03:03:30 | Thaldena (Mahaweli Ganga) | 1.03 | 🟢 Normal | -0.050 |  |
| 2026-11-10 03:03:15 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.098 |  |
| 2026-11-10 03:03:25 | Wellawaya (Kirindi Oya) | 2.25 | 🟢 Normal | -0.099 |  |
| 2026-11-10 03:02:12 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.120 |  |
| 2026-11-10 03:02:53 | Glencourse (Kelani Ganga) | 14.73 | 🟢 Normal | -0.137 |  |
| 2026-11-10 03:01:39 | Nakkala (Kumbukkan Oya) | 1.40 | 🟢 Normal | -0.150 |  |
| 2026-11-10 03:03:40 | Nawalapitiya (Mahaweli Ganga) | 1.99 | 🟢 Normal | -0.161 |  |
| 2026-11-10 03:02:56 | Peradeniya (Mahaweli Ganga) | 4.60 | 🟢 Normal | -0.470 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)