# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--06_08:17:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **253,265 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-06 08:17:52 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:17:06 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:14:58 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:14:51 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:14:41 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:12:12 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-06 08:11:24 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-09-06 08:11:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.05 | 🟢 Normal | -0.053 |  |
| 2026-09-06 08:09:36 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:09:14 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:08:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.188 |  |
| 2026-09-06 08:08:24 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-09-06 08:08:08 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-09-06 08:07:07 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:05:47 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:05:39 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:05:14 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-06 08:05:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-09-06 08:05:00 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:04:57 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:04:39 | Glencourse (Kelani Ganga) | 9.22 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-06 08:04:09 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:03:50 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.038 |  |
| 2026-09-06 08:03:22 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:03:07 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:03:00 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-06 08:02:47 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:02:37 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-06 08:02:34 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-09-06 08:02:30 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:02:25 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-09-06 08:02:13 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:01:55 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:01:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:01:36 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:01:24 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:00:59 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-06 08:00:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:00:24 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:00:13 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:00:10 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.103 |  |
| 2026-09-06 08:00:06 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-06 08:04:39 | Glencourse (Kelani Ganga) | 9.22 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-09-06 08:12:12 | Ellagawa (Kalu Ganga) | 4.60 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-09-06 08:00:58 | Nawalapitiya (Mahaweli Ganga) | 1.13 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-06 08:05:14 | Galgamuwa (Mee Oya) | -0.12 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-09-06 08:03:00 | Hanwella (Kelani Ganga) | 0.80 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-09-06 08:02:13 | Wellawaya (Kirindi Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:02:47 | Nakkala (Kumbukkan Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:02:30 | Moragaswewa (Deduru Oya) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:01:38 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:09:36 | Giriulla (Maha Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:00:47 | Horowpothana (Yan Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:14:58 | Magura (Kalu Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:14:41 | Pitabeddara (Nilwala Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:04:09 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:09:14 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:05:00 | Moraketiya (Walawe Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:00:59 | Siyambalanduwa (Heda Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:14:51 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:05:39 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:01:24 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:07:07 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:01:36 | Manampitiya (Mahaweli Ganga) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:00:24 | Rathnapura (Kalu Ganga) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:03:07 | Thanthirimale (Malwathu Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:05:47 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:17:06 | Thalgahagoda (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:17:52 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:04:57 | Thanamalwila (Kirindi Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-09-06 08:11:24 | Holombuwa (Kelani Ganga) | 0.18 | 🟢 Normal | -0.009 |  |
| 2026-09-06 08:02:34 | Deraniyagala (Kelani Ganga) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-09-06 08:02:37 | Norwood (Kelani Ganga) | 0.53 | 🟢 Normal | -0.010 |  |
| 2026-09-06 08:02:25 | Peradeniya (Mahaweli Ganga) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-09-06 08:08:08 | Panadugama (Nilwala Ganga) | 2.38 | 🟢 Normal | -0.020 |  |
| 2026-09-06 08:08:24 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | -0.020 |  |
| 2026-09-06 08:05:11 | Nagalagam Street (Kelani Ganga) | 0.43 | 🟢 Normal | -0.030 |  |
| 2026-09-06 08:03:50 | Thaldena (Mahaweli Ganga) | 0.32 | 🟢 Normal | -0.038 |  |
| 2026-09-06 08:11:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.05 | 🟢 Normal | -0.053 |  |
| 2026-09-06 08:00:10 | Weraganthota (Mahaweli Ganga) | -3.10 | 🟢 Normal | -0.103 |  |
| 2026-09-06 08:08:26 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | -0.188 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

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

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)