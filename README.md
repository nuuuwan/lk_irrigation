# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--22_23:27:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **268,252 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Kalawellawa (Millakanda) — Minor Flood; 🟠 Baddegama — Minor Flood; 🟡 Thalgahagoda — Alert; 🟡 Magura — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 23:27:54 | Magura (Kalu Ganga) | 4.49 | 🟡 Alert | -72.000 |  |
| 2026-09-22 23:27:52 | Magura (Kalu Ganga) | 4.53 | 🟡 Alert | -72.000 |  |
| 2026-09-22 23:26:53 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.037 |  |
| 2026-09-22 23:09:44 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.039 |  |
| 2026-09-22 23:07:43 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:07:07 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-09-22 23:05:39 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-22 23:05:28 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:05:26 | Thawalama (Gin Ganga) | 2.67 | 🟢 Normal | -0.019 |  |
| 2026-09-22 23:05:06 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.048 |  |
| 2026-09-22 23:04:37 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:04:37 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | -0.015 |  |
| 2026-09-22 23:04:28 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-09-22 23:04:26 | Nawalapitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-22 23:04:18 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-22 23:04:11 | Rathnapura (Kalu Ganga) | 3.92 | 🟢 Normal | -0.067 |  |
| 2026-09-22 23:03:45 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 11.277 | 🔺 Rising |
| 2026-09-22 23:03:42 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 23:03:41 | Hanwella (Kelani Ganga) | 4.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-22 23:03:11 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:03:06 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-22 23:03:04 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:03:02 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:02:56 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:02:50 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:02:48 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:02:22 | Peradeniya (Mahaweli Ganga) | 3.50 | 🟢 Normal | 11.277 | 🔺 Rising |
| 2026-09-22 23:01:55 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:01:53 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:01:53 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-22 23:01:51 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:01:05 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:00:31 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-22 22:04:13 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.15 | 🟠 Minor Flood | 0.000 |  |
| 2026-09-22 23:05:39 | Baddegama (Gin Ganga) | 4.07 | 🟠 Minor Flood | -0.011 |  |
| 2026-09-22 23:04:37 | Thalgahagoda (Nilwala Ganga) | 1.52 | 🟡 Alert | -0.015 |  |
| 2026-09-22 23:27:54 | Magura (Kalu Ganga) | 4.49 | 🟡 Alert | -72.000 |  |
| 2026-09-22 23:03:45 | Peradeniya (Mahaweli Ganga) | 3.76 | 🟢 Normal | 11.277 | 🔺 Rising |
| 2026-09-22 22:02:49 | Glencourse (Kelani Ganga) | 12.59 | 🟢 Normal | 0.125 | 🔺 Rising |
| 2026-09-22 23:03:06 | Deraniyagala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-09-22 23:04:26 | Nawalapitiya (Mahaweli Ganga) | 2.36 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-09-22 23:04:18 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.015 | 🔺 Rising |
| 2026-09-22 23:03:41 | Hanwella (Kelani Ganga) | 4.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-22 23:03:42 | Kithulgala (Kelani Ganga) | 2.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-22 18:00:33 | Weraganthota (Mahaweli Ganga) | -3.02 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:03:04 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:00:31 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:01:05 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-09-22 22:01:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:01:51 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-09-22 18:04:56 | Galgamuwa (Mee Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:05:28 | Pitabeddara (Nilwala Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:01:53 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:02:48 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:02:50 | Dunamale (Aththanagalu Oya) | 2.72 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:03:02 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:02:56 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:07:43 | Badalgama (Maha Oya) | 3.05 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:03:11 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:04:37 | Urawa (Nilwala Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:01:55 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-09-22 23:07:07 | Norwood (Kelani Ganga) | 0.89 | 🟢 Normal | -0.009 |  |
| 2026-09-22 18:02:46 | Thanthirimale (Malwathu Oya) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-09-22 23:04:28 | Holombuwa (Kelani Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-09-22 23:01:53 | Thanamalwila (Kirindi Oya) | 1.12 | 🟢 Normal | -0.010 |  |
| 2026-09-22 22:07:34 | Putupaula (Kalu Ganga) | 2.95 | 🟢 Normal | -0.012 |  |
| 2026-09-22 23:05:26 | Thawalama (Gin Ganga) | 2.67 | 🟢 Normal | -0.019 |  |
| 2026-09-22 23:26:53 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.037 |  |
| 2026-09-22 23:09:44 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.039 |  |
| 2026-09-22 23:05:06 | Giriulla (Maha Oya) | 1.86 | 🟢 Normal | -0.048 |  |
| 2026-09-22 23:04:11 | Rathnapura (Kalu Ganga) | 3.92 | 🟢 Normal | -0.067 |  |
| 2026-09-22 22:08:18 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -2.165 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)