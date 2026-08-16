# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_18:10:59-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,250 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 18:10:59 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:07:55 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-08-16 18:07:36 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:06:57 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-08-16 18:06:55 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.036 |  |
| 2026-08-16 18:06:22 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:05:42 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.122 |  |
| 2026-08-16 18:05:36 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-16 18:05:15 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:04:13 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-08-16 18:04:08 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.022 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 18:01:41 | Moragaswewa (Deduru Oya) | 0.09 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-08-16 18:02:27 | Thalgahagoda (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-16 18:03:38 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-16 18:04:08 | Baddegama (Gin Ganga) | 1.17 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-16 18:02:25 | Panadugama (Nilwala Ganga) | 2.51 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-16 18:00:49 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:01:45 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:07:36 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:02:18 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:00:09 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:02:57 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:03:46 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:06:22 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:01:41 | Ellagawa (Kalu Ganga) | 5.13 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:02:37 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:02:06 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:02:19 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:05:15 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:02:19 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:02:09 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:10:59 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:00:38 | Thawalama (Gin Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:02:21 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 18:07:55 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | -0.009 |  |
| 2026-08-16 18:05:36 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | -0.010 |  |
| 2026-08-16 18:03:24 | Thanamalwila (Kirindi Oya) | 0.14 | 🟢 Normal | -0.010 |  |
| 2026-08-16 18:06:57 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-08-16 18:03:20 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-08-16 18:03:12 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |
| 2026-08-16 18:01:38 | Putupaula (Kalu Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-08-16 18:02:26 | Hanwella (Kelani Ganga) | 1.37 | 🟢 Normal | -0.021 |  |
| 2026-08-16 18:02:18 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.26 | 🟢 Normal | -0.022 |  |
| 2026-08-16 18:04:13 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | -0.030 |  |
| 2026-08-16 18:06:55 | Magura (Kalu Ganga) | 1.41 | 🟢 Normal | -0.036 |  |
| 2026-08-16 18:03:38 | Glencourse (Kelani Ganga) | 9.55 | 🟢 Normal | -0.052 |  |
| 2026-08-16 18:03:04 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | -0.090 |  |
| 2026-08-16 18:03:34 | Deraniyagala (Kelani Ganga) | 1.00 | 🟢 Normal | -0.103 |  |
| 2026-08-16 18:05:42 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.122 |  |
| 2026-08-16 18:00:40 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | -0.141 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)