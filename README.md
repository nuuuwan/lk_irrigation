# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--17_18:06:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **236,135 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **36** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 18:06:55 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:06:25 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:06:22 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:05:14 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 18:05:14 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 18:05:08 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:39 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:31 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:21 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:13 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:03 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-17 18:03:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.125 |  |
| 2026-08-17 18:03:49 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-17 18:03:37 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-17 18:03:28 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-08-17 18:03:16 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.029 |  |
| 2026-08-17 18:03:08 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-17 18:02:57 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.080 |  |
| 2026-08-17 18:02:40 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:02:33 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-08-17 18:02:31 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:02:30 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-17 18:02:21 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-17 18:01:55 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:01:48 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-17 18:01:45 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:01:31 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:01:28 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:01:17 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.102 |  |
| 2026-08-17 18:01:17 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-17 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:00:44 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:00:18 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-17 18:00:13 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-17 18:02:33 | Rathnapura (Kalu Ganga) | 1.76 | 🟢 Normal | 0.097 | 🔺 Rising |
| 2026-08-17 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.45 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-08-17 18:01:16 | Nawalapitiya (Mahaweli Ganga) | 1.67 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-08-17 18:03:08 | Deraniyagala (Kelani Ganga) | 1.23 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-08-17 18:00:18 | Putupaula (Kalu Ganga) | 0.74 | 🟢 Normal | 0.042 | 🔺 Rising |
| 2026-08-17 18:01:48 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-08-17 18:03:49 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-08-17 18:02:30 | Ellagawa (Kalu Ganga) | 5.35 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-17 18:03:37 | Thawalama (Gin Ganga) | 1.45 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-17 17:05:08 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-17 18:02:21 | Thanamalwila (Kirindi Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 18:05:14 | Glencourse (Kelani Ganga) | 9.76 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 18:05:14 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-17 18:01:09 | Weraganthota (Mahaweli Ganga) | -3.44 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:01:28 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:01:17 | Moragaswewa (Deduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:02:40 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:02:31 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:06:25 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:13 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:21 | Magura (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-17 17:02:25 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:39 | Hanwella (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:05:08 | Panadugama (Nilwala Ganga) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:31 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:00:13 | Moraketiya (Walawe Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:01:45 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-08-17 17:06:35 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:06:55 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:01:55 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:06:22 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:00:44 | Thanthirimale (Malwathu Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:01:31 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-17 18:04:03 | Wellawaya (Kirindi Oya) | 0.50 | 🟢 Normal | -0.010 |  |
| 2026-08-17 18:03:28 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | -0.010 |  |
| 2026-08-17 18:03:16 | Manampitiya (Mahaweli Ganga) | -0.20 | 🟢 Normal | -0.029 |  |
| 2026-08-17 18:02:57 | Peradeniya (Mahaweli Ganga) | 2.68 | 🟢 Normal | -0.080 |  |
| 2026-08-17 18:01:17 | Kithulgala (Kelani Ganga) | 1.95 | 🟢 Normal | -0.102 |  |
| 2026-08-17 18:03:57 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.125 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)