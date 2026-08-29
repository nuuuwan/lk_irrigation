# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_03:24:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,786 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 03:24:54 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-30 03:23:38 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.007 |  |
| 2026-08-30 03:22:04 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | -0.015 |  |
| 2026-08-30 03:21:14 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:17:37 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:16:05 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-30 03:11:27 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.017 |  |
| 2026-08-30 03:11:14 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-30 03:10:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-30 03:10:02 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -36.000 |  |
| 2026-08-30 03:10:01 | Magura (Kalu Ganga) | 1.50 | 🟢 Normal | -36.000 |  |
| 2026-08-30 03:10:00 | Magura (Kalu Ganga) | 1.52 | 🟢 Normal | -36.000 |  |
| 2026-08-30 03:07:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:07:40 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:07:19 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:06:52 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-08-30 03:06:50 | Glencourse (Kelani Ganga) | 9.99 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-08-30 03:05:56 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.200 |  |
| 2026-08-30 03:05:53 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:05:43 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.035 |  |
| 2026-08-30 03:05:32 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.011 |  |
| 2026-08-30 03:04:25 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-08-30 03:04:10 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:03:19 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-30 03:03:12 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:02:56 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 03:02:42 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-30 03:02:29 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:02:19 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:01:43 | Giriulla (Maha Oya) | 0.16 | 🟢 Normal | -0.835 |  |
| 2026-08-30 03:01:38 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:01:33 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:01:24 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-30 03:01:23 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:01:17 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-30 03:01:08 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-08-30 02:59:47 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.259 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 03:06:52 | Glencourse (Kelani Ganga) | 10.00 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-08-30 03:04:25 | Peradeniya (Mahaweli Ganga) | 2.72 | 🟢 Normal | 0.259 | 🔺 Rising |
| 2026-08-30 03:10:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-08-30 03:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-30 03:01:17 | Kithulgala (Kelani Ganga) | 2.02 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-30 03:02:56 | Hanwella (Kelani Ganga) | 1.49 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-30 03:24:54 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-08-30 03:11:14 | Thalgahagoda (Nilwala Ganga) | 0.71 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-30 03:16:05 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-08-30 03:01:23 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:07:40 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:07:49 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:02:26 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-29 18:02:54 | Galgamuwa (Mee Oya) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:02:19 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:02:29 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:04:10 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:05:44 | Moraketiya (Walawe Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:03:12 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:01:33 | Dunamale (Aththanagalu Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:01:38 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:02:42 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:21:14 | Badalgama (Maha Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:23:59 | Rathnapura (Kalu Ganga) | 1.57 | 🟢 Normal | 0.000 |  |
| 2026-08-29 18:00:49 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:17:37 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-30 02:10:05 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 03:23:38 | Thawalama (Gin Ganga) | 1.69 | 🟢 Normal | -0.007 |  |
| 2026-08-30 03:03:19 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-08-30 03:01:24 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-30 03:01:08 | Pitabeddara (Nilwala Ganga) | 1.07 | 🟢 Normal | -0.011 |  |
| 2026-08-30 03:05:32 | Ellagawa (Kalu Ganga) | 5.11 | 🟢 Normal | -0.011 |  |
| 2026-08-30 03:22:04 | Moragaswewa (Deduru Oya) | -0.23 | 🟢 Normal | -0.015 |  |
| 2026-08-30 03:11:27 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.017 |  |
| 2026-08-29 18:01:39 | Weraganthota (Mahaweli Ganga) | -3.51 | 🟢 Normal | -0.030 |  |
| 2026-08-30 03:05:43 | Panadugama (Nilwala Ganga) | 3.63 | 🟢 Normal | -0.035 |  |
| 2026-08-30 03:05:56 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.200 |  |
| 2026-08-30 03:01:43 | Giriulla (Maha Oya) | 0.16 | 🟢 Normal | -0.835 |  |
| 2026-08-30 03:10:02 | Magura (Kalu Ganga) | 1.49 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)