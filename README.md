# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--23_19:09:34-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **296,036 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 19:09:34 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.030 |  |
| 2026-10-23 19:07:54 | Badalgama (Maha Oya) | 3.24 | 🟢 Normal | -0.039 |  |
| 2026-10-23 19:07:28 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-10-23 19:07:19 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 19:06:52 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | -0.064 |  |
| 2026-10-23 19:06:24 | Putupaula (Kalu Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-10-23 19:06:12 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-10-23 19:06:04 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-10-23 19:06:01 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.020 |  |
| 2026-10-23 19:05:28 | Siyambalanduwa (Heda Oya) | 1.43 | 🟢 Normal | -0.314 |  |
| 2026-10-23 19:05:20 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 19:05:14 | Padiyathalawa (Maduru Oya) | 1.44 | 🟢 Normal | 1.099 | 🔺 Rising |
| 2026-10-23 19:05:12 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-23 19:05:06 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.076 |  |
| 2026-10-23 19:03:49 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-23 19:03:33 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-23 19:03:04 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-23 19:02:59 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.030 |  |
| 2026-10-23 19:02:57 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.019 |  |
| 2026-10-23 19:02:53 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.079 |  |
| 2026-10-23 19:02:41 | Moragaswewa (Deduru Oya) | 4.35 | 🟢 Normal | -0.061 |  |
| 2026-10-23 19:02:38 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.023 |  |
| 2026-10-23 19:02:27 | Hanwella (Kelani Ganga) | 3.73 | 🟢 Normal | -0.051 |  |
| 2026-10-23 19:02:00 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-23 19:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.030 |  |
| 2026-10-23 19:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-23 19:01:16 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-23 19:01:15 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-23 19:01:13 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-23 19:01:05 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | -0.128 |  |
| 2026-10-23 19:00:56 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 19:00:44 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-10-23 19:00:41 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-23 19:00:37 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:33:39 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-23 19:05:14 | Padiyathalawa (Maduru Oya) | 1.44 | 🟢 Normal | 1.099 | 🔺 Rising |
| 2026-10-23 19:05:12 | Deraniyagala (Kelani Ganga) | 1.07 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-23 19:02:00 | Peradeniya (Mahaweli Ganga) | 2.79 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-23 19:00:56 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-23 19:00:41 | Pitabeddara (Nilwala Ganga) | 1.42 | 🟢 Normal | 0.000 |  |
| 2026-10-23 19:03:04 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | 0.000 |  |
| 2026-10-23 19:05:20 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-23 19:03:49 | Holombuwa (Kelani Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-23 19:07:19 | Thawalama (Gin Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-10-23 18:33:39 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-23 19:00:37 | Thanamalwila (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-10-23 19:07:28 | Wellawaya (Kirindi Oya) | 1.27 | 🟢 Normal | -0.009 |  |
| 2026-10-23 19:06:24 | Putupaula (Kalu Ganga) | 1.94 | 🟢 Normal | -0.009 |  |
| 2026-10-23 19:01:16 | Thalgahagoda (Nilwala Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-10-23 19:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-10-23 19:03:33 | Moraketiya (Walawe Ganga) | 1.05 | 🟢 Normal | -0.010 |  |
| 2026-10-23 19:01:15 | Kuda Oya (Kirindi Oya) | 1.30 | 🟢 Normal | -0.010 |  |
| 2026-10-23 19:01:13 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-10-23 18:01:50 | Thanthirimale (Malwathu Oya) | 2.15 | 🟢 Normal | -0.010 |  |
| 2026-10-23 19:06:12 | Magura (Kalu Ganga) | 1.80 | 🟢 Normal | -0.010 |  |
| 2026-10-23 19:02:57 | Giriulla (Maha Oya) | 1.93 | 🟢 Normal | -0.019 |  |
| 2026-10-23 19:06:01 | Glencourse (Kelani Ganga) | 11.18 | 🟢 Normal | -0.020 |  |
| 2026-10-23 19:06:04 | Manampitiya (Mahaweli Ganga) | 1.05 | 🟢 Normal | -0.020 |  |
| 2026-10-23 19:02:38 | Baddegama (Gin Ganga) | 2.11 | 🟢 Normal | -0.023 |  |
| 2026-10-23 19:09:34 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.030 |  |
| 2026-10-23 19:02:59 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.030 |  |
| 2026-10-23 19:01:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.70 | 🟢 Normal | -0.030 |  |
| 2026-10-23 19:00:44 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | -0.030 |  |
| 2026-10-23 18:11:30 | Panadugama (Nilwala Ganga) | 4.20 | 🟢 Normal | -0.032 |  |
| 2026-10-23 19:07:54 | Badalgama (Maha Oya) | 3.24 | 🟢 Normal | -0.039 |  |
| 2026-10-23 18:05:52 | Galgamuwa (Mee Oya) | 2.48 | 🟢 Normal | -0.048 |  |
| 2026-10-23 19:02:27 | Hanwella (Kelani Ganga) | 3.73 | 🟢 Normal | -0.051 |  |
| 2026-10-23 19:02:41 | Moragaswewa (Deduru Oya) | 4.35 | 🟢 Normal | -0.061 |  |
| 2026-10-23 19:06:52 | Ellagawa (Kalu Ganga) | 7.20 | 🟢 Normal | -0.064 |  |
| 2026-10-23 19:05:06 | Rathnapura (Kalu Ganga) | 2.98 | 🟢 Normal | -0.076 |  |
| 2026-10-23 19:02:53 | Thaldena (Mahaweli Ganga) | 0.65 | 🟢 Normal | -0.079 |  |
| 2026-10-23 19:01:05 | Horowpothana (Yan Oya) | 2.41 | 🟢 Normal | -0.128 |  |
| 2026-10-23 19:05:28 | Siyambalanduwa (Heda Oya) | 1.43 | 🟢 Normal | -0.314 |  |
| 2026-10-23 18:03:29 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -6.108 |  |

## River Water Level Charts by Station

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)