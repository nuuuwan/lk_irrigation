# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--14_01:40:15-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **232,808 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **28** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 01:40:15 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:20:47 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-08-14 01:12:38 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:08:31 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.019 |  |
| 2026-08-14 01:07:52 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.019 |  |
| 2026-08-14 01:05:50 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:05:42 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-08-14 01:05:00 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-08-14 01:04:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:04:13 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:04:05 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-14 01:03:50 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:03:32 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:03:26 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:03:23 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-14 01:03:18 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:02:36 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:02:35 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:02:34 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-08-14 01:02:16 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-14 01:02:13 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:01:53 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:01:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-14 01:01:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:01:21 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:01:12 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-08-14 01:01:00 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.040 |  |
| 2026-08-14 01:00:46 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-14 01:01:52 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-14 01:03:23 | Kithulgala (Kelani Ganga) | 1.90 | 🟢 Normal | 0.089 | 🔺 Rising |
| 2026-08-14 00:03:00 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | 0.087 | 🔺 Rising |
| 2026-08-14 00:16:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-08-14 00:06:49 | Putupaula (Kalu Ganga) | 0.42 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-14 01:02:16 | Ellagawa (Kalu Ganga) | 4.80 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-08-14 00:00:28 | Wellawaya (Kirindi Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:01:29 | Nakkala (Kumbukkan Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:12:38 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:40:15 | Nawalapitiya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:01:46 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:04:13 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:13:34 | Galgamuwa (Mee Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:14:01 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:03:26 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:03:50 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:09:59 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:02:35 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:04:30 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:03:32 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:05:50 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-13 18:06:46 | Thanthirimale (Malwathu Oya) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:01:53 | Peradeniya (Mahaweli Ganga) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:03:18 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:01:21 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-14 01:02:13 | Thanamalwila (Kirindi Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-08-14 00:14:04 | Magura (Kalu Ganga) | 1.39 | 🟢 Normal | -0.005 |  |
| 2026-08-14 01:20:47 | Thalgahagoda (Nilwala Ganga) | 0.29 | 🟢 Normal | -0.008 |  |
| 2026-08-14 01:04:05 | Dunamale (Aththanagalu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-08-14 01:00:46 | Thawalama (Gin Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-08-14 01:01:12 | Pitabeddara (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.011 |  |
| 2026-08-14 01:07:52 | Glencourse (Kelani Ganga) | 9.96 | 🟢 Normal | -0.019 |  |
| 2026-08-14 01:08:31 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.019 |  |
| 2026-08-14 00:03:41 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | -0.019 |  |
| 2026-08-14 01:05:00 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-08-14 01:05:42 | Baddegama (Gin Ganga) | 1.26 | 🟢 Normal | -0.020 |  |
| 2026-08-14 01:02:34 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | -0.021 |  |
| 2026-08-13 18:00:14 | Weraganthota (Mahaweli Ganga) | -3.27 | 🟢 Normal | -0.040 |  |
| 2026-08-14 01:01:00 | Horowpothana (Yan Oya) | 1.63 | 🟢 Normal | -0.040 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)