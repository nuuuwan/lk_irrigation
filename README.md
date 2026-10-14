# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_18:10:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,871 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Holombuwa — Minor Flood; 🟠 Thalgahagoda — Minor Flood; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Panadugama — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 18:10:25 | Panadugama (Nilwala Ganga) | 5.58 | 🟡 Alert | -0.061 |  |
| 2026-10-14 18:08:17 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.053 |  |
| 2026-10-14 18:08:08 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-14 18:07:03 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-14 18:06:53 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-14 18:06:47 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.648 | 🔺 Rising |
| 2026-10-14 18:06:35 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-10-14 18:05:50 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-10-14 18:05:48 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-10-14 18:05:44 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:05:16 | Dunamale (Aththanagalu Oya) | 2.37 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-14 18:05:15 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-10-14 18:04:42 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:04:23 | Magura (Kalu Ganga) | 4.69 | 🟡 Alert | -0.103 |  |
| 2026-10-14 18:04:16 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 18:04:15 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:03:56 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | 0.507 | 🔺 Rising |
| 2026-10-14 18:03:36 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-10-14 18:03:22 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-10-14 18:03:09 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.065 |  |
| 2026-10-14 18:02:59 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 18:02:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:57 | Holombuwa (Kelani Ganga) | 3.85 | 🟠 Minor Flood | 1.216 | 🔺 Rising |
| 2026-10-14 18:02:47 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:30 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:13 | Peradeniya (Mahaweli Ganga) | 3.45 | 🟢 Normal | 0.544 | 🔺 Rising |
| 2026-10-14 18:02:10 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-10-14 18:01:58 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-14 18:01:56 | Thalgahagoda (Nilwala Ganga) | 1.71 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 18:01:44 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-14 18:01:33 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-10-14 18:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.02 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-10-14 18:01:08 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:00:52 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:00:40 | Putupaula (Kalu Ganga) | 2.15 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-14 18:00:35 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.032 |  |
| 2026-10-14 18:00:13 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.013 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 18:02:57 | Holombuwa (Kelani Ganga) | 3.85 | 🟠 Minor Flood | 1.216 | 🔺 Rising |
| 2026-10-14 18:01:56 | Thalgahagoda (Nilwala Ganga) | 1.71 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 18:01:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.02 | 🟡 Alert | 0.076 | 🔺 Rising |
| 2026-10-14 18:10:25 | Panadugama (Nilwala Ganga) | 5.58 | 🟡 Alert | -0.061 |  |
| 2026-10-14 18:04:23 | Magura (Kalu Ganga) | 4.69 | 🟡 Alert | -0.103 |  |
| 2026-10-14 18:06:47 | Thawalama (Gin Ganga) | 3.10 | 🟢 Normal | 0.648 | 🔺 Rising |
| 2026-10-14 18:02:13 | Peradeniya (Mahaweli Ganga) | 3.45 | 🟢 Normal | 0.544 | 🔺 Rising |
| 2026-10-14 18:03:56 | Glencourse (Kelani Ganga) | 11.71 | 🟢 Normal | 0.507 | 🔺 Rising |
| 2026-10-14 18:05:50 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.326 | 🔺 Rising |
| 2026-10-14 18:03:36 | Rathnapura (Kalu Ganga) | 3.43 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-10-14 18:05:16 | Dunamale (Aththanagalu Oya) | 2.37 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-14 18:06:53 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-10-14 17:05:08 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-14 18:07:03 | Hanwella (Kelani Ganga) | 2.94 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-10-14 18:08:08 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-14 18:00:40 | Putupaula (Kalu Ganga) | 2.15 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-10-14 18:04:16 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-14 18:00:13 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-10-14 18:02:59 | Ellagawa (Kalu Ganga) | 7.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 18:02:30 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:00:52 | Wellawaya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:01:08 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:04:15 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 17:02:53 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:04:42 | Manampitiya (Mahaweli Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:47 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:05:44 | Urawa (Nilwala Ganga) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:05:48 | Pitabeddara (Nilwala Ganga) | 1.69 | 🟢 Normal | -0.010 |  |
| 2026-10-14 18:01:58 | Moragaswewa (Deduru Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-14 18:01:33 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-10-14 18:01:44 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-10-14 18:03:22 | Giriulla (Maha Oya) | 1.43 | 🟢 Normal | -0.011 |  |
| 2026-10-14 18:05:15 | Baddegama (Gin Ganga) | 2.66 | 🟢 Normal | -0.020 |  |
| 2026-10-14 18:06:35 | Badalgama (Maha Oya) | 2.75 | 🟢 Normal | -0.020 |  |
| 2026-10-14 18:02:10 | Thanamalwila (Kirindi Oya) | 0.82 | 🟢 Normal | -0.021 |  |
| 2026-10-14 18:00:35 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.032 |  |
| 2026-10-14 18:08:17 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.053 |  |
| 2026-10-14 18:03:09 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)