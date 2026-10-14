# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_13:10:21-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **287,666 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 13:10:21 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:09:57 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.097 |  |
| 2026-10-14 13:08:03 | Baddegama (Gin Ganga) | 2.73 | 🟢 Normal | -0.009 |  |
| 2026-10-14 13:07:25 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:07:23 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-10-14 13:07:07 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:06:37 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:06:16 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-14 13:05:05 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:05:05 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:05:03 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | -0.010 |  |
| 2026-10-14 13:04:45 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | -0.010 |  |
| 2026-10-14 13:04:29 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.019 |  |
| 2026-10-14 13:04:28 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:04:22 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-14 13:03:51 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.115 |  |
| 2026-10-14 13:03:46 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.061 |  |
| 2026-10-14 13:03:33 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-10-14 13:03:14 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:03:12 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:03:12 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | -0.070 |  |
| 2026-10-14 13:02:46 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-10-14 13:02:26 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:02:06 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-10-14 13:02:01 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:01:52 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.020 |  |
| 2026-10-14 13:01:49 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.033 |  |
| 2026-10-14 13:01:41 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.010 |  |
| 2026-10-14 13:01:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:01:17 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:01:15 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.117 |  |
| 2026-10-14 13:00:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.82 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-10-14 13:00:26 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.033 |  |
| 2026-10-14 13:00:12 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 13:00:12 | Thalgahagoda (Nilwala Ganga) | 1.70 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 12:08:36 | Panadugama (Nilwala Ganga) | 5.28 | 🟡 Alert | 6.308 | 🔺 Rising |
| 2026-10-14 13:00:49 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.82 | 🟡 Alert | 0.021 | 🔺 Rising |
| 2026-10-14 12:02:58 | Magura (Kalu Ganga) | 5.21 | 🟡 Alert | -0.090 |  |
| 2026-10-14 13:06:16 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-10-14 12:02:55 | Wellawaya (Kirindi Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:01:36 | Nakkala (Kumbukkan Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:01:17 | Moragaswewa (Deduru Oya) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:07:25 | Nawalapitiya (Mahaweli Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:06:37 | Yaka Wewa (Ma Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 12:02:07 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:02:01 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:03:14 | Norwood (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:05:05 | Deraniyagala (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:04:28 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:03:12 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:05:05 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:07:07 | Holombuwa (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:10:21 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:02:26 | Urawa (Nilwala Ganga) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 13:08:03 | Baddegama (Gin Ganga) | 2.73 | 🟢 Normal | -0.009 |  |
| 2026-10-14 13:05:03 | Glencourse (Kelani Ganga) | 10.84 | 🟢 Normal | -0.010 |  |
| 2026-10-14 13:04:22 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.010 |  |
| 2026-10-14 13:02:06 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | -0.010 |  |
| 2026-10-14 13:04:45 | Ellagawa (Kalu Ganga) | 7.75 | 🟢 Normal | -0.010 |  |
| 2026-10-14 13:03:33 | Giriulla (Maha Oya) | 1.49 | 🟢 Normal | -0.010 |  |
| 2026-10-14 13:01:41 | Weraganthota (Mahaweli Ganga) | -3.37 | 🟢 Normal | -0.010 |  |
| 2026-10-14 13:04:29 | Moraketiya (Walawe Ganga) | 1.25 | 🟢 Normal | -0.019 |  |
| 2026-10-14 13:02:46 | Kuda Oya (Kirindi Oya) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-10-14 13:07:23 | Badalgama (Maha Oya) | 2.85 | 🟢 Normal | -0.020 |  |
| 2026-10-14 13:01:52 | Manampitiya (Mahaweli Ganga) | -0.11 | 🟢 Normal | -0.020 |  |
| 2026-10-14 11:59:50 | Dunamale (Aththanagalu Oya) | 2.29 | 🟢 Normal | -0.031 |  |
| 2026-10-14 13:01:49 | Thanamalwila (Kirindi Oya) | 0.96 | 🟢 Normal | -0.033 |  |
| 2026-10-14 13:00:26 | Pitabeddara (Nilwala Ganga) | 1.80 | 🟢 Normal | -0.033 |  |
| 2026-10-14 13:03:46 | Thawalama (Gin Ganga) | 2.35 | 🟢 Normal | -0.061 |  |
| 2026-10-14 13:03:12 | Hanwella (Kelani Ganga) | 2.96 | 🟢 Normal | -0.070 |  |
| 2026-10-14 13:09:57 | Rathnapura (Kalu Ganga) | 3.54 | 🟢 Normal | -0.097 |  |
| 2026-10-14 13:03:51 | Peradeniya (Mahaweli Ganga) | 2.71 | 🟢 Normal | -0.115 |  |
| 2026-10-14 13:01:15 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)