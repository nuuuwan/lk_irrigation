# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--25_13:13:25-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,097 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 13:13:25 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:11:40 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-25 13:11:35 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:10:33 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:10:03 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:09:13 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-25 13:08:18 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.054 |  |
| 2026-08-25 13:07:39 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-25 13:07:19 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 13:06:47 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:06:40 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-25 13:06:20 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:06:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.73 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-25 13:05:59 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:05:13 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-08-25 13:05:06 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:04:50 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 13:04:46 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-08-25 13:04:45 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-08-25 13:04:35 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:04:34 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.708 | 🔺 Rising |
| 2026-08-25 13:04:21 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-25 13:04:13 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:03:51 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:03:45 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-25 13:03:37 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:03:22 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:03:17 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:02:51 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:02:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:02:39 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:02:33 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:02:22 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-25 13:02:00 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:01:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:01:44 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:01:31 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:01:15 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 13:00:51 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:00:27 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-25 13:00:10 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 12:31:16 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.089 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-25 13:04:34 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.708 | 🔺 Rising |
| 2026-08-25 13:05:13 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | 0.176 | 🔺 Rising |
| 2026-08-25 13:04:46 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-08-25 13:11:40 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-25 13:09:13 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | 0.074 | 🔺 Rising |
| 2026-08-25 13:06:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.73 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-08-25 13:02:22 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-25 13:00:27 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-25 13:07:39 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-08-25 13:04:21 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-25 13:01:15 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 13:04:50 | Moragaswewa (Deduru Oya) | -0.08 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-25 13:07:19 | Urawa (Nilwala Ganga) | 0.19 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-25 13:05:06 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:00:10 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:11:35 | Nawalapitiya (Mahaweli Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:02:39 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:04:35 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:00:51 | Horowpothana (Yan Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:06:47 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:02:39 | Magura (Kalu Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:01:44 | Pitabeddara (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:03:17 | Hanwella (Kelani Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:10:03 | Panadugama (Nilwala Ganga) | 2.49 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:05:59 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:10:33 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:02:00 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:03:37 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:01:57 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:06:20 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:02:33 | Manampitiya (Mahaweli Ganga) | -0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:13:25 | Rathnapura (Kalu Ganga) | 1.44 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:01:31 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:03:22 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:04:13 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-25 13:06:40 | Dunamale (Aththanagalu Oya) | 0.62 | 🟢 Normal | -0.010 |  |
| 2026-08-25 13:03:45 | Norwood (Kelani Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-08-25 13:04:45 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | -0.011 |  |
| 2026-08-25 13:08:18 | Peradeniya (Mahaweli Ganga) | 2.52 | 🟢 Normal | -0.054 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)