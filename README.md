# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--12_14:24:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **231,516 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **10** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 14:24:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-12 14:15:46 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:15:07 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:11:11 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:09:40 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:09:28 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-08-12 14:09:21 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:08:44 | Peradeniya (Mahaweli Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:06:59 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-12 14:05:00 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.020 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-12 14:03:35 | Putupaula (Kalu Ganga) | 0.80 | 🟢 Normal | 0.108 | 🔺 Rising |
| 2026-08-12 14:24:28 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.56 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-08-12 14:02:14 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-08-12 14:02:31 | Nagalagam Street (Kelani Ganga) | 0.75 | 🟢 Normal | 0.046 | 🔺 Rising |
| 2026-08-12 14:00:12 | Thalgahagoda (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-08-12 14:04:02 | Kithulgala (Kelani Ganga) | 2.20 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-12 14:04:36 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-12 14:05:00 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-12 14:01:53 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-08-12 14:04:01 | Nawalapitiya (Mahaweli Ganga) | 1.62 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-12 14:09:21 | Wellawaya (Kirindi Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:02:22 | Nakkala (Kumbukkan Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:04:34 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:01:33 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:01:31 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:03:22 | Hanwella (Kelani Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:15:07 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:01:11 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:02:59 | Moraketiya (Walawe Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:02:30 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:15:46 | Dunamale (Aththanagalu Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:03:11 | Badalgama (Maha Oya) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:11:11 | Holombuwa (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:00:57 | Thanthirimale (Malwathu Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:08:44 | Peradeniya (Mahaweli Ganga) | 3.33 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:04:22 | Urawa (Nilwala Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:03:49 | Kuda Oya (Kirindi Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:01:52 | Thanamalwila (Kirindi Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-08-12 14:04:21 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.009 |  |
| 2026-08-12 14:04:41 | Norwood (Kelani Ganga) | 0.77 | 🟢 Normal | -0.010 |  |
| 2026-08-12 14:06:59 | Pitabeddara (Nilwala Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-08-12 14:03:21 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | -0.010 |  |
| 2026-08-12 14:02:42 | Ellagawa (Kalu Ganga) | 5.25 | 🟢 Normal | -0.011 |  |
| 2026-08-12 14:02:03 | Giriulla (Maha Oya) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-08-12 14:09:28 | Magura (Kalu Ganga) | 1.61 | 🟢 Normal | -0.019 |  |
| 2026-08-12 14:03:18 | Glencourse (Kelani Ganga) | 10.46 | 🟢 Normal | -0.020 |  |
| 2026-08-12 14:04:22 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.021 |  |
| 2026-08-12 14:02:39 | Rathnapura (Kalu Ganga) | 1.52 | 🟢 Normal | -0.042 |  |
| 2026-08-12 14:01:29 | Weraganthota (Mahaweli Ganga) | -3.01 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)