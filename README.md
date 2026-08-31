# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--31_13:39:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **248,074 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 13:39:55 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:21:07 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.008 |  |
| 2026-08-31 13:13:22 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:12:59 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:11:47 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:11:02 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-31 13:10:46 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.071 |  |
| 2026-08-31 13:08:19 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-08-31 13:06:53 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | -0.009 |  |
| 2026-08-31 13:06:35 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | -0.019 |  |
| 2026-08-31 13:06:34 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.188 |  |
| 2026-08-31 13:05:33 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-08-31 13:05:18 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:04:37 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-31 13:04:30 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-31 13:04:11 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-08-31 13:04:04 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:03:57 | Manampitiya (Mahaweli Ganga) | -0.52 | 🟢 Normal | -0.010 |  |
| 2026-08-31 13:03:52 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-08-31 13:03:38 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:03:29 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-08-31 13:03:25 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 13:03:08 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:02:51 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:02:51 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:02:30 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:02:09 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:02:06 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-08-31 13:01:42 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:01:21 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:01:20 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-08-31 13:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-31 13:01:15 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:01:07 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:00:53 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:00:46 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:00:44 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:00:43 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.010 |  |
| 2026-08-31 13:00:17 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 12:59:52 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-31 13:05:33 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.133 | 🔺 Rising |
| 2026-08-31 13:03:29 | Kuda Oya (Kirindi Oya) | 0.98 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-08-31 13:01:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.48 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-08-31 13:04:30 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-08-31 13:04:37 | Panadugama (Nilwala Ganga) | 2.91 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-31 13:03:25 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-31 13:11:02 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-31 13:01:42 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:00:46 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:01:07 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:01:21 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:01:00 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:05:18 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:02:51 | Giriulla (Maha Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:00:53 | Horowpothana (Yan Oya) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:13:22 | Galgamuwa (Mee Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:02:51 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:01:15 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:03:38 | Moraketiya (Walawe Ganga) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:00:44 | Siyambalanduwa (Heda Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:03:08 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:02:30 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:02:09 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:04:04 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:12:59 | Rathnapura (Kalu Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:39:55 | Thanthirimale (Malwathu Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:11:47 | Thanamalwila (Kirindi Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-31 13:21:07 | Thawalama (Gin Ganga) | 1.75 | 🟢 Normal | -0.008 |  |
| 2026-08-31 13:06:53 | Ellagawa (Kalu Ganga) | 4.77 | 🟢 Normal | -0.009 |  |
| 2026-08-31 13:03:57 | Manampitiya (Mahaweli Ganga) | -0.52 | 🟢 Normal | -0.010 |  |
| 2026-08-31 13:08:19 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-08-31 13:00:43 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.010 |  |
| 2026-08-31 13:04:11 | Baddegama (Gin Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-08-31 13:03:52 | Pitabeddara (Nilwala Ganga) | 0.76 | 🟢 Normal | -0.010 |  |
| 2026-08-31 13:06:35 | Glencourse (Kelani Ganga) | 9.73 | 🟢 Normal | -0.019 |  |
| 2026-08-31 13:01:20 | Thalgahagoda (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-08-31 13:02:06 | Deraniyagala (Kelani Ganga) | 0.64 | 🟢 Normal | -0.031 |  |
| 2026-08-31 13:10:46 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | -0.071 |  |
| 2026-08-31 13:06:34 | Peradeniya (Mahaweli Ganga) | 2.10 | 🟢 Normal | -0.188 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)