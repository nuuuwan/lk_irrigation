# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--05_16:27:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **225,721 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 16:27:29 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:20:41 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:19:19 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.008 |  |
| 2026-08-05 16:13:22 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.036 |  |
| 2026-08-05 16:10:55 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.043 |  |
| 2026-08-05 16:10:34 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-08-05 16:08:51 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.029 |  |
| 2026-08-05 16:06:44 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:06:40 | Peradeniya (Mahaweli Ganga) | 6.35 | 🟡 Alert | 0.047 | 🔺 Rising |
| 2026-08-05 16:06:33 | Glencourse (Kelani Ganga) | 12.27 | 🟢 Normal | -0.058 |  |
| 2026-08-05 16:05:31 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | -0.019 |  |
| 2026-08-05 16:05:08 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-05 16:05:08 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-08-05 16:05:05 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:04:36 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-05 16:04:19 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:04:11 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 16:04:02 | Kithulgala (Kelani Ganga) | 2.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-05 16:03:59 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-08-05 16:03:44 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-08-05 16:03:39 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-08-05 16:03:32 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | -0.127 |  |
| 2026-08-05 16:03:25 | Hanwella (Kelani Ganga) | 4.20 | 🟢 Normal | -0.050 |  |
| 2026-08-05 16:03:23 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:03:17 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-08-05 16:03:07 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-08-05 16:02:53 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.029 |  |
| 2026-08-05 16:02:43 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-05 16:02:39 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.048 |  |
| 2026-08-05 16:02:23 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | -0.050 |  |
| 2026-08-05 16:02:15 | Ellagawa (Kalu Ganga) | 8.79 | 🟢 Normal | -0.030 |  |
| 2026-08-05 16:02:04 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:01:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:01:27 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:00:55 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.034 |  |
| 2026-08-05 16:00:52 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-08-05 16:00:23 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 15:59:29 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-05 16:06:40 | Peradeniya (Mahaweli Ganga) | 6.35 | 🟡 Alert | 0.047 | 🔺 Rising |
| 2026-08-05 15:13:19 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-05 16:04:02 | Kithulgala (Kelani Ganga) | 2.65 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-05 16:05:08 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-05 16:04:11 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-05 16:04:36 | Horowpothana (Yan Oya) | 1.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-05 16:01:27 | Weraganthota (Mahaweli Ganga) | -3.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:04:19 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:02:04 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:01:37 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:02:23 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:20:41 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:05:05 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:03:23 | Siyambalanduwa (Heda Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:06:44 | Manampitiya (Mahaweli Ganga) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:27:29 | Urawa (Nilwala Ganga) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:00:23 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-05 16:19:19 | Giriulla (Maha Oya) | 1.26 | 🟢 Normal | -0.008 |  |
| 2026-08-05 16:10:34 | Holombuwa (Kelani Ganga) | 0.80 | 🟢 Normal | -0.009 |  |
| 2026-08-05 16:03:39 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-08-05 16:02:43 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-05 16:03:07 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-08-05 16:00:52 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | -0.010 |  |
| 2026-08-05 16:05:31 | Putupaula (Kalu Ganga) | 2.00 | 🟢 Normal | -0.019 |  |
| 2026-08-05 16:03:44 | Deraniyagala (Kelani Ganga) | 1.42 | 🟢 Normal | -0.019 |  |
| 2026-08-05 16:05:08 | Badalgama (Maha Oya) | 2.45 | 🟢 Normal | -0.020 |  |
| 2026-08-05 16:03:17 | Norwood (Kelani Ganga) | 1.07 | 🟢 Normal | -0.020 |  |
| 2026-08-05 16:08:51 | Panadugama (Nilwala Ganga) | 2.78 | 🟢 Normal | -0.029 |  |
| 2026-08-05 16:02:53 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | -0.029 |  |
| 2026-08-05 16:02:15 | Ellagawa (Kalu Ganga) | 8.79 | 🟢 Normal | -0.030 |  |
| 2026-08-05 16:00:55 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.034 |  |
| 2026-08-05 16:13:22 | Baddegama (Gin Ganga) | 1.68 | 🟢 Normal | -0.036 |  |
| 2026-08-05 16:03:59 | Dunamale (Aththanagalu Oya) | 1.00 | 🟢 Normal | -0.039 |  |
| 2026-08-05 16:10:55 | Thawalama (Gin Ganga) | 1.58 | 🟢 Normal | -0.043 |  |
| 2026-08-05 16:02:39 | Nawalapitiya (Mahaweli Ganga) | 2.45 | 🟢 Normal | -0.048 |  |
| 2026-08-05 16:02:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.98 | 🟢 Normal | -0.050 |  |
| 2026-08-05 16:03:25 | Hanwella (Kelani Ganga) | 4.20 | 🟢 Normal | -0.050 |  |
| 2026-08-05 16:06:33 | Glencourse (Kelani Ganga) | 12.27 | 🟢 Normal | -0.058 |  |
| 2026-08-05 16:03:32 | Rathnapura (Kalu Ganga) | 4.15 | 🟢 Normal | -0.127 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)