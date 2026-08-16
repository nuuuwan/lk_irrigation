# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--16_16:19:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **235,171 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 16:19:19 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:17:28 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-16 16:12:42 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-16 16:09:07 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:08:59 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:08:26 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.052 |  |
| 2026-08-16 16:07:12 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:07:11 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:06:24 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-16 16:06:21 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:06:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-08-16 16:05:58 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-16 16:05:47 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:05:38 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-16 16:05:38 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.093 |  |
| 2026-08-16 16:05:29 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-08-16 16:04:18 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.020 |  |
| 2026-08-16 16:04:16 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:04:10 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:04:05 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:03:44 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.019 |  |
| 2026-08-16 16:03:38 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-16 16:03:12 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:03:05 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:03:01 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.021 |  |
| 2026-08-16 16:03:01 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:02:52 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:02:28 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-08-16 16:02:26 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:02:26 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-08-16 16:02:17 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-16 16:02:11 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:01:59 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-16 16:01:12 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-16 16:00:58 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:00:48 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-16 16:00:12 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:00:08 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-16 16:02:28 | Deraniyagala (Kelani Ganga) | 1.02 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-08-16 16:01:59 | Putupaula (Kalu Ganga) | 0.75 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-08-16 16:00:48 | Siyambalanduwa (Heda Oya) | 0.22 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-08-16 16:17:28 | Thalgahagoda (Nilwala Ganga) | 0.32 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-08-16 16:06:24 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-16 16:01:12 | Rathnapura (Kalu Ganga) | 1.34 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-16 16:02:17 | Dunamale (Aththanagalu Oya) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-16 16:03:38 | Peradeniya (Mahaweli Ganga) | 2.70 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-16 16:12:42 | Panadugama (Nilwala Ganga) | 2.46 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-08-16 16:05:38 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-16 16:05:58 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-16 16:00:08 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:03:05 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:00:58 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:02:52 | Galgamuwa (Mee Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:08:59 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:19:19 | Baddegama (Gin Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:03:01 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:05:47 | Moraketiya (Walawe Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:00:12 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:06:21 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:07:11 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:04:05 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:02:26 | Kuda Oya (Kirindi Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-08-16 16:05:29 | Thaldena (Mahaweli Ganga) | 0.08 | 🟢 Normal | -0.009 |  |
| 2026-08-16 16:09:07 | Holombuwa (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:04:10 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:03:12 | Thanamalwila (Kirindi Oya) | 0.16 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:04:16 | Norwood (Kelani Ganga) | 0.66 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:02:08 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:07:12 | Magura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:02:11 | Wellawaya (Kirindi Oya) | 0.55 | 🟢 Normal | -0.010 |  |
| 2026-08-16 16:03:44 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | -0.019 |  |
| 2026-08-16 16:04:18 | Kithulgala (Kelani Ganga) | 1.77 | 🟢 Normal | -0.020 |  |
| 2026-08-16 16:06:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.30 | 🟢 Normal | -0.020 |  |
| 2026-08-16 16:02:26 | Hanwella (Kelani Ganga) | 1.41 | 🟢 Normal | -0.020 |  |
| 2026-08-16 16:03:01 | Weraganthota (Mahaweli Ganga) | -3.20 | 🟢 Normal | -0.021 |  |
| 2026-08-16 16:08:26 | Ellagawa (Kalu Ganga) | 5.10 | 🟢 Normal | -0.052 |  |
| 2026-08-16 16:05:38 | Glencourse (Kelani Ganga) | 9.66 | 🟢 Normal | -0.093 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)