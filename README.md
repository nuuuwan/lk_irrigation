# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--08_05:11:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **227,549 measurements** from **39** stations.
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
| 2026-08-08 05:11:28 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-08 05:11:13 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.017 |  |
| 2026-08-08 05:09:34 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.011 |  |
| 2026-08-08 05:09:18 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 05:08:52 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 05:08:33 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:06:38 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | -0.028 |  |
| 2026-08-08 05:06:19 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:05:53 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:05:09 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:04:47 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:04:41 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:04:40 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:04:31 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-08 05:03:57 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-08-08 05:03:22 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-08 05:03:10 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:02:52 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:02:26 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:02:20 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:02:10 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:01:18 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 05:01:14 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-08 05:01:10 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.040 |  |
| 2026-08-08 05:00:59 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:00:56 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:00:55 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:00:53 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:44:59 | Thalgahagoda (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-08 04:38:21 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.026 |  |
| 2026-08-08 04:30:23 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 04:28:07 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-08 05:03:22 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-08-08 05:04:31 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-08 05:01:14 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-08 05:08:52 | Pitabeddara (Nilwala Ganga) | 0.57 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-08 05:11:28 | Baddegama (Gin Ganga) | 1.50 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-08 05:01:18 | Moraketiya (Walawe Ganga) | 0.73 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 05:09:18 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-08 04:22:53 | Panadugama (Nilwala Ganga) | 2.50 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-08 05:02:26 | Kithulgala (Kelani Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-08-07 18:00:27 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:00:59 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:00:53 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:00:55 | Nawalapitiya (Mahaweli Ganga) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:02:10 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:04:40 | Giriulla (Maha Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:03:10 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-08-07 18:10:22 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:04:41 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:02:52 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:06:19 | Glencourse (Kelani Ganga) | 10.88 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:00:56 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:04:47 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:05:53 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:05:09 | Holombuwa (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:02:20 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-07 18:01:27 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:08:33 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:01:10 | Peradeniya (Mahaweli Ganga) | 3.70 | 🟢 Normal | 0.000 |  |
| 2026-08-08 03:01:22 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-08 03:03:37 | Thanamalwila (Kirindi Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-08 05:03:57 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-08-08 05:09:34 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | -0.011 |  |
| 2026-08-08 05:11:13 | Hanwella (Kelani Ganga) | 2.43 | 🟢 Normal | -0.017 |  |
| 2026-08-08 04:38:21 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.026 |  |
| 2026-08-08 05:06:38 | Ellagawa (Kalu Ganga) | 5.36 | 🟢 Normal | -0.028 |  |
| 2026-08-08 04:03:57 | Rathnapura (Kalu Ganga) | 1.72 | 🟢 Normal | -0.031 |  |
| 2026-08-08 04:19:25 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | -0.035 |  |
| 2026-08-08 05:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.70 | 🟢 Normal | -0.040 |  |
| 2026-08-08 03:12:16 | Magura (Kalu Ganga) | 1.48 | 🟢 Normal | -72.000 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)