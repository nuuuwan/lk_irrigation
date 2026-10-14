# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--15_02:32:35-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,164 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Dunamale — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 02:32:35 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.007 |  |
| 2026-10-15 02:32:23 | Panadugama (Nilwala Ganga) | 5.25 | 🟡 Alert | -1.895 |  |
| 2026-10-15 02:31:26 | Panadugama (Nilwala Ganga) | 5.28 | 🟡 Alert | -1.895 |  |
| 2026-10-15 02:20:41 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.052 |  |
| 2026-10-15 02:19:03 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-15 02:09:57 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-15 02:08:47 | Holombuwa (Kelani Ganga) | 2.35 | 🟢 Normal | -0.248 |  |
| 2026-10-15 02:07:41 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-10-15 02:06:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-15 02:06:16 | Rathnapura (Kalu Ganga) | 4.72 | 🟢 Normal | 0.000 |  |
| 2026-10-15 02:06:16 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.063 |  |
| 2026-10-15 02:05:53 | Hanwella (Kelani Ganga) | 4.65 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-10-15 02:04:40 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | 0.202 | 🔺 Rising |
| 2026-10-15 02:04:34 | Peradeniya (Mahaweli Ganga) | 3.67 | 🟢 Normal | -0.183 |  |
| 2026-10-15 02:04:29 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 02:03:55 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.100 |  |
| 2026-10-15 02:03:27 | Giriulla (Maha Oya) | 3.92 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-15 02:02:59 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.091 |  |
| 2026-10-15 02:02:53 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-10-15 02:02:51 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-10-15 02:02:35 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-15 02:02:18 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 02:02:18 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-15 02:01:54 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-15 02:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.043 |  |
| 2026-10-15 02:01:20 | Glencourse (Kelani Ganga) | 13.44 | 🟢 Normal | 0.558 | 🔺 Rising |
| 2026-10-15 02:01:18 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-10-15 02:01:15 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 02:00:55 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-15 02:00:06 | Rathnapura (Kalu Ganga) | 4.72 | 🟢 Normal | 0.000 |  |
| 2026-10-15 01:57:02 | Glencourse (Kelani Ganga) | 13.40 | 🟢 Normal | 0.558 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-15 02:09:57 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.019 | 🔺 Rising |
| 2026-10-15 02:04:40 | Dunamale (Aththanagalu Oya) | 3.80 | 🟡 Alert | 0.202 | 🔺 Rising |
| 2026-10-15 01:01:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.08 | 🟡 Alert | 0.000 |  |
| 2026-10-15 01:06:29 | Magura (Kalu Ganga) | 4.24 | 🟡 Alert | -0.030 |  |
| 2026-10-15 02:32:23 | Panadugama (Nilwala Ganga) | 5.25 | 🟡 Alert | -1.895 |  |
| 2026-10-15 01:02:17 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 8.000 | 🔺 Rising |
| 2026-10-15 02:01:20 | Glencourse (Kelani Ganga) | 13.44 | 🟢 Normal | 0.558 | 🔺 Rising |
| 2026-10-15 02:02:51 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.235 | 🔺 Rising |
| 2026-10-15 02:07:41 | Badalgama (Maha Oya) | 3.20 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-10-15 02:05:53 | Hanwella (Kelani Ganga) | 4.65 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-10-15 02:03:27 | Giriulla (Maha Oya) | 3.92 | 🟢 Normal | 0.139 | 🔺 Rising |
| 2026-10-15 02:19:03 | Nagalagam Street (Kelani Ganga) | 0.76 | 🟢 Normal | 0.078 | 🔺 Rising |
| 2026-10-15 02:02:18 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-10-15 02:02:35 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-15 01:01:38 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-15 02:01:54 | Ellagawa (Kalu Ganga) | 8.00 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-10-15 00:14:59 | Putupaula (Kalu Ganga) | 2.19 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-15 02:04:29 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-15 02:02:18 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-15 02:06:59 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-14 18:02:30 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-15 02:00:55 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-15 02:01:15 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-15 02:06:16 | Rathnapura (Kalu Ganga) | 4.72 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:47 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-15 01:01:45 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-15 02:32:35 | Baddegama (Gin Ganga) | 2.48 | 🟢 Normal | -0.007 |  |
| 2026-10-15 00:24:41 | Pitabeddara (Nilwala Ganga) | 1.63 | 🟢 Normal | -0.012 |  |
| 2026-10-15 02:01:18 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.030 |  |
| 2026-10-15 02:02:53 | Norwood (Kelani Ganga) | 1.25 | 🟢 Normal | -0.030 |  |
| 2026-10-15 02:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.043 |  |
| 2026-10-15 02:20:41 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.052 |  |
| 2026-10-15 02:06:16 | Thawalama (Gin Ganga) | 2.70 | 🟢 Normal | -0.063 |  |
| 2026-10-15 02:02:59 | Yaka Wewa (Ma Oya) | 0.73 | 🟢 Normal | -0.091 |  |
| 2026-10-15 02:03:55 | Deraniyagala (Kelani Ganga) | 1.11 | 🟢 Normal | -0.100 |  |
| 2026-10-15 02:04:34 | Peradeniya (Mahaweli Ganga) | 3.67 | 🟢 Normal | -0.183 |  |
| 2026-10-15 02:08:47 | Holombuwa (Kelani Ganga) | 2.35 | 🟢 Normal | -0.248 |  |
| 2026-10-15 01:00:57 | Moraketiya (Walawe Ganga) | 1.18 | 🟢 Normal | -0.723 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)