# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_22:22:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **233,597 measurements** from **39** stations.
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
| 2026-08-14 22:22:30 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:13:17 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-08-14 22:13:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-14 22:10:40 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-14 22:10:25 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:10:09 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.057 |  |
| 2026-08-14 22:09:53 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.012 |  |
| 2026-08-14 22:07:56 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-14 22:07:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:07:02 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:06:08 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:05:19 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:04:18 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:04:16 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 22:04:05 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.033 |  |
| 2026-08-14 22:03:50 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-08-14 22:03:48 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-14 22:03:45 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.050 |  |
| 2026-08-14 22:03:37 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-08-14 22:03:19 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:03:14 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-08-14 22:03:09 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-14 22:03:07 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:02:51 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-08-14 22:02:20 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-08-14 22:02:19 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:02:08 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-14 22:01:57 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:01:45 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-14 22:00:52 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:00:18 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-14 22:00:17 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 22:02:51 | Ellagawa (Kalu Ganga) | 5.50 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-08-14 22:10:40 | Glencourse (Kelani Ganga) | 9.75 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-14 22:02:08 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-14 22:00:18 | Peradeniya (Mahaweli Ganga) | 3.18 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-14 22:03:48 | Manampitiya (Mahaweli Ganga) | -0.13 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-08-14 22:13:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.11 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-08-14 22:04:16 | Magura (Kalu Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-14 22:01:45 | Moragaswewa (Deduru Oya) | 0.05 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-14 22:07:56 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-14 22:00:17 | Wellawaya (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:01:50 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:03:19 | Giriulla (Maha Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:00:52 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-14 18:02:32 | Galgamuwa (Mee Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:07:02 | Pitabeddara (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:03:07 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:10:40 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:06:08 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:05:19 | Siyambalanduwa (Heda Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-14 21:02:46 | Thaldena (Mahaweli Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:07:40 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:04:18 | Badalgama (Maha Oya) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:02:19 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:10:25 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:22:30 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:01:57 | Thanamalwila (Kirindi Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-14 22:13:17 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-08-14 22:03:50 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-08-14 22:02:20 | Hanwella (Kelani Ganga) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-08-14 22:03:14 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | -0.010 |  |
| 2026-08-14 22:03:09 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-14 22:03:37 | Baddegama (Gin Ganga) | 1.13 | 🟢 Normal | -0.010 |  |
| 2026-08-14 22:09:53 | Panadugama (Nilwala Ganga) | 2.42 | 🟢 Normal | -0.012 |  |
| 2026-08-14 18:00:09 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.020 |  |
| 2026-08-14 22:04:05 | Nawalapitiya (Mahaweli Ganga) | 1.81 | 🟢 Normal | -0.033 |  |
| 2026-08-14 21:03:03 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | -0.042 |  |
| 2026-08-14 22:03:45 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | -0.050 |  |
| 2026-08-14 18:01:00 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | -0.055 |  |
| 2026-08-14 22:10:09 | Putupaula (Kalu Ganga) | 0.45 | 🟢 Normal | -0.057 |  |

## River Water Level Charts by Station

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)