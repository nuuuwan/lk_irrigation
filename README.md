# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_04:34:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **245,919 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 04:34:56 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:19:25 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.184 |  |
| 2026-08-29 04:17:26 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:14:21 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.382 | 🔺 Rising |
| 2026-08-29 04:12:34 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | -0.065 |  |
| 2026-08-29 04:12:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.027 |  |
| 2026-08-29 04:11:11 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-08-29 04:09:39 | Magura (Kalu Ganga) | 1.76 | 🟢 Normal | -0.184 |  |
| 2026-08-29 04:08:25 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-29 04:07:35 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -2.483 |  |
| 2026-08-29 04:07:06 | Rathnapura (Kalu Ganga) | 1.66 | 🟢 Normal | -2.483 |  |
| 2026-08-29 04:07:06 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-29 04:06:46 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 04:06:13 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-29 04:05:10 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-29 04:04:03 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:03:50 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:03:06 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:46 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.079 |  |
| 2026-08-29 04:02:39 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:38 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:29 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-08-29 04:02:21 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:48 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:37 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:22 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:17 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:10 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 04:01:08 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-29 03:53:56 | Thalgahagoda (Nilwala Ganga) | 0.46 | 🟢 Normal | 0.382 | 🔺 Rising |
| 2026-08-29 03:49:44 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 04:14:21 | Thalgahagoda (Nilwala Ganga) | 0.59 | 🟢 Normal | 0.382 | 🔺 Rising |
| 2026-08-29 04:08:25 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-29 03:03:37 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-29 04:07:06 | Baddegama (Gin Ganga) | 1.60 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-29 04:01:08 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-29 04:05:10 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-29 04:01:10 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 04:06:46 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-28 17:03:05 | Thanthirimale (Malwathu Oya) | 0.58 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 04:06:13 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-29 03:06:14 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-08-29 04:03:50 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-08-28 17:00:29 | Weraganthota (Mahaweli Ganga) | -3.29 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:38 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:17 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:01:58 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:03:06 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:03:44 | Horowpothana (Yan Oya) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:04:03 | Pitabeddara (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:39 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:17:26 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:03:11 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:29 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:02:21 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:37 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:22 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:34:56 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:04:03 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-29 04:01:17 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-29 03:04:09 | Panadugama (Nilwala Ganga) | 2.98 | 🟢 Normal | -0.010 |  |
| 2026-08-29 04:11:11 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | -0.011 |  |
| 2026-08-28 17:01:59 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | -0.011 |  |
| 2026-08-29 03:06:19 | Padiyathalawa (Maduru Oya) | 0.00 | 🟢 Normal | -0.017 |  |
| 2026-08-29 04:12:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.72 | 🟢 Normal | -0.027 |  |
| 2026-08-29 04:02:21 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | -0.040 |  |
| 2026-08-29 04:12:34 | Glencourse (Kelani Ganga) | 10.21 | 🟢 Normal | -0.065 |  |
| 2026-08-29 04:02:46 | Peradeniya (Mahaweli Ganga) | 3.20 | 🟢 Normal | -0.079 |  |
| 2026-08-29 04:19:25 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | -0.184 |  |
| 2026-08-29 04:07:35 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -2.483 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)