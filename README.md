# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_10:27:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,356 measurements** from **39** stations.
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
| 2026-08-12 10:27:18 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | -0.007 |  |
| 2026-08-12 10:23:34 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-12 10:21:44 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-12 10:15:14 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:12:34 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.027 |  |
| 2026-08-12 10:10:05 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.037 |  |
| 2026-08-12 10:08:48 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-08-12 10:07:36 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:07:07 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-08-12 10:06:46 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | -0.010 |  |
| 2026-08-12 10:06:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:05:59 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -2.191 |  |
| 2026-08-12 10:05:45 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.013 |  |
| 2026-08-12 10:05:29 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.020 |  |
| 2026-08-12 10:05:28 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:05:28 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:05:19 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:05:03 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-08-12 10:04:54 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.048 |  |
| 2026-08-12 10:04:14 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:04:10 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:04:06 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:03:29 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:03:27 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:03:10 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.020 |  |
| 2026-08-12 10:03:04 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:03:03 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | -0.010 |  |
| 2026-08-12 10:02:58 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-08-12 10:02:55 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-12 10:02:43 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:02:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:02:05 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:01:25 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:00:55 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.032 |  |
| 2026-08-12 10:00:40 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:00:36 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-08-12 10:00:26 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-12 09:57:01 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 10:02:55 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-12 10:21:44 | Magura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-12 10:23:34 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-08-12 10:00:40 | Weraganthota (Mahaweli Ganga) | -3.33 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:03:04 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:00:26 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-12 09:03:17 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:02:41 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:05:28 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:04:06 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:03:29 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:02:43 | Norwood (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:03:27 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:04:14 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:06:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:07:36 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:01:25 | Dunamale (Aththanagalu Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:04:10 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:05:19 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:10:05 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:05:28 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:15:14 | Urawa (Nilwala Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:02:05 | Thanamalwila (Kirindi Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-12 10:27:18 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | -0.007 |  |
| 2026-08-12 10:08:48 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-08-12 10:06:46 | Glencourse (Kelani Ganga) | 10.51 | 🟢 Normal | -0.010 |  |
| 2026-08-12 10:07:07 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-08-12 10:03:03 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | -0.010 |  |
| 2026-08-12 10:05:45 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.013 |  |
| 2026-08-12 10:05:29 | Ellagawa (Kalu Ganga) | 5.28 | 🟢 Normal | -0.020 |  |
| 2026-08-12 10:03:10 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.020 |  |
| 2026-08-12 10:02:58 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.020 |  |
| 2026-08-12 10:00:36 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-08-12 10:05:03 | Baddegama (Gin Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-08-12 10:12:34 | Kithulgala (Kelani Ganga) | 2.22 | 🟢 Normal | -0.027 |  |
| 2026-08-12 10:00:55 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | -0.032 |  |
| 2026-08-12 10:09:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.22 | 🟢 Normal | -0.037 |  |
| 2026-08-12 10:04:54 | Rathnapura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.048 |  |
| 2026-08-12 10:05:59 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | -2.191 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)