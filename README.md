# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--14_23:32:41-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **288,061 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood; 🟠 Holombuwa — Minor Flood; 🟡 Dunamale — Alert; 🟡 Panadugama — Alert; 🟡 Kalawellawa (Millakanda) — Alert…
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 23:32:41 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:29:14 | Holombuwa (Kelani Ganga) | 3.55 | 🟠 Minor Flood | -0.553 |  |
| 2026-10-14 23:23:34 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:21:34 | Magura (Kalu Ganga) | 4.32 | 🟡 Alert | -0.042 |  |
| 2026-10-14 23:17:28 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:13:30 | Putupaula (Kalu Ganga) | 2.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-14 23:11:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-14 23:10:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.07 | 🟡 Alert | 0.000 |  |
| 2026-10-14 23:08:46 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:08:46 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.030 |  |
| 2026-10-14 23:07:46 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 23:07:34 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-14 23:07:19 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:06:59 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:06:39 | Giriulla (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:06:28 | Rathnapura (Kalu Ganga) | 5.30 | 🟡 Alert | -0.097 |  |
| 2026-10-14 23:05:46 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.293 |  |
| 2026-10-14 23:05:45 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:05:31 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:05:17 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:04:50 | Peradeniya (Mahaweli Ganga) | 4.26 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-14 23:04:22 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-10-14 23:04:18 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.285 |  |
| 2026-10-14 23:04:06 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 23:03:59 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.080 |  |
| 2026-10-14 23:03:39 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-14 23:03:33 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | -0.093 |  |
| 2026-10-14 23:03:28 | Dunamale (Aththanagalu Oya) | 3.40 | 🟡 Alert | 0.155 | 🔺 Rising |
| 2026-10-14 23:03:24 | Hanwella (Kelani Ganga) | 4.04 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-14 23:02:53 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-14 23:02:48 | Ellagawa (Kalu Ganga) | 7.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-14 23:02:47 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.050 |  |
| 2026-10-14 23:02:30 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-10-14 23:01:46 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 23:01:42 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-10-14 23:01:41 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:00:47 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-14 22:58:51 | Giriulla (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-14 23:07:46 | Thalgahagoda (Nilwala Ganga) | 1.75 | 🟠 Minor Flood | 0.000 |  |
| 2026-10-14 23:29:14 | Holombuwa (Kelani Ganga) | 3.55 | 🟠 Minor Flood | -0.553 |  |
| 2026-10-14 23:03:28 | Dunamale (Aththanagalu Oya) | 3.40 | 🟡 Alert | 0.155 | 🔺 Rising |
| 2026-10-14 22:11:24 | Panadugama (Nilwala Ganga) | 5.40 | 🟡 Alert | 0.000 |  |
| 2026-10-14 23:10:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.07 | 🟡 Alert | 0.000 |  |
| 2026-10-14 23:21:34 | Magura (Kalu Ganga) | 4.32 | 🟡 Alert | -0.042 |  |
| 2026-10-14 23:06:28 | Rathnapura (Kalu Ganga) | 5.30 | 🟡 Alert | -0.097 |  |
| 2026-10-14 22:02:46 | Glencourse (Kelani Ganga) | 12.76 | 🟢 Normal | 0.267 | 🔺 Rising |
| 2026-10-14 23:03:24 | Hanwella (Kelani Ganga) | 4.04 | 🟢 Normal | 0.192 | 🔺 Rising |
| 2026-10-14 23:04:22 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-10-14 23:07:34 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.122 | 🔺 Rising |
| 2026-10-14 23:11:13 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-10-14 23:04:50 | Peradeniya (Mahaweli Ganga) | 4.26 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-10-14 23:02:48 | Ellagawa (Kalu Ganga) | 7.85 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-14 23:02:53 | Manampitiya (Mahaweli Ganga) | -0.01 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-14 23:03:39 | Badalgama (Maha Oya) | 2.81 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-10-14 23:13:30 | Putupaula (Kalu Ganga) | 2.17 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-10-14 23:01:46 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-14 18:02:30 | Weraganthota (Mahaweli Ganga) | -3.34 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:00:47 | Wellawaya (Kirindi Oya) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:01:41 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:05:17 | Moragaswewa (Deduru Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:06:39 | Giriulla (Maha Oya) | 2.26 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:58 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:32:41 | Pitabeddara (Nilwala Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:05:31 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:23:34 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:08:46 | Katharagama (Menik Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-10-14 18:02:47 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:07:19 | Urawa (Nilwala Ganga) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:17:28 | Kuda Oya (Kirindi Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-10-14 23:01:42 | Moraketiya (Walawe Ganga) | 1.20 | 🟢 Normal | -0.020 |  |
| 2026-10-14 23:02:30 | Thanamalwila (Kirindi Oya) | 0.78 | 🟢 Normal | -0.020 |  |
| 2026-10-14 23:08:46 | Baddegama (Gin Ganga) | 2.51 | 🟢 Normal | -0.030 |  |
| 2026-10-14 23:02:47 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | -0.050 |  |
| 2026-10-14 23:03:59 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | -0.080 |  |
| 2026-10-14 23:03:33 | Thawalama (Gin Ganga) | 2.93 | 🟢 Normal | -0.093 |  |
| 2026-10-14 23:04:18 | Deraniyagala (Kelani Ganga) | 1.59 | 🟢 Normal | -0.285 |  |
| 2026-10-14 23:05:46 | Yaka Wewa (Ma Oya) | 1.02 | 🟢 Normal | -0.293 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)