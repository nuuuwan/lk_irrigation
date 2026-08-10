# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_14:12:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,714 measurements** from **39** stations.
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
| 2026-08-10 14:12:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-08-10 14:11:55 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.033 |  |
| 2026-08-10 14:10:58 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:10:57 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:09:55 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.043 |  |
| 2026-08-10 14:09:49 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 14:09:05 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:08:59 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:08:49 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.020 |  |
| 2026-08-10 14:07:26 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-08-10 14:07:16 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:06:02 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 7.448 | 🔺 Rising |
| 2026-08-10 14:06:00 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:05:50 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:05:38 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.059 |  |
| 2026-08-10 14:05:33 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 7.448 | 🔺 Rising |
| 2026-08-10 14:04:13 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:03:53 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | -0.095 |  |
| 2026-08-10 14:03:44 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:03:22 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:03:00 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:02:55 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.012 |  |
| 2026-08-10 14:02:49 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-08-10 14:02:44 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 14:02:24 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.030 |  |
| 2026-08-10 14:02:17 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-08-10 14:02:13 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-10 14:02:13 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.039 |  |
| 2026-08-10 14:02:11 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-10 14:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:01:49 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-08-10 14:01:44 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 14:01:41 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:01:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:01:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-08-10 14:01:28 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-10 14:01:20 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:01:15 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.060 |  |
| 2026-08-10 14:00:38 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:00:31 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:00:12 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 14:06:02 | Badalgama (Maha Oya) | 2.06 | 🟢 Normal | 7.448 | 🔺 Rising |
| 2026-08-10 14:12:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-08-10 14:07:26 | Kithulgala (Kelani Ganga) | 1.97 | 🟢 Normal | 0.103 | 🔺 Rising |
| 2026-08-10 14:02:13 | Deraniyagala (Kelani Ganga) | 0.97 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-08-10 14:01:28 | Putupaula (Kalu Ganga) | 1.00 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-10 14:09:49 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-10 14:02:44 | Thaldena (Mahaweli Ganga) | 0.21 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 14:01:44 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 14:00:12 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:06:00 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:01:57 | Nawalapitiya (Mahaweli Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:01:34 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:01:20 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:09:05 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:10:58 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:03:22 | Baddegama (Gin Ganga) | 2.30 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:07:16 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:04:13 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:03:00 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:03:44 | Holombuwa (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:01:41 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:00:38 | Thanthirimale (Malwathu Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:08:59 | Urawa (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:00:31 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:05:50 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 14:01:49 | Moraketiya (Walawe Ganga) | 0.83 | 🟢 Normal | -0.010 |  |
| 2026-08-10 14:02:11 | Pitabeddara (Nilwala Ganga) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-08-10 14:02:49 | Norwood (Kelani Ganga) | 0.92 | 🟢 Normal | -0.011 |  |
| 2026-08-10 14:02:55 | Panadugama (Nilwala Ganga) | 3.77 | 🟢 Normal | -0.012 |  |
| 2026-08-10 14:08:49 | Peradeniya (Mahaweli Ganga) | 3.60 | 🟢 Normal | -0.020 |  |
| 2026-08-10 14:02:17 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | -0.020 |  |
| 2026-08-10 14:02:24 | Hanwella (Kelani Ganga) | 2.28 | 🟢 Normal | -0.030 |  |
| 2026-08-10 14:01:34 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.031 |  |
| 2026-08-10 14:11:55 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | -0.033 |  |
| 2026-08-10 14:02:13 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | -0.039 |  |
| 2026-08-10 14:09:55 | Weraganthota (Mahaweli Ganga) | -3.06 | 🟢 Normal | -0.043 |  |
| 2026-08-10 14:05:38 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.059 |  |
| 2026-08-10 14:01:15 | Ellagawa (Kalu Ganga) | 6.20 | 🟢 Normal | -0.060 |  |
| 2026-08-10 14:03:53 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | -0.095 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)