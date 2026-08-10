# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_21:12:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **229,982 measurements** from **39** stations.
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
| 2026-08-10 21:12:48 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:11:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | -0.037 |  |
| 2026-08-10 21:11:27 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | -0.056 |  |
| 2026-08-10 21:10:24 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-08-10 21:10:15 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:08:09 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:07:25 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:06:55 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:06:25 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-08-10 21:06:21 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:05:36 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:05:34 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-10 21:05:32 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:04:22 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:03:55 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-08-10 21:03:29 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 21:02:58 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:02:58 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 21:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-08-10 21:02:51 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:02:47 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:02:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:02:39 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-08-10 21:02:33 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:02:11 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 21:02:08 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:01:32 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:01:26 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:01:17 | Ellagawa (Kalu Ganga) | 5.89 | 🟢 Normal | -0.030 |  |
| 2026-08-10 21:01:16 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:01:13 | Peradeniya (Mahaweli Ganga) | 3.54 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:01:06 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:00:52 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:00:51 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.033 |  |
| 2026-08-10 21:00:37 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 20:32:18 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-10 20:28:58 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 21:05:34 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-10 21:03:29 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 21:02:11 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-10 21:02:58 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 21:02:51 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:02:58 | Wellawaya (Kirindi Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:01:16 | Nakkala (Kumbukkan Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:01:06 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:01:48 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:02:33 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:00:37 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:02:17 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:05:32 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:07:25 | Hanwella (Kelani Ganga) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:02:08 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:05:36 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:01:26 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:00:52 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:08:09 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:02:39 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:06:21 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:04:22 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:42:25 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:10:15 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:01:13 | Peradeniya (Mahaweli Ganga) | 3.54 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:12:48 | Urawa (Nilwala Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-08-10 20:28:58 | Thalgahagoda (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:06:55 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:02:47 | Thanamalwila (Kirindi Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:06:25 | Pitabeddara (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-08-10 21:02:52 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-08-10 21:10:24 | Magura (Kalu Ganga) | 1.75 | 🟢 Normal | -0.010 |  |
| 2026-08-10 21:02:39 | Deraniyagala (Kelani Ganga) | 1.01 | 🟢 Normal | -0.020 |  |
| 2026-08-10 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-10 21:03:55 | Rathnapura (Kalu Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-08-10 21:01:17 | Ellagawa (Kalu Ganga) | 5.89 | 🟢 Normal | -0.030 |  |
| 2026-08-10 21:00:51 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.033 |  |
| 2026-08-10 21:11:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.12 | 🟢 Normal | -0.037 |  |
| 2026-08-10 21:11:27 | Panadugama (Nilwala Ganga) | 3.56 | 🟢 Normal | -0.056 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)