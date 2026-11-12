# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--11--12_09:27:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **313,666 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Moraketiya — Alert; 🟡 Dunamale — Alert; 🟡 Magura — Alert; 🟡 Panadugama — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 09:27:22 | Urawa (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.137 |  |
| 2026-11-12 09:13:36 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-12 09:11:17 | Thanamalwila (Kirindi Oya) | 2.66 | 🟢 Normal | -0.170 |  |
| 2026-11-12 09:10:20 | Moraketiya (Walawe Ganga) | 3.92 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-12 09:09:24 | Badalgama (Maha Oya) | 4.50 | 🟢 Normal | -0.055 |  |
| 2026-11-12 09:09:20 | Magura (Kalu Ganga) | 5.46 | 🟡 Alert | 0.000 |  |
| 2026-11-12 09:08:13 | Kuda Oya (Kirindi Oya) | 2.78 | 🟢 Normal | -0.049 |  |
| 2026-11-12 09:07:06 | Dunamale (Aththanagalu Oya) | 4.25 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-12 09:06:15 | Rathnapura (Kalu Ganga) | 5.37 | 🟡 Alert | -0.048 |  |
| 2026-11-12 09:06:05 | Moragaswewa (Deduru Oya) | 3.44 | 🟢 Normal | -0.084 |  |
| 2026-11-12 09:06:01 | Holombuwa (Kelani Ganga) | 1.82 | 🟢 Normal | -0.127 |  |
| 2026-11-12 09:05:59 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | -0.011 |  |
| 2026-11-12 09:05:58 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.252 |  |
| 2026-11-12 09:05:26 | Pitabeddara (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.084 |  |
| 2026-11-12 09:05:17 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | -0.048 |  |
| 2026-11-12 09:05:04 | Thaldena (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.043 |  |
| 2026-11-12 09:04:57 | Glencourse (Kelani Ganga) | 13.40 | 🟢 Normal | -0.163 |  |
| 2026-11-12 09:04:23 | Peradeniya (Mahaweli Ganga) | 5.05 | 🟡 Alert | -0.049 |  |
| 2026-11-12 09:04:23 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-11-12 09:03:53 | Ellagawa (Kalu Ganga) | 8.32 | 🟢 Normal | 0.000 |  |
| 2026-11-12 09:03:38 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 09:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | 0.000 |  |
| 2026-11-12 09:03:31 | Norwood (Kelani Ganga) | 1.46 | 🟢 Normal | -0.039 |  |
| 2026-11-12 09:03:25 | Panadugama (Nilwala Ganga) | 5.98 | 🟡 Alert | 0.000 |  |
| 2026-11-12 09:03:18 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.137 |  |
| 2026-11-12 09:02:59 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-12 09:02:58 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | -0.031 |  |
| 2026-11-12 09:02:50 | Thawalama (Gin Ganga) | 4.04 | 🟡 Alert | -0.290 |  |
| 2026-11-12 09:02:48 | Hanwella (Kelani Ganga) | 5.65 | 🟢 Normal | -0.010 |  |
| 2026-11-12 09:02:36 | Wellawaya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.039 |  |
| 2026-11-12 09:02:10 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-11-12 09:02:06 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-11-12 09:01:52 | Giriulla (Maha Oya) | 3.16 | 🟢 Normal | -0.081 |  |
| 2026-11-12 09:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-12 09:01:31 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-12 09:00:55 | Nakkala (Kumbukkan Oya) | 1.69 | 🟢 Normal | -0.081 |  |
| 2026-11-12 09:00:29 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-12 09:00:27 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.091 |  |
| 2026-11-12 09:00:13 | Siyambalanduwa (Heda Oya) | 1.26 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-11-12 09:03:38 | Thalgahagoda (Nilwala Ganga) | 1.80 | 🟠 Minor Flood | 0.000 |  |
| 2026-11-12 09:05:59 | Baddegama (Gin Ganga) | 4.09 | 🟠 Minor Flood | -0.011 |  |
| 2026-11-12 09:10:20 | Moraketiya (Walawe Ganga) | 3.92 | 🟡 Alert | 0.041 | 🔺 Rising |
| 2026-11-12 09:07:06 | Dunamale (Aththanagalu Oya) | 4.25 | 🟡 Alert | 0.009 | 🔺 Rising |
| 2026-11-12 09:09:20 | Magura (Kalu Ganga) | 5.46 | 🟡 Alert | 0.000 |  |
| 2026-11-12 09:03:25 | Panadugama (Nilwala Ganga) | 5.98 | 🟡 Alert | 0.000 |  |
| 2026-11-12 09:03:32 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.33 | 🟡 Alert | 0.000 |  |
| 2026-11-12 09:06:15 | Rathnapura (Kalu Ganga) | 5.37 | 🟡 Alert | -0.048 |  |
| 2026-11-12 09:04:23 | Peradeniya (Mahaweli Ganga) | 5.05 | 🟡 Alert | -0.049 |  |
| 2026-11-12 09:02:50 | Thawalama (Gin Ganga) | 4.04 | 🟡 Alert | -0.290 |  |
| 2026-11-12 09:00:29 | Horowpothana (Yan Oya) | 2.42 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-11-12 09:01:31 | Manampitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-12 09:02:59 | Kithulgala (Kelani Ganga) | 2.33 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-11-12 09:13:36 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-11-12 09:03:53 | Ellagawa (Kalu Ganga) | 8.32 | 🟢 Normal | 0.000 |  |
| 2026-11-12 09:02:06 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | -0.010 |  |
| 2026-11-12 09:04:23 | Putupaula (Kalu Ganga) | 2.56 | 🟢 Normal | -0.010 |  |
| 2026-11-12 09:02:48 | Hanwella (Kelani Ganga) | 5.65 | 🟢 Normal | -0.010 |  |
| 2026-11-12 09:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.66 | 🟢 Normal | -0.020 |  |
| 2026-11-12 09:02:58 | Nagalagam Street (Kelani Ganga) | 0.78 | 🟢 Normal | -0.031 |  |
| 2026-11-12 09:00:13 | Siyambalanduwa (Heda Oya) | 1.26 | 🟢 Normal | -0.031 |  |
| 2026-11-12 09:02:10 | Yaka Wewa (Ma Oya) | 0.84 | 🟢 Normal | -0.031 |  |
| 2026-11-12 09:02:36 | Wellawaya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.039 |  |
| 2026-11-12 09:03:31 | Norwood (Kelani Ganga) | 1.46 | 🟢 Normal | -0.039 |  |
| 2026-11-12 09:05:04 | Thaldena (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.043 |  |
| 2026-11-12 09:05:17 | Katharagama (Menik Ganga) | 0.66 | 🟢 Normal | -0.048 |  |
| 2026-11-12 09:08:13 | Kuda Oya (Kirindi Oya) | 2.78 | 🟢 Normal | -0.049 |  |
| 2026-11-12 09:09:24 | Badalgama (Maha Oya) | 4.50 | 🟢 Normal | -0.055 |  |
| 2026-11-12 09:00:55 | Nakkala (Kumbukkan Oya) | 1.69 | 🟢 Normal | -0.081 |  |
| 2026-11-12 09:01:52 | Giriulla (Maha Oya) | 3.16 | 🟢 Normal | -0.081 |  |
| 2026-11-12 09:05:26 | Pitabeddara (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.084 |  |
| 2026-11-12 09:06:05 | Moragaswewa (Deduru Oya) | 3.44 | 🟢 Normal | -0.084 |  |
| 2026-11-12 09:00:27 | Weraganthota (Mahaweli Ganga) | -1.43 | 🟢 Normal | -0.091 |  |
| 2026-11-12 09:06:01 | Holombuwa (Kelani Ganga) | 1.82 | 🟢 Normal | -0.127 |  |
| 2026-11-12 09:27:22 | Urawa (Nilwala Ganga) | 1.95 | 🟢 Normal | -0.137 |  |
| 2026-11-12 09:03:18 | Deraniyagala (Kelani Ganga) | 1.09 | 🟢 Normal | -0.137 |  |
| 2026-11-12 09:04:57 | Glencourse (Kelani Ganga) | 13.40 | 🟢 Normal | -0.163 |  |
| 2026-11-12 09:11:17 | Thanamalwila (Kirindi Oya) | 2.66 | 🟢 Normal | -0.170 |  |
| 2026-11-12 09:05:58 | Padiyathalawa (Maduru Oya) | 1.00 | 🟢 Normal | -0.252 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)