# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--29_14:29:09-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,311 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 14:29:09 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-29 14:15:22 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-29 14:13:29 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-29 14:10:51 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:09:40 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:09:37 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:09:01 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:08:38 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-29 14:08:17 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:07:16 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:06:00 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-29 14:05:38 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 14:05:34 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.049 |  |
| 2026-08-29 14:05:12 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:04:57 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:04:52 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:04:51 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:04:34 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-29 14:04:25 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:04:21 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 14:04:02 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-08-29 14:03:52 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:03:50 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | -0.010 |  |
| 2026-08-29 14:03:36 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-29 14:03:16 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 14:02:49 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-29 14:02:45 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:02:07 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-08-29 14:02:00 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-29 14:01:50 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-29 14:01:44 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:01:32 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.161 |  |
| 2026-08-29 14:01:16 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:01:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:00:57 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:00:50 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-08-29 14:00:34 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:00:18 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.045 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-29 14:02:49 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-29 14:02:00 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-29 14:03:36 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-29 14:15:22 | Panadugama (Nilwala Ganga) | 3.67 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-29 14:00:18 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-29 14:04:34 | Nawalapitiya (Mahaweli Ganga) | 1.55 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-29 14:13:29 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-29 14:08:38 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-08-29 14:03:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.54 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-29 14:05:38 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 14:04:21 | Kithulgala (Kelani Ganga) | 1.83 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-29 14:29:09 | Baddegama (Gin Ganga) | 1.72 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-29 14:03:16 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-29 13:00:09 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:03:52 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:01:11 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:04:51 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:09:40 | Magura (Kalu Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:04:25 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:02:45 | Hanwella (Kelani Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:01:16 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:00:34 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:05:12 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:10:51 | Dunamale (Aththanagalu Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:09:37 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:08:17 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:00:57 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:01:44 | Thawalama (Gin Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:09:01 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:07:16 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:04:52 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-29 14:03:50 | Ellagawa (Kalu Ganga) | 5.21 | 🟢 Normal | -0.010 |  |
| 2026-08-29 14:02:07 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | -0.010 |  |
| 2026-08-29 14:06:00 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | -0.010 |  |
| 2026-08-29 14:01:50 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.010 |  |
| 2026-08-29 14:04:02 | Rathnapura (Kalu Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-08-29 14:00:50 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | -0.010 |  |
| 2026-08-29 14:05:34 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.049 |  |
| 2026-08-29 14:01:32 | Manampitiya (Mahaweli Ganga) | -0.29 | 🟢 Normal | -0.161 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)