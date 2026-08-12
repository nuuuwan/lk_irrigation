# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_12:11:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,436 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 12:11:29 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:11:23 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:09:43 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.047 |  |
| 2026-08-12 12:09:28 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:08:01 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-12 12:07:20 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:07:11 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:06:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-08-12 12:06:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:05:44 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:05:42 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:04:56 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:04:24 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:04:24 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.039 |  |
| 2026-08-12 12:04:21 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:03:54 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:03:52 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:03:48 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | -0.010 |  |
| 2026-08-12 12:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-08-12 12:03:11 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:03:10 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:03:09 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.077 |  |
| 2026-08-12 12:03:08 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:54 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:48 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-08-12 12:02:45 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.011 |  |
| 2026-08-12 12:02:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-12 12:02:39 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.142 |  |
| 2026-08-12 12:02:32 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:32 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:21 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-12 12:02:19 | Ellagawa (Kalu Ganga) | 5.27 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:18 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:18 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:15 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-08-12 12:02:15 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-08-12 12:01:54 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:01:24 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:00:37 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:00:14 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.376 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 12:00:14 | Weraganthota (Mahaweli Ganga) | -2.98 | 🟢 Normal | 0.376 | 🔺 Rising |
| 2026-08-12 12:02:15 | Putupaula (Kalu Ganga) | 0.57 | 🟢 Normal | 0.121 | 🔺 Rising |
| 2026-08-12 12:02:42 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.120 | 🔺 Rising |
| 2026-08-12 12:06:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.32 | 🟢 Normal | 0.115 | 🔺 Rising |
| 2026-08-12 12:08:01 | Magura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-12 12:05:44 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:00:37 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:06:18 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:03:11 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:03:54 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:11:29 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:04:24 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:03:10 | Pitabeddara (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:04:21 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:54 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:19 | Ellagawa (Kalu Ganga) | 5.27 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:07:11 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:11:23 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:05:42 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:32 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:18 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:04:56 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:03:08 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:07:20 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:18 | Manampitiya (Mahaweli Ganga) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:32 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:01:24 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:09:28 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:01:54 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-12 12:02:15 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.010 |  |
| 2026-08-12 12:03:48 | Glencourse (Kelani Ganga) | 10.49 | 🟢 Normal | -0.010 |  |
| 2026-08-12 12:02:21 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | -0.010 |  |
| 2026-08-12 12:03:32 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | -0.010 |  |
| 2026-08-12 12:02:48 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | -0.010 |  |
| 2026-08-12 12:02:45 | Thawalama (Gin Ganga) | 1.67 | 🟢 Normal | -0.011 |  |
| 2026-08-12 12:04:24 | Rathnapura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.039 |  |
| 2026-08-12 12:09:43 | Kithulgala (Kelani Ganga) | 2.18 | 🟢 Normal | -0.047 |  |
| 2026-08-12 12:03:09 | Thaldena (Mahaweli Ganga) | 0.19 | 🟢 Normal | -0.077 |  |
| 2026-08-12 12:02:39 | Deraniyagala (Kelani Ganga) | 0.72 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)