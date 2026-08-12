# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_17:03:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,614 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 17:03:46 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:03:30 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-08-12 17:03:27 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-12 17:02:51 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.052 |  |
| 2026-08-12 17:02:39 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:02:38 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.015 |  |
| 2026-08-12 17:02:30 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:02:23 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-08-12 17:02:16 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-12 17:01:55 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:01:50 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:01:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:01:41 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:01:24 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-12 17:01:18 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:00:52 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 17:00:33 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:00:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.031 |  |
| 2026-08-12 16:22:41 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | -0.015 |  |
| 2026-08-12 16:20:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-12 16:17:33 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.009 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 16:20:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.69 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-08-12 17:01:24 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-12 17:02:16 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-12 16:02:24 | Baddegama (Gin Ganga) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 17:00:52 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 16:17:33 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-12 17:01:41 | Wellawaya (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:01:44 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:01:55 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:01:18 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 16:08:15 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 16:13:45 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-08-12 16:06:22 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-12 16:07:48 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:03:46 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-12 16:03:25 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-12 16:05:29 | Moraketiya (Walawe Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:02:30 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:02:39 | Dunamale (Aththanagalu Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-12 16:02:41 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-12 16:08:00 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 16:00:42 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:00:33 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-12 16:10:57 | Peradeniya (Mahaweli Ganga) | 3.34 | 🟢 Normal | 0.000 |  |
| 2026-08-12 17:01:50 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-12 16:05:17 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | -0.005 |  |
| 2026-08-12 16:05:35 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-08-12 17:03:27 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | -0.010 |  |
| 2026-08-12 17:02:38 | Badalgama (Maha Oya) | 1.99 | 🟢 Normal | -0.015 |  |
| 2026-08-12 16:12:03 | Ellagawa (Kalu Ganga) | 5.22 | 🟢 Normal | -0.018 |  |
| 2026-08-12 16:05:39 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.019 |  |
| 2026-08-12 16:04:09 | Thaldena (Mahaweli Ganga) | 0.18 | 🟢 Normal | -0.020 |  |
| 2026-08-12 17:02:23 | Thanamalwila (Kirindi Oya) | 0.22 | 🟢 Normal | -0.020 |  |
| 2026-08-12 17:03:30 | Nawalapitiya (Mahaweli Ganga) | 1.65 | 🟢 Normal | -0.020 |  |
| 2026-08-12 17:00:21 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.031 |  |
| 2026-08-12 17:02:51 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.052 |  |
| 2026-08-12 16:04:25 | Kithulgala (Kelani Ganga) | 2.19 | 🟢 Normal | -0.060 |  |
| 2026-08-12 16:03:09 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.061 |  |
| 2026-08-12 16:02:57 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)