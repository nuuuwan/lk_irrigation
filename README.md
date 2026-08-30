# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--30_06:34:17-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **246,895 measurements** from **39** stations.
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
| 2026-08-30 06:34:17 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-30 06:31:40 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | -0.001 |  |
| 2026-08-30 06:14:38 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:14:14 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:13:41 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | -0.009 |  |
| 2026-08-30 06:13:12 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:12:59 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.079 |  |
| 2026-08-30 06:10:02 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:09:41 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-30 06:07:44 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:07:15 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-30 06:06:05 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:05:35 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:05:30 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:05:23 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:05:19 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 06:04:32 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.029 |  |
| 2026-08-30 06:04:03 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:03:50 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-30 06:03:39 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 06:03:37 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:03:28 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:03:27 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.035 |  |
| 2026-08-30 06:03:16 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:03:10 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-30 06:03:05 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.042 |  |
| 2026-08-30 06:02:42 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.036 |  |
| 2026-08-30 06:02:36 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-08-30 06:02:35 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:02:33 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.013 |  |
| 2026-08-30 06:02:21 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-08-30 06:02:20 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:02:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:02:17 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-30 06:02:17 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.003 |  |
| 2026-08-30 06:02:02 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-08-30 06:01:36 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:01:25 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | -0.056 |  |
| 2026-08-30 06:00:40 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:00:34 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.107 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-30 06:00:34 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | 0.107 | 🔺 Rising |
| 2026-08-30 06:03:10 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-08-30 06:02:17 | Thalgahagoda (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-08-30 06:03:50 | Peradeniya (Mahaweli Ganga) | 2.74 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-30 06:34:17 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-30 06:09:41 | Baddegama (Gin Ganga) | 1.76 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-30 06:05:19 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 06:03:39 | Moragaswewa (Deduru Oya) | -0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-30 06:07:15 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-30 06:00:40 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:01:36 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:03:37 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:02:20 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:14:38 | Horowpothana (Yan Oya) | 1.66 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:05:23 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:05:30 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:06:05 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:03:28 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:10:02 | Thaldena (Mahaweli Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:02:35 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:13:12 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:01:25 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-29 18:00:49 | Thanthirimale (Malwathu Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:14:14 | Urawa (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:04:03 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:05:35 | Thanamalwila (Kirindi Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-30 06:31:40 | Galgamuwa (Mee Oya) | -0.08 | 🟢 Normal | -0.001 |  |
| 2026-08-30 06:02:17 | Weraganthota (Mahaweli Ganga) | -3.55 | 🟢 Normal | -0.003 |  |
| 2026-08-30 06:13:41 | Panadugama (Nilwala Ganga) | 3.59 | 🟢 Normal | -0.009 |  |
| 2026-08-30 06:02:36 | Giriulla (Maha Oya) | 0.94 | 🟢 Normal | -0.010 |  |
| 2026-08-30 06:02:02 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.010 |  |
| 2026-08-30 06:02:33 | Hanwella (Kelani Ganga) | 1.53 | 🟢 Normal | -0.013 |  |
| 2026-08-30 06:04:32 | Glencourse (Kelani Ganga) | 9.90 | 🟢 Normal | -0.029 |  |
| 2026-08-30 06:02:21 | Deraniyagala (Kelani Ganga) | 0.82 | 🟢 Normal | -0.030 |  |
| 2026-08-30 06:03:27 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | -0.035 |  |
| 2026-08-30 06:02:42 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | -0.036 |  |
| 2026-08-30 06:03:05 | Pitabeddara (Nilwala Ganga) | 1.01 | 🟢 Normal | -0.042 |  |
| 2026-08-30 06:01:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.68 | 🟢 Normal | -0.056 |  |
| 2026-08-30 06:12:59 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.079 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)