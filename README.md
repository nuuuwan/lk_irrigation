# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--19_17:14:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **237,879 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 17:14:34 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:13:26 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:12:59 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-19 17:10:10 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:08:10 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | -0.009 |  |
| 2026-08-19 17:07:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.065 |  |
| 2026-08-19 17:07:24 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:07:22 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:07:02 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-19 17:07:02 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-08-19 17:06:49 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-19 17:06:41 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:06:41 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-08-19 17:05:42 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-19 17:02:28 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.127 | 🔺 Rising |
| 2026-08-19 17:01:11 | Nawalapitiya (Mahaweli Ganga) | 1.51 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-08-19 17:12:59 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2026-08-19 17:01:44 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-08-19 17:06:49 | Peradeniya (Mahaweli Ganga) | 2.60 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-19 17:07:02 | Magura (Kalu Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-19 17:03:50 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-19 17:02:43 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-19 17:02:59 | Wellawaya (Kirindi Oya) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-19 17:02:08 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:07:22 | Giriulla (Maha Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:00:42 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:01:55 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:03:57 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:03:00 | Hanwella (Kelani Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:05:21 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:01:18 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:02:43 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:00:29 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:10:10 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:06:41 | Thaldena (Mahaweli Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:07:24 | Katharagama (Menik Ganga) | -0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:03:04 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:14:34 | Manampitiya (Mahaweli Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:04:03 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:13:26 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:01:28 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:01:21 | Thanamalwila (Kirindi Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-19 17:08:10 | Moragaswewa (Deduru Oya) | -0.15 | 🟢 Normal | -0.009 |  |
| 2026-08-19 17:02:42 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | -0.010 |  |
| 2026-08-19 17:02:31 | Baddegama (Gin Ganga) | 1.09 | 🟢 Normal | -0.010 |  |
| 2026-08-19 17:00:18 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-08-19 17:05:42 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-08-19 17:07:02 | Thawalama (Gin Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-08-19 17:06:41 | Putupaula (Kalu Ganga) | 0.73 | 🟢 Normal | -0.019 |  |
| 2026-08-19 17:02:24 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.020 |  |
| 2026-08-19 17:01:06 | Ellagawa (Kalu Ganga) | 5.00 | 🟢 Normal | -0.030 |  |
| 2026-08-19 17:03:54 | Glencourse (Kelani Ganga) | 9.60 | 🟢 Normal | -0.040 |  |
| 2026-08-19 17:07:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.04 | 🟢 Normal | -0.065 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

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

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)